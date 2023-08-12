import requests
from decouple import config
from datetime import datetime
pixela_enpoint = "https://pixe.la/v1/users"
token = config("PIXEL_KEY")
USERNAME = "gabotov"
grapd_id = "graph1"
user_params = {
    "token": token,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
# response = requests.post(url=pixela_enpoint, json=user_params)

pixela_graph = f"{pixela_enpoint}/{USERNAME}/graphs"
graph_config = {
    "id": "graph1",
    "name": "Programming",
    "unit": "hour",
    "type": "float",
    "color": "ajisai"
}
headers = {
    "X-USER-TOKEN": token
}
# responsa = requests.post(url=pixela_graph, json=graph_config, headers=headers)
url = "https://pixe.la/v1/users/gabotov/graphs/graph1"
today = datetime.now()
params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "2",
}
# response = requests.post(url=url, json=params, headers=headers)

put_url = f"{pixela_enpoint}/{USERNAME}/graphs/{grapd_id}/{today.strftime('%Y%m%d')}"
put_params = {
    "quantity": "1"
}
response = requests.put(url=put_url, headers=headers, json=put_params)
response = requests.delete(url=put_url, headers=headers)

print(response.text)
