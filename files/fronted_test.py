from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# Setting up Chrome driver service
driver_service = Service("C:/Users\pavel/OneDrive/שולחן העבודה/chromeDrive")
driver = webdriver.Chrome(service=driver_service)

# Accessing the website
driver.get('http://127.0.0.1:5001/users/get_user_data/1')

user_name = driver.find_element(By.ID, value="user")

# Check if the username exists
if user_name.is_displayed():
    print('element is displayed')
else:
    print('no such element')

print(user_name.text)

time.sleep(20)

# Close the browser window
driver.quit()
