from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome(service=Service("C:/Users\pavel/OneDrive/שולחן העבודה/chromeDrive"))

driver.get('http://127.0.0.1:5000/users/1')
