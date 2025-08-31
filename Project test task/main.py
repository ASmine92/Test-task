import requests
import math

request = requests.get('https://catfact.ninja/facts')
total_facts = (request.json()['total'])
facts_per_page = (request.json()['per_page'])

total_pages = (math.ceil(total_facts/facts_per_page))

request = requests.get('https://catfact.ninja/facts?page='+str(total_pages))

shortest_fact_length = request.json()['data'][0]['length']

for fact_length in request.json()['data']:
    if (fact_length['length']) < shortest_fact_length:
        shortest_fact_length = fact_length['length']

for fact in request.json()['data']:
    if fact['length'] == shortest_fact_length:
        print(fact['fact'])
