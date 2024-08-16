import requests
from bs4 import BeautifulSoup

def  fetchAndSaveToFile(url, path):
    r = requests.get(url)
    with open(path, "w") as f:
        f.write(r.text)

url = "https://www.exploit-db.com/"

fetchAndSaveToFile(url, "data/exploit.html")

r = requests.get(url)
print(r.text)


with open("exploit.html", "r") as f:
    exploit_doc = f.read()

soup = BeautifulSoup(exploit_doc, 'html.parser')
print(soup.prettify())
print(soup.title, type(soup.title))
print(soup.div)
