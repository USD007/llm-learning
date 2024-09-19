### SCRAPING CODE FROM LINKED IN

import requests

# api_key = 'hV9KNueID5y4gndZKJtdiA'
# headers = {'Authorization': 'Bearer ' + api_key}
# api_endpoint = 'https://nubela.co/proxycurl/api/v2/linkedin'
# params = {
#     'linkedin_profile_url': 'https://www.linkedin.com/in/ujwal-d-72a66b244/'
# }
# response = requests.get(api_endpoint,
#                         params=params,
#                         headers=headers)
# print(response.json())


gist_response= requests.get("https://gist.githubusercontent.com/USD007/9c5fe2f601f933651de64467541c3c5c/raw/6c9a539ab82eaae20db1382aad412c860f3da5b4/ujwal-d.json")
print(gist_response.json())