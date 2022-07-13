from flask import Flask, request, jsonify
import logging
import requests
import os


from dotenv import load_dotenv
load_dotenv()

logging.basicConfig(level=logging.DEBUG)


request_url = os.environ.get('REQUEST_URL')

logging.info("Microservice connection checker for internal tests")
logging.info("**** Environment variables:")
logging.info("** REQUEST_URL: {}".format(request_url))
logging.info ("Contact: klodnicki.k@pg.com")

if (request_url==None):  logging.error("Missing env variable 'REQUEST_URL'")

app = Flask(__name__)





@app.route('/', methods=['GET'])
def request_main_page():

	json_output = requests.get(request_url).json()

	message = {
	'request_url' :  request_url,
	'response_output' : json_output
	}

	return jsonify(message)



if __name__ == "__main__":
	app.run(host='0.0.0.0', port=8080)