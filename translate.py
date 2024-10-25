import requests
import json

with open("language_code.json", "r") as files:
    files = json.load(files)
with open("./lyrics_library/all_lyrics.txt", "r") as file:
    text_to_translate = file.read()


def translate_text(text, target_language):
    api_key = 'AIzaSyAxHjthtr1Sc6InCsfu_k9TcCsZHjuK3FI'
    try:
        url = f"https://translation.googleapis.com/language/translate/v2?key={api_key}&q={text}&target={target_language}"

        response = requests.post(url)
        response.raise_for_status()
        
        translated_text = response.json()['data']['translations'][0]['translatedText']
        return translated_text
    except requests.exceptions.RequestException as error:
        print(error)

def ask_user_language():
    language = input("Enter the language  you want to translate to: ").lower()
    return language
def get_language_code(language):
    if language in files:
        code = files[language]
        return code
