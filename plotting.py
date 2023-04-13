from matplotlib import pyplot as plt

import time
import numpy as np
import pandas as pd

def NAN_clearer(array_1,array_2):
    last_index = len(array_1) - 1
    for element in array_1:
        if array_1[last_index] == "NAN":
            array_1 = np.delete(array_1,last_index)
            array_2 = np.delete(array_2,last_index)
        last_index = last_index - 1
    return array_1,array_2
df = pd.read_excel(open('output_101.xlsx', 'rb'))
df_citations = np.array([])
df_year = np.array([])
for i in df:
    try:
        number_1 = int(float(df[i][2].strip()))
        number_1 = float(number_1)
        df_citations = np.append(df_citations,int(number_1))
    except:
        df_citations = np.append(df_citations,"NAN")
    try:
        number_2 = int(float(df[i][0].strip()))
        number_2 = float(number_2)
        df_year = np.append(df_year, int(number_2))
    except:
        df_year = np.append(df_year,"NAN")
df_year, df_citations = zip(*sorted(zip(df_year, df_citations)))
df_year,df_citations = NAN_clearer(df_year,df_citations)
df_citations,df_year = NAN_clearer(df_citations,df_year)
df_citations = [int(i) for i in df_citations]
df_year = [int(i) for i in df_year]
print(df_year)
#plt.scatter(df_year,df_citations)
plt.xlabel("Year")

plt.ylabel("# of Citations")

plt.title("Citations vs. Year")
coef = np.polyfit(df_year,df_citations,3)
poly1d_fn = np.poly1d(coef)
# poly1d_fn is now a function which takes in x and returns an estimate for y

plt.plot(df_year,df_citations, 'x', df_year, poly1d_fn(df_year), '--k') #'--k'=black dashed line, 'yo' = yellow circle marker

plt.xlim(1985, 2022)
plt.ylim(0, 100)
plt.show()