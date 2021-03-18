import datetime as dt
from collections import defaultdict

def date_list(csv):
    dct_month = defaultdict(list)
    for i,rows in csv.iterrows():
        d = rows[0]
        temp_d = d[:len(d)-2] +"20"+ d[len(d)-2:] 
        date_obj = dt.datetime.strptime(temp_d, "%d-%b-%Y")
        month = date_obj.month
        year = date_obj.year
        month = f"{month} {year}" 
        dct_month[str(month)].append(i)
    return dct_month
