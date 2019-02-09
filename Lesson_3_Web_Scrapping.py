from bs4 import BeautifulSoup
import urllib.request

soup = BeautifulSoup(urllib.request.urlopen('https://en.wikipedia.org/wiki/Deep_learning'), features="html.parser")

print(soup.title.string) # prints title of wiki page

for link in soup.find_all('a'):     # finds all links in wiki page (<a> tag defines hyperlink)
    print(link.get('href'))         # href attribte indicates the link destination