import Patient_new

def test_name():
    assert Patient_new.patient.findname("John","Smith") == "John Smith"

def test_age():
    assert Patient_new.patient.findage() == 20

def test_sal():
    assert Patient_new.patient.findsal() == 44000

def test_gender():
    assert Patient_new.patient.findgender() == "male"

def test_phone ():
    assert Patient_new.patient.findphone() == "0708888888"

