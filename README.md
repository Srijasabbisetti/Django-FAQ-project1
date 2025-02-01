Django FAQ Project
This is a Django-based web application for managing multilingual FAQs. The project allows users to view and manage FAQs with support for multiple languages. It also includes a WYSIWYG editor for formatting answers and a caching mechanism to optimize performance.

Features
Multilingual FAQ management
WYSIWYG editor (django-ckeditor) for formatting answers
Caching using Redis to improve performance
REST API for managing FAQs and selecting languages
Docker support for easy deployment
Prerequisites
Before running the project, ensure you have the following installed:

Python 3.x
Django 5.x
Redis (for caching)
Google Translate API or googletrans library (for translation)
Installation Steps
1. Clone the repository
git clone https://github.com/your-username/faq_project.git
cd faq_project
Set up a Virtual Environment It's recommended to use a virtual environment for managing dependencies.
python -m venv venv
Activate the virtual environment:

Windows:

.\venv\Scripts\activate
Mac/Linux:

source venv/bin/activate
Install Dependencies Install the required dependencies from the requirements.txt file.
pip install -r requirements.txt
Set up the Database Run the migrations to set up the database.
python manage.py migrate
Create a Superuser (Optional) To access the Django admin panel, you need to create a superuser.
python manage.py createsuperuser
Follow the prompts to set the username, email, and password.

Run the Development Server Start the Django development server.
python manage.py runserver
The application will be available at http://127.0.0.1:8000/.

API Usage You can interact with the FAQ API to fetch FAQs in different languages. Here are some examples:

Fetch FAQs in English (default)
curl http://127.0.0.1:8000/api/faqs/
Fetch FAQs in Hindi
curl http://127.0.0.1:8000/api/faqs/?lang=hi
Fetch FAQs in Bengali
curl http://127.0.0.1:8000/api/faqs/?lang=bn
API Endpoints GET /api/faqs/: Fetch all FAQs. GET /api/faqs/?lang=<language_code>: Fetch FAQs in a specific language. Admin Panel To access the Django admin panel, visit http://127.0.0.1:8000/admin/ and log in with the superuser credentials you created earlier.

Managing FAQs You can add, edit, and delete FAQs directly from the Django admin interface. Each FAQ has:

A question (TextField) An answer (formatted with the WYSIWYG editor) Translations for different languages Testing To run the tests for the project:

pytest
Deployment Docker Support To run the project with Docker, use the following commands:

Build the Docker image:

docker build -t faq_project .
Run the container:

docker run -p 8000:8000 faq_project
The application will be accessible at http://127.0.0.1:8000/.

# Fork the repository.
- Create a new branch for your changes (`git checkout -b feature-branch`).
- Commit your changes (`git commit -m "Add feature"`).
- Push to your branch (`git push origin feature-branch`).
- Open a pull request.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments
- Django for the web framework.
- django-ckeditor for the WYSIWYG editor.
- Google Translate API for multilingual support.
- Redis for caching.
