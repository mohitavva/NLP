import pandas as pd
import numpy as np
from nltk.tokenize import (word_tokenize, sent_tokenize)


splits = 6
for i in range(0, 6):
    df = pd.read_pickle("./split/pickle"+str(i)+".pkl")

    df.drop("article", axis=1, inplace=True)
    df["tokens"] = ""
    BATCH_SIZE = 500

    def batching(df):
        temp = 0
        steps = np.ceil((df["cleaned"].size)/BATCH_SIZE)
        while(steps>=0):
            df_temp = df.iloc[temp*BATCH_SIZE:(temp+1)*BATCH_SIZE, 1]
            yield df_temp
            temp+=1
            steps-=1 

    count = 0

    for j in batching(df):
        temp = j.transform(lambda x: word_tokenize(x, "english", preserve_line=True))
        # temp = word_tokenize(i, "english", preserve_line=True)
        df.iloc[count*BATCH_SIZE:(count+1)*BATCH_SIZE, 2] = temp 
        print(count)
        count += 1

    df.to_pickle("./split/tokenized"+str(i)+".pkl")