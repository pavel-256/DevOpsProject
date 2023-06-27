import requests

# Define the base URL of the Dockerized application
base_url = "http://localhost:5000"

# Perform a GET request to the API endpoint
response = requests.get(f"{base_url}/api/endpoint")

# Check the response status code
if response.status_code == 200:
    print("Dockerized app is running successfully!")
    print("Response:", response.text)
else:
    print("Error: Failed to access the Dockerized app.")
    print("Response status code:", response.status_code)
