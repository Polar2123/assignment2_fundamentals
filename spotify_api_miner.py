import re
import json
import requests

def get_artist_json():
    welcome_message = """To continue, please enter the link of the song;
    
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
    artist_link = song_information["album"]["artists"][0]["external_urls"]["spotify"] + "?"
    file_name = f"./{artist_name} - {song_name}.json"

    with open(file_name,"w") as stored_information:
        json.dump(song_information,stored_information)

    return artist_name, song_name, artist_link

def get_id(link):
    pattern = r"\/\w*?\?"
    song_sequence = re.findall(pattern, link)
    pattern_id = r"\w+?\b"
    spotify_id = re.findall(pattern_id, song_sequence[0])[0]
    return spotify_id


def get_similar_artist(link):
    artist_id = get_id(link)
    similar_artist = get_json(f"/artists/{artist_id}/related-artists")
    artist_name = input("Type how you would like to save the recommendations: ")
    with open(f"./recommendations/{artist_name}.json","w") as stored_information:
        json.dump(similar_artist,stored_information)

    return artist_name

def get_lyrics(artist,song):
    api_website = "https://api.lyrics.ovh/v1"
    url = f"{api_website}/{artist}/{song}"
    response = requests.get(url)
    lyrics = response.json()

    with open(f"./lyrics_library/all_lyrics.txt","a") as file:
        file.write(f"{artist.capitalize()}-{song.capitalize()}.txt\n")
    with open(f"./lyrics_library/{artist.capitalize()}-{song.capitalize()}.txt","w") as file:
        file.write("Translated lyrics:\n")
    return lyrics["lyrics"]

def get_json(link_extension):
    try:
        root_link = "https://dit009-spotify-assignment.vercel.app/api/v1/"
        full_link = root_link + link_extension
        response = requests.get(full_link)
        response.raise_for_status()
        json_file = response.json()
        return json_file
    except requests.exceptions.RequestException as error:
        print(error)


def artist_info(artist_id):
    try:
        artist_url = f"https://dit009-spotify-assignment.vercel.app/api/v1/artists/{artist_id}"
        response = requests.get(artist_url)
        response.raise_for_status()
        return response.json()
        
    except requests.exceptions.RequestException as error:
        print(error)
    
def compare_artists(artist_1_id, artist_2_id):
    artist_1_info = artist_info(artist_1_id)
    artist_2_info = artist_info(artist_2_id)

    if not artist_1_info or not artist_2_info:
        print("Unable to fetch comparison data.")
        return

    print(f"\nComparison between {artist_1_info['name']} and {artist_2_info['name']}:")

    artist_1_followers = artist_1_info.get("followers", {}).get("total", 0)
    artist_2_followers = artist_2_info.get("followers", {}).get("total", 0)
    print(f"Followers:\n{artist_1_info['name']}: {artist_1_followers:,}\n{artist_2_info['name']}: {artist_2_followers:,}")

    artist_1_popularity = artist_1_info.get("popularity", 0)
    artist_2_popularity = artist_2_info.get("popularity", 0)
    print(f"Popularity:\n{artist_1_info['name']}: {artist_1_popularity}\n{artist_2_info['name']}: {artist_2_popularity}")    

def artist_top_tracks(artist_id):
    try:
        top_tracks_url = f"https://dit009-spotify-assignment.vercel.app/api/v1/artists/{artist_id}/top-tracks"
        response = requests.get(top_tracks_url)
        response.raise_for_status()
        
        return response.json().get("tracks", [])
        
    except requests.exceptions.RequestException as error:
        print(error)