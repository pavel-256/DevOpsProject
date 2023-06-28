import requests

# Define the base URL of your Dockerized application
base_url = 'http://localhost:5000'


# Example test: Send a GET request to an endpoint and verify the response
def test_get_request():
    endpoint = '/api/example'
    url = base_url

    response = requests.get(url)

    # Verify the response status code
    assert response.status_code == 200

    # Verify the response content or any other assertions
    assert response.json() == {'message': 'Example response'}

    print('Test passed: GET request')

# Example test: Send a POST request to an endpoint and verify the response


# Run the tests
def run_tests():
    test_get_request()


if __name__ == '__main__':
    run_tests()

