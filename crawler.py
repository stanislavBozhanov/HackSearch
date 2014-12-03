from urllib.parse import urljoin
from bs4 import BeautifulSoup
import requests


class Cralwer:

    def __init__(self, url, session):
        self.url = url
        self.home_url = 'http://' + url + '/'
        self.session = session
        self.crawl_queue = [self.home_url]
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

    def prepare_link(self, home_url, href):
        return urljoin(home_url, href)

    def filter_links(self, base_url, all_links, visited):
        filtered_links = []
        for link in all_links:
            if base_url in link and link not in visited:
                filtered_links.append(link)
        return filtered_links

    def crawl_more(self):
        return len(self.crawl_queue) != 0

    def get_next_craw(self):
        return self.crawl_queue.pop()

    def crawl(self, url, base_url):
        print(url)
        self.visited.append(url)
        a_tags = self.get_a_tags(url)
        all_hrefs = self.get_hrefs(a_tags)
        all_links = []
        for href in all_hrefs:
            all_links.append(self.prepare_link(self.home_url, href))
        # print(all_links)
        all_links = self.filter_links(base_url, all_links, self.visited)
        #print(all_links)
        #self.store_data(all_links)
        self.crawl_queue.extend(all_links)

    def start(self):
        while self.crawl_more():
            current_url = self.get_next_craw()
            self.crawl(current_url, self.url)
        return self.crawled_data
        #self.crawl(self.get_next_craw())
