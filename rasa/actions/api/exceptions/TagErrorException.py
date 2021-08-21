class TagErrorException(Exception):
    def __init__(self, tag):
        self.tag = tag
        self.message = f'Erro ao processar o título "{tag}".'
        super().__init__(self.message)