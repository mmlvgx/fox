from tokenizer import Token


class Lexer:
    def __init__(self, lineList: list[str], tokenList: list[Token]) -> None:
        self.lineList = lineList
        self.tokenList = tokenList

    def analyze(self, filename: str) -> list[Token]: ...
