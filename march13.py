# python and json
# import json

# data = json.load(open('cs_people.json'))

# print(data['people'][0]['firstName'])

# for person in data['people']:
#   print(f'{person["firstName"]}', end='')
#   print(f' {person["lastName"]} ', end='')
#   print('is a famous Computer Scientist.')

# for person in data['people']:
#   print(f'{person["firstName"]} {person["lastName"]} is a famous Computer Scientist.')

# NASA API
import requests, json
from pprint import pprint

my_key = 'ZyQeDGiLhU50TusiKw06vtDTVPJhOXzxSzEGUVej'

payload = {
    'api_key': my_key,
    'start_date': '2023-03-09',
    'end_date': '2023-03-11'
}

endpoint = 'https://api.nasa.gov/planetary/apod'

try:
    r = requests.get(endpoint, params=payload)
    data = r.json()
    pprint(data)
except:
    print('please try again')