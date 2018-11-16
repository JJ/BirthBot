import datetime

from pytest import fixture


@fixture

#Operación que comprueba si el cumpleaños está bien
def op():
    from src.birthbot import Birthday
    cumpleanios = Birthday()
    cumpleanios.init_argumentos(datetime.date(1995,11,25), "Jorge Gutierrez Segovia")
    return cumpleanios

def test_birt_date(op):
    assert (op.get_birth_date() == datetime.date(1995,11,25))

def test_name(op):
    assert op.get_name() == "Jorge Gutierrez Segovia"

