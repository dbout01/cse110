import pathlib
cwd = pathlib.Path(__file__).parent.resolve()
bs = f'{cwd}/books.txt'

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

with open(bs) as book_file:

    for line in book_file:
        book = line.strip()
        print(book)