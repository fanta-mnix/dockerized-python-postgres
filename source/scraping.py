import bs4
import requests


def fetch_list(page):
    assert page > 0
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
        'cookie': 'ahoy_visitor=06509f38-4325-45d4-af65-4a8c585e904b; G_ENABLED_IDPS=google; _ym_uid=1508926870619291470; visits_count=2; ahoy_visit_last_counted=22856362-0ac1-4ca2-a7a7-c9c7470c3714; _ym_isad=2; G_AUTHUSER_H=0; user_credentials=f4cdfecda0832ec0ff90331045f4bd18e1cdefe9b678355a29adbec63cbef834055e6e96bcfd0fe03eaff2e9a19fb1ba4d42d4b7a097294fade1eeb80f993156%3A%3A415454%3A%3A2018-01-26T11%3A32%3A22Z; _ga=GA1.2.1534052107.1508926868; _gid=GA1.2.439928894.1509017528; _ym_visorc_32365145=w; __smVID=21c90b95175f139387f542a843fe2e634b4674e1af20ead2044fde398da2c172; __smToken=6q9HjHFVSL1udLBiehRDg5pE; ahoy_visit=22856362-0ac1-4ca2-a7a7-c9c7470c3714; _rocky_session=VWVQalpveXpDSzJ4Umt1VW1Ndzlzblh2L3p3Sm1YcHMya29kQkpXTXVEZm1VNDIxQWJINUFyYnNrQkVLT0ZsTStYR09odzkxaVFyQzdjV1o4blJRTjBMNkdySE4xYWVmTUdXOXNkWTNIajlwSysxbGtVVnAvZitEV3dwaHpTeTR6bnJtMlZRbDhUazlIU3U2OU9WdGpqbi82UC9FRVpPS3c1aStOMVQ2UVdpeEtmVUVnZWZCcHVrYWJIa3grVHUvOUwwOE1vYWJWdllqdUhjVFNmU3BBcWg5ajZOaUVaQ2JvOWw2dkU0YkR6MjU0WjAzbzJvdEVsZHZrMGY4T2dHTFZlckY3eCtkZHpXZFl2UUdWZ05rbCtzSUFQV2d6RG91V2ZyWTV1NlBjbjVBS1J1K2ZOd0g5K09xZk5LRk9QaUJFZWl6TzFPeVdZbFZRWE04RjFtSGJBPT0tLTh4c1Q4YUF1a05MaENLazhxTGhncWc9PQ%3D%3D--5a28d466e6ca6a9719649316fa7486208417e513; AWSELB=D95FE35D1EC9470BBAF917432AE1C08AF731593EA5EA9C820B5DF86C68228C305FFC6F3919071CAA4F3690DD8F47587A6DE2271A606032A83823DE6BB5488905D8B5BEA398'
    }
    response = requests.get('https://www.inkitt.com/list', params={'page': page, 'period': 'alltime'}, headers=headers)
    if response.status_code != 200:
        raise ValueError('Request failed with status {}'.format(response.status_code))
    return str(response.content, 'utf-8')


def parse_list(content):
    import re

    def normalize_whitespace(text):
        return re.sub('\s+', ' ', text).strip()

    def extract_features(book):
        title = book.select_one('a.storyCard-title').text
        description = book.select_one('p.story-description').text
        meta = book.select_one('p.story-meta-information').text
        match = re.match(r'(?us)(.*?)\sby\s(.*?)\s•', meta)
        if not match:
            raise ValueError("Unknown format: '{}'".format(meta))

        return {'title': normalize_whitespace(title),
                'description': normalize_whitespace(description),
                'genre': normalize_whitespace(match.group(1)),
                'author': normalize_whitespace(match.group(2))}

    page = bs4.BeautifulSoup(content, 'html5lib')
    books = page.select('div.story-desc-container')

    return (extract_features(book) for book in books)


def books_at(page):
    print("Scraping results at page {}".format(page))
    return parse_list(fetch_list(page))
