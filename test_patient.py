import Patient_new

def test_name():
    assert Patient_new.patient.findname("John","Smith") == "John Smith"

def test_age():
    assert Patient_new.patient.findage() == 21