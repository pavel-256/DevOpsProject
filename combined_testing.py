import requests
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


def testing():
    try:
        # Send a POST request to add a new user
        response_post = requests.post('http://127.0.0.1:5000/users/2', json={"user_name": "Parker"})
        response_post.raise_for_status()

        # Send a GET request to retrieve user data
        response_get = requests.get('http://127.0.0.1:5000/users/1')
        response_get.raise_for_status()
        result = json.loads(response_get.text)
        print(result['user name'])

        # Use Selenium to retrieve user data
        driver_path = "C:/Users/pavel/OneDrive/שולחן העבודה/chromeDrive"
        driver = webdriver.Chrome(service=Service(driver_path))
        driver.get('http://127.0.0.1:5001/users/get_user_data/1')
        user_name = driver.find_element(By.ID, value="user").text
        if user_name != result['user name']:
            print('Test failed')

    except requests.exceptions.RequestException as e:
        print(f'Test failed with {e}')


testing()
