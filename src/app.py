from flask import Flask, jsonify, request
import requests
from src.stats import get_stats

app = Flask(__name__)

@app.route('/')
def root():
  return jsonify({ 'message': 'Stats service up and running' })

@app.route('/stats/<organization>', methods=['GET'])
def stats(organization):
  url = 'https://api.github.com/orgs/{}/repos'.format(organization)
  headers = {'Authorization': request.headers.get('Authorization')}
  r = requests.get(url, headers = headers)
  if r.status_code == requests.codes.ok:
    return jsonify(get_stats(r.json(), headers)), 200, {'Content-Type': 'application/json'}
  else:
    return r.content, r.status_code, {'Content-Type': 'application/json'}