/**
 * Generic handler for interactive video clips.
 *
 * This script looks for a video element with the class '.clip-video'
 * and reads data attributes to set up interactive events.
 *
 * Required Elements:
 * - A video element: <video class="clip-video" ...>
 * - A choices container: <div id="choices" ...>
 *
 * Data Attributes for video element:
 * - data-choices-show-time: (Required) Time in seconds to show choices.
 * - data-pause-on-choices: (Optional) "true" to pause video when choices appear.
 * - data-voice-prompt-selector: (Optional) CSS selector for an audio element to play.
 * - data-idle-timeout-ms: (Optional) Milliseconds of inactivity before auto-choosing.
 * - data-idle-choice-selector: (Optional) CSS selector for the default choice button.
 */
function setupInteractiveClip() {
  const video = document.querySelector('.clip-video');
  if (!video) return;

  const choicesDiv = document.getElementById('choices');
  if (!choicesDiv) return;

  // Read configuration from data attributes
  const showTime = parseFloat(video.dataset.choicesShowTime);
  const pauseOnChoices = video.dataset.pauseOnChoices === 'true';
  const voicePrompt = video.dataset.voicePromptSelector ? document.querySelector(video.dataset.voicePromptSelector) : null;
  const idleTimeout = parseInt(video.dataset.idleTimeoutMs, 10);
  const idleChoiceSelector = video.dataset.idleChoiceSelector;

  let choicesShown = false;
  let idleTimer = null;

  choicesDiv.style.display = 'none';

  video.addEventListener('timeupdate', () => {
    if (video.currentTime >= showTime && !choicesShown) {
      choicesDiv.style.display = 'block';
      choicesShown = true;

      if (pauseOnChoices) {
        video.pause();
      }

      if (voicePrompt && voicePrompt.paused) {
        voicePrompt.play();
      }

      if (idleTimeout && idleChoiceSelector) {
        idleTimer = setTimeout(() => {
          const defaultChoice = document.querySelector(idleChoiceSelector);
          if (defaultChoice) defaultChoice.click();
        }, idleTimeout);
      }
    }
  });

  choicesDiv.addEventListener('click', (e) => {
    if (e.target.classList.contains('choice-link')) {
      if (idleTimer) clearTimeout(idleTimer);
    }
  });
}

document.addEventListener('DOMContentLoaded', setupInteractiveClip);
document.body.addEventListener('htmx:afterSwap', setupInteractiveClip);