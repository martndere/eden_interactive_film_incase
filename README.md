# Eden Interactive Film

Eden Interactive Film is a Django-based web application for presenting an interactive, branching video narrative. Users watch video clips and make choices that affect the story's progression, with each choice leading to a different video segment.

## Features

- Interactive video playback with branching choices
- Choices appear at specific times or after video ends
- Audio prompts for user engagement
- Automatic transitions if the user is idle
- AJAX navigation for seamless user experience (using [htmx](https://htmx.org/))
- Modular Django templates for each clip

## Project Structure

```
eden_interactive_film/
├── eden/                  # Django app with models, views, templates, static files
│   ├── templates/eden/
│   │   ├── base_clip.html
│   │   ├── clip_a.html
│   │   ├── clip_b.html
│   │   ├── clip_c.html
│   │   ├── clip_d.html
│   │   ├── clip_e.html
│   │   ├── clip_f.html
│   │   ├── clip_g.html
│   │   └── clip_h.html
│   └── static/audio/      # Audio prompts (e.g., "he was manic.mp3")
├── manage.py
└── ...
```

## Requirements

- Python 3.8+
- Django 3.2+
- [htmx](https://htmx.org/) (included via CDN in base template)
- Modern web browser

## Setup

1. **Clone the repository:**
    ```bash
    git clone <your-repo-url>
    cd eden_interactive_film
    ```

2. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3. **Collect static files:**
    ```bash
    python manage.py collectstatic
    ```

4. **Run migrations:**
    ```bash
    python manage.py migrate
    ```

5. **Create a superuser (optional, for admin):**
    ```bash
    python manage.py createsuperuser
    ```

6. **Run the development server:**
    ```bash
    python manage.py runserver
    ```

7. **Access the app:**
    - Open [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser.

## Usage

- Watch each video clip.
- Make choices when prompted; your decision determines the next clip.
- If you do not choose within the idle timeout, the app may auto-select a default path.
- Some clips play audio prompts automatically.

## Adding/Editing Clips and Choices

- Use the Django admin to add or edit `Clip` and `Choice` objects.
- Each `Clip` can have multiple `Choice` objects, each pointing to another `Clip`.
- Choices can be configured to appear at specific times via template logic.

## Customization

- **Templates:** Edit the HTML in `eden/templates/eden/clip_*.html` to change the look and feel or logic for each clip.
- **Audio:** Place audio files in `eden/static/audio/` and reference them in templates.
- **Video:** Upload video files and link them to `Clip` objects in the admin.

## Troubleshooting

- **Choices not appearing:** Ensure your video is long enough and the JavaScript logic matches the template.
- **Audio not playing:** Check the filename and path in the `static/audio/` directory.
- **JS errors:** Open your browser console for error messages and debug as needed.

## License

MIT License

---

**Enjoy your interactive film experience!**