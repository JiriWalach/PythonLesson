class Auto:
    def __init__(self,rychlost,vaha):
        self.rychlost = rychlost
        self.vaha = vaha

    def checkSpeedLimitObec (self):
        if self.rychlost > 50:
            return "Jedeš moc rychle, dostaneš pokutu"
        else:
            return "Tvá rychlost je v pořádku"
    def checkSpeedLimitDalnice (self):
        if self.rychlost < 80:
            print("Jedeš pomalu zrychli")
        elif self.rychlost > 130:
            print("Jedeš moc rychle, zpomal, dostaneš pokutu!")
        else:
            print("Tvá rychlost je v pořádku")
class Kamion(Auto):
    def __init__(self,rychlost,vaha,zatizeni):
        super().__init__(rychlost,vaha)
        self.zatizeni=zatizeni
    def checkSpeedLimitDalnice (self):
        if self.rychlost < 80:
            print("Jedeš pomalu zrychli")
        elif self.rychlost > 110:
            print("Jedeš moc rychle, zpomal, dostaneš pokutu!")
        else:
            print("Tvá rychlost je v pořádku")
kamion1 = Kamion(95,8000,5000)
auto1 = Auto(132,3200)

kamion1.checkSpeedLimitDalnice()
auto1.checkSpeedLimitDalnice()

print(auto1.checkSpeedLimitObec())
print(kamion1.checkSpeedLimitObec())
