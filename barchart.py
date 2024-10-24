import requests
import json
import matplotlib.pyplot as plt


API_KEY = "AIzaSyAxHjthtr1Sc6InCsfu_k9TcCsZHjuK3FI"
#youtube api miner
def get_id_yt(artist_name, api_key):
    url = f"https://youtube.googleapis.com/youtube/v3/search?part=snippet&maxResults=25&q={artist_name}&key={api_key}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()

        artist_id = data['items'][0]['id']['channelId']
        return artist_id
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None
#youtube api miner
def get_channel_info_yt(artist_name,api_key):
    artist_id = get_id_yt(artist_name,api_key)
    url = f"https://youtube.googleapis.com/youtube/v3/channels?part=snippet%2CcontentDetails%2Cstatistics&id={artist_id}&key={api_key}"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        with open('youtube_channel.json', 'w') as file:
            json.dump(data, file)
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None

#spotify api miner
def get_names(artist_name):
    names=[]
    names = artist_name.split(" ")
    if len(names)>= 2:
        message = '%20'.join(names)
        return message
    else:
        return artist_name
#spotify api miner
def get_artist_sp(artist_name):
    artist_name=get_names(artist_name)
    service = "https://dit009-spotify-assignment.vercel.app/api/v1"
    url = f"{service}/search?q={artist_name}&type=artist&limit=1"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        with open('spotify_info.json', 'w') as file:
            json.dump(data, file)    
        
    else:
        return None

#spotify analyze 
def analyze_spotify():
    with open('spotify_info.json', 'r') as file:
        data=json.load(file)
    #id = data['artists']['items'][0]['id']
    followers = int(data['artists']['items'][0]['followers']['total'])
    popularity = int(data['artists']['items'][0]['popularity'])
    return followers,popularity
#youtube analyze
def analyze_youtube():
    with open('youtube_channel.json', 'r') as file:
        data=json.load(file)
        viewCount = int(data['items'][0]['statistics']['viewCount'])
        subCount = int(data['items'][0]['statistics']['subscriberCount'])
        artist_name = data['items'][0]['snippet']['title']
        youtube= [viewCount, subCount]
        return youtube, artist_name

#analyze
def get_youtube_popularity(youtube_list):
    viewCount=youtube_list[0]
    subCount = youtube_list[1]
    per_point_view = 80000000  
    per_point_sub = 5000000
    view_score=viewCount/per_point_view
    sub_score = subCount / per_point_sub
    popularity = view_score + sub_score
    if popularity > 100:
        popularity = 100
    
    return popularity
def get_new_data(artist_name):
    get_channel_info_yt(artist_name,API_KEY)
    get_artist_sp(artist_name)
#analyze
def youtube_vs_spotify():
    spotify=analyze_spotify()
    youtube_list, artist_name = analyze_youtube()
    spotify_list = list(spotify)
    followers_spotify = spotify_list[0] / 1000000  
    followers_youtube = youtube_list[1] / 1000000
    followers = [followers_spotify, followers_youtube]
    popularity_yt=get_youtube_popularity(youtube_list)
    popularity = [spotify_list[1],popularity_yt]
    text = ['Spotify', 'Youtube']
    fig, (ax1, ax2) = plt.subplots(1,2)
    plt.suptitle(artist_name)

    bar_labels = ['Spotify', 'Youtube']
    bar_colors = ['tab:green', 'tab:red']

    ax1.bar(text, followers, label=bar_labels, color=bar_colors)

    ax1.set_ylabel("Followers by million")
    ax1.set_title('Followers')
    ax1.legend(title='Followers')
    ax2.set_ylim(0, 1000000000)

    ax2.bar(text, popularity,label=bar_labels, color=bar_colors)
    ax2.set_ylim(0, 100)

    ax2.set_ylabel("Popularity")
    ax2.set_title('Popularity')
    ax2.legend(title='Popularity')

    plt.show()

#artist_name = input("Which artist do you want to compare: ")
#youtube_vs_spotify(artist_name)
