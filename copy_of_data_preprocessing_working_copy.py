# -*- coding: utf-8 -*-
"""Copy of Data Preprocessing Working Copy.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17QeKB5OKSsJEnbOIhowjvCtde3bn3wSj

# Data Preprocessing

## Importing the libraries
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

"""## Importing Dataset"""

dataset = pd.read_csv('netflixdata.csv', header = None)
transactions=[]
for i in range(0,7):
  transactions.append([str(dataset.values[i,j]) for j in range(0,3)])
print(dataset)

"""# New Section

results
"""

!pip install apyori

from apyori import apriori
rules=apriori(transactions = transactions, min_support=0.03)

results=list(rules)
print(results)

"""# New Section"""

from tabulate import tabulate
print(tabulate([[results]], headers=['movie1', 'movie2','support']))

"""# New Section

# New Section
"""



from pandas.core.groupby.grouper import DataFrame
df = pd.DataFrame(list(zip(results)))
columns = ['movie1','movie2']



print(df)