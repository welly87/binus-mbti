import requests
import pandas as pd 

# conda activate binusx

forms = []


def get_personality(answer):
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    
    response = requests.post('https://tes.anthonykusuma.com/16-kepribadian/tes', data=answer, headers=headers)
    
    return response.headers['Refresh'].split('/')[-1]


if __name__ == "__main__":

    df = pd.read_csv("30programmer.csv")

    # join = df.loc[:, 'ch':'ch.59']

    df.columns = ['time'] + ['c' + str(i) for i in range(1, 61)] + ['email', 'name', 'wa']

    def find_personality(row):
        form_data = {}

        for j in range(1, 61):
            form_data["q" + str(j)] = "q" + str(j) + "a" + str(row['c' + str(j)])

        form_data["btnSubmit"] = "Lihat+Hasilnya"

        p = get_personality(form_data)

        return p


    def check_programmer(row):
        programmer = ['istp', 'istj', 'entp', 'intp', 'intj']

        return row["personality"] in programmer


    df["personality"] = df.apply(find_personality, axis=1)

    df["progr"] = df.apply(check_programmer, axis=1)

    personality_df = df[["name", "email", "wa", "personality", "progr"]]

    print(personality_df.head())

    personality_df.to_csv ('30prog.csv', index = False, header=True)

    personality_df[personality_df["progr"]].to_csv ('30true.csv', index = False, header=True)

    

