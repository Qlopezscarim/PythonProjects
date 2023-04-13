from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import numpy as np
import pandas as pd
name_array = np.array([])
def scroll_down(xpath):
    loader = driver.find_element_by_xpath(xpath)
    loader.send_keys(Keys.PAGE_DOWN)
driver = webdriver.Chrome()
driver.implicitly_wait(4)
driver.get("https://www.google.com/maps/search/daycares+near+me/@26.7899333,-80.0870147,15z/data=!3m1!4b1")
driver.implicitly_wait(4)
scroll_down("//*[@id=\"pane\"]/div/div[1]/div/div/div[2]/div[1]")
scroll_down("//*[@id=\"pane\"]/div/div[1]/div/div/div[2]/div[1]")
driver.implicitly_wait(4)
scroll_down("//*[@id=\"pane\"]/div/div[1]/div/div/div[2]/div[1]")
scroll_down("//*[@id=\"pane\"]/div/div[1]/div/div/div[2]/div[1]")


driver.implicitly_wait(4)
sorter = driver.find_elements_by_xpath("//*[@id=\"pane\"]/div/div[1]/div/div/div[2]/div[1]")

#print(sorter.text.split("\n"))
number = 0
for header in sorter:
    print(header.text)
    string_unfiltered = header.text
    potential_names = header.text.split("\n")
    number = number + 1
    print(number)
#for name in potential_names:
#    try:
#        driver.find_elements_by_css_selector("[aria-label=XXXX]")
#        name_array = np.append(name_array, name)
#    except:
#        pass


string_unfiltered = string_unfiltered.split("\n")
print("-----------------------------------------------------------------")
print(string_unfiltered)
capatilized_array = np.array([])
for string_element in string_unfiltered:
    greater_split = string_element.split(" ")
    for word in greater_split:
        if word[0].isupper():
            capatilized_array = np.append(capatilized_array,word)
        else:
            pass




