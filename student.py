class Student:
    def __init__(self,name,gender):
        self.name = name
        self.gender = gender

    def pozdraav (self):
        print(f'Ahoj, jsem. {self.name}')

studentPavel=Student("Adam", "muž")
print(studentPavel.name)