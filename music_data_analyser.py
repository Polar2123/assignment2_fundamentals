import requests
import json
import re
from spotify_api_miner import get_artist_json

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

            song_id = get_artist_json()
            with open(f"./{song_id}.json","r") as file:
                artist_information = json.load(file)
                artist_name = artist_information["album"]["artists"][0]["name"]
                song_name = artist_information["name"]
                print(artist_name,song_name)




if __name__ == "__main__":
    main()