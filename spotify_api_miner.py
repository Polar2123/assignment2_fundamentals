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
    song_information = get_json(f"tracks/{song_id}")
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

def get_similar_artist(link):
    artist_id = get_id(link)
    similar_artist = get_json(f"{artist_id}/related-artists")

    artist_name = input("Type how you would like to save the data: ")
    with open(f"./recommendations/{artist_name}.json","w") as stored_information:
        json.dump(similar_artist,stored_information)

    return artist_name

def get_lyrics(artist,song):
    api_website = "https://api.lyrics.ovh/v1"
    url = f"{api_website}/{artist}/{song}"
    response = requests.get(url)
    lyrics = response.json()
    print(lyrics["lyrics"])

def get_json(link_extension):
    root_link = "https://dit009-spotify-assignment.vercel.app/api/v1/artists/"
    full_link = root_link + link_extension
    response = requests.get(full_link)
    json_file = response.json()
    return json_file