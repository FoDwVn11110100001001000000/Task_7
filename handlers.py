import pickle
import os

from class_storage import AddressBook, Name, Phone, Birthday, Record

address_book = AddressBook()

def hello(*_):
    print('How can I help you?')

def add(data):
    name = data.get('name')
    phone = data.get('phone')
    birthday = data.get('birthday')
    record = Record(Name(name), Phone(phone), Birthday(birthday))
    address_book.add_record(record)

def change(record, phone, new_phone):
    record.change_phone(phone, new_phone)
    print("Phone number changed successfully.")

def add_phone(record, phone):
    record.add_phone(phone)
    print("Phone number added successfully.")

def remove_phone(record, phone):
    record.remove_phone(phone)
    print("Phone number removed successfully.")

def show_all(address_book):
    for record in address_book.data.values():
        print(f"Name: {record.name.value}")
        print("Phones:")
        for phone in record.phones:
            print(phone.value)
        print("---")

def help_lists(*_):
    text = ('Доступні команди для формування запиту:\n'
        '- Hello - навіть наш бот любить ввічливих\n'
        '- Add - додати контакт (формат запиту: Add *Name* 0500000000)\n'
        '- Change - змінити номер телефону в контакті (формат запиту: Change *Name* 0500000000)\n'
        '- Show all - показати список всіх контактів\n'
        '- Help me - викликати меню команд\n'
        'Для завершення роботи бота введіть "good bye", "close", "exit"'
        )
    print(text)

script_directory = os.path.dirname(os.path.abspath(__file__))
address_book_file = os.path.join(script_directory, 'address_book.bin')

def load():
    try:
        with open(address_book_file, 'rb') as file:
            return pickle.load(file)
    except FileNotFoundError:
        return AddressBook()

def save(address_book):
    with open(address_book_file, 'wb') as file:
        pickle.dump(address_book, file)



commands = {
    'hello': hello,
    'add': add,
    'change': change,
    'add phone': add_phone,
    'remove phone': remove_phone,
    'show all': show_all,
    'help me': help_lists,
    'load': load
}

