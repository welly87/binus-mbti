import requests
import random

forms = []

def get_personality(answer):
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    
    response = requests.post('https://tes.anthonykusuma.com/16-kepribadian/tes', data=answer, headers=headers)
    
    return response.headers['Refresh'].split('/')[-1]

counter = 0
f = open("mbti-dataset.txt","w+")
personality = []

def recurse_answer(form_data, choices):
    global forms, personality

    if len(choices) == 60:
        print(str(choices))

        form_data["btnSubmit"] = "Lihat+Hasilnya"
        
        p = get_personality(form_data)
        print(p)

        if p not in personality:
            personality.append(p)

        f.write(",".join(choices) + "," + p + "\n")
        f.flush()

        return

    code = ["1", "2"]

    c = random.choice(code)

    choices += c

    form_data["q" + str(len(choices))] = "q" + str(len(choices)) + "a" + c

    recurse_answer(form_data, choices)

if __name__ == "__main__":
    while len(personality) != 16:
        recurse_answer({}, [])

    print(personality)
