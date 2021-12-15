from collections import Counter
import re

# n most popular words
def n_most_frequent(n, lyrics):
    split_string = lyrics.split()
    counted = Counter(split_string)
    most_freq = counted.most_common(n)
    return most_freq

# total occurence of specific word
def occurences_of_word(word, lyrics)
    return len(re.findall(f"{word}/i", lyrics))

# total occurrences of multiple words
def occurrences_of_words(*argv, lyrics):
    total = 0
    for arg in argv:
        total += len(re.findall(f"{arg}/i", lyrics))
    return total

# number of unique words
def no_unique_words(lyrics):
    unique = set()
    split_lyrics = lyrics.spliit()
    for word in split_lyrics:
        unique.add(word)
    return len(unique)