first_name = ("John Smith")
age = 20

is_new = False
patient_cred = ("No patient")

if is_new == True:
    patient_cred = (first_name, int(age))

else:
    print("Patient exists")

print(patient_cred)
