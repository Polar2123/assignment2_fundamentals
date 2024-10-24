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
                3. Artist Analytics (Top 5, No. of followers etc.)
                4. Translate the lyrics of a song
                5. Recommend similar artists
                """
    print(menu_message)
    while choice <= 0 or choice > 5:
        try:
            choice = int(input("Enter the number for your option:\n"))
            if choice <= 0 or choice > 5:
                print("Please type a number between 1 and 5.\n")
        except ValueError:
            print("The input must be an integer.\n")

    return choice


def analytics_menu(artist_id):
    choice = 0
    while choice <= 0 or choice > 4:
        try:
            choice = int(input(f"""
    You picked Analytics for the artist.
        Here are your options:
                1: Top 5 most listened songs (recent)
                2: No. of followers
                3: Popularity (1-100)
                4: Compare with Another Artist

                Enter your choice: """))
            
            if choice == 1:
                print("\nDisplaying top 5 most-listened (by popularity) songs...\n")
                top_tracks = artist_top_tracks(artist_id)
                if top_tracks:
                    for index, track in enumerate(top_tracks[:5], 1):
                        track_name = track.get('name', 'Unknown Track')
                        popularity = track.get('popularity', 'Unknown Popularity')
                        print(f"{index}. {track_name} (Popularity: {popularity})")
                else:
                    print("No top tracks found.")

            elif choice == 2:
                print("\nDisplaying total number of followers...\n")
                artist = artist_info(artist_id)
                if artist:
                    followers = artist.get('followers', {}).get('total', 'Unknown Followers')
                    print(f"Artist has {followers:,} followers.\n")
                else:
                    print("Unable to retrieve artist's followers information.")

            elif choice == 3:
                print("\nDisplaying artist popularity...\n")
                artist = artist_info(artist_id)
                if artist:
                    popularity = artist.get('popularity', 'Unknown Popularity')
                    print(f"Artist popularity: {popularity}")
                else:
                    print("Unable to retrieve artist's popuplarity information.")

            elif choice == 4:
                print("\nCompare with another artist...\n")
                second_artist_link = input("Enter the other artist's Spotify link: ")
                other_artist_id = get_id(second_artist_link)
                compare_artists(artist_id, other_artist_id)

            else:
                print("Invalid choice. Please pick between 1 and 4.")
                
        except ValueError:
            print("Invalid input. Please enter an integer.")


def main():
    user_choice = 0
    while user_choice != 1:
        user_choice = get_user_choice()
        if user_choice == 1:
            print("Thank you for trying the application!")
        elif user_choice == 2:
            artist_name, song_name = get_artist_json()
            get_lyrics(artist_name, song_name)
        elif user_choice == 3:
            artist_link = input("Enter the artist's Spotify link:\n")
            artist_id = get_id(artist_link)
            analytics_menu(artist_id)
        elif user_choice == 5:
            artist_link = input("Enter the artist link:\n")
            get_similar_artist(artist_link)


def get_lyrics(artist,song):
    api_website = "https://api.lyrics.ovh/v1"
    url = f"{api_website}/{artist}/{song}"
    response = requests.get(url)
    lyrics = response.json()
    print(lyrics["lyrics"])




if __name__ == "__main__":
    main()
