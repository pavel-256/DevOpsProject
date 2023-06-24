import requests
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


def testing():
    try:
        # Send a POST request to add a new user
        response_get_front = requests.get('http://127.0.0.1:5000/stop_server')
        response_get_front.raise_for_status()

        response_get_backend = requests.get('http://127.0.0.1:5001/stop_server')
        response_get_backend.raise_for_status()

    except requests.exceptions.RequestException as e:
        print(f'Clean Test failed with  {e}')


testing()



