import re
import json
import requests

def get_artist_json():
    welcome_message = """Welcome to the lyrics translation section!
Before starting please find the song link by following these steps:

Click on the three dots next to the artist's song
Click on "Share"
Click on "Copy link"
Then paste the link here!\n
    """
    print(f"{welcome_message}")
    song_link = input("Type the song link:\n")
    song_id = get_id(song_link)

    spotify_api = "https://dit009-spotify-assignment.vercel.app/api/v1"
    url = f"{spotify_api}/tracks/{song_id}"
    response = requests.get(url)
    song_information = response.json()

    artist_name = song_information["album"]["artists"][0]["name"]
    song_name = song_information["name"]
    file_name = f"./{artist_name} - {song_name}.json"

    with open(file_name,"w") as stored_information:
        json.dump(song_information,stored_information)
    return artist_name, song_name

def get_id(link):
    pattern = r"\/\w*?\?"
    song_sequence = re.findall(pattern, link)

    pattern_id = r"\w+?\b"
    spotify_id = re.findall(pattern_id, song_sequence[0])[0]
    return spotify_id
