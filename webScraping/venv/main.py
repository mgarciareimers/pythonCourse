import requests
from bs4 import BeautifulSoup


def create_custom_hacker_news(links, subtexts):
    hacker_news = []

    for index, link in enumerate(links):
        title = link.getText()
        href = link.get('href', None)

        vote = subtexts[index].select('.score')

        if len(vote):
            hacker_news.append({'title': title, 'href': href, 'votes': int(vote[0].getText().replace(' points', ''))})

    return hacker_news


url = 'https://news.ycombinator.com/news'
response = requests.get(url)

# Parse the response to HTML
soup = BeautifulSoup(response.text, 'html.parser')

# Get the links and the votes.
links = soup.select('.storylink')
subtexts = soup.select('.subtext')

# Get the custom hacker news.
print(create_custom_hacker_news(links, subtexts))
