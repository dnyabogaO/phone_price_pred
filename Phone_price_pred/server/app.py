from flask import Flask, request, jsonify
import pandas as pd
import util

app = Flask(__name__)
@app.route('/get_phone_names', methods=['GET'])
def get_phone_names():
    response = jsonify({
        'phones': util.get_phone_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
@app.route('/predict_phone_price', methods=['GET', 'POST'])
def predict_phone_price():
    phone_make = request.form['phone_make']
    OS = int(request.form['OS'])
    ROM = int(request.form['ROM'])
    RAM = int(request.form['RAM'])
    screen_size = float(request.form['screen_size'])
    back_camera = int(request.form['back_camera'])
    front_camera = int(request.form['front_camera'])
    Battery = int(request.form['Battery'])
    Rating = int(request.form['Rating'])
    Likes = int(request.form['Likes'])
    specs_score = int(request.form['specs_score'])
    response = jsonify({
        'estimated_price': util.get_estimated_price(phone_make,OS,ROM,RAM,screen_size,back_camera,front_camera,Battery,Rating,Likes,specs_score)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    util.load_saved_artifacts()
    app.run()