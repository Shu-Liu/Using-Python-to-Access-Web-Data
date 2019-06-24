import urllib.request, urllib.parse, urllib.error
import json

url = input('Enter URL:')
data = urllib.request.urlopen(url).read()

info = json.loads(data)

sum = 0
for comment in info["comments"]:
    sum += comment["count"]
print(sum)
