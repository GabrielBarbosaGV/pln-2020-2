from bs4 import BeautifulSoup

from .AbstractParser import AbstractParser

class StatusInvestParserReit(AbstractParser):
  def get_info(self, bs):
    def filter_by_str(tag, infos_str = {'cnpj', 'nome pregão', 'início do fundo', 'prazo de duração', 'tipo anbima', 'segmento anbima'}):
      return tag.find('h3', {'class': 'title'}).string.lower() in infos_str

    info_container = bs.find(
      'div', {
        'class': 'company',
      }).find(
        'div', {
          'class': 'top-info top-info-1 top-info-md-2 sm d-flex justify-between'
        })
    info_iterable = filter(
      filter_by_str, info_container.find_all('div', {'class': "info"})
    )
    info_dict = {}
    for info in info_iterable:
      title = info.find('h3', {'class': 'title'}).string
      value = info.find('strong', {'class': 'value'}).string
      info_dict[title] = value
    return info_dict

  def get_indicators(self, bs):
    def filter_by_str(
      tag, 
      infos_str = {'val. patrimonial p/cota', 'p/vp', 'valor em caixa'}):
      tag_str = tag.find('h3', {'class': 'title'}).string
      return tag_str.lower() in infos_str if tag_str else False

    indicators_container = bs.find(
        'div', {'class': 'top-info top-info-2 top-info-md-3 top-info-lg-n d-flex justify-between'}
        )
    indicators_iterable = filter(
        filter_by_str, indicators_container.find_all('div', {'class': 'info'})
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
        'dividend_yield': self.get_dividend_yield(bs),
        'info': self.get_info(bs),
        'indicators': self.get_indicators(bs),
    }