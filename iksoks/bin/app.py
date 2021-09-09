from flask import Flask, request, jsonify, make_response, render_template
import time
import json
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return "hello!"

@app.route('/asocijacijerunda', methods=["GET"])
def runda():
    if request.method == "OPTIONS" or request.method == "GET":
        data = {'poruka':'OK', 'poeni':5}
        return jsonify(data)

@app.route('/asocijacijepobednik', methods=["POST"])
def pobednik():
    if request.method == "OPTIONS" or request.method == "POST":
        print(request.json)
        data = {'poruka':'OK'}
        return jsonify(data)

@app.route('/koznaznapitanje', methods=["POST"])
def pitanje():
    if request.method == "OPTIONS" or request.method == "POST":
        data = {'poruka':'OK'}
        return jsonify(data)

@app.route('/koznaznapobednik', methods=["POST"])
def rang():
    if request.method == "OPTIONS" or request.method == "POST":
        print(request.json)
        data = {'poruka':'OK'}
        return jsonify(data)