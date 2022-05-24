import json
import csv
import pandas as pd  
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher
import requests
f = open('data.json',encoding="mbcs")
data = json.load(f)
res=[]
for faq in data['data']:
  print(faq['ques'])
for faq in data['data']:
    fdata=json.dumps({"text":faq["ques"],"message_id": "b28"})
    response=requests.post(url="http://localhost:5005/model/parse",data=fdata)
    print(response)
    response_list=json.loads(response.text)
    print(response_list)
    res.append({"ans":faq["ans"],"bot_ans":response_list})
#print(res)
b=[]
que=[]
an=[]
q1=[]
qno=[]
con=[]
for i in res:
  a=[]
  que.append(i['bot_ans']['text'])
  an.append(i['ans'])
  q1.append(i['bot_ans']['intent_ranking'][0:3])
  qno.append(i['bot_ans']['intent']['name'])
  con.append(i['bot_ans']['intent']['confidence'])

  
dict = {'question': que,'question label':qno,'confidence':con,'answer':an,'Top 3 confidence scores':q1}
df = pd.DataFrame(dict)
df.to_csv('data_file.csv')