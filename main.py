from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Chrome driver setup
service = Service(executable_path="./chromedriver") #object call
driver = webdriver.Chrome(service=service) 

# Navigate to any website
driver.get("https://google.com")

# This is a timeout based on input given it will crash the program if the element doesn't exist 
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "gLFyf"))
)

# Search by class name getting class name from original google search bar using inspect
input_element = driver.find_element(By.CLASS_NAME, "gLFyf") 

# If there is anything in input field it will clear as sent_keys will append the exsisting input
input_element.clear()

# Passing text string and hitting search key using Keys
input_element.send_keys("FACEBOOK" + Keys.ENTER) 

# This is a timeout based on input given it will crash the program if the element doesn't exist 
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Facebook"))
)

# To click on link using text
link = driver.find_element(By.PARTIAL_LINK_TEXT, "Facebook")
link.click()

# Let driver stay there for some time
time.sleep(10)

# Close driver
driver.quit()



