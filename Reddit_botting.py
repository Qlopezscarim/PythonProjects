
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import numpy as np
import pandas as pd
import sounddevice as sd
import speech_recognition as sr
print(sd.query_devices())
sd.default.dtype='int32', 'int32'
sd.default.device[0] = 18
fs = 44100  # Sample rate
seconds = 9  # Duration of recording

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-notifications")
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.implicitly_wait(10)
driver.get("https://www.guerrillamail.com/inbox")
def switch_to_window_path(xpath_1):
    iframe_captcha_thing = driver.find_element_by_xpath(xpath_1)
    driver.switch_to.frame(iframe_captcha_thing)
def send_keyse(xpath,text,text_1):
    holder = driver.find_element_by_xpath(xpath)
    holder.send_keys(text)
    time.sleep(1)
    holder.send_keys(Keys.ENTER)
def send_keyss(xpath,text):
    holder = driver.find_element_by_xpath(xpath)
    holder.send_keys(text)
def element_clicker(xpath_location):
    holder_1 = driver.find_element_by_xpath(xpath_location)
    holder_1.click()
    time.sleep(1)
def get_text(xpath_location):
    holder_2 = driver.find_element_by_xpath(xpath_location)
    return holder_2.text

# Gets email
element_clicker("//*[@id=\"gm-host-select\"]")
time.sleep(1)
element_clicker("//*[@id=\"gm-host-select\"]/option[2]")
temporary_email = get_text("//*[@id=\"inbox-id\"]") + "@guerrillamail.info"
print(temporary_email)


# Opens new tab for reddit and switches to it
driver.execute_script('''window.open("https://www.reddit.com/","_blank");''')
window_name = driver.window_handles[-1]
driver.switch_to.window(window_name=window_name)


#enters basic info to reddit
element_clicker("//*[@id=\"SHORTCUT_FOCUSABLE_DIV\"]/div[1]/header/div/div[2]/div/div[1]/a[2]")
time.sleep(1)
initial_frame = driver.find_element_by_tag_name('iframe')
driver.switch_to.frame(driver.find_element_by_tag_name('iframe'))
email_enter = driver.find_element_by_xpath("//*[@id=\"regEmail\"]")
print(email_enter)
email_enter.send_keys(temporary_email)
email_enter.send_keys(Keys.ENTER)


decision_maker = 0
try:
    time.sleep(3)
    potential_email = driver.find_element_by_xpath("/html/body/div/main/div[2]/div/div[2]/div/h1")
    if ("your" in potential_email.text):
        decision_maker = decision_maker+1
    else:
        ""
except:
    pass

if decision_maker ==1:
    #Responds to reddit auto-email process
    hold_loop = 0
    window_name = driver.window_handles[0]
    driver.switch_to.window(window_name=window_name)
    pull_out_of_loop = ""
    while hold_loop == 0:
        for element in driver.find_elements_by_tag_name("td"):
            if "reddit" in element.text or "Reddit" in element.text:
                hold_loop = hold_loop+1
                pull_out_of_loop = element
            else:
                ""
    pull_out_of_loop.click()
    container_Thing = driver.find_element_by_xpath("//*[@id=\"display_email\"]/div/div[2]/div/center/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[1]/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[4]/td/table/tbody/tr/td/a")
    link = container_Thing.get_attribute("href")
    print("here brother")
    print(link)
    print('''window.open('''+"\""+link+"\""+''',"_blank");''')
    driver.execute_script('''window.open('''+"\""+link+"\""+''',"_blank");''')
    #driver.execute_script('''window.open("https://www.reddit.com/","_blank");''')
else:
    #Start of Captcha workaround
    time.sleep(.6)
    potential_names = driver.find_elements_by_class_name("Onboarding__usernameSuggestion")
    for name in potential_names:
        used_name = name.text
    send_keyss("//*[@id=\"regUsername\"]",used_name)
    send_keyss("//*[@id=\"regPassword\"]","Cashmakers")
    time.sleep(3)
    ##for elemement_thing in driver.find_elements_by_tag_name('iframe'):
    ##    print("hello")
    ##    print(elemement_thing.text())

    #Start of CAPTCH SOLVING
    switch_to_window_path("//*[@id=\"g-recaptcha\"]/div/div/iframe")
    #driver.switch_to.frame(driver.find_elements_by_tag_name('iframe')[-1])
    captcha_thing = driver.find_element_by_xpath("//*[@id=\"recaptcha-anchor\"]/div[1]").click()

    time.sleep(3)

    #driver.switch_to.frame(initial_frame)\
    #driver.switch_to.default_content()
    driver.switch_to.parent_frame()
    all_frames = driver.find_element_by_xpath("/html/body/div[2]/div[2]/iframe")
    driver.switch_to.frame(all_frames)
    #driver.find_element_by_name("iframe")
    #WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.NAME, "c-49shgmbcmzw")))

    #switch_to_window_path("/html/body/div[2]/div[2]/iframe")
    time.sleep(3)
    element_clicker("//*[@id=\"recaptcha-audio-button\"]")
    time.sleep(1)
    element_clicker("//*[@id=\":2\"]")
    #start of audio code again
    myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
    sd.wait()  # Wait until recording is finished
    from scipy.io import wavfile

    wavfile.write('words_to_decode.wav', fs, myrecording)
    print("done")
    r = sr.Recognizer()
    with sr.AudioFile("words_to_decode.wav") as source:
        # listen for the data (load audio to memory)
        r.adjust_for_ambient_noise(source)
        audio_data = r.record(source)
        # recognize (convert from speech to text)
        text = r.recognize_google(audio_data, language='en-IN', show_all=True)
        print(text)
        captcha_decoded = text.get('alternative')[0].get('transcript')
    send_keyss("//*[@id=\"audio-response\"]",captcha_decoded)
    element_clicker("//*[@id=\"recaptcha-verify-button\"]")
    driver.switch_to.parent_frame()
    element_clicker("/html/body/div[1]/main/div[2]/div/div/div[3]/button")




# Start of reddit navigation after account creation
element_clicker("//*[@id=\"SHORTCUT_FOCUSABLE_DIV\"]/div[4]/div/div/div/header/div[1]/div[2]/button")
element_clicker("//*[@id=\"SHORTCUT_FOCUSABLE_DIV\"]/div[4]/div/div/div/div[1]/div/button[1]")
element_clicker("//*[@id=\"SHORTCUT_FOCUSABLE_DIV\"]/div[4]/div/div/div/div[1]/div/button[2]")
element_clicker("//*[@id=\"SHORTCUT_FOCUSABLE_DIV\"]/div[4]/div/div/div/div[1]/div/button[3]")
element_clicker("//*[@id=\"SHORTCUT_FOCUSABLE_DIV\"]/div[4]/div/div/div/div[2]/button")
element_clicker("//*[@id=\"SHORTCUT_FOCUSABLE_DIV\"]/div[4]/div/div/div/div[1]/div/div[2]")

def next_page():
    next_button = driver.find_element_by_xpath("//*[@id=\"gs_n\"]/center/table/tbody/tr/td[12]/a/b")
    next_button.click()
def sub_last_char(full_string,char):
    index_full = len(full_string) -1
    while full_string[index_full] != char:
        index_full = index_full - 1
    return full_string[index_full:len(full_string)]
def getresults():
    result_list = driver.find_elements_by_xpath("//*[@id=\"gs_res_ccl_mid\"]")
    for i in result_list:
        print(i.text)
