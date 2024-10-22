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
    song_link = input("Type the song ID:\n")
    pattern = r"/\w*?\?"
    song_sequence = re.findall(pattern,song_link)

    pattern_id = r"\w+?\b"
    song_id = re.findall(pattern_id,song_sequence[0])[0]
    spotify_api = "https://dit009-spotify-assignment.vercel.app/api/v1"
    url = f"{spotify_api}/tracks/{song_id}"
    response = requests.get(url)
    song_information = response.json()
    with open(f"./{song_id}.json","w") as stored_information:
        json.dump(song_information,stored_information)
    return song_id