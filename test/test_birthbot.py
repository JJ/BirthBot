import datetime

from pytest import fixture


@fixture

#Operación que comprueba si el cumpleaños está bien
def op():
    from travistest.birthbot import Birthday
    cumple = Birthday()
    cumple.init_argumentos(datetime.date(1995,11,25), "Jorge Gutierrez Segovia")
    return cumple

def test_birt_date(op):
    assert op.get_birth_date()

def test_name(op):
    assert op.get_name()

