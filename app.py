from flask import Flask, render_template, request
import requests
import os
import uuid
from dotenv import load_dotenv 
load_dotenv() 

# creating a Flask app
app = Flask(__name__)

# create a route to render the home HTML page with root URL '/' when accessed via a "GET" request
@app.route('/', methods=['GET'])
def index():
	return render_template('index.html')

# create a route to render the home HTML page with root URL '/' when accessed via a "POST" request
@app.route('/', methods=['POST']) 
def index_post(): 
	
	# Read the values from the form 
	original_text = request.form['text'] 
	target_language = request.form['language'] 

	# Load the values from .env 
	key = os.environ['KEY'] 
	endpoint = os.environ['ENDPOINT'] 
	location = os.environ['LOCATION'] 

	# Constructing the API's URL
	path = '/translate?api-version=3.0'
	
	# Add the target language parameter 
	target_language_parameter = '&to=' + target_language 
	
	# Create the full URL 
	constructed_url = endpoint + path + target_language_parameter 

	# Setting up header
	headers = { 
		'Ocp-Apim-Subscription-Key': key, 
		'Ocp-Apim-Subscription-Region': location, 
		'Content-type': 'application/json', 
		'X-ClientTraceId': str(uuid.uuid4()) 
	} 

	# Create the body of the request with the text to be translated 
	body = [{'text': original_text}] 

	# Make the API call using post 
	translator_request = requests.post( 
		constructed_url, headers=headers, json=body) 
	
	# Retrieve the JSON response from API
	translator_response = translator_request.json() 
	
	# Retrieve the translation 
	translated_text = translator_response[0]['translations'][0]['text'] 

	# Rendering the result HTML page
	return render_template( 
		'results.html', 
		translated_text=translated_text, 
		original_text=original_text, 
		target_language=target_language 
	) 


if __name__=='__main__':
    app.run()
