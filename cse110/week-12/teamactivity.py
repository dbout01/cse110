# This is one of many ways to do this. A good stretch would be to use a menu instead.
choice = input(
    'What volume of scripture do you want to print? ').strip().lower()

with open('book.txt') as f:

    largest_chapter = 0
    largest_book = ''

    for line in f:

        book, chapter, scripture = line.strip().split(':')

        # This may or may not need to be changed.
        print(f'Scripture: {scripture}, Book: {book}, Chapter: {chapter}')

        if int(chapter) > largest_chapter:
            largest_chapter = int(chapter)
            largest_book = book

        # if conditions... if-elif
        if scripture.lower() == choice:
            # This means the user picked this volume of scripture.

            """
            You will need to make new variables similar to largest_chapter and
            largest_book to track the same type of data but only for the volume
            of scripture the user choose.
            """
            pass

# This may or may not need to be changed.
print(
    f'The largest volume of scripture is {largest_book} with {largest_chapter} chapters.')

# You will most likely print more things here...