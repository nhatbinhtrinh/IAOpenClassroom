# -*- coding: utf-8 -*-
"""
Created on Fri Jan 21 17:35:58 2022

@author: nguyen.trinh
"""
import requests, uuid, json, random

from dotenv import load_dotenv

import os

load_dotenv() 

# Subscription key 
subscription_key =  os.getenv("SUBSCRIPTION_KEY")
# Endpoint
endpoint = os.getenv("END_POINT")
# Location
location =os.getenv("LOCATION")

path = '/detect'

constructed_url = endpoint + path

params = {
    'api-version': '3.0'
}
constructed_url = endpoint + path
 
headers = {
    'Ocp-Apim-Subscription-Key': subscription_key,
    'Ocp-Apim-Subscription-Region': location,
    'Content-type': 'application/json',
    'X-ClientTraceId': str(uuid.uuid4())
}
# Define functions
def random_line(fname):
    '''
     to take randomly a line in the text file with name fname
    '''
    lines = open(fname,encoding='utf-8').read().splitlines()
    return random.choice(lines)

def myDectectLangF(sentence, opt = 'NotRandom'):   
    '''
        Function to detect the language of the input sentence
        In the case of opt is 'Random', the input sentence now is choosen randomly from the given data.
    '''
    if(opt =='Random'):
        sentence = random_line("./Data/x_test.txt")
        print("Sentence choosen randomly from data to send the service to detect language:\n")
        print(sentence)
    # Create a body 
    body = [ {"id1": "1", "text": sentence}]
    # Send resquest to the service to detect a language
    request = requests.post(constructed_url, params=params, headers=headers, json=body)
    response = request.json()
    print("\n This sentence may be written in the language: " + response[0]["language"])
      
# Application of the language detect function
myDectectLangF("Hello")
myDectectLangF("Bonjour", opt = "Random")