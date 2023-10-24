def bedroom():
    print('You have entered the bedroom')
    input()
    foyer()
def library():
    print('You have entered the library')
    input()
    foyer()
def living_room():
    print('You have entered the living room')
    input()
    foyer()


def foyer():
    print('You enter a dark foyer...')
    print('What room would you like to go to next?')
    room = input()
    if room in 'bedroom':
        bedroom()
    elif room in 'library':
        library()
    else:
        living_room()

foyer()