import os
from flask import Flask
from flask import request
from flask import jsonify
from flask import json
from flask import Response
from flask_restful import Api
import gensim
import logging

logging.basicConfig(format='w2vapi - %(asctime)-12s: %(message)s')

app = Flask(__name__)
api = Api(app)

HOST_URL = "http://localhost:8000"
MODEL_PATH = os.environ.get('MODEL_PATH', '~/Downloads/GoogleNews-vectors-negative300.bin')
LOCAL = os.environ.get('LOCAL',1)

try:
	if not LOCAL:
		logging.warning("attempting model load")	
		MODEL = gensim.models.KeyedVectors.load_word2vec_format(MODEL_PATH, binary=True)
	logging.warning("model load success")
except (IOError, MemoryError) as err:
	logging.critical("model load fail: %s" % err)
	raise

def get_word_distance(w1, w2):
	"""
	run the keras w2v model
	"""
	try:
		# word in model
		res = MODEL.similarity('w1', 'w2')
		return json.dumps(res)
	except Exception as err: # gensim exception class?
		logging.warning("similarity check error: %s" % err)
	return json.dumps(None)

@app.route('/<word1>/<word2>')
def w2v_similarity(word1, word2):
	"""
	route for w2v word cosine distance evaluation
	"""
	distance = get_word_distance(word1, word2)
	resp = Response(distance, status=200, mimetype='application/json')
	resp.headers['Link'] = HOST_URL
	return resp

@app.route('/')
def api_root():
	"""
	hello
	"""
	resp = Response({"hello":"world"}, status=200, mimetype='application/json')
	resp.headers['Link'] = HOST_URL
	return resp

@app.errorhandler(404)
def not_found(error=None):
	message = {
			'status': 404,
			'message': 'Not Found: ' + request.url,
	}
	resp = jsonify(message)
	resp.status_code = 404

	return resp

@app.errorhandler(500)
def serv_err(error=None):
	message = {
		'status': 500,
		'message': 'Server Error, ' + request.url
		}
	resp = jsonify(message)
	resp.status_code = 500

	return resp

if __name__ == "__main__":
	if LOCAL:
		app.run(debug=True, host='0.0.0.0', port=8000)
	else:
		app.run(debug=False, host='0.0.0.0', port=8000)
