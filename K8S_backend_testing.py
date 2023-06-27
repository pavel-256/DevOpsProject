import requests


def read_k8s_url():
    with open('k8s_url.txt', 'r') as file:
        url = file.read().strip()
    return url


def test_application():
    url = read_k8s_url()
    test_endpoint = url + '/user/1'  # Modify the endpoint as per your requirement

    try:
        response = requests.get(test_endpoint)
        if response.status_code == 200:
            print('Test successful. Application is accessible.')
        else:
            print(f'Test failed. Received status code: {response.status_code}')
    except requests.exceptions.RequestException as e:
        print(f'Test failed. Error: {str(e)}')


if __name__ == '__main__':
    test_application()
