import pathlib
cwd = pathlib.Path(__file__).parent.resolve()
bc = f'{cwd}/bc.txt'

choice = input('Which volume of scripture would you like to review?').strip().lower()


with open(bc) as f:

    largest_chapter = 0
    largest_book = ''


    for line in f:
        book, chapter, scripture = line.strip().split(':')

        if choice in scripture.lower():
            print(f' Scripture: {scripture}, Book: {book}, Chapters: {chapter}')

        if int(chapter) > largest_chapter:
            largest_chapter = int(chapter)
            largest_book = book


print(f'The largest amount of chapters is {largest_chapter} in {largest_book}')