# Eden Interactive Film

Eden Interactive Film is a Django-based web application for presenting an interactive, branching video narrative. Users watch video clips and make choices that affect the story's progression, with each choice leading to a different video segment.
Eden Interactive Film is a web application for presenting an interactive, branching video narrative. The backend is powered by Django and the frontend is designed to be a modern single-page application.

## Features

- Interactive video playback with branching choices
- Choices appear at specific times or after video ends
- Audio prompts for user engagement
- Automatic transitions if the user is idle
- AJAX navigation for seamless user experience (using [htmx](https://htmx.org/))
- Modular Django templates for each clip
- RESTful API for managing story progression and user data
- AI-powered asset generation capabilities
- 2D and 3D interactive scenes

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

- Python 3.10+
- Django 4.2+
- Node.js & npm (for frontend development)

## Backend Setup

1. **Clone the repository:**
    ```bash
    git clone <your-repo-url>
    cd eden_interactive_film_incase
    ```

2. **Create and activate a virtual environment:**
    ```powershell
    # Create the environment
    python -m venv venv
    # Activate it (on Windows PowerShell)
    .\venv\Scripts\Activate.ps1
    ```

3. **Install Python dependencies:**
    Navigate into the backend directory and install the requirements.
    ```bash
    cd backend
    pip install -r requirements.txt
    ```

4. **Create a `.env` file:**
    Inside the `backend` directory, create a `.env` file and add your `SECRET_KEY` and other environment variables.
    
    **Example `.env` for development:**
    ```
    SECRET_KEY=your-super-secret-key-goes-here
    DEBUG=True
    ALLOWED_HOSTS=127.0.0.1,localhost
    OPENAI_API_KEY=your-openai-api-key
    ```
    
5. **Run database migrations:**
    ```bash
    python manage.py migrate
    ```

6. **Create a superuser (optional, for admin):**
    ```bash
    python manage.py createsuperuser
    ```

7. **Run the development server:**
    ```bash
    python manage.py runserver
    ```

7. **Access the app:**
    - Open [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser.

## License

MIT License


**Enjoy your interactive film experience!**
