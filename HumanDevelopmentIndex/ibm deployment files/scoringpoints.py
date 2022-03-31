# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 14:14:23 2022

@author: MAHIMA
"""

import requests

# NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account.
API_KEY = "HgjReQuqvfe6WSKv0jztS6WiDsbVXPG024ZdJfFQWsKh"
token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey": API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

# NOTE: manually define and pass the array(s) of values to be scored in the next line
payload_scoring = {"input_data": [{"field": [["Country","Life expectancy","Mean years of schooling","Gross national income (GNI) per capita","Internet users"]], "values": [[13,72.0,5.2,3341.0,14.4]] }]}

response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/d5f2f110-2d28-4beb-8aef-79fbfc07fca4/predictions?version=2022-03-25', json=payload_scoring, headers={'Authorization': 'Bearer ' + mltoken})
print("Scoring response")
print(response_scoring.json())
