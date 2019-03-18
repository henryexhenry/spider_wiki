import requests
from bs4 import BeautifulSoup

req = requests.get('https://en.wikipedia.org/wiki/Reinforcement_learning')
soup = BeautifulSoup(req.text, "html.parser")
save = []
for i in soup.body.find_all('a'):
    try:
        save.append(i['href'])
    except(KeyError):
        print('KeyError')
print(len(save))