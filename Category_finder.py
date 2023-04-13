from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import numpy as np
import pandas as pd

df = pd.read_excel(open('output_10.xlsx', 'rb'))
df_names = np.array([])
print(df[2][2])
for i in df:
    df_names = np.append(df_names,df[i][2])
print(df_names)
df_names = np.delete(df_names,0)
driver = webdriver.Chrome()
def array_cleaner(array):
    ones_total = array.tolist().count("1")
    twos_total = array.tolist().count("2")
    if ones_total + twos_total > 0:
        return (ones_total + (2*twos_total))/(ones_total+twos_total)
    else:
        return 0

def array_cleaner2(array):
    zeros_total = array.tolist().count("0")
    ones_total = array.tolist().count("1")
    twos_total = array.tolist().count("2")
    if ones_total + twos_total > 0:
        return ones_total,twos_total,zeros_total
    else:
        return 0,0,0
def scrape_person(name_person):
    job_list = np.array([])
    if name_person.count(",") > 0:
        array_hold = name_person.split(",")
        for i in array_hold:
            job_list = np.append(job_list,scrape_person(i))
    else:
        letters_in_name = len(name_person)
        first_search = driver.find_element_by_xpath("//*[@id=\"gs_hdr_tsi\"]")
        first_search.send_keys(name_person)
        time.sleep(2)
        first_search.send_keys(Keys.ENTER)
        people_found = driver.find_elements_by_xpath("//*[@id=\"gsc_sa_ccl\"]/div/div/div")
        for i in people_found:
            holder = i.find_elements_by_xpath(".//div[@class=\"gs_ai_int\"]")
            for element in holder:
                print(element.text)
                time.sleep(1)
                job_list = np.append(job_list, element.text)
        first_search = driver.find_element_by_xpath("//*[@id=\"gs_hdr_tsi\"]")
        while letters_in_name > 0:
            first_search.send_keys(Keys.BACK_SPACE)
            letters_in_name = letters_in_name - 1

        n = 0
        for i in job_list:
            if job_list[n] == "0" or job_list[n] == "1":
                pass
            elif i.upper().count("MATH") > 0 or i.upper().count("LINEAR")> 0 or i.count("0") > 0 or i.upper().count("LINEAR")> 0 or i.upper().count("NUMBER")> 0 or i.upper().count("ALGEBRA")> 0:
                job_list[n] = "2"
            elif i.upper().count("COMPUT") > 0 or i.count("1") > 0 or i.upper().count("NETWORK") > 0 or i.upper().count("MACHINE") > 0 or i.upper().count("CODING") or i.upper().count("DATA") > 0:
                job_list[n] = "1"
            else:
                job_list[n] = "0"
            n = n+1
    time.sleep(2)
    return job_list

wait = driver.implicitly_wait(4)
driver.get("https://scholar.google.com/citations?hl=en&view_op=search_authors&mauthors=&btnG=")
wait
clean_array = np.array([])
cleaner_array = np.array([])
for person in df_names:
    uncleaned_array = scrape_person(person)
    clean_array = np.append(clean_array,array_cleaner(uncleaned_array))
    #cleaner_array  testing shinanigans
    time.sleep(6)
print(clean_array)
print(len(df_names))
print(len(clean_array))
df = df.append(clean_array)
df.to_excel("output_12.xlsx")
