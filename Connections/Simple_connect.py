import spotipy
import spotipy.util as util
import sys
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth

def Simple_connect(): 
    token = util.oauth2.SpotifyClientCredentials()
    cache_token = token.get_access_token()
    sp = spotipy.Spotify(cache_token)
    return sp
