class Builder:
    def __init__(self, html, tokenList):
        self.html = html
        self.tokenList = tokenList

    def build(self):
        for token in self.tokenList:
            content = token.content.strip()

            element = token.type.element(content)

            match element.parent:
                case 'head':
                    self.html.head.content += \
                        element.html()
                case 'body':
                    self.html.body.content += \
                        element.html()
