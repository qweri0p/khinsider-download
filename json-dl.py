#!/usr/bin/env python
import khinsider, json
f = open('music.json')
def dl(ost, fmt):
    khinsider.download(ost,ost,True,[fmt],True)
data = json.load(f)
for i in data["flac"]:
    dl(i,"flac")
print("Downloaded all flac soundtracks")
for i in data["m4a"]:
    dl(i, 'm4a')
print("Downloaded all m4a soundtracks")
for i in data["mp3"]:
    dl(i, 'mp3')
print("Downloaded all mp3 soundtracks")
print("Done")
