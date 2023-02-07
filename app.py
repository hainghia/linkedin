import requests
from bs4 import BeautifulSoup
import os

HTMLFileToBeOpened = open("index.html", "r")
contents = HTMLFileToBeOpened.read()

soup = BeautifulSoup(contents, 'html.parser')
data = soup.text
os.remove('temp.txt')
os.remove('file.txt')

with open('temp.txt', 'w') as wf:
    data = str(data)
    wf.write(str(data))
result = ''

with open('temp.txt', 'r') as file:
    for line in file:
        if not line.isspace():
            result += line

    file.seek(0)
    with open('file.txt', 'w') as wf:
        wf.write(result)
