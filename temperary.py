import numpy as np
import pandas as pd
"""
replace string_1 with output from category finder, then take that output and paste it into
df_profession, this is an easier way of reformatting everything than some alternative methods
"""
string_1 = """2.         1.         2.         1.         0.         1.
 2.         0.         1.         1.         2.         1.
 2.         1.         0.         1.         2.         0.
 1.         0.         1.         0.         0.         1.
 0.         1.         0.         1.         1.66666667 1.
 1.         0.         0.         1.33333333 2.         1.2
 2.         0.         1.         1.22222222 0.         0.
 0.         2.         0.         1.33333333 0.         0.
 1.16666667 0.         0.         1.         1.         1.
 1.         0.         1.5        2.         1.         0.
 1.         0.         0.         1.33333333 1.         0.
 0.         0.         0.         0.         0.         2.
 0.         0.         0.         1.         0.         0.
 0.         0.         1.25       0.         1.         0.
 0.         0.         1.         1.66666667 0.         1.
 1.         0.         2.         1.         1.         0.
 0.         0.         0.         1.         1.         0.
 0.         1.         0.         0.         1.5        1.
 2.         1.         0.         2.         0.         1.
 2.         0.         1.         0.         1.33333333 0.
 1.         1.5        0.         1.         0.         2.
 1.         0.         0.         1.         1.         1.66666667
 0.         1.         0.         1.         0.         1.
 1.         2.         2.         2.         0.         1.
 0.         2.         0.         1.         0.         0.
 0.         0.         0.         0.         0.         0.
 0.         1.         1.         0.         0.         1.
 0.         0.         0.         1.         0.         1.
 1.         2.         0.         0.         0.         1.
 0.         0.         1.5        0.         0.         1.5
 0.         0.         0.         2.         2.         0.
 2.         0.         1.         2.         1.         0.
 1.         0.         0.         0.         1.125      0.
 2.         2.         1.33333333 1.         1.5        1.
 0.         0.         1.         1.         0.         1.
 1.         1.         0.         0.         0.         2.
 1.5        2.         0.         0.         1.         1.
 1.         1.         2.         0.         1.         2.
 1.         0.         0.         1.33333333 1.         0.
 0.         0.         1.5        1.         1.         0.
 0.         0.         0.         0.         0.         1.
 1.         1.5        0.         1.16666667 1.66666667 0.
 1.         0.         1.         1.         1.         2.
 0.         0.         1.5        0.         0.         1.
 0.         1.         1.         1.16666667 0.         2.
 0.         0.         1.         2.         1.         1.
 0.         0.         0.         0.         1.         2.
 0.         0.         0.         0.         1.5        0.
 2.         0.         0.         1.         1.         0.
 0.         0.         1.66666667 0.         0.         1.
 1.         1.5        1.         1.         2.         0.
 0.         0.         1.         1.5        0.         2.
 0.         1.         0.         0.         0.         1.5
 1.         0.         1.22222222 0.         0.         2.
 0.         1.5        0.         2.         1.125      1.
 0.         0.         0.         1.66666667 1.         2.
 0.         1.         0.         1.         0.         0.
 1.         1.         1.         0.         1.         2.
 0.         1.         0.         0.         0.         1.
 0.         0.         0.         1.         1.         1.
 1.         1.         1.         1.         1.         1.
 1.66666667 0.         1.         1.         0.         1.
 1.22222222 1.         0.         1.         2.         0.
 0.         0.         0.         1.33333333 1.         1.
 1.         1.         1.         1.         1.         0.
 1.         0.         1.         1.         1.         1.
 1.         0.         1.33333333 0.         2.         0.
 0.         0.         0.         1.         0.         0.
 0.         1.         0.         0.         0.         1.
 1.         0.         1.         0.         0.         0.
 0.         0.         1.         0.         0.         1.
 1.         1.2        1.         0.         1.         0.
 1.         1.         1.         0.         1.18181818 0.
 1.         0.         0.         0.         1.5        1.
 0.         1.         0.         0.         1.         0.
 1.         1.         1.         0.         1.         0.
 0.         1.         1.         1.         1.         0.
 1.         0.         0.         0.         1.33333333 0.
 0.         0.         0.         0.         0.         1.
 1.         2.         1.         1.         0.         1.
 1.         0.         1.         0.         0.         1.
 0.         1.         1.         1.         0.         0.
 0.         1.         0.         2.         0.         0.
 0.         0.         2.         1.         1.         2.
 0.         0.         0.         1.         0.         2.
 0.         0.         1.         0.         0.         1.
 2.         0.         2.         2.         0.         2.
 1.         2.         1.         0.         2.         0.
 1.         0.         2.         1.         2.         2.
 1.125      1.33333333 0.         1.         1.         0.
 0.         1.5        1.33333333 1.         1.33333333 2.
 0.         1.33333333 0.         0.         2.         0.
 1.         2.         0.         1.         1.         1.
 1.         0.         0.         1.         0.         1.
 0.         0.         0.         2.         1.         1.
 0.         0.         0.         1.         0.         0.
 0.         0.         1.         1.         0.         0.
 2.         2.         2.         0.         1.         0.
 0.         2.         0.         1.         1.         0.
 1.         1.         0.         0.         1.         1.
 0.         0.         0.         1.         1.33333333 0.
 0.         1.        """
