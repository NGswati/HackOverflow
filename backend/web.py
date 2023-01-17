# prediction function
import pickle
import numpy as np
from flask import Flask,render_template,request,jsonify,json
import re
import requests
import requests_html
import pandas as pd

app=Flask(__name__)
@app.route('/predict')
def predict_salary():
    df = pd.read_pickle("model.pkl")
    # return render_template('data.html', tables=[df.to_html(classes='data')], titles=df.columns.values)
    return render_template('data.html', data=df)
if __name__=="__main__":
    app.run()
#placeholder empty