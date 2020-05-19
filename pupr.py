import json
from collections import namedtuple
import requests
import random
import os 
from bs4 import BeautifulSoup
import pandas as pd

def get_personality_pupr(answer):
    form_data = {}
    for i in range(len(answer)):
      form_data["d[" + str(i+1) + "]"] = answer[i]

    headers = {'Content-Type': 'application/x-www-form-urlencoded'}    
    response = requests.post('https://bpsdm.pu.go.id/tesmbti/result.php', data=form_data, headers=headers)

    soup = BeautifulSoup(response.text)

    result = soup.select('body > div > h1')[0]
    return result.text

def compute_mbti(s):
  answer = s[0:60].astype(int)
  result = get_personality_pupr(answer)
  
  print(result)

  return result


df = pd.read_csv("mbti-dataset.txt", header=None)
# small_df = df.head()

df['pupr'] = df.apply(compute_mbti, axis=1)

file_name = "mbti-pupr" + str(os.getpid()) + ".csv"
df.to_csv(file_name, header=False)

