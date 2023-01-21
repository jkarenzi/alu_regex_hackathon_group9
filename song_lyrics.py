#!/usr/bin/python3
#Song lyrics that match the pattern "[Verse X} some lyrics"
#X as the number and "some lyrics" as any string of characters.

import re

song_lyrics = re.compile(r"\[verse [0-9]\] [ \w]+")


def song_search(string):
    lyrics_pattern = song_lyrics.findall(String)
    if lyrics_pattern:
        return 'The lyrics are: ' + ', '.join(lyrics)
    else:
        return 'There are no lyrics.'

