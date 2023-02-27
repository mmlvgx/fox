class Tag:
    def __init__(self, title: str) -> None:
        self.title = title


class OpeningTag(Tag):
    def __init__(self, title: str) -> None:
        super().__init__(title)

    def html(self) -> str:
        ...


class ClosingTag(Tag):
    def __init__(self, title: str) -> None:
        super().__init__(title)

    def html(self) -> str:
        ...


class Element:
    def __init__(
            self,
            opening: OpeningTag,
            content: str = None,
            closing: ClosingTag = None,
            parent: str = None
    ) -> None:
        self.opening = opening
        self.content = content if content is not None else str()
        self.closing = closing if closing is not None else str()
        self.parent = parent

    def html(self) -> str:
        ...


class Head(Element):
    def __init__(self, content: str = None) -> None:
        self.opening = OpeningTag('head')
        self.closing = ClosingTag('head')

        super().__init__(self.opening, content, self.closing)


class Body(Element):
    def __init__(self, content: str = None) -> None:
        self.opening = OpeningTag('body')
        self.closing = ClosingTag('body')

        super().__init__(self.opening, content, self.closing)


class PAR(Element):
    def __init__(self, content: str) -> None:
        self.opening = OpeningTag('p')
        self.closing = ClosingTag('p')

        super().__init__(self.opening, content, self.closing, 'body')


class TITLE(Element):
    def __init__(self, content: str) -> None:
        self.opening = OpeningTag('title')
        self.closing = ClosingTag('title')

        super().__init__(self.opening, content, self.closing, 'head')


class HEADER(Element):
    def __init__(self, content):
        self.opening = OpeningTag('h1')
        self.closing = ClosingTag('h1')

        super().__init__(self.opening, content, self.closing, 'body')


class HTML:
    def __init__(self, head: Head, body: Body) -> None:
        self.head = head
        self.body = body

        self.opening = OpeningTag('html')
        self.closing = OpeningTag('html')

    def html(self) -> str:
        ...
