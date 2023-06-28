import sys
from handlers import *


while True:
    cmd = input('Enter command: ')

    if cmd in ['close', 'good bye', 'exit']:
        save(address_book)
        print('Good bye')
        sys.exit()

    elif cmd.lower() in commands:
        func = commands[cmd](address_book)