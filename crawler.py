from urllib.parse import urljoin
from bs4 import BeautifulSoup
import requests


def get_a_tags(base_url):
    r = requests.get(base_url)
    html = r.text
    soup = BeautifulSoup(html)
    return soup.find_all('a', href=True)


def get_href(all_links):
    all_urls = []
    for line in all_links:
        all_urls.append(line['href'])
    return all_urls


def prepare_link(url, href):
    return urljoin(url, href)


# it will ignore realtive links
def get_related_links(all_hrefs, base_url):
    related_urls = []
    for link in all_hrefs:
        new_link = prepare_link(base_url, link)
        if url in new_link:
            related_urls.append(url)
    return related_urls


def print_related_urls(related_urls):
    for url in related_urls:
        print(url)


def main():
    
    url = 'hackbulgaria.com'
    base_url = 'http://hackbulgaria.com/'
    # all_urls = []
    related_urls = []
    a_tags = get_a_tags(base_url)
    all_hrefs = get_href(a_tags)
    related_links = get_related_links(all_hrefs, base_url)
    print(related_links)


if __name__ == '__main__':
    main()
