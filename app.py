first_name = input("What is your name? ")
age = input("What is your age? ")
is_new = False
if is_new == True:
 patient_cred = (first_name, int(age))
else:
 print("patient exists")
is_new = False
print(patient_cred)
assert patient_cred == ("John Smith", 20)
