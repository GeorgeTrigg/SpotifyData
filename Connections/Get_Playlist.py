from Simple_connect.py import Simple_connect

def Get_Playlist(user, PlaylistID):
    playlist_id = str(PlaylistID)
    username = str(user)
    sp = Simple_connect()
    playlist = sp.user_playlist_tracks(user, playlist_id)
    return playlist
    

def Get_MY_Playlist(PlaylistID):
    playlist_id = str(PlaylistID)
    sp = Simple_connect()
    playlist = sp.user_playlist_tracks("1148975055", playlist_id)
    return playlist
