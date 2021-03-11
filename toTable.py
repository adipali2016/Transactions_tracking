import pandas as pd

def turn_to_table(arr, csv):
    df = pd.DataFrame(columns=csv.columns)
    for i, rows in csv.iterrows():
        if i in arr:
            dct = dict(rows)
            df1 = pd.DataFrame(dct, index=range(1))
            df = pd.concat([df, df1])
    return df.reset_index(drop=True, inplace=True)     