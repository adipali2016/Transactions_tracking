#   This function will read csv and try to resolve it for better understanding

import calendar
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
from resolving_payments import check_card, check_upi, check_atm, summing
from toTable import turn_to_table
from resolving_dates import date_list
from converting_to_plots import bar_graph, pie_chart
from tkinter.filedialog import askopenfilename

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
    #filename = askopenfilename()
    filename = r"C:\Users\asus\OneDrive - IIIT Bhopal\Documents\GitHub\Transactions_tracking/training_data.xls"
    csv_reader = pd.read_table(filename, engine="python")
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
    dct_sum_debit = dict()
    dct_sum_credit = dict()
    for i in dct:
        df = turn_to_table(dct[i],csv)
        sm = summing(df)
        dct_sum_debit[str(i)] = sm[0]
        dct_sum_credit[str(i)] = sm[1]
    return [dct_sum_debit,dct_sum_credit]


def convert_keys(dct):
    dct_debit, dct_credit = dct
    new_dct_debit = dict()
    new_dct_credit = dict()
    #print(dct_debit.keys())
    for i in dct_debit.keys():
        splt = i.split()
        new_i = f"{calendar.month_name[int(splt[0])]} {splt[1]}"
        #print(new_i)
        new_dct_debit[new_i] = dct_debit[i]
        #print(dct_debit.keys())
    for i in dct_credit.keys():
        splt = i.split()
        #print(splt[0], splt[1])
        new_i = f"{calendar.month_name[int(splt[0])]} {splt[1]}"
        new_dct_credit[new_i] = dct_credit[i]
    return [new_dct_debit,new_dct_credit]

if __name__=="__main__":
    csv = reading_csv()
    lt_upi = check_upi(csv)
    lt_card = check_card(csv)
    lt_atm = check_atm(csv)
    i=1;
    # Bar graph and pie chart for Transactions based on months 
    dct = date_list(csv)
    dct_ans = sum_list(dct, csv)
    dct_ans = convert_keys(dct_ans)
    bar = bar_graph(dct_ans[0], dct_ans[1], i)
    i += 1
    pie = pie_chart(dct_ans[0], i)
    i += 1

    # Bar graph and pie chart for Transactions based on Payment types.
    df_upi = turn_to_table(lt_upi, csv)
    df_card = turn_to_table(lt_card, csv)
    df_atm = turn_to_table(lt_atm, csv)
    sum_upi = summing(df_upi)
    sum_card = summing(df_card)
    sum_atm = summing(df_atm)
    bar_pay = bar_graph({'UPI': sum_upi[0] ,'Card': sum_card[0], 'ATM': sum_atm[0]}, {'UPI': sum_upi[1] ,'Card': sum_card[1], 'ATM': sum_atm[1]}, i)
    i += 1
    pie_pay = pie_chart({'UPI': sum_upi[0] ,'Card': sum_card[0], 'ATM': sum_atm[0]}, i)
    i += 1

    plt.show()
    
    input()
    
