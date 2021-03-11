import requests
import json
import configparser

config = configparser.ConfigParser()
config.read('tokens/config.ini')

# Use this URL: http://www.strava.com/oauth/authorize?client_id=[REPLACE_WITH_YOUR_CLIENT_ID]&response_type=code&redirect_uri=http://localhost/exchange_token&approval_prompt=force&scope=profile:read_all,activity:read_all


# Make Strava auth API call with your client_code, client_secret and code
response = requests.post(
                    url = 'https://www.strava.com/oauth/token',
                    data = {
                            'client_id': int(config['STRAVA_TOKENS']['client_id']),
                            'client_secret': config['STRAVA_TOKENS']['client_secret'],
                            #'code': 'PASTE_CODE_FROM_URL_HERE',
                            'grant_type': 'authorization_code'})

# Save tokens (json response) to file
with open('tokens/strava_tokens.json', 'w') as outfile:
    json.dump(response.json(), outfile)

# Open JSON file and print the file contents to check it's worked properly
#with open('tokens/strava_tokens.json') as check:
#  data = json.load(check)
#print(data)