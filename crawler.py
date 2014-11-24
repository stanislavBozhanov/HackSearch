from bs4 import BeautifulSoup
import requests

url = 'teyadiya.com'
base_url = 'http://teyadiya.com/'
all_urls = []
related_urls = []


def get_href(all_links):
    for line in all_links:
        all_urls.append(line['href'])


# it will ignore realtive links
def get_internal_links(all_urls, url):
    for link in all_urls:
        if url in link:
            related_urls.append(link)


def get_a_tags(base_url):
    r = requests.get(base_url)
    html = r.text
    soup = BeautifulSoup(html)
    return soup.find_all('a', href=True)


def print_related_urls():
    for url in related_urls:
        print(url)


def main():
    all_links = get_a_tags(base_url)
    get_href(all_links)
    get_internal_links(all_urls, url)
    print_related_urls()

if __name__ == '__main__':
    main()
