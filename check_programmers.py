import requests
import pandas as pd 

# conda activate binusx

forms = []
programmer = ['istp', 'istj', 'entp', 'intp', 'intj']

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


    df["personality"] = df.apply(find_personality, axis=1)

    # need to improve the loop into more declarative pandas
    # for i in range(0, len(df)):
    #     for j in range(1, 61):
    #         form_data["q" + str(j)] = "q" + str(j) + "a" + str(df.iloc[i]['c' + str(j)])

    #     form_data["btnSubmit"] = "Lihat+Hasilnya"

    #     p = get_personality(form_data)

    

        # if not p in programmer and not p in dfset:
        #     dfset.append(p)

    print(df.head())
