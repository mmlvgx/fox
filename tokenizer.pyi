from annotations import Pattern
from forms import PAR, TITLE, HEADER


class TokenType:
    def __init__(
            self,
            element: PAR | TITLE,
            title: str,
            regex: Pattern | str
    ) -> None:
        self.element = element
        self.title = title
        self.regex = regex


class Token:
    def __init__(
            self,
            type: PAR | TITLE,
            content: str,
            line: str,
            row: int
    ) -> None:
        self.type = type
        self.content = content
        self.line = line
        self.row = row


tokenTypeList = [
    TokenType(HEADER, '#', r'\#'),
    TokenType(PAR, '.', r'\.'),
    TokenType(TITLE, '@', r'\@')
]
