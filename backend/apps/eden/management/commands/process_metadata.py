import os
import tempfile
from django.core.management.base import BaseCommand
from django.conf import settings
from ...models import Clip
from apps.eden.models import Clip

# Check if the optional libraries are installed
try:
    import whisper
    from moviepy.editor import VideoFileClip
    LIBRARIES_AVAILABLE = True
except ImportError:
    LIBRARIES_AVAILABLE = False

class Command(BaseCommand):
    help = 'Generates transcripts for video clips using OpenAI Whisper.'

    def handle(self, *args, **options):
        if not LIBRARIES_AVAILABLE:
            self.stdout.write(self.style.ERROR(
                "Required libraries not found. Please run: pip install moviepy openai-whisper"
            ))
            self.stdout.write(self.style.WARNING(
                "You may also need to install ffmpeg on your system for moviepy to work correctly."
            ))
            return

        self.stdout.write("Loading Whisper model (this may take a moment on first run)...")
        # Using the 'base' model is a good balance for local performance.
        # Other options: 'tiny', 'small', 'medium', 'large'
        model = whisper.load_model("base")
        self.stdout.write(self.style.SUCCESS("Whisper model loaded."))

        clips_to_process = Clip.objects.filter(transcript__isnull=True)
        total_clips = clips_to_process.count()

        if total_clips == 0:
            self.stdout.write("No clips found that need transcription.")
            return

        self.stdout.write(f"Found {total_clips} clip(s) to process.")

        for i, clip in enumerate(clips_to_process):
            self.stdout.write(f"Processing clip {i+1}/{total_clips}: {clip.name}...")

            video_path = os.path.join(settings.MEDIA_ROOT, clip.video.name)

            if not os.path.exists(video_path):
                self.stdout.write(self.style.ERROR(f"  Video file not found: {video_path}"))
                continue

            try:
                # Extract audio using moviepy
                video = VideoFileClip(video_path)
                
                # Create a temporary audio file
                with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as tmp_audio_file:
                    audio_path = tmp_audio_file.name
                    video.audio.write_audiofile(audio_path, codec='mp3', logger=None)

                self.stdout.write(f"  Audio extracted. Transcribing...")

                # Transcribe using Whisper
                result = model.transcribe(audio_path, fp16=False) # fp16=False for CPU
                transcript_text = result["text"].strip()

                # Save the transcript
                clip.transcript = transcript_text
                clip.save()

                self.stdout.write(self.style.SUCCESS(f"  Successfully transcribed: '{transcript_text[:70]}...'"))

                os.remove(audio_path)

            except Exception as e:
                self.stdout.write(self.style.ERROR(f"  An error occurred: {e}"))
                if 'audio_path' in locals() and os.path.exists(audio_path):
                    os.remove(audio_path)

        self.stdout.write(self.style.SUCCESS("Metadata pipeline finished."))
