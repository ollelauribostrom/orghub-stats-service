from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def root():
  return jsonify({ 'message': 'Stats service up and running' })
