import requests  # getting content from the TED Talk page
from bs4 import BeautifulSoup
import re
import sys  # for argument parsing


# Exception Handling

if len(sys.argv) > 1:
    url = sys.argv[1]
else:
    sys.exit("Error: Please enter the TED Talk URL")

# url = "https://www.ted.com/talks/jia jiang what i learned from 100 days of
# url = "https://www.ted.com/talks/ken robinson says schools kill creativity"

r = requests.get(url)

print("Download about to start")

soup = BeautifulSoup(r.content, features="lxml")

for val in soup.find_all("script"):
    if(re.search("talkPage.init", str(val))) is not None:
        result = str(val)

result_mp4 = re.search("(?P<url>https?://[^\s]+)(mp4)", result).group("url")

mp4_url = result_mp4.split('"')[0]

print("Downloading video from ......" + mp4_url)

file_name = mp4_url.split("/")[len(mp4_url.split("/"))-1].split('?')[0]

print("Storing video in ......." + file_name)
