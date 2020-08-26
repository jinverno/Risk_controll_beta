#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 10:12:56 2020

@author: rafaelmello
"""

#import flask

import time 
from flask import Flask, render_template, request

from helper import run_model

#create a flask object
app = Flask(__name__)

#create route 


# for each route you define one python function to be executed (and this will be the result)
@app.route('/', methods = ['POST','GET'])
def index():
    # the python logic that will be run when the route is called
    if request.method == 'POST':
        # do stuff
        parameter_1 = request.form['parameter 1']
        parameter_2 = str(request.form['parameter 2'])
        parameter_3 = str(request.form['parameter 3'])
        parameter_4 = str(request.form['parameter 4'])
        parameter_5 = int(request.form['parameter 5'])
        
        print("------------------")
        print(parameter_1)
        print("------------------")
        print(parameter_2)
        print("------------------")
        print(parameter_3)
        print("------------------")
        print(parameter_4)
        print("------------------")
        print(parameter_5)
        print("------------------")
        time.sleep(2)
        prediction = [run_model(parameter_1,parameter_2,parameter_3,parameter_4,parameter_5)]
        print("the prediction is", prediction)
        predictions = prediction

        return render_template('index.html', predictions = prediction)
    else:
        return render_template('index.html')
    
#running our flask app
if __name__ == "__main__" : 
    app.run(debug = True)   
    

