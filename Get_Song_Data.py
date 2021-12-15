from API_Key import client_access_token
import lyricsgenius
import re

# lyrics genius config
client_id = 'lk42cP4HOSpxuP1nmNyYDMqEe-T5os6phfxxxCM3B7zrRWXLszOct-RBgmNS0RQo'
genius = lyricsgenius.Genius(client_access_token,
                             remove_section_headers=True,
                             skip_non_songs=True,
                             excluded_terms=["(Remix)", "(Live)"])

genius.verbose = False

def cleanString(string):
    inline_string = string.replace('\n', ' ')
    return re.sub("\d?\d?\dEmbedShare URLCopyEmbedCopy\s?", "", inline_string)

def getLyricsOfSong(artist, song):
    artist = genius.search_artist(artist, max_songs=0)
    song = artist.song(song)
    return cleanString(song.lyrics)

def getTopSongs(artist, max_songs):
    songs = genius.search_artist(f"{artist}", max_songs=max_songs, include_features=False).songs
    return songs

def getLyricsFromSongs(songs):
    lyrics = [song.lyrics.replace('\n', ' ') for song in songs]
    clean_lyrics = list(map(lambda x: re.sub("\d?\d?\dEmbedShare URLCopyEmbedCopy\s?", "", x), lyrics))
    return clean_lyrics

#### Final Function ####

## Needs error handling...try/catch?
def getLyrics(artist, max_songs):
        songs = getTopSongs(artist, max_songs)
        lyrics = getLyricsFromSongs(songs)
        print(lyrics)

