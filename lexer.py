from re import search
from warning import warn
from tokenizer import tokenTypeList
from tokenizer import Token


class Lexer:
    def __init__(self, lineList, tokenList):
        self.lineList = lineList
        self.tokenList = tokenList

    def analyze(self, filename):
        print(self.lineList)

        for line in self.lineList:
            row = self.lineList.index(line) + 1

            for tokenType in tokenTypeList:
                result = search(tokenType.regex, line)
                content = search(tokenType.regex + r'(.*?)$', line)

                if result is None:
                    continue
                elif content is None:
                    continue
                else:
                    break

            if result is None:
                warn(filename, line, row, 'Unknown Type')
                continue
            if content is None:
                warn(filename, line, row, 'Can not handle')
                continue

            self.tokenList.append(
                Token(tokenType, content.group(1), line, row))

            continue

        return self.tokenList
