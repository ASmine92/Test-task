import requests
import math

# Get first page data
response = requests.get('https://catfact.ninja/facts')
response = response.json()
total_facts = response['total']
facts_per_page = response['per_page']

# Calculate last page
total_pages = (math.ceil(total_facts/facts_per_page))

# Get last page data
response = requests.get('https://catfact.ninja/facts?page='+str(total_pages))
response = response.json()

shortest_fact_length = response['data'][0]['length']

# Figure out shortest fact length
for fact_length in response['data']:
    if (fact_length['length']) < shortest_fact_length:
        shortest_fact_length = fact_length['length']

# Print shortest facts (might be multiple answers)
for fact in response['data']:
    if fact['length'] == shortest_fact_length:
        print(fact['fact'])
