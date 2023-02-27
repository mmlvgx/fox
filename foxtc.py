from click import command, option
from compiler import compile


@command()
@option('-i', '--inp', default='index.fox', help='The name of the fox code file to transcompile')
@option('-o', '--out', default='index.html', help='The name of the output HTML code file')
def main(inp: str, out: str) -> None:
    '''Transcompiler fox code into HTML'''
    compile(inp, out)


if __name__ == '__main__':
    main()
