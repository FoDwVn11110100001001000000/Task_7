from collections import UserDict
import phonenumbers
from datetime import datetime
from datetime import date as dates


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record
    
    def iterator(self, n):
        count = 0
        for k, v in self.data.items():
            if count < n:
                count += 1
                yield f'{k}: {v}'
            else:
                raise StopIteration


class Field:
    def __init__(self, value):
        self.value = value
        self._value2 = None

    @property
    def value2(self):
        return self._value2

    @value2.setter
    def value2(self, new_value):
        self._value2 = new_value

        
class Name(Field):
    pass


class Phone(Field):
    
    def true_number(self, number):
        try:
            parsed_number = phonenumbers.parse(number, "UA")
            if phonenumbers.is_valid_number(parsed_number):
                return True
            else:
                return False
        except phonenumbers.phonenumberutil.NumberParseException:
            print("Failed to parse phone number")
    
    @property
    def value(self):
        return self._value2
    
    @value.setter
    def value(self, new_value):
        if self.true_number(new_value):
            self._value2 = new_value
        else:
            return 'Invalid phone number'

class Birthday(Field):
    
    def check_correct(self, date):
        if isinstance(date, dates):
            return True

        @property
        def value(self):
            return self._value2
        
        @value.setter
        def value(self, new_value):

            if self.check_correct(new_value):
                self._value2 = new_value

            else:
                print(f'Invalid date')

class Record(Field):
    
    def __init__(self, name, phone, birthday=None):
        self.name = name

        if phone:
           self.phones = []
           self.phones.append(phone)

        if birthday:
            self.birthday = birthday

    def days_to_birthday(self):
        if self.birthday.value2:
            current_date = datetime.datetime.now()
            birth_date = datetime.datetime.strptime(self.value2, "%Y-%m-%d")
            if birth_date < current_date:
                next_birthday = datetime.datetime(year=current_date.year + 1, month=birth_date.month, day=birth_date.day)
            else: 
                next_birthday = birth_date
            days_left = (next_birthday - current_date).days + 1
            print("Days until next birthday:", days_left)
            return days_left
        else:
            return 'You didn\'t give your date of birth'   
    
    def add_birthday(self, birthday):
        self.birthday = birthday
    
    def add_phone(self, phone):
        try:
            self.phones.append(phone)
        except AttributeError:
            self.phones = []
            self.phones.append(phone)

    def remove_phone(self, phone):
        for old_phone in self.phones:
            if phone == old_phone.value:
                self.phones.remove(old_phone)

    def change_phone(self, phone, new_phone):
        for old_phone in self.phones:
            if phone == old_phone.value:
                self.phones[self.phones.index(old_phone)] = Phone(new_phone)
            