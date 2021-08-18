from .crawler import StatusInvestCrawler
from .parser import StatusInvestParser

class StatusInvestAPI:
    def __init__(self):
        self.crawler = StatusInvestCrawler(None)
        self.parser = StatusInvestParser()

    def query(self, tag_type, tag):
        response = self.crawler.get_html(tag_type, tag)
        return self.parser.parse(tag_type, response.text)