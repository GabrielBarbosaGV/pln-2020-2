import abc
import requests

from ..exceptions import InternalErrorException

class AbstractCrawler(abc.ABC):
  def crawl(self, url):
    try:
      return requests.get(url)
    except Exception:
      raise InternalErrorException()