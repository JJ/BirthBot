import datetime

from pytest import fixture

@fixture

def op():
    from travistest.birthbot import Birthday
    return Birthday(datetime.date(1995,11,25), "Jorge Gutiérrez Segovia")

def test_birt_date(op):
    assert op.get_birth_date(self)

def test_equipo_local(op):
    assert op.comprobar_equipo_local()

def test_equipo_visitante(op):
    assert op.comprobar_equipo_visitante()
       
def test_fecha(op):
    assert op.comprobar_fecha()

def test_hora(op):
    assert op.comprobar_hora()

def test_lugar(op):
    assert op.comprobar_lugar()

def test_canalTV(op):
    assert op.comprobar_canalTV()