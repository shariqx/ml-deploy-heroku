from flask import Flask,request, url_for, redirect, render_template, jsonify
import pandas as pd
import pickle
import numpy as np
# Initalise the Flask app
app = Flask(__name__)

cols = ['Weight', 'Length1', 'Length3', 'Height', 'Width']

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/predict',methods=['POST'])
def predict():
    int_features = [x for x in request.form.values()]
    final = np.array(int_features)
    data_unseen = pd.DataFrame([final], columns = cols)
    #prediction = predict_model(model, data=data_unseen, round = 0)
    # load the model from disk
    loaded_model = pickle.load(open('model.sav', 'rb'))
    y_pred = loaded_model.predict(data_unseen)
    predictions = [value for value in y_pred]
    print(predictions)
    predictions = "test"
    return render_template('home.html', pred='Expected Bill will be {}'.format(predictions))

@app.route('/predict1',methods=['POST'])
def predict1():
    predictions = "test"
    return 'Expected Bill will be 123'


if __name__ == '__main__':
    app.run(debug=True)