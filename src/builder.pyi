from tokenizer import Token
from forms import HTML


class Builder:
    def __init__(self, html: HTML, tokenList: list[Token]) -> None:
        self.html = html
        self.tokenList = tokenList

    def build(self) -> None:
        ...
