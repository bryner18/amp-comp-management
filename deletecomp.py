import requests

client_id = 'client-id'

api_key = 'api-key'

session = requests.session()

session.auth = (client_id, api_key)

url = 'https://api.amp.cisco.com/v1/computers'

response = session.get(url)

response_json = response.json()

hostname = 'hostname-to-search-for'
store = []

for computer in response_json['data']:
    if computer['hostname'] == hostname:
        print(computer['connector_guid'], computer['hostname'])
        store.append(computer['connector_guid'])

while 'next' in response_json['metadata']['links']:
    next_url = response_json['metadata']['links']['next']
    response = session.get(next_url)
    response_json = response.json()
    for computer in response_json['data']:
        if computer['hostname'] == hostname:
            print(computer['connector_guid'], computer['hostname'])
            store.append(computer['connector_guid'])

for n in store:
    delrequest = requests.delete(
        'https://api.amp.cisco.com/v1/computers/{n}'.format(n=n), auth=(client_id, api_key))
    # print(delrequest.json())   <- don't delete
    print("Computer deleted. computer_guid=", n)
print("All computers with hostname", hostname, "were deleted")
