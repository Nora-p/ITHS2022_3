
firstname = ("John")
lastname = ("Smit")
age = 20
tel = "0708888888"
sal = 44000
gender = ("male")
is_new = False


class patient:

    def findname (firstname, lastname):
        return firstname + lastname

    def findphone (tel):
        return tel

    def findsal (sal):
        return sal

    def findage (age):
        return age

    def findgender (gender):
        return gender

print(firstname, lastname, age, gender, sal, tel)
