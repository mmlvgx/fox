class Tag:
    def __init__(self, title):
        self.title = title


class OpeningTag(Tag):
    def __init__(self, title):
        super().__init__(title)

    def html(self):
        return f'<{self.title}>'


class ClosingTag(Tag):
    def __init__(self, title):
        super().__init__(title)

    def html(self):
        return f'</{self.title}>'


class Element:
    def __init__(self, opening, content=None, closing=None, parent=None):
        self.opening = opening
        self.content = content if content is not None else str()
        self.closing = closing if closing is not None else str()
        self.parent = parent

    def html(self):
        return f'{self.opening.html()}{self.content}{self.closing.html()}'


class Head(Element):
    def __init__(self, content=None):
        self.opening = OpeningTag('head')
        self.closing = ClosingTag('head')

        super().__init__(self.opening, content, self.closing)


class Body(Element):
    def __init__(self, content=None):
        self.opening = OpeningTag('body')
        self.closing = ClosingTag('body')

        super().__init__(self.opening, content, self.closing)


class PAR(Element):
    def __init__(self, content):
        self.opening = OpeningTag('p')
        self.closing = ClosingTag('p')

        super().__init__(self.opening, content, self.closing, 'body')


class TITLE(Element):
    def __init__(self, content):
        self.opening = OpeningTag('title')
        self.closing = ClosingTag('title')

        super().__init__(self.opening, content, self.closing, 'head')


class HEADER(Element):
    def __init__(self, content):
        self.opening = OpeningTag('h1')
        self.closing = ClosingTag('h1')

        super().__init__(self.opening, content, self.closing, 'body')


class HTML:
    def __init__(self, head, body):
        self.head = head
        self.body = body

        self.opening = OpeningTag('html')
        self.closing = OpeningTag('html')

    def html(self):
        return f'{self.opening.html()}{self.head.html()}{self.body.html()}{self.closing.html()}'
