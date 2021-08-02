#!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from sty import fg, rs
import time

chrome_options = Options()
chrome_options.add_argument('--log-level=3')

usernames_file = "names.txt"
base_url = "https://www.twitch.tv/"

browser = webdriver.Chrome()
f = open(usernames_file, 'r')

available = False

names = [n for n in f.read().splitlines() if n != '']
print(names)
for name in names:
    #make request for every name
    browser.get(base_url+name)

    time.sleep(2)

    elements = browser.find_elements_by_css_selector('p')
    
    for element in elements:
        if "time machine" in element.text:
            print(fg.green + name + " is AVAILABLE!" + fg.rs)
            available = True
    
    if(not available):
        print(fg.red + name + ' is NOT available' + fg.rs)
    available = False

browser.close()
    


