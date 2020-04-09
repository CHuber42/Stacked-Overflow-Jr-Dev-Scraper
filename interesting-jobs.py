import urllib.request
from bs4 import BeautifulSoup
import csv
from selenium import webdriver
import pandas as pd
from selenium.webdriver.chrome.options import Options
import os
import time
from selenium.common.exceptions import NoSuchElementException

#INITIALIZE BROWSER-DRIVER-CONFIGURATION
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920x1080")
chrome_driver = "C:/bin/phantomjs/bin/chromedriver.exe"

###################################################################

def get_stackoverflow_jobs() :

    all_results = []
    interesting_results = []

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

    extract_info(list_holder)


    #EXTRA PAGES lOOP
    for i in range(2, 13) :
        myurl = ("https://stackoverflow.com/jobs?c=usd&mxs=Junior&sort=p&pg={}").format(i)
        driver.get(myurl)
        list_found = False
        print("Now Processing Page: ", i)

        while list_found == False :
            try:
                list_holder = driver.find_element_by_xpath('/html/body/div[4]/div[2]/div[2]/div[2]/div[1]/div[1]/div')
                if list_holder is not None:
                    list_found = True
            except NoSuchElementException:
                print("List Not Yet Found. Waiting...")
                time.sleep(2)
                pass

        extract_info(list_holder)



    driver.close()
##################################################################

def extract_info(jobs_list) :






###################################################################3



def main () :
    get_stackoverflow_jobs()





main()
