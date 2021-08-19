class InternalErrorException(Exception):
    def __init__(self):
        self.message = 'Ocorreu um erro internamente.' 
        super().__init__(self.message)