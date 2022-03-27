from selenium import webdriver
import os
driver = webdriver.Firefox(executable_path="./firefoxDriver/geckodriver")
from selenium.webdriver.common.by import By
driver.get("https://doko.dwit.edu.np/class/show/1?stream=BSc.CSIT")
alllinks = driver.find_elements(By.XPATH,'//html/body/div[2]/section/section/section/div/div/a/p')
for link in alllinks:
    print(link.text)

finalPath = os.path.join(os.getcwd(),"MyText.txt")
print(finalPath)

for x in alllinks:
    name = x.text
    filename = x.text + ".txt"
    d = open(filename,"w")
    d.write("i am "+ name  )
driver.close()
 