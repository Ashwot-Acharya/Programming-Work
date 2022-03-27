from selenium import webdriver
import re #re -> regular expression
from json import dumps
from pprint import pprint
import requests, os
path = "firefoxDriver/geckodriver"
url = "https://logisparktech.com/"
print(path)
regex = ('?:\+977[- ])?\d{1}-?\d{7}|^98.{8}')

try :
    
    # driver = webdriver.Firefox(executable_path=path) 
    # driver.get(url)
    # all_html :str = driver.find_element_by_tag_name('body').text
    # final['link'] = url
    # numbers = re.findall(r'01-\d\d\d\d\d\d|98\d\d\d\d\d\d\d|01\d\d\d\d\d\d|01-\d\d\d\d\d\d\d',all_html)
    # driver.close()
    # numbers = set(numbers)
    # numbers = list(numbers)
    # print(numbers)
    getall = requests.get(url)
    html = getall.text.find("a")
   
    print(html)
    

except Exception as E:
    print(E)
