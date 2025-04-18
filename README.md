# Photo Album Project

A Django-based photo album application that allows users to create albums and upload photos with captions.

## Features
- User authentication (register, login, logout)
- Create, view, edit, and delete photo albums
- Upload photos with captions
- Edit photo captions inline
- Responsive design with modern UI
- Image preview during upload

## Requirements
- Python 3.8 or higher
- Django 5.2
- Pillow for image processing

## Setup Instructions

1. Clone the repository:
```bash
git clone <repository-url>
cd photo_project
```

2. Create and activate a virtual environment:
```bash
# On macOS/Linux:
python -m venv venv
source venv/bin/activate

# On Windows:
python -m venv venv
.\venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Apply database migrations:
```bash
python manage.py migrate
```

5. Create a superuser (admin):
```bash
python manage.py createsuperuser
```

6. Start the development server:
```bash
python manage.py runserver
```

7. Access the application:
- Open your browser and go to http://127.0.0.1:8000/
- Admin interface is available at http://127.0.0.1:8000/admin/

## Project Structure
- `/albums/`: Main application directory
  - `/templates/`: HTML templates
  - `/static/`: CSS, JavaScript, and image files
  - `/models.py`: Database models
  - `/views.py`: View logic
  - `/urls.py`: URL routing

## Media Files
The project uses a local media directory for storing uploaded photos. Make sure the `media/` directory exists and is writable.

## Development Notes
- Debug mode is enabled by default
- Static and media files are served by Django development server
- For production deployment, configure proper static/media file serving and security settings