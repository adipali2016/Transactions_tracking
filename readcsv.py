#   This function will read csv and try to resolve it for better understanding

from collections import defaultdict
from tkinter import Tk
import numpy as np
import pandas as pd
from pandas.core.frame import DataFrame
from IPython.display import display
from resolving_payments import check_card, check_upi, check_atm, summing
from toTable import turn_to_table
from resolving_dates import date_list

def start_index(csv):
    for i, rows in csv.iterrows():
        if "Credit" in rows.values:
            return i
    return -1

def end_index(csv):
    for i, rows in csv.iterrows():
        if np.nan in rows.values:
            return i
    return -1 

def reading_csv():
    csv_reader = pd.read_table(r"C:/Users/asus/OneDrive - IIIT Bhopal\Documents/GitHub/Transactions_tracking/training_data.xls", engine="python")
    start_ind = start_index(csv_reader)
    csv_reader = csv_reader[start_ind:]
    new_reader = csv_reader.iloc[0]
    csv_reader = csv_reader[1:]
    csv_reader.columns = new_reader
    new_columns = []
    for i in new_reader.values:
        j = i.lower()
        if "debit" in j:
            i = "Debit"
        elif "credit" in j:
            i = "Credit"
        new_columns.append(i)        

    csv_reader = pd.DataFrame(csv_reader,columns=new_reader.values)
    csv_reader.columns = new_columns
    csv_reader.reset_index(drop=True, inplace=True)
    end_ind = end_index(csv_reader)
    csv_reader = csv_reader[:end_ind-1]
    csv_reader = creating_table(csv_reader)
    return csv_reader

def creating_table(csv):
    csv.fillna(0.00, inplace=True)
    for col in csv.columns:
        csv[col] = csv[col].replace([" "], 0)
    return csv


def sum_list(dct,csv):
    dct_sum = defaultdict(list)
    for i in dct:
        df = turn_to_table(dct[i],csv)
        sm = summing(df)
        dct_sum[i].append(sm)
    return dct_sum


if __name__=="__main__":
    csv = reading_csv()
    lt_upi = check_upi(csv)
    lt_card = check_card(csv)
    lt_atm = check_atm(csv)
    print(len(lt_upi))
    print(len(lt_card))
    print(len(lt_atm))
    df_upi = turn_to_table(lt_upi, csv)
    #print(df_upi)
    sum_upi = summing(df_upi)
    print(sum_upi)
    dct = date_list(csv)
    print(dct.keys())
    dct_sm = sum_list(dct,csv)
    print(dct_sm)
    
