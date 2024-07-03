from flask import Flask, render_template, jsonify, request
import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient  

app = Flask(__name__)

client = MongoClient('mongodb+srv://sparta:jungle@cluster0.gsunejv.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')  # MongoDB Altas 사이트의 링크를 가져옵니다
db = client.dbjungle 


@app.route('/')
def home():
    return render_template('index.html')

# @app.route('/memo', methods=['POST'])

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)