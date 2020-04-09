import urllib.request
from bs4 import BeautifulSoup
import csv
from selenium import webdriver
import pandas as pd
from selenium.webdriver.chrome.options import Options
import os
import time
from selenium.common.exceptions import NoSuchElementException


keyword_dictionary = {}

#INITIALIZE BROWSER-DRIVER-CONFIGURATION
chrome_options = Options()
#chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920x1080")
chrome_driver = "C:/bin/phantomjs/bin/chromedriver.exe"

myurl = "https://stackoverflow.com/jobs?c=usd&mxs=Junior&sort=p"
driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=chrome_driver)
driver.get(myurl)



list_found = False


while list_found == False :
    try:
        list_holder = driver.find_element_by_xpath('/html/body/div[4]/div[2]/div[3]/div[2]/div[1]')
        if list_holder is not None:
            list_found = True
    except NoSuchElementException:
        print("List Not Yet Found. Waiting...")
        time.sleep(2)
        pass


tags = list_holder.find_elements_by_class_name('post-tag')
for i in tags :
    keyword = i.text
    if keyword in keyword_dictionary :
        keyword_dictionary[keyword] += 1
    else :
        keyword_dictionary[keyword] = 1




#EXTRA PAGES lOOP
for i in range(2, 13) :
    myurl = ("https://stackoverflow.com/jobs?c=usd&mxs=Junior&sort=p&pg={}").format(i)
    driver.get(myurl)
    list_found = False
    print("Now Processing Page: ", i)

    while list_found == False :
        try:
            list_holder = driver.find_element_by_xpath('/html/body/div[4]/div[2]/div[3]/div[2]/div[1]')
            if list_holder is not None:
                list_found = True
        except NoSuchElementException:
            print("List Not Yet Found. Waiting...")
            time.sleep(2)
            pass


    tags = list_holder.find_elements_by_class_name('post-tag')
    for i in tags :
        keyword = i.text
        if keyword in keyword_dictionary :
            keyword_dictionary[keyword] += 1
        else :
            keyword_dictionary[keyword] = 1



driver.close()

for key, value in sorted(keyword_dictionary.items(), key=lambda item: item[1], reverse=True):
    print("%s: %s" % (key, value))



#sortable_dict = {}
#for k,v in keyword_dictionary:
#    sortable_dict[v] = k








#extra page loop
# https://stackoverflow.com/jobs?c=usd&mxs=Junior&pg=2
