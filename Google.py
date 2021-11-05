from googlesearch import search
import urllib.request
from bs4 import BeautifulSoup

def google_scrape(url):
    thepage = urllib.request.urlopen(url)
    soup = BeautifulSoup(thepage, "html.parser")
    return soup.title.text

def Buscar(text):
    query = text
    for url in search(query, num_results=10):
        print(url)

