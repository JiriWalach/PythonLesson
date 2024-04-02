class Person:
    def __init__(self, name, surename, age):
        self.name = name
        self. surename = surename
        self.age = age

    def showMsg(self):
        return(f"Jmenuji se {self.name} {self.surename} a je mi {self.age}")


person1 = Person("Pavel", "Novak", 45)
# volám metodu přes objekt tečka metoda
person1.showMsg()

class Student(Person):
    spec="Computer science"
    def __init__(self,  name, surename, age, spec):
        super().__init__(name, surename, age)
        self.spec = spec

    def showMsg(self):
        return (f"{super().showMsg()} a profese je {self.spec}")



student1 = Student ("Adam", "Veselovský", 23, "HW")
print (student1.spec)
print(student1.showMsg())