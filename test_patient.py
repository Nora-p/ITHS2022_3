import Patient_new


def test_name():
    fullname = input("What is the patient's firstname and lastname? ")
    assert Patient_new.patient.findname(fullname) == "John Smith"


def test_age():
    age = input("What is the patient's age? ")
    assert Patient_new.patient.findage(age) == "20"


def test_sal():
    sal = input("What is the patient's salary? ")
    assert Patient_new.patient.findsal(sal) == "44000"


def test_gender():
    gender = input("What is the patient's gender? ")
    assert Patient_new.patient.findgender(gender) == "male"


def test_phone():
    tel = input("What is the patient's phone number? ")
    assert Patient_new.patient.findphone(tel) == "0708112233"
