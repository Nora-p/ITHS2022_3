import pytest
import Patient_new

print("1")


def test_name():
    assert Patient_new.patient.findname("John", "Smith") == ("JohnSmith")


print("2")


def test_age():
    assert Patient_new.patient.findage(20) == 20


def test_sal():
    assert Patient_new.patient.findsal(44000) == 44000


def test_gender():
    assert Patient_new.patient.findgender("male") == "male"


def test_phone():
    assert Patient_new.patient.findphone("0708112233") == "0708112233"
