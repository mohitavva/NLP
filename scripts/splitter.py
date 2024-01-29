import pandas as pd

df = pd.read_pickle("./cleaned.pkl")
df.drop("article", axis=1)
BATCH_SIZE = 50000
name = "pickle"
exten = ".pkl"

for i in range(0, 6):
    pd.to_pickle(df.iloc[i*BATCH_SIZE: (i+1)*BATCH_SIZE], "./split/"+name+str(i)+exten)
    print("SPLIT: ", i)