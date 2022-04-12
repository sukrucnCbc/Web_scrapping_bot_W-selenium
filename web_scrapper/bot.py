import os
from selenium import webdriver 
import time

os.environ['PATH'] += r"C:/Selenium_Drivers/chromedriver.exe"

driver = webdriver.Chrome(executable_path=r'C:/Selenium_Drivers/chromedriver.exe')

driver.implicitly_wait(5)
driver.get("https://www.farmazon.com.tr/")
driver.implicitly_wait(5)
girisyap= driver.find_element_by_xpath("//*[@id='root']/div/main/div/div[1]/header/div/div/div[2]/a[2]")
girisyap.click()
time.sleep(2)
username = driver.find_element_by_name("loginUsername")
password = driver.find_element_by_name("loginPassword")
username.send_keys("sukrucan.cebeci")
password.send_keys("uEfpV-rnRWGa_wpWFXhMPnm6")
time.sleep(5)
girisyap_button = driver.find_element_by_xpath("//*[@id='root']/div/main/div/div/div/div[2]/div/form/button")
girisyap_button.click()
time.sleep(5)