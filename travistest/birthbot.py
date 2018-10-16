import datetime

class Birthday:
    def __init__(self, birth_date, name):

        self.birth_date = birth_date
        self.name = name

    def get_birth_date(self):
        return isinstance(self.birth_date, datetime.date)

    def set_name(self):
        return isinstance(self.name, str)

    def set_birth_date(self, birth_date):
        self.birth_date = birth_date

    def set_name(self, name):
        self.name = name

    def get_birthday(self):
        print("Nombre: ", self.name)
        print("Birth Date: ", self.birth_date)

 
    
