#!/usr/bin/env python
# coding: utf-8




import json
import re
import tqdm
# Opening JSON file
def preprocess():
    f = open('article.json')
  
# returns JSON object as 
# a dictionary
    data = json.load(f)

# Iterating through the json
# list
    l=[]
    for j,i in  tqdm.tqdm(data.items()):
        j=re.sub("\<.*?\>","",j[1:-1])
        i=re.sub("\<.*?\>","",i[1:-1])
   
        l.append(j+' . '+i)
    return l













