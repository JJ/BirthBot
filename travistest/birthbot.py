import datetime

class Birthday:
    #Dos atributos , la fecha del cumpleaños y el nombre
    def __init__(self, birth_date, name):

        self.birth_date = birth_date
        self.name = name

    # Consultor de la fecha de cumpleaños
    def get_birth_date(self):
        return isinstance(self.birth_date, datetime.date)

    #Consultor del nombre 
    def set_name(self):
        return isinstance(self.name, str)

    #Modificador de la fecha de cumpleaños en modo año,mes,día
    def set_birth_date(self, birth_date):
        self.birth_date = birth_date

    #Modificador del nombre
    def set_name(self, name):
        self.name = name

    #Consultor del cumpleaños
    def get_birthday(self):
        print("Nombre: ", self.name)
        print("Birth Date: ", self.birth_date)

 
    