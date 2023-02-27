import re

from tokenizer import tokenTypeList
from tokenizer import Token


class Lexer:
    def __init__(self, lineList, tokenList):
        self.lineList = lineList
        self.tokenList = tokenList

    def analyze(self):
        for line in self.lineList:
            row = self.lineList.index(line) + 1

            for tokenType in tokenTypeList:
                result = re.search(tokenType.regex, line)
                content = re.search(tokenType.regex + r'(.*?)$', line)

                if result is not None and content is not None:
                    self.tokenList.append(
                        Token(tokenType, content.group(1), line, row))

        return self.tokenList
