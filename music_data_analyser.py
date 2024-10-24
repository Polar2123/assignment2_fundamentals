import requests
import json
import re
from spotify_api_miner import *

def get_user_choice():
    choice = 0
    menu_message = """Welcome to the Music helper
    Here are your options:
                1. Exit the application
                2. Compare top 5 songs of an artist
                3. Translate the lyrics of a song
                4. Recommend similar artists
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




def main():
    user_choice = 0
    while user_choice != 1:
        user_choice = get_user_choice()
        if user_choice == 1:
            print("Thank you for trying the application!")
        elif user_choice == 2:
            artist_name, song_name = get_artist_json()
            get_lyrics(artist_name, song_name)
        elif user_choice == 4:
            artist_link = input("Enter the artist link:\n")
            artist_name = get_similar_artist(artist_link)
            recommend_artists(artist_name)

def recommend_artists(artist_name):
    with open(f"./recommendations/{artist_name}.json", "r") as file:
        artist_name = json.load(file)
    print("Here are a few artists you might like:\n")
    for i in range(3):
        print(f"{artist_name["artists"][i]["name"]}\n")




if __name__ == "__main__":
    main()
