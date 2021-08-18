import abc
import requests

class AbstractCrawler(abc.ABC):
  def __init__(self, parser):
    self.__parser = parser

  def crawl(self, url):
    try:
      return requests.get(url)
    except Exception as ex:
      print(ex)