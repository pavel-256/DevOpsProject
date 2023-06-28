import requests

# Example test code
response = requests.get('http://127.0.0.1:5000/users/1')
print(response.json())