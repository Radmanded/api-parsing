# Get user input asking what company to search for
# POST request to API with company name as parameter and return JSON response
# Parse JSON response and return partnerName and certification
# Print partnerName and certification to console and print
# If no partnerName is returned, print "No partner found" and exit
# If no certification is returned, print "No certification found" and exit

import requests
import json
import sys

# send POST request to API with payload

url = "https://wsgx.cisco.com/wwchannels/services/external/getData"

payload = json.dumps({
  "service": "getRessellerData",
  "ccoId": "rubend@synnex.com",
  "profileId": "975",
  "entity": [
    {
      "sourceName": "COMSTOR",
      "resellerAccNo": "",
      "soldToName": "",
      "partnerName": "24/7 NETWORKS LLC",
      "city": "",
      "state": "",
      "postalCode": "",
      "country": "USA",
      "specialization": "",
      "certification": "",
      "authorization": "",
      "theaterCode": "USA",
      "partnerType": "",
      "partnerSiteid": "",
      "pageNumber": 1,
      "pageSize": 50
    }
  ]
})
headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Basic ZGlzdGlfc2VydmljZXMuZ2VuOkQhc3RyaWJ1dDFu',
}

response = requests.request("POST", url, headers=headers, data=payload)

# Testing the API response
''' 
if response.status_code == 200:
  print(response.json())
else:
    print("No partner found")
    sys.exit()
'''

# Get user input asking what company to search for
responsecompany = input("Enter company name: ")


# parse JSON response and return partnerName and certification to console and print to console

partnerName = response.json()['entity'][0][0]['partnerName']
certification = response.json()['entity'][0][0]['certification']

# Create if statement to check user input against partnerName
if responsecompany == partnerName:
  print(partnerName, certification)
else:
    print("No partner found")
    sys.exit()

# if no partnerName is returned, print "No partner found" and exit

if not partnerName:
    print("No partner found")
    sys.exit()





