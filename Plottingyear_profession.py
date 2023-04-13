from matplotlib import pyplot as plt

import time
import numpy as np
import pandas as pd

def NAN_clearer(array_1,array_2):
    last_index = len(array_1) - 1
    for element in array_1:
        if array_1[last_index] == "nan":
            array_1 = np.delete(array_1,last_index)
            array_2 = np.delete(array_2,last_index)
        last_index = last_index - 1
    return array_1,array_2
def NAN_clearer_3(array_1,array_2,array_3):
    last_index = len(array_1) - 1
    for element in array_1:
        if array_1[last_index] == "nan":
            array_1 = np.delete(array_1,last_index)
            array_2 = np.delete(array_2,last_index)
            array_3 = np.delete(array_3,last_index)
        last_index = last_index - 1
    return array_1,array_2,array_3
df = pd.read_excel(open('output_13.xlsx', 'rb'))
df_title = np.array([])
df_citations = np.array([])
df_names = np.array([])
df_website = np.array([])
df_year = np.array([])
df_professions = np.array([])

print(df[2][1])
for i in df:
    df_title = np.append(df_title,df[i][0])
for i in df:
    df_citations = np.append(df_citations,df[i][1])
for i in df:
    df_names = np.append(df_names,df[i][2])
for i in df:
    df_website = np.append(df_website,df[i][3])
for i in df:
    df_year = np.append(df_year,df[i][4])
for i in df:
    df_professions = np.append(df_professions,df[i][5])

print(df_title)
df_title = np.delete(df_title,0)
df_citations = np.delete(df_citations,0)
df_names = np.delete(df_names,0)
df_website = np.delete(df_website,0)
df_year = np.delete(df_year,0)
df_professions = np.delete(df_professions,0)

df_names,df_professions,df_citations = NAN_clearer_3(df_names,df_professions,df_citations)
df_professions,df_citations = NAN_clearer(df_professions,df_citations)
df_citations,df_professions = NAN_clearer(df_citations,df_professions)
df_professions, df_citations = zip(*sorted(zip(df_professions, df_citations)))
df_citations = [float(i) for i in df_citations]
df_professions = [float(i) for i in df_professions]
df_citations = [int(i) for i in df_citations]
df_professions = [int(i) for i in df_professions]
plt.ylabel("# of Citations")

plt.title("Citations vs. Year")
coef = np.polyfit(df_professions,df_citations,99)
poly1d_fn = np.poly1d(coef)
plt.plot(df_professions,df_citations, 'x',df_professions,poly1d_fn(df_professions),'--k')
plt.xlim(0, 2)
plt.ylim(3, 10)
plt.show()

print(df_professions)
print(df_citations)
print(len(df_citations))
