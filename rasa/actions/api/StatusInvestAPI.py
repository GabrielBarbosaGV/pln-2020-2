from .crawler import StatusInvestCrawler
from .parser import StatusInvestParser

class StatusInvestAPI:
    def __init__(self):
        self.crawler = StatusInvestCrawler(None)
        self.parser = StatusInvestParser()

    def query(self, tag, tag_type):
        return self.__query_stock(tag) if tag_type == 1 else self.__query_reit(tag)

    def __query_stock(self, tag):
        response = self.crawler.get_html(1, tag)
        return self.parser.parse(response.text)

    def __query_reit(self, tag):
        pass