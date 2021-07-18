import requests
import json


data_on_deaths = requests.get('https://breakingbadapi.com/api/deaths').text
data_episode = requests.get('https://breakingbadapi.com/api/episodes').text
# TODO, к data_on_deaths стоит применить json.loads (десериализация объекта), и только после этого передать в функцию max.

max_deaths = max(data_on_deaths, key=lambda x: x['number_of_deaths'])
print(max_deaths)

