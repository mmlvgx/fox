from forms import PAR, TITLE, HEADER


class TokenType:
    def __init__(self, element, title, regex):
        self.element = element
        self.title = title
        self.regex = regex


class Token:
    def __init__(
            self,
            type,
            content,
            line,
            row
    ):
        self.type = type
        self.content = content
        self.line = line
        self.row = row


tokenTypeList = [
    TokenType(HEADER, '#', r'\#\s'),
    TokenType(PAR, '.', r'\.\s'),
    TokenType(TITLE, '@', r'\@\s')
]
