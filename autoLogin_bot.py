from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

#setup webdriver
driver = webdriver.Chrome()

#Open login page
driver.get("https://example.com/")  #Replace with your actual login page 

#Find and fill login fields
try:
    username_field = driver.find_element(By.ID, "username_field") #Replace with your credentials
    password_field = driver.find_element(By.ID, "password_field")

    #Enter your login credentials
    username_field.send_kenys("username_field")  #Replace with your credentials
    password_field.send_keys("password_field")

    #Submit the form
    password_field.send_keys(Keys.RETURN)

    #Wait for page to load
    time.sleep(5)

    #Verify the login success
    if "example" in driver.current_url: # replace example with yout term
        print("Login successful!")

    else:
        print("Login failed!")

finally:
    driver.quit()
