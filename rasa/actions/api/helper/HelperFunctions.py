from ..exceptions import InternalErrorException, InvalidFundamentalistIndexException, UnrecognizedQueryTypeException

def get_info(tag_type, f_idx, response):
    try:
        return (__get_info_stock if tag_type == 1 else __get_info_reit)(f_idx, response)
    except Exception as e:
        raise e

def get_tag_type(q_type):
    lower_type = q_type.lower()
    if lower_type in ['da', 'da ação', 'da acao']:
        return 1
    elif lower_type in ['do', 'do fundo']:
        return 2
    else:
        raise UnrecognizedQueryTypeException()

def __get_info_stock(f_idx, response):
    try:
        clean_text = f_idx.lower()
        if clean_text in ['preço', 'preco']:
            return response.get('current_price')
        elif clean_text in ['nome', 'empresa', 'titulo']:
            return response.get('title')
        elif clean_text in ['cnpj']:
            return response.get('cnpj')
        elif clean_text in ['dividend yield', 'dy', 'd.y.', 'dy.', 'd.y']:
            return response.get('dividend_yield')
        elif clean_text in ['p/vp', 'pvp']:
            return response.get('indicators').get('P/VP')
    except Exception:
        raise InternalErrorException()
    raise InvalidFundamentalistIndexException(f_idx)
    
def __get_info_reit(f_idx, response):
    try:
        clean_text = f_idx.lower()
        if clean_text in ['preço', 'preco']:
            return response.get('current_price')
        elif clean_text in ['nome', 'empresa', 'titulo']:
            return response.get('title')
        elif clean_text in ['cnpj']:
            return response.get('info').get('CNPJ')
        elif clean_text in ['dividend yield', 'dy', 'd.y.', 'dy.', 'd.y']:
            return response.get('dividend_yield')
        elif clean_text in ['p/vp', 'pvp']:
            return response.get('indicators').get('P/VP')
    except Exception:
        raise InternalErrorException()
    raise InvalidFundamentalistIndexException(f_idx)