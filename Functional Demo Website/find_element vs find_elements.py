from selenium import webdriver
from selenium.webdriver.common.by import By

driver= webdriver.Chrome()
driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()
driver.implicitly_wait(10)
##Find_element - Returns the single element

#Locating the single element
driver.find_element(By.ID,"small-searchterms").send_keys("Mobiles")


#Locating the single element with multiple matches(webelements)
element = driver.find_element(By.XPATH,"//div[@class='footer-upper']//a")
print(element.text)

#Element not available then throw NoSuchElement Exception
login_element=driver.find_element(By.LINK_TEXT,"Log in")
login_element.click()

##Find_elements - Returns the multiple elements

#Locating multiple elements using find_elements
elements=driver.find_elements(By.XPATH,"//div[@class='footer-upper']//a")
print(len(elements))
for ele in elements:
    print(ele.text)

#Locator matching with single web element
elements2= driver.find_elements(By.ID,"small-searchterms")
print(len(elements2))
elements2[0].send_keys("Mobiles")

driver.close()



