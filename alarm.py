from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import sys
import pprint
import datetime
import webbrowser as web
import pyautogui
from time import sleep

currDate = datetime.datetime.now()

print(currDate.hour, ":", currDate.minute)

# Search for a song by it's name
def searchSong(song):
    song = song.replace(" ", "%20")
    web.open(f"spotify:search:{song}")
    sleep(8)

    for i in range(27):
        pyautogui.press("tab")

    for i in range(2):
        pyautogui.press("enter")
        sleep(1)


client_id = "Here goes the client id value"
client_secret = "here goes your client secrect values"

author = ""
song = "something in the way".upper()
flag = 0

sp = spotipy.Spotify(
    client_credentials_manager=SpotifyClientCredentials(client_id, client_secret)
)

try:
    result = sp.search(author)

    for i in range(0, len(result["tracks"]["items"])):
        song_name = result["tracks"]["items"][i]["name"].upper()

        if song == song_name:
            flag = 1
            web.open(result["tracks"]["items"][i]["uri"])

        if flag == 0:
            searchSong(song)
except:
    searchSong(song)
