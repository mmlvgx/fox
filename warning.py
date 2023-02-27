from colorama import init
from colorama import Back

init(autoreset=True)


def warn(filename, line, row, description):
    print(Back.RED + 'WARNING', end=' ')
    print(f'In {filename}, row {row}')
    print(f'\t{line}')
    print(f'\t{"^" * len(line)}')
    print(description)
