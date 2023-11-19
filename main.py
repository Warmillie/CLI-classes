from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    pass


class Phone(Field):
    def __init__(self, value):
        self.validate(value)
        self.value = value

    def validate(self, value):
        if len(value) != 10 or not value.isdigit():
            raise ValueError('Phone should be 10 symbols')
        else:
            self.value = value
        
        


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

    def add_phone(self, phone_number: str):
        phone = Phone(phone_number)
        phone.validate(phone_number)
        if phone not in self.phones:
            self.phones.append(phone)

    def find_phone(self, phone_number: str):
        try:
            for phone in self.phones:
                if phone.value == phone_number:
                    return phone
        except Exception:
            raise ValueError("Phone not found")

    def edit_phone(self, old_phone, new_phone):
        for phone in self.phones:
            if phone.value == old_phone:
                phone.validate(new_phone)
                phone.value = new_phone
                return
        raise ValueError("Phone not found")
       
        

    def remove_phone(self, phone_number):
        for phone in self.phones:
            if phone.value == phone_number:
                self.phones.remove(phone)
                return
        raise ValueError("Phone not found")
        


class AddressBook(UserDict):
    # def __init__(self):
    #     self.contacts = {}

    def add_record(self, record: Record):
        self.data[record.name.value] = record

    def find(self, name: str):
        return self.data.get(name, None)
            

    def delete(self, name: str) -> None:
        if name in self.data:
            del self.data[name]
      
 