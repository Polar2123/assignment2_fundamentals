import requests
import json
import re

def get_user_choice():
    choice = 0
    menu_message = """Welcome to the Music helper
    Here are your options:
                1. Exit the application
                2. Compare top 5 songs of an artist
                3. Translate the lyrics of a song
                4. something
                """
    print(menu_message)
    while choice <= 0 or choice > 4:
        try:
            choice = int(input("Enter the number for your option:\n"))
            if choice <= 0 or choice > 4:
                print("Please type a number between 1 and 4.\n")
        except ValueError:
            print("The input must be an integer.\n")

    return choice

def get_artist_track():
    welcome_message = """Welcome to the lyrics translation section!
Before starting please find the song link by following these steps:

Click on the three dots next to the artist's song
Click on "Share"
Click on "Copy link"
Then paste the link here!\n
    """
    print(f"{welcome_message}")
    pattern = r"/\w*?\?"
    song_link = input("Type the song ID:\n")
    song_sequence = re.findall(pattern,song_link)
    pattern_id = r"\w+?\b"
    song_id = re.findall(pattern_id,song_sequence[0])
    spotify_api = "https://dit009-spotify-assignment.vercel.app/api/v1/"
    url = f"{spotify_api}/tracks/{song_id}"
    response = requests.get(url)
    song_information = response.json()
    #with open(f"./{song_id}.json","w") as stored_information:
    #    json.dump(response,stored_information)
    #Need to fix this part, write the .json files and store them for later use here.

    #api_website = "https://api.lyrics.ovh/v1"
    #url = f"{api_website}/{artist}/{song}"


    #print(song_lyrics["lyrics"])


def main():
    user_choice = 0
    while user_choice != 1:
        user_choice = get_user_choice()
        if user_choice == 1:
            print("Thank you for trying the application!")
        elif user_choice == 2:
            get_artist_track()



if __name__ == "__main__":
    main()