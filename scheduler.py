import requests

url = "https://rata.digitraffic.fi/api/v1/train-locations/latest/1"
response = requests.get(url)
print(response.content)
