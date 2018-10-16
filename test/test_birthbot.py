import datetime

from pytest import fixture


@fixture

def op():
    from travistest.birthbot import Birthday
    return Birthday(datetime.date(1995,11,25), "Jorge Gutierrez Segovia")

def test_birt_date(op):
    assert op.get_birth_date()

def test_name(op):
    assert op.get_name()

