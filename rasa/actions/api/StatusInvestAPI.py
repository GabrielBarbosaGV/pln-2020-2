from .exceptions import TagErrorException
from .crawler import StatusInvestCrawler
from .parser import StatusInvestParser

class StatusInvestAPI:
    def __init__(self):
        self.crawler = StatusInvestCrawler()
        self.parser = StatusInvestParser()

    def query(self, tag_type, tag):
        try:
            response = self.crawler.get_html(tag_type, tag)
            return self.parser.parse(tag_type, response.text)
        except Exception:
            raise TagErrorException(tag)