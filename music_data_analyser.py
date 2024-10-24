import requests
import json
import re
from spotify_api_miner import *
from barchart import *

def main():
    user_choice = 0
    while user_choice != 4:
        user_choice = get_user_choice()
        local_files = input("Do you wish to use local files? y/n?")
        lyrics_recommendation = input("Type the number for the option you want\n1.Lyrics Translation\n2.Artist Recommendations")
        if user_choice == 1:

            if local_files == "n":

                recommend_live()

            elif local_files == "y":

                recommend_local()

            else:

                input("Please type y/n, you will now be sent back to the menu.")


        elif user_choice == 2:
            artist_name = input("Enter the other artist's name: ")
            youtube_vs_spotify(artist_name)
        elif user_choice == 3:
            artist_link = input("Enter the artist's Spotify link:\n")
            artist_id = get_id(artist_link)
            analytics_menu(artist_id)
        elif user_choice == 4:
            print("Thank you for trying the application!")






def get_user_choice():
    choice = 0
    menu_message = """Welcome to the Music helper
    Here are your options:
                1. Lyric Translation and Artist Recommendation
                2. YouTube and Spotify comparison
                3. Artist Analytics (Top 5, No. of followers, Popularity, Compare...)
                4. Exit the application
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
                5: Back to main menu

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
                print()

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
                    print("Unable to retrieve artist's popularity information.")
                print()

            elif choice == 4:
                print("\nCompare with another artist...\n")
                second_artist_link = input("Enter the other artist's Spotify link: ")
                other_artist_id = get_id(second_artist_link)
                compare_artists(artist_id, other_artist_id)
                print()
            elif choice == 5:
                return
            else:
                print("Invalid choice. Please pick between 1 and 4.")

                
                
        except ValueError:
            print("Invalid input. Please enter an integer.")



def get_artist_recommendation(artist_name):

    with open(f"./recommendations/{artist_name}.json", "r") as file:
        recommended_artists = json.load(file)
    print("Here are a few artists you might like:\n")

    with open(f"./recommendations/{artist_name}.txt","w")as recommendations:

        for i in range(3):
            recommendations.write(f"{recommended_artists["artists"][i]["name"]}\n")
            print(f"{recommended_artists["artists"][i]["name"]}\n")

    with open(f"./recommendations/all_recommendations.txt", "a") as recommended_artists:
        recommended_artists.write(f"{artist_name}.txt\n")


def recommend_live():
    artist_name, song_name, artist_link = get_artist_json()
    lyrics = get_lyrics(artist_name, song_name)
    artists = get_similar_artist(artist_link)
    get_artist_recommendation(artists)
    input("Type anything when you are ready to go back to the menu.")

def recommend_local():
    print("Here are the artists we have song recommendations for:")
    with open("./recommendations/all_recommendations.txt", "r") as file:
        print(file.read())

    song_recommendations = input(
        "Write the name of the file you wish to see, make sure to write it correctly. Do not include the file type\n")
    try:

        print("Here are your recommendations:\n")
        with open(f"./recommendations/{song_recommendations}.txt", "r") as recommendation_file:
            print(recommendation_file.read())

        input("Type anything when you are ready to go back to the menu.")

    except FileNotFoundError:

        input("It seems like you typed it incorrectly. Type anything when you are ready to go back to the menu.")


if __name__ == "__main__":
    main()
