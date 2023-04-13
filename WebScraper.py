from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import numpy as np
import pandas as pd


driver = webdriver.Chrome()
driver.implicitly_wait(4)
driver.get("https://scholar.google.com/scholar?hl=en&as_sdt=0%2C10&q=ethics+in+artificial+intelligence&oq=ethi")
time.sleep(15)

#Uses the x_path of the next button on google-scholar's webpage to move to the next page
def next_page():
    next_button = driver.find_element_by_xpath("//*[@id=\"gs_n\"]/center/table/tbody/tr/td[12]/a/b")
    next_button.click()
#Find the last instance of a particular character, and returns the string from that instance onwards
def sub_last_char(full_string,char):
    index_full = len(full_string) -1
    while full_string[index_full] != char:
        index_full = index_full - 1
    return full_string[index_full:len(full_string)]

#returns the general information for each search result - mainly used for testing the program
def getresults():
    result_list = driver.find_elements_by_xpath("//*[@id=\"gs_res_ccl_mid\"]")
    for i in result_list:
        print(i.text)

# returns the name/title of each result
def getnames():
    n = 1
    names = np.array([])
    result_list = driver.find_elements_by_xpath("//*[@id=\"gs_res_ccl_mid\"]")
    for i in result_list:
        holder = i.find_elements_by_xpath(".//h3[@class=\"gs_rt\"]")
        for element in holder:
            print(element.text)
            names = np.append(names,element.text)
    return names

def getYear(string_gendata):
    final_int = "N/A"
    index_last = len(string_gendata) - 1
    for character in string_gendata:
        char_1 = string_gendata[index_last - 3]
        char_2 = string_gendata[index_last - 2]
        char_3 = string_gendata[index_last - 1]
        char_4 = string_gendata[index_last]
        try:
            number_year = int(char_1+char_2+char_3+char_4)
            if number_year > 1000:
                final_int = number_year
                return final_int
        except:
            pass
        index_last = index_last - 1
    return final_int

#returns the main body of data for each search result, which contains much of the information we desire
def getGenData():
    data = np.array([])
    result_list = driver.find_elements_by_xpath("//*[@id=\"gs_res_ccl_mid\"]")
    for i in result_list:
        holder = i.find_elements_by_xpath(".//div[@class=\"gs_a\"]")
        for element in holder:
            print(element.text)
            data = np.append(data,element.text)
    return data

#returns the name of the website for each search result
def getcitation():
    citation = np.array([])
    result_list = driver.find_elements_by_xpath("//*[@id=\"gs_res_ccl_mid\"]")
    for i in result_list:
        holder = i.find_elements_by_xpath(".//div[@class=\"gs_fl\"]")
        for element in holder:
            try:
                holder_2 = element.text[19]
                holder_2 = int(holder_2)
                try:
                    holder_2 = int(str(holder_2) + element.text[20])
                except:
                    pass
            except:
                holder_2 = "N/A"

            if (isinstance(holder_2,int)):
                citation = np.append(citation, holder_2)
            else:
                citation = np.append(citation,"N/A")
    return citation

# Sorts the general data for the information we weant - specifically the author names and the list of websites we found
def sortGenData(gendata):
    authorlist = np.array([])
    websitelist = np.array([])
    yearlist = np.array([])
    for stringss in gendata:
        print(stringss)
        yearlist = np.append(yearlist,getYear(stringss))
        try:
            authorlist = np.append(authorlist,stringss[0:stringss.index("-")+1])
        except:
            authorlist = np.append(authorlist,"N/A")
        try:
            websitelist = np.append(websitelist,sub_last_char(stringss,"-"))
        except:
            websitelist = np.append(websitelist,"N/A")
    return authorlist,websitelist,yearlist

#removes extra spaces and hyphens to clean up the data
def cleanup(some_data):
    some_data = some_data.replace("-"," ")
    some_data = some_data.strip()
    return some_data

#sets up general arrays
getresults()
Names = getnames()
Gendata = getGenData()
Citations = getcitation()

 #sets up a loop to search and gather information using the methods above for number_of_pages - just change this
 #variable to get more or less data
number_of_pages = 60
while number_of_pages > 0:
    Names = np.append(Names,getnames())
    Gendata = np.append(Gendata,getGenData())
    Citations = np.append(Citations,getcitation())
    next_page()
    number_of_pages = number_of_pages - 1
    print(Names)
    print(Gendata)
    print(Citations)
    time.sleep(10)


Authorlist,Websitelist,Yearlist = sortGenData((Gendata[1:len(Gendata)-1]))

#cleaning up data and results using functions defined above

indexer = 0
for i in Authorlist:
    Authorlist[indexer] = cleanup(i)
    indexer = indexer+1

indexer = 0
for i in Websitelist:
    Websitelist[indexer] = cleanup(i)
    indexer = indexer+1


Names = list(filter(None, Names))
Citations = list(filter(None, Citations))
Authorlist = list(filter(None, Authorlist))
Websitelist = list(filter(None, Websitelist))

# Disaplying data for testing reasons
print("START ===========================================================================")
print("\n")
print("\n")
print(Names)
print("\n")
print("\n")
print(Citations)
print("\n")
print("\n")
print(Authorlist)
print("\n")
print("\n")
print(Websitelist)

print("\n")
print(Yearlist)
#first and last result are messed up for two arrays so we simply remove them here
Names = np.delete(Names,0)
Names = np.delete(Names,len(Names)-1)
Citations = np.delete(Citations,0)
Citations = np.delete(Citations,len(Citations) - 1)

# changing data into correct format for pandas so we can export it to an excel file
print(str(len(Names))+  str(len(Citations)) + str(len(Authorlist)) + str(len(Websitelist))+ str(len(Yearlist)))
#driver.close()
table_2 = np.array([Names,Citations,Authorlist,Websitelist,Yearlist])
df_2 = pd.DataFrame(table_2)

#Last line exports data to an excel file names "output_50.xlsx"
df_2.to_excel("output_100.xlsx")
