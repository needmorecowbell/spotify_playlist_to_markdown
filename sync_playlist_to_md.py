import os
from typing import Dict
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

SPOTIPY_CLIENT_ID= os.getenv("SPOTIPY_CLIENT_ID","123123123123")
SPOTIPY_CLIENT_SECRET=os.getenv("SPOTIPY_CLIENT_SECRET","123123123123123")

NOTES_PATH="/home/user/Notes/Songs/"
PLAYLIST_ID="SPOTIFY_PLAYLIST_ID_HERE"


def setup_spotify_auth(id,secret) -> spotipy.Spotify:
    """
    Sets up the spotipy auth manager
    
    :param id: the client id
    :param secret: the client secret
    :return: a spotipy auth manager
    
    """
    try:
        auth_manager = SpotifyClientCredentials(SPOTIPY_CLIENT_ID,SPOTIPY_CLIENT_SECRET)
        return spotipy.Spotify(auth_manager=auth_manager)
    except Exception as e:
        print(e)

def song_to_md(song: Dict) -> str:
    """
    Takes a song object and returns a string in markdown format

    :param song: a Dict from the spotipy API representing a song with full track details
    :return: a string in markdown format
    """
    content = ""
    added_at= item["added_at"]
    song_name = item["track"]["name"]
    song_link = item["track"]["external_urls"]["spotify"]
    album = item["track"]["album"]["name"]
    album_link= item["track"]["album"]["external_urls"]["spotify"]

    artists_block= ""
    for artist in song["track"]["artists"]:
       artists_block+=f"**Artist**:: [{artist['name']}]({artist['external_urls']['spotify']})\n"

    # Template
    content = f"""
---
tags: ['song']
aliases: []
---

# {song_name}
-----------
**Song**:: [{song_name}]( {song_link} )
**Album**::  [{album}]( {album_link} )
{artists_block}
**Added**::   {added_at}
**Tags**:: 

------
## Associations
- 
-------
## Notes
- 
----------
"""

    return content

if __name__ == "__main__":
    sp = setup_spotify_auth(SPOTIPY_CLIENT_ID,SPOTIPY_CLIENT_SECRET)

    playlist = sp.playlist_items(PLAYLIST_ID)

    while playlist:
        for i, item in enumerate(playlist["items"]):

            if(os.path.exists(NOTES_PATH+item["track"]["name"]+".md")): # don't overwrite existing files
                print(f"[-] {item['track']['name']} already exists as a file") 
            else:
                song_md = song_to_md(item) # get the markdown for the song

                try:
                    with open(NOTES_PATH+item["track"]["name"]+".md", "w") as f:
                        f.write(song_md)
                except Exception as e:
                    print(f"[!] {item['track']['name']}.md could not be written to vault")
                    print(e)

                print(f"[+] {item['track']['name']}.md written to vault")

        if playlist['next']:
            playlist = sp.next(playlist)
        else:
            playlist = None
