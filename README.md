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

You can install all required dependencies by running the following command:
  >pip install -r requirements.txt

The `requirements.txt` file lists all the Python packages and their versions required to run this application.
Additionally, you will need an Azure subscription to access the Translator Text API. Obtain the API key, endpoint, and location from the Azure portal and store them in a `.env` file in the root directory of the project. 

## Screenshots

### Home Page
![Home Page](https://github.com/Rohith2811/Translator/assets/91714071/ddbe2b59-cf0e-49a2-8fb6-918206a6041e)

Description: This screenshot shows the home page of the application where users can input text and select a target language.

### Translation Results
![Translation Results](https://github.com/Rohith2811/Translator/assets/91714071/9cda3406-a116-411a-bd2e-742be5708f66)

Description: This screenshot displays the translation results after the user submits the form, showing the original text and its translation.

