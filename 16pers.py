import json
from collections import namedtuple
import requests
import random
import os 

file = open('16pers.json',mode='r')

data = file.read()

file.close()

def get_personality(answer):
    headers = {'Content-Type': 'application/json'}
    response = requests.post('https://www.16personalities.com/test-results', data=json.dumps(answer), headers=headers)
    # return response.headers['Refresh'].split('/')[-1]
    return response.content.decode("utf-8").split('/')[-1].split('-')[-2]

x = json.loads(data)

code = [-3, 3]
f = open("16personality-" + str(os.getpid()) + ".txt","a+")

counter = 0

for n in range(1000000):
    answer = []

    for i in range(60):
        c = random.choice(code)
        x['questions'][i]['answer'] = c
        answer.append(str(c))

    p = get_personality(x)
    f.write(",".join(answer) + "," + p + "\n")
    f.flush()