string_1 = string_1.replace("         "," ")
string_1 = string_1.replace("  "," ")
string_1 = string_1.replace("  "," ")
string_1 = string_1.replace("  "," ")
string_1 = string_1.replace("  "," ")
string_1 = string_1.replace(" ",",")
###Print here cuz why not true true
df_profession = np.array([2.,1.,2.,1.,0.,1.
,2.,0.,1.,1.,2.,1.
,2.,1.,0.,1.,2.,0.
,1.,0.,1.,0.,0.,1.
,0.,1.,0.,1.,1.66666667,1.
,1.,0.,0.,1.33333333,2.,1.2
,2.,0.,1.,1.22222222,0.,0.
,0.,2.,0.,1.33333333,0.,0.
,1.16666667,0.,0.,1.,1.,1.
,1.,0.,1.5,2.,1.,0.
,1.,0.,0.,1.33333333,1.,0.
,0.,0.,0.,0.,0.,2.
,0.,0.,0.,1.,0.,0.
,0.,0.,1.25,0.,1.,0.
,0.,0.,1.,1.66666667,0.,1.
,1.,0.,2.,1.,1.,0.
,0.,0.,0.,1.,1.,0.
,0.,1.,0.,0.,1.5,1.
,2.,1.,0.,2.,0.,1.
,2.,0.,1.,0.,1.33333333,0.
,1.,1.5,0.,1.,0.,2.
,1.,0.,0.,1.,1.,1.66666667
,0.,1.,0.,1.,0.,1.
,1.,2.,2.,2.,0.,1.
,0.,2.,0.,1.,0.,0.
,0.,0.,0.,0.,0.,0.
,0.,1.,1.,0.,0.,1.
,0.,0.,0.,1.,0.,1.
,1.,2.,0.,0.,0.,1.
,0.,0.,1.5,0.,0.,1.5
,0.,0.,0.,2.,2.,0.
,2.,0.,1.,2.,1.,0.
,1.,0.,0.,0.,1.125,0.
,2.,2.,1.33333333,1.,1.5,1.
,0.,0.,1.,1.,0.,1.
,1.,1.,0.,0.,0.,2.
,1.5,2.,0.,0.,1.,1.
,1.,1.,2.,0.,1.,2.
,1.,0.,0.,1.33333333,1.,0.
,0.,0.,1.5,1.,1.,0.
,0.,0.,0.,0.,0.,1.
,1.,1.5,0.,1.16666667,1.66666667,0.
,1.,0.,1.,1.,1.,2.
,0.,0.,1.5,0.,0.,1.
,0.,1.,1.,1.16666667,0.,2.
,0.,0.,1.,2.,1.,1.
,0.,0.,0.,0.,1.,2.
,0.,0.,0.,0.,1.5,0.
,2.,0.,0.,1.,1.,0.
,0.,0.,1.66666667,0.,0.,1.
,1.,1.5,1.,1.,2.,0.
,0.,0.,1.,1.5,0.,2.
,0.,1.,0.,0.,0.,1.5
,1.,0.,1.22222222,0.,0.,2.
,0.,1.5,0.,2.,1.125,1.
,0.,0.,0.,1.66666667,1.,2.
,0.,1.,0.,1.,0.,0.
,1.,1.,1.,0.,1.,2.
,0.,1.,0.,0.,0.,1.
,0.,0.,0.,1.,1.,1.
,1.,1.,1.,1.,1.,1.
,1.66666667,0.,1.,1.,0.,1.
,1.22222222,1.,0.,1.,2.,0.
,0.,0.,0.,1.33333333,1.,1.
,1.,1.,1.,1.,1.,0.
,1.,0.,1.,1.,1.,1.
,1.,0.,1.33333333,0.,2.,0.
,0.,0.,0.,1.,0.,0.
,0.,1.,0.,0.,0.,1.
,1.,0.,1.,0.,0.,0.
,0.,0.,1.,0.,0.,1.
,1.,1.2,1.,0.,1.,0.
,1.,1.,1.,0.,1.18181818,0.
,1.,0.,0.,0.,1.5,1.
,0.,1.,0.,0.,1.,0.
,1.,1.,1.,0.,1.,0.
,0.,1.,1.,1.,1.,0.
,1.,0.,0.,0.,1.33333333,0.
,0.,0.,0.,0.,0.,1.
,1.,2.,1.,1.,0.,1.
,1.,0.,1.,0.,0.,1.
,0.,1.,1.,1.,0.,0.
,0.,1.,0.,2.,0.,0.
,0.,0.,2.,1.,1.,2.
,0.,0.,0.,1.,0.,2.
,0.,0.,1.,0.,0.,1.
,2.,0.,2.,2.,0.,2.
,1.,2.,1.,0.,2.,0.
,1.,0.,2.,1.,2.,2.
,1.125,1.33333333,0.,1.,1.,0.
,0.,1.5,1.33333333,1.,1.33333333,2.
,0.,1.33333333,0.,0.,2.,0.
,1.,2.,0.,1.,1.,1.
,1.,0.,0.,1.,0.,1.
,0.,0.,0.,2.,1.,1.
,0.,0.,0.,1.,0.,0.
,0.,0.,1.,1.,0.,0.
,2.,2.,2.,0.,1.,0.
,0.,2.,0.,1.,1.,0.
,1.,1.,0.,0.,1.,1.
,0.,0.,0.,1.,1.33333333,0.
,0.,1.])

df = pd.read_excel(open('output_12.xlsx', 'rb'))
df_title = np.array([])
df_citations = np.array([])
df_names = np.array([])
df_website = np.array([])
df_year = np.array([])

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

print(df_title)
df_title = np.delete(df_title,0)
df_citations = np.delete(df_citations,0)
df_names = np.delete(df_names,0)
df_website = np.delete(df_website,0)
df_year = np.delete(df_year,0)
df_title = list(filter(None, df_title))
df_citations = list(filter(None, df_citations))
df_names = list(filter(None, df_names))
df_website = list(filter(None, df_website))
df_year = list(filter(None,df_year))
#df_profession = np.delete(df_profession,0)
#df_profession = np.delete(df_profession,len(df_profession)-1)
df_profession = list(df_profession)

print(len(df_title))
print(len(df_citations))
print(len(df_names))
print(len(df_website))
print(len(df_year))
print(len(df_profession))

table_2 = np.array([df_title,df_citations,df_names,df_website,df_year,df_profession])
print(table_2)
df_2 = pd.DataFrame(table_2)
print(df.dtypes)
df_2.to_excel("output_13.xlsx")