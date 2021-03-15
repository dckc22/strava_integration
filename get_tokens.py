import requests
import json
import configparser
import webbrowser

config = configparser.ConfigParser()
config.read('tokens/config.ini')

# Enter your strava client_id to bring you to the authorization page
my_client_id = input("Enter your Strava client_id: ")

# Create the URL to authorize: 
authorize_url = 'http://www.strava.com/oauth/authorize?client_id=' + my_client_id + '&response_type=code&redirect_uri=http://localhost/exchange_token&approval_prompt=force&scope=profile:read_all,activity:read_all'

# Opens a webbrowser to accept authorization:
webbrowser.open(authorize_url, new=2)

# Paste the code from the URL to authenticate this session
my_authorization_code = input("Enter the authorization code from the URL: ")

# Make Strava auth API call with client_code, client_secret and code
response = requests.post(
                    url = 'https://www.strava.com/oauth/token',
                    data = {
                            'client_id': int(config['STRAVA_TOKENS']['client_id']),
                            'client_secret': config['STRAVA_TOKENS']['client_secret'],
                            'code': my_authorization_code,
                            'grant_type': 'authorization_code'})

# Save tokens (json response) to file
with open('tokens/strava_tokens.json', 'w') as outfile:
    json.dump(response.json(), outfile)

# Open JSON file and print the file contents to check it's worked properly
#with open('tokens/strava_tokens.json') as check:
#  data = json.load(check)
#print(data)
