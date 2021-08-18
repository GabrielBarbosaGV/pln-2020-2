from .StatusInvestParserReit import StatusInvestParserReit
from .StatusInvestParserStock import StatusInvestParserStock

class StatusInvestParser:
    def __init__(self):
        self.reit = StatusInvestParserReit()
        self.stock = StatusInvestParserStock()

    def parse(self, tag_type, bs):
        return (self.stock if tag_type == 1 else self.reit).parse(bs)
