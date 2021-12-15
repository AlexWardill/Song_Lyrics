from bs4 import BeautifulSoup
import requests
import re
from Get_Song_Data import getLyricsOfSong
import pandas as pd
from IPython.display import display
import pickle

headers = {"Referer": "https://www.google.com/",
           "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp",
           "Accept-Encoding": "gzip",
           "Accept-Language": "en-US,en;q=0.9,es;q=0.8"}

def url(year: int):
    url = f"https://www.billboard.com/charts/year-end/{year}/hot-100-songs/"
    return url

songs = {}
def get_songs_dict(year):
    # get html content and parse page
    html_content = requests.get(url(year), headers=headers).text
    soup = BeautifulSoup(html_content, "html.parser")


    titles = []
    artists = []

    song_div = soup.find_all("div", class_="o-chart-results-list-row-container")
    for container in song_div:
        # make clean titles array
        titles.append(re.sub("\n","", container.find("h3", class_="c-title").text))
        # clean artist array
        clean_artist = re.sub("\n","", container.find("span", class_="lrv-u-display-block").text)
        artist_no_feat = re.sub("Featuring.*", "", clean_artist)
        if "The Black Eyed Peas" in artist_no_feat:
            artist_no_feat = "The Black Eyed Peas"
        artists.append(artist_no_feat)
    # Song dict, title : artist
    songs[f"{year}"] = dict(zip(titles, artists))
    return songs



# songs contains all top 100s from 2006-present
for i in range(2006,2007):
    get_songs_dict(i)

del songs["2006"]["My Humps"]
df = pd.DataFrame(columns=["Year", "Artist", "Song"])
pd.set_option('display.max_rows', 100)
display(df)
for year in songs:
    for song in songs[year]:
        # print(song, songs[year][song])
        df = df.append({"Year": year, "Artist": songs[year][song], "Song": song}, ignore_index=True)
display(df)

lyrics = df.apply(
    lambda row: getLyricsOfSong(row["Artist"], row["Song"]), axis=1
)
df["Lyrics"] = lyrics

display(df)

# copy into csv file


