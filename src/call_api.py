import requests

url = "https://jsonplaceholder.typicode.com/posts/1"

response = requests.get(url)

print(response.status_code)

response_dict = response.json()

print(response_dict)

# The response will look like this:
# {'userId': 1,
#  'id': 1,
#  'title': 'sunt aut facere repellat provident occaecati excepturi optio reprehenderit',
#  'body': 'quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit'}

# As we learned in dictionaries, we can access data from the response like so:
print(response_dict['title'])