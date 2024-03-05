# Translation Web Application

This is a Flask web application that translates text inputted by the user into a target language using the Azure Translator Text API.

## Description

The application allows users to input text and select a target language from a dropdown menu. When the form is submitted, the text is sent to the Azure Translator Text API for translation. The translated text is then displayed to the user.

## Prerequisites

Before running this application, ensure you have the following installed:
- Python (version 3.6 or higher)
- Flask (install via pip: `pip install Flask`)
- requests (install via pip: `pip install requests`)
- python-dotenv (install via pip: `pip install python-dotenv`)

Additionally, you will need an Azure subscription to access the Translator Text API. Obtain the API key, endpoint, and location from the Azure portal and store them in a `.env` file in the root directory of the project. Example `.env` file:

translation-web-app/
│
├── app.py # Main Flask application file
├── templates/ # Directory for HTML templates
│ ├── index.html # HTML template for the input form
│ └── results.html # HTML template for displaying translation results
├── requirements.txt # File listing dependencies
├── .env # File containing API credentials (not included in repository)
└── README.md # Documentation file
