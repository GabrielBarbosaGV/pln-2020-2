class InvalidFundamentalistIndexException(Exception):
    def __init__(self, f_idx):
        self.f_idx = f_idx
        self.message = f'O índice fundamentalista "{f_idx}" não foi reconhecido.'
        super().__init__(self.message)