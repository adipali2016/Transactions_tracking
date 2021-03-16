import pandas as pd

def turn_to_table(arr, csv):
    df = pd.DataFrame(columns=csv.columns)
    for i, rows in csv.iterrows():
        if i in arr:
            dct = dict(rows)
            #print(dct)
            df1 = pd.DataFrame(dct, index=range(1))
            df = pd.concat([df, df1])
            df.reset_index(drop=True, inplace=True)       
    return df   