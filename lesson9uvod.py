class Student:
    spec = "devOps"
    def __init__(self, name, age): #konstruktor
        self.name=name #levá část vlastnost, pravá co přiřazujeme
        self.age=age

    def showMsg(self):
        print(f"Moje jméno je {self.name} a můjvěk je {self.age}")
    def sayHi(self, greeting):
        print(f" {greeting} Moje jméno je {self.name} a můjvěk je {self.age}")

    def checkage (self):
        if self.age<18:
            return False
        else:
            return True

student = Student("Adam", 50)
student1=Student("Pavel", 2000)
student.showMsg()

student.sayHi("ach  jo")
student.sayHi("Dobrý den")
# vlastnosti vytahuji přes tečkovou notaci

# print(student1.age)
# #
# student2 = Student("Adam", 1999)
# print(student2.age)
# print(student2.spec)
# student2.name="Petr"
# print(student2.name)