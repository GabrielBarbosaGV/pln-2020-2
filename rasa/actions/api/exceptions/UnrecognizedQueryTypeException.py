class UnrecognizedQueryTypeException(Exception):
    def __init__(self):
        self.message = "Não consegui diferenciar entre ação e fundos." 
        super().__init__(self.message)