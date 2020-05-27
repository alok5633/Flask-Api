# -*- coding: utf-8 -*-
"""
Created on Wed May 27 09:24:46 2020

@author: Alok
"""

from flask import *
import csv
app=Flask(__name__)

'''
import csv

with open('data.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

print(data)
'''

@app.route('/search',methods=['GET','POST'])  
def search():
    text=request.json['input']
    text=text.lower()
    print(text)
    with open('data.csv', newline='') as f:
            reader = csv.reader(f)
            data = list(reader)
    search=[]        
    for i in range(1,100):
        if data[i][0].lower().find(text,0)!=-1:
            search.append(data[i])
        elif data[i][1].lower().find(text,0)!=-1:
            search.append(data[i])
        elif data[i][2].lower().find(text,0)!=-1:
            search.append(data[i])
        elif data[i][3].lower().find(text,0)!=-1:
            search.append(data[i])
        elif data[i][4].lower().find(text,0)!=-1:
            search.append(data[i])
        elif data[i][5].lower().find(text,0)!=-1:
            search.append(data[i])  
    
    return jsonify({ 'search': search })
    
    

@app.route('/',methods=['GET','POST'])  
def index():
        
    if request.method == 'GET':
        with open('data.csv', newline='') as f:
            reader = csv.reader(f)
            data = list(reader)
        print(data[1])
        
        print(data[2])
        size=len(data)
        return render_template("home.html",data=json.dumps(data),size=json.dumps(size)) 

if __name__ =='__main__':
    app.run()