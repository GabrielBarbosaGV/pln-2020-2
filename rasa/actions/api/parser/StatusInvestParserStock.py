from bs4 import BeautifulSoup

from .AbstractParser import AbstractParser

class StatusInvestParserStock(AbstractParser):
  def get_indicator_container(self, bs):
    return bs.find('div', {'class': 'indicator-today-container'})

  def get_cnpj(self, bs):
    return bs.find('div', {'class': 'company-description'}).find('small').string

  def get_indicators(self, bs, indicators = ['P/L', 'D.Y', 'VPA', 'Dív. líquida/PL', 'P/VP']):
    def filter_indicators(tag):
      return tag.find('h3', {'class': 'title'}).string in indicators

    indicators_container = bs.find(
        'div', {'class': 'indicator-today-container'}
        )
    indicators_iterable = filter(
        filter_indicators, indicators_container.find_all('div', {'title': True})
        )
    filtered_indicators = {}
    for indicator in indicators_iterable:
      title = indicator.find('h3', {'class': 'title'}).string
      value = indicator.find('strong', {'class': 'value'}).string
      filtered_indicators[title] = value
    return filtered_indicators

  def parse(self, html):
    bs = BeautifulSoup(html, 'html.parser')
    return {
        'title': self.get_title(bs),
        'current_price': self.get_current_price(bs),
        'indicators': self.get_indicators(bs),
        'cnpj': self.get_cnpj(bs),
        'dividend_yield': self.get_dividend_yield(bs),
    }