import requests

res1 = requests.post('http://127.0.0.1:5000/users/1', json={"user_name": "John"})
if res1.ok:
    print(res1.json())
else:
    print('post request failed')

res2 = requests.get('http://127.0.0.1:5000/users/1')

if res2.status_code == 200:
    print("post, get and status is ok")
else:
    print('something gone wrong')
