#This import keeps you fron typing out the whole path

import pathlib
cwd = pathlib.Path(__file__).parent.resolve()
hr = f'{cwd}/hr.txt'

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# This sets the groundwork for opening files

with open(hr) as f:

    for line in f:
        parts = line.strip().split(' ')
        name = parts[0]
        title = parts[2]
        print(f'Name: {name}, Title: {title}')

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -