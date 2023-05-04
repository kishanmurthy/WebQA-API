import os

from flask import Flask, jsonify, request
from flask_cors import CORS

from config import OPENAI_API_KEY
from question_answer import get_qa_result

app = Flask(__name__)
CORS(app)

@app.route('/question_answer', methods=["POST"])
def question_answer():
	webpage = request.json['webpage']
	question = request.json['question']
	#return jsonify({"output_text": "Hello World"})
	return jsonify(get_qa_result(webpage, question))

if __name__ == '__main__':
   os.environ['OPENAI_API_KEY'] = OPENAI_API_KEY
   app.run()