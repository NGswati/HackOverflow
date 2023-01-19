# prediction function
import pickle
import numpy as np
from flask import Flask,render_template,request,jsonify,json,redirect
import re
import requests
import requests_html
import pandas as pd
images_link=[ "static/image1.jpg","static/image2.jpg","static/image3.jpg","static/image4.jpg","static/image5.jpg","static/image6.jpg","static/image7.jpg","static/image8.jpg","static/image9.jpg","static/image10.jpg", "static/image11.jpg","static/image12.jpg","static/image13.jpg","static/image14.jpg","static/image15.jpg","static/image16.jpg","static/image17.jpg","static/image18.jpg","static/image19.jpg","static/image20.jpg","static/image21.jpg","static/image22.jpg","static/image23.jpg","static/image24.jpg","static/image25.jpg","static/gpu2.png"]
app=Flask(__name__,static_folder='static')
@app.route('/predict',methods=['POST','GET'])
def predict():
    df = pd.read_pickle("model.pkl")
    return render_template('data.html', data=df,images_link=images_link)
@app.route('/landing',methods=['POST','GET'])
def landing():
    return render_template('landingPage.html')
@app.route('/cover',methods=['POST','GET'])
def cover():
    return render_template('cover.html')
@app.route('/gpu',methods=['POST','GET'])
def gpu():
    
    return render_template('data.html')
@app.route('/cart',methods=['POST','GET'])
def cart():
    return render_template('cart.html')
if __name__=="__main__":
    app.run()
#placeholder empty