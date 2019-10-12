# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 00:11:12 2019

@author: Jakey
"""


#import sys

#sys.path.append(r"C:\Users\Jakey\Anaconda3\lib\site-packages")
#print(sys.path)

import requests
from os import environ

TOKEN = environ['BOT_TOKEN']

HEADERS = {
    'Accept-Encoding': 'gzip, deflate, br',
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'Connection': 'keep-alive',
    'DNT': '1',
    'Origin': 'https://api.foretold.io',
    }

PARAMS = (
    ('token', TOKEN),
) 

query = """
mutation {
  measurementCreate(input: {
    value: {
      floatCdf: {
          xs: [0, 1, 2, 3]
          ys: [0.1, 0.5, 0.9, 1]   
          }
    }
    competitorType: COMPETITIVE
    measurableId: "5c42c5de-9b77-4c48-8158-a43f6bc9b8c0"
  }) {id}
}
"""        


response = requests.post('https://api.foretold.io/graphql', json={'query': query}, headers=HEADERS, params=PARAMS)

print(response)