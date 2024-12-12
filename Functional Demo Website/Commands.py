#get commands / application specific commands - title,get(),current_url,page_source

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import element_to_be_clickable
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver= webdriver.Chrome()
driver.get("https://demo.automationtesting.in/Register.html")
driver.maximize_window()
print(driver.title)
print(driver.current_url)
#print(driver.page_source)

#Conditional Commands - (is_displayed(),is_enabled(),is_selected())
rd_male= driver.find_element(By.XPATH,"//input[@value='Male']")
rd_female = driver.find_element(By.XPATH,"//input[@value='FeMale']")
print(rd_male.is_selected())
print(rd_female.is_selected())
rd_male.click()
print(rd_male.is_selected())
print(rd_female.is_selected())
rd_female.click()
print(rd_male.is_selected())
print(rd_female.is_selected())

#navigational commands - Refresh, forward,back,get()
face= driver.find_element(By.XPATH,"//a[normalize-space()='WebTable']")
face.click()
print(driver.title)
driver.back()
driver.refresh()
print(driver.title)
driver.forward()
print(driver.title)

#To.navigate() commands
driver.get("https://www.google.com/")
search_box= WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.CLASS_NAME,"gLFyf")))
search_box.send_keys("Geekforgeeks org")
btn= WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.NAME,"btnK")))
btn.click()
driver.get("https://www.facebook.com/")
email_field= WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID,"email")))
email_field.send_keys("Kiruthika")
driver.refresh()
driver.back()
print(driver.title)
driver.forward()
print(driver.title)







