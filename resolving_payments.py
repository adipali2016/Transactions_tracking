# This scripts resoves all strings

import pandas as pd


def check_upi(df):
    lt_upi = list()
    n = 0
    for i in df["Description"]:
        if "float" not in str(type(i)):
            i = i.lower()
            if "upi" in i:
                lt_upi.append(n)
            n=n+1
    return lt_upi

def check_card(df):
    lt_card = list()
    n = 0
    for i in df["Description"]:
        if "float" not in str(type(i)):
            i = i.lower()
            if "debit card" in i:
                lt_card.append(n)
            n = n+1    
    return lt_card


def check_atm(df):
    lt_atm = list()
    n = 0
    for i in df["Description"]:
        if "float" not in str(type(i)):
            i = i.lower()
            if "atm" in i:
                lt_atm.append(n)
            n = n+1    
    return lt_atm    


def summing(csv):
    sum_lt = 0
    for i, rows in csv.iterrows():
        i = rows['Debit']
        if "str" in str(type(i)):
            i = i.replace(",","")
        sum_lt = sum_lt + float(i)
    return sum_lt 