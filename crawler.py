from urllib.parse import urljoin
from bs4 import BeautifulSoup
import requests


class Cralwer:

    def __init__(self, url):
        self.url = url
        self.home_url = 'http://' + url + '/'
        self.crawl_queue = []
        self.visited = []

    def get_a_tags(self, home_url):
        r = requests.get(home_url)
        html = r.text
        soup = BeautifulSoup(html)
        return soup.find_all('a', href=True)

    def get_hrefs(self, all_a_tags):
        all_hrefs = []
        for a_tag in all_a_tags:
            all_hrefs.append(a_tag['href'])
        return all_hrefs

    def filter_links(base_url, all_links, visited):
        filtered_links = []
        for link in all_links:
            if base_url in link and link not in visited:
                filtered_links.append(link)
        return filtered_links

    def prepare_link(self, home_url, href):
        return urljoin(home_url, href)
