from .AbstractCrawler import AbstractCrawler
from ..exceptions import InternalErrorException

class StatusInvestCrawler(AbstractCrawler):
  def __init__(self):
    super(StatusInvestCrawler, self).__init__()
    self.__base_url = 'https://statusinvest.com.br'

  def get_stock(self, code):
    return self.crawl(f'{self.__base_url}/acoes/{code}')

  def get_reit(self, code):
    return self.crawl(f'{self.__base_url}/fundos-imobiliarios/{code}')

  def get_html(self, stock_type, code):
    try:
      if stock_type == 1:
        return self.get_stock(code)
      elif stock_type == 2:
        return self.get_reit(code)
      raise Exception()
    except Exception:
      raise InternalErrorException('Erro ao buscar as informações.')