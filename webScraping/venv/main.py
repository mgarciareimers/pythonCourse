import requests
from bs4 import BeautifulSoup
import pprint  # To format printing
import sys


# Method that sorts the news by votes (DESC).
def sort_stories_by_votes(news_list):
    return sorted(news_list, key=lambda k: k['votes'], reverse=True)


# Method that creates the custom hacker news list.
def create_custom_hacker_news(links, subtexts):
    hacker_news = []

    for index, link in enumerate(links):
        title = link.getText()
        href = link.get('href', None)

        vote = subtexts[index].select('.score')

        if len(vote):
            votes = int(vote[0].getText().replace(' points', ''))

            if votes >= 100:
                hacker_news.append({'title': title, 'href': href, 'votes': votes})

    return hacker_news


print('* Welcome to Hacker News Top News')

download = True
page_number = 0
custom_hacker_news = []

print('  Starting download...')

while download:
    page_number = page_number + 1
    url = f'https://news.ycombinator.com/news?p={ page_number }'
    response = requests.get(url)

    # Parse the response to HTML
    soup = BeautifulSoup(response.text, 'html.parser')

    # Get the links and the votes.
    links = soup.select('.storylink')
    subtexts = soup.select('.subtext')

    if len(links) <= 0 or len(subtexts) <= 0:
        download = False
        continue

    for new in create_custom_hacker_news(links, subtexts):
        custom_hacker_news.append(new)

    sys.stdout.write(f'\r  Current Page Number: { page_number }')
    sys.stdout.flush()

# Get the custom hacker news.
custom_hacker_news = sort_stories_by_votes(custom_hacker_news)
print(f'\n\n Custom news ({len(custom_hacker_news)}): \n')
pprint.pp(f'{custom_hacker_news}')
