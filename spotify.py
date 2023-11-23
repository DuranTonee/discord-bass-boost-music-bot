import base64
import json
import requests
from youtube_search import YoutubeSearch
from config import CLIENT_ID, CLIENT_SECRET

def get_token():
    auth_string = f"{CLIENT_ID}:{CLIENT_SECRET}"
    auth_bytes = auth_string.encode(encoding="utf-8")
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")

    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": f"Basic {auth_base64}",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {"grant_type": "client_credentials"}
    result = requests.post(url, headers=headers, data=data)
    json_result = json.loads(result.content)
    token = json_result["access_token"]
    return token


def get_auth_header(token):
    return {"Authorization": f"Bearer {token}"}


def get_track_name_spotify(track_url) -> str:
    token = get_token()
    auth_header = get_auth_header(token=token)
    track_id = track_url[31:]
    endpoint = f"https://api.spotify.com/v1/tracks/{track_id}"
    response = requests.get(endpoint, headers=auth_header)
    json_response = json.loads(response.content)
    artist = json_response['artists'][0]['name']
    name = json_response['name']
    return f"{artist} - {name}"


def get_track_names_from_list_spotify(playlist_url) -> list:
    print('spotify playlist')
    token = get_token()
    auth_header = get_auth_header(token=token)
    print('spotify playlist again')
    playlist = []
    # get the playlist json using endpoint (from docs) and request
    playlist_id = playlist_url[34:]
    endpoint = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks"
    response = requests.get(endpoint, headers=auth_header)
    json_response = json.loads(response.content)
    for track in json_response['tracks']['items']:
        artist = track['track']['artists'][0]['name'] 
        name = track['track']['name']
        result = f"{artist} - {name}"
        
        search = YoutubeSearch(result, max_results=1).to_dict()
        url = f"https://www.youtube.com/watch?v={search[0]['id']}"
        playlist.append(url)
    return playlist


if __name__ == '__main__':
    get_track_name_spotify("https://open.spotify.com/track/0ct6r3EGTcMLPtrXHDvVjc?si=c553540f6d924392")
