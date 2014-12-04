import unittest
from crawler import Cralwer
from connection import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


class CrawerTests(unittest.TestCase):
    def setUp(self):
        self.url = 'boredpanda.com'
        self.home_url = 'http://' + self.url + '/'
        self.engine = create_engine("sqlite:///hacksearch.db")
        self.session = Session(bind=self.engine)
        Base.metadata.create_all(self.engine)
        self.crawler = Cralwer(self.url, self.session)
        self.soup = self.crawler.get_beautiful_soup(self.home_url)

    def test_soup_get_html_version(self):
        self.assertEqual(self.crawler.soup_get_html_version(self.soup), 'html5')

if __name__ == '__main__':
    unittest.main()
