
# Spotify Playlist to Markdown

## Description

- I use this script with a spotify playlist that I add songs to that I want to remember, and it will be automatically be added to my obsidian vault for me to expand upon. I feel like I remember music by relating it to events, people, or places. This is my way of tying those things together, while still being able to access the media quickly.

## Requirements

- a spotify account with credentials 
- python3
- spotipy

## Setup

- Fill out the required credentials as per [Spotipy's](https://spotipy.readthedocs.io/en/2.19.0/) requirements
- `pip install spotipy`
- create spotify playlist to watch and get it's playlist id, fill in that id within the script

## Usage

- `python3 sync_playlist_to_md.py`

## Tips

- You could watch multiple directories if you'd like by running this file on multiple playlist ids. I like having a single "ingress" playlist that I determine where things go incrementally, but it is useful to just unload an entire playlist into a directory as markdown files.

## Output

Example output of a song taken from a playlist and put into a markdown file:

```markdown
---
tags: ['song']
aliases: []
---

# Never Gonna Give You Up
-----------
**Song**:: [Never Gonna Give You Up]( https://open.spotify.com/track/4cOdK2wGLETKBW3PvgPWqT )
**Album**::  [Whenever You Need Somebody]( https://open.spotify.com/album/5Z9iiGl2FcIfa3BMiv6OIw )
**Artist**:: [Rick Astley](https://open.spotify.com/artist/0gxyHStUsqpMadRV0Di1Qt)

**Added**::   2022-05-05T01:27:57Z
**Tags**:: 

------
## Associations
- 
-------
## Notes
- 
----------
```