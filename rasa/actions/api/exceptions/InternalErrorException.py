class InternalErrorException(Exception):
    def __init__(self, message = ''):
        self.message = f'Ocorreu um erro internamente. {message}' 
        super().__init__(self.message)