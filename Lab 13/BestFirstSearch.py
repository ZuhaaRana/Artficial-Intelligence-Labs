
import csv
from matplotlib import pyplot as plt
import pandas as py

with open('data.csv') as file:
    reader = csv.reader(file)
    count = 0
    for row in reader:
        print(row)
        if count > 200:
            break
        count+=1

show_scatter_plot = py.read_csv (r'data.csv')
x = show_scatter_plot["Annual_Income_(k$)"]
y = show_scatter_plot["Age"]
plt.scatter(x,y)
plt.show()

        