import requests
from bs4 import BeautifulSoup
import pprint

response = requests.get('https://news.ycombinator.com/news')

soup = BeautifulSoup(markup=response.text,
                     features='html.parser')

links = soup.select('.storylink')
subtexts = soup.select('.subtext')


def sort_news_by_votes(hackernews):
    return sorted(hackernews,
                  key=lambda x: x['votes'],
                  reverse=True)


def create_custom_hackernews(links, subtexts):
    hackernews = []
    for index, item in enumerate(links):
        title = links[index].getText()
        href = links[index].get('href', None)
        vote = subtexts[index].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points > 99:
                hackernews.append({'title': title,
                                   'link': href,
                                   'votes': points})
    return sort_news_by_votes(hackernews)


for item in create_custom_hackernews(links, subtexts):
    pprint.pprint(item)
