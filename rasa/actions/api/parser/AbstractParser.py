import abc

class AbstractParser(abc.ABC):
  def get_title(self, bs):
    return bs.find(
        'header', {'role': 'heading'}
        ).find('h1', {'class': 'lh-4'}).text

  def get_current_price(self, bs):
    return bs.find(
        'div', {'title': 'Valor atual do ativo'}
        ).find('strong', {'class': 'value'}).string

  def get_dividend_yield(self, bs):
    return bs.find(
        'div', {'title': 'Dividend Yield com base nos últimos 12 meses'}
        ).find('strong', {'class': 'value'}).string

  @abc.abstractmethod
  def parse(self, html):
    pass