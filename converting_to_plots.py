# Functions will help in converting table data to arrays for plotting
import matplotlib.pyplot as plt
import numpy as np

def bar_graph(dct_debit, dct_credit):
    bar = plt.figure(1)
    xpos = dct_debit.keys()
    ypos1 = dct_debit.values()
    ypos2 = dct_credit.values()
    ypos = np.arange(len(dct_debit))
    plt.xticks(ypos, xpos)
    plt.bar(ypos-0.2,ypos1, width=0.4, label="Debit")
    plt.bar(ypos+0.2,ypos2, width=0.4,label="Credit")
    return bar

def pie_chart(dct_debit, dct_credit):
    pie = plt.figure(2)
    keys = dct_debit.keys()
    dct_values = dct_debit.values()
    plt.pie(dct_values, labels = keys, autopct='%0.02f%%')
    return pie    