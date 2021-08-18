from bs4 import BeautifulSoup

from .AbstractParser import AbstractParser

class StatusInvestParser(AbstractParser):
  # Fields commons for stocks and reit
  def min_52_weeks():
    pass

  def min_last_month():
    pass

  def max_52_weeks():
    pass

  def max_last_month():
    pass

  def dividend_yield_last_12_months():
    pass

  def dividend_yield_last_12_months_sum_values():
    pass

  def valorization_last_year():
    pass

  def valorization_cur_month():
    pass

  def get_indicator_container(self, bs):
    return bs.find('div', {'class': 'indicator-today-container'})

  def get_cnpj(self, bs):
    return bs.find('div', {'class': 'company-description'}).find('small').string
  
  def get_title(self, bs):
    return bs.find(
        'header', {'role': 'heading'}
        ).find('h1', {'class': 'lh-4'}).get('title')

  def get_current_price(self, bs):
    return bs.find(
        'div', {'title': 'Valor atual do ativo'}
        ).find('strong', {'class': 'value'}).string

  def get_indicators(self, bs, indicators):
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

  def parse(self, html, indicators = ['P/L', 'D.Y', 'VPA', 'Dív. líquida/PL']):
    bs = BeautifulSoup(html, 'html.parser')
    return {
        'title': self.get_title(bs),
        'current_price': self.get_current_price(bs),
        'indicators': self.get_indicators(bs, indicators),
        'cnpj': self.get_cnpj(bs),
    }