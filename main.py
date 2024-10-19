import requests
import json


def get_user_choice():
    choice = 0
    menu_message = """Welcome to the Music helper
    Here are your options:
                1. Exit the application
                2. Check which words are said the most
                3. something
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

def get_artist_career():
    print("Welcome to word counter!\n")
    artist = input("Please type the artist:\n")
    song = input("Please type the song:\n")
    api_website = "https://api.lyrics.ovh/v1"
    url = f"{api_website}/{artist}/{song}"
    response = requests.get(url)
    song_lyrics = response.json()
    print(song_lyrics["lyrics"])


def main():
    user_choice = 0
    while user_choice != 1:
        user_choice = get_user_choice()
        if user_choice == 1:
            print("Thank you for trying the application!")
        elif user_choice == 2:
            get_artist_career()



if __name__ == "__main__":
    main()