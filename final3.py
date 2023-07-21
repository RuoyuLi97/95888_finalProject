# Name: Ruoyu Li
# Andrew ID: ruoyuli

import requests
import pandas as pd
import os
import base64
import json
from dotenv import load_dotenv

load_dotenv()

# For retrieving structured data using the API of the playlist -  
# "Taylor Swift - The Eras Tour Setlist" to sort out:
#   dataframe groupby album

# References:
#   https://www.youtube.com/watch?v=WAmEZBEeNmg
#   https://developer.spotify.com/documentation/web-api/tutorials

# Client ID: f69b3352714d4147b173c65ece84229b
# Client Secret: 7904bb22bba44ba09ba6a27cddbefbac

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

# get token access from Spotify api
def getToken():
    auth_string = client_id + ":" + client_secret
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")
    
    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": "Basic " + auth_base64,
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {"grant_type": "client_credentials"}
    result = requests.post(url, headers=headers, data=data)
    json_result = json.loads(result.content)
    token = json_result["access_token"]
    return token

token = getToken()

# get authorized token
def getAuthHeader(token):
    return {"Authorization": "Bearer " + token}

urlPlaylist = 'https://api.spotify.com/v1/playlists/2orpJ0h2eOpRu1VRLm9K4l?si=ab025ca48cef451b'
headers = getAuthHeader(token)
result = requests.get(urlPlaylist, headers=headers)
if (result.status_code == 200):
    playlistData = json.loads(result.content.decode('utf-8'))

dataList = list()
for item in playlistData['tracks']['items']:
    itemList = list()
    itemInfo = item['track']
    itemName = itemInfo['name']
    itemList.append(itemName)
    itemPopularity = int(itemInfo['popularity'])
    itemList.append(itemPopularity)
    itemAlbum = itemInfo['album']['name']
    itemList.append(itemAlbum)
    dataList.append(itemList)

playListDF = pd.DataFrame(dataList, 
                          columns=['Song Name', 'Popularity', 'Album'])