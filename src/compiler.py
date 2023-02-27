from filer import lines
from lexer import Lexer
from builder import Builder
from forms import HTML, Body, Head


def compile(input__, output__=None):

    with open(input__, 'r') as _input:
        lineList = lines(_input)

    tokenList = list()
    html = HTML(Head(), Body())

    tokenList = Lexer(lineList, tokenList)\
        .analyze(input__)
    Builder(html, tokenList)\
        .build()

    with open(output__, 'w') as _output:
        _output.write(html.html())
