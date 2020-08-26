#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 11:49:58 2020

@author: rafaelmello
"""
import pandas as pd
import numpy as np

import pickle

def run_model(parameter_1,parameter_2,parameter_3,parameter_4,parameter_5):
    pkl_filename = "model_new_client_forest.pkl"
    # Load from fil
          
    my_dict= {'LIMIT_BAL':0, 'AGE':0 , 'SEX_Male':0, 'SEX_Female':0, 'EDUCATION_University':0, 'EDUCATION_High School':0,
    'EDUCATION_Others':0, 'EDUCATION_Graduate School':0, 'MARRIAGE_Single':0, 'MARRIAGE_Married':0, 'MARRIAGE_Others':0,'MARRIAGE_Extra':0}
     
    my_dict['LIMIT_BAL'] = parameter_1
     
    my_dict['SEX_'+parameter_2] = 1
     
    my_dict['EDUCATION_'+parameter_3] = 1
       
    my_dict['MARRIAGE_'+parameter_4] = 1
     
    my_dict['AGE'] = parameter_5
      
    to_predict = np.array(list(my_dict.values()))
    
    with open(pkl_filename, 'rb') as file:
        pickle_model = pickle.load(file)
    prediction = round(pickle_model.predict_proba([to_predict])[0][1], 2)
    
    return prediction


#print(run_model(1000,"1","1","1",30))

"""
# simulate the results of what the user will insert
user_inputs = {'MARRIAGE' : 1 , 'SEX' : 2, 'EDUCATION' : 2}

extra_inputs = {"LIMIT_BAL" : 10000, "AGE" : 20}


data = pd.read_csv('credit_dummies.csv')

data = data.drop(['Unnamed: 0', 'default','AGE','LIMIT_BAL'], axis = 1)
keys = data.columns

new_dict = {}

for key in keys:
    new_dict[key] = 0
    

for in_key in user_inputs.keys():
    for key in new_dict.keys():
        if (in_key in key) and (str(user_inputs[in_key]) in key):
            new_dict[key] += 1


data_1 = pd.DataFrame.from_dict(new_dict, orient = 'index').T
data_2 = pd.DataFrame.from_dict(extra_inputs, orient = 'index').T

final_result = pd.concat([data_2,data_1], axis = 1)

### stuff ###

features = final_result.iloc[0].values
print(features)


print(run_model(features))
"""
