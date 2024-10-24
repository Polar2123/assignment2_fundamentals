import requests
import json

with open("language_code.json", "r") as files:
    files = json.load(files)
with open("lyrics.txt", "r") as file:
    text_to_translate = file.read()


def translate_text(text, target_language):
    api_key = 'AIzaSyAxHjthtr1Sc6InCsfu_k9TcCsZHjuK3FI'
    url = f"https://translation.googleapis.com/language/translate/v2?key={api_key}&q={text}&target={target_language}"

    response = requests.post(url)
    
    if response.status_code == 200:
        translated_text = response.json()['data']['translations'][0]['translatedText']
        return translated_text
    else:
        print("Failed")

def user_ask_language():
    language = input("Enter the language  you want to translate to: ").lower()
    return language
def get_language_code(language):
    if language in files:
        code = files[language]
        return code
