from selenium import webdriver 
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
import secrets , path

email = secrets.email
passwd = secrets.password

options = Options()
options.set_preference('permissions.default.microphone', 1)
options.set_preference('permissions.default.camera', 1)

url = "https://classroom.google.com/u/0/"
Opath = "firefoxDriver/geckodriver"
def __cow__(email , password):
    web = webdriver.Firefox(executable_path=Opath , options = options)
    web.get(url )
    time.sleep(2)
    emailputting = web.find_element_by_xpath(path.emailpath)
    buttonclicking = web.find_element_by_xpath(path.buttonxpath)
    emailputting.send_keys(email)
    buttonclicking.click()
    time.sleep(2)
    password_but = web.find_element_by_xpath(path.passwordbuttonxpath)
    passthis=web.find_element_by_xpath(path.passwordXpath)
    passthis.send_keys(passwd)
    password_but.click()
    time.sleep(2)
    classroom = web.find_element_by_xpath(path.classroompath)
    classroom.click()
    time.sleep(2)
    meet = web.find_element_by_xpath(path.joinmeetxpath)
    meet.click()
    time.sleep(5)
    meetbutton_click = web.find_element_by_xpath(path.meetbutton)
    meetbutton_click.click()
    time.sleep(7)
    
    join_button.click()


   
    
__cow__(email,passwd)