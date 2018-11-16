import datetime

class Birthday:

    @classmethod 
    #Constructor por parámetros
    #Dos atributos , la fecha del cumpleaños y el nombre
    def init_argumentos(self, birth_date, name):

        self.birth_date = birth_date
        self.name = name

    @classmethod 
    #Constructor por defecto
    def init_defecto(self):
        self.birth_date = None
        self.name = None

    #Función que evalua el estado de la clase
    def status(self):
        return True
        
    # Consultor de la fecha de cumpleaños
    def get_birth_date(self):
        return self.birth_date

    #Consultor del nombre 
    def get_name(self):
        return self.name

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

 
    
