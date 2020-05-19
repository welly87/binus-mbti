import pandas as pd

# https://www.thecalculator.co/personality/Personality-Type-Test-31.html#calculator-top

def get_questions():
    file = open('16pers.json',mode='r')
    data = file.read()
    file.close()
    return data

df = pd.read_csv("16personality-29640.txt", header=None)

print(df.head())