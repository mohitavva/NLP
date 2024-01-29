import pandas as pd
import numpy as np

df = pd.read_csv("./cnn_dailymail/train.csv")
df.drop(["id"], axis=1, inplace=True)

df["cleaned"]= ""

df_size = df["article"].size

def remove_splchars(text):
    spl_chars = ["/", ":", "@", "*", "[", "]", "(", ")", "+", "-", "=", "|"]
    res = ""
    for i in text:
        if i in spl_chars:
            continue
        else:
            res += i
    return res

for i in range (0, df_size):
    temp = df["article"][i]
    cleaned = remove_splchars(temp)
    df["cleaned"][i] = cleaned

df.to_pickle("./pickles/cleaned.pkl")