import urllib.request
import json

url = "https://raw.githubusercontent.com/dwyl/english-words/master/words_alpha.txt"
urllib.request.urlretrieve(url, "words_alpha.txt")

with open("words_alpha.txt") as f:
    words = [w.strip() for w in f if len(w.strip()) >= 4]

with open("words_4plus.json", "w") as f:
    json.dump(words, f)

print(f"Total words: {len(words)}")