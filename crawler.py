from urllib.parse import urljoin
from bs4 import BeautifulSoup, Doctype
import requests
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

url = 'boredpanda.com'
home_url = 'http://' + url + '/'
engine = create_engine("sqlite:///hacksearch.db")
session = Session(bind=engine)

class Cralwer():

    def __init__(self, url, session):
        self.url = url
        self.home_url = 'http://' + url + '/'
        self.session = session
        self.crawl_queue = [self.home_url]
        self.visited = []

    def get_beautiful_soup(self, home_url):
        r = requests.get(home_url)
        html = r.text
        soup = BeautifulSoup(html)
        return soup

    def soup_is_html_version_five(self, soup):
        items = [item for item in soup.contents if isinstance(item, Doctype)]
        if not items[0]:
            return None
        if items[0].lower() == 'doctype html':
            return True
        return False

    def soup_get_page_description(self, soup):
            desc = soup.findAll(attrs={"name": "description"})
            return desc[0]['content']

    def soup_get_title(self, soup):
        return soup.title.string

    def store_data(self, url):
        pass

    def get_a_tags(self, soup):
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
        #self.store_data(url)
        soup = self.get_beautiful_soup(url)
        a_tags = self.get_a_tags(soup)
        all_hrefs = self.get_hrefs(a_tags)
        all_links = []
        for href in all_hrefs:
            all_links.append(self.prepare_link(self.home_url, href))
        # print(all_links)
        all_links = self.filter_links(base_url, all_links, self.visited)
        #print(all_links)
        self.crawl_queue.extend(all_links)

    def start(self):
        while self.crawl_more():
            current_url = self.get_next_craw()
            self.crawl(current_url, self.url)
        return self.crawled_data
        #self.crawl(self.get_next_craw())


def main():
    crawler = Cralwer(url, session)
    soup = crawler.get_beautiful_soup(crawler.home_url)
    if crawler.soup_is_html_version_five(soup)
    print(crawler.soup_get_html_version(soup))
    print(crawler.soup_get_title(soup))
    print(crawler.soup_get_page_description(soup))

if __name__ == '__main__':
    main()
