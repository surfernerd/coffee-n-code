import base64
import requests
import os

from dotenv import load_dotenv

load_dotenv()

# BASE_URL = 'https://api.spotify.com/v1/'
client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")
print(f"client_secret: {client_secret}")

##########
### auth with limited scope CANNOT ACCESS USER PROFILE!!!
token_url = 'https://accounts.spotify.com/api/token'

client_string = client_id + client_secret
b = base64.b64encode(bytes(client_string, 'utf-8'))
client_string = b.decode('utf-8')

headers = {
    'Authorization': 'Basic ' + client_string
}
data = {
    'grant_type': 'client_credentials'
}

auth_response = requests.post(token_url, headers=headers, data=data, auth=(client_id, client_secret))
print(f"auth_response: {auth_response}")
auth_response_json = auth_response.json()
print(f"auth_response_json: {auth_response_json}")
access_token = auth_response_json['access_token']
##########

# Get user's recently played list
headers = {
    'Authorization': f'Bearer {access_token}'
}
track_history_url = 'https://api.spotify.com/v1/me/player/recently-played'
response = requests.get(track_history_url, headers=headers)

# Parse the response
recent_tracks = response.json()

print(f"{recent_tracks}")
