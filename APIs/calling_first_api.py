import requests

# define the values you want to pass to the API 
name = "Peace"
age = 21

#pass the variables to the API
response = requests.get(f"http://127.0.0.1:8000/myFirstAPI?name={name}&age={age}")
output = response.json()
print(output)