import time

class Critter:
    def __init__(self, critterName):
        self.foodQuantity = 5
        self.isAlive = True
        self.tiredness = 0
        self.name = critterName
        self.happiness = 20
        self.sleeping = False

    def sleep(self):
        if self.isAlive:
            print(f"{self.name} is sleeping")

            self.sleeping = True
            if self.sleeping == True:
                print("Zzz...")
                time.sleep(5)

            self.foodQuantity -= 1
            self.tiredness -= 3
            if self.tiredness < 0:
                self.tiredness = 0

            if 5 <= self.tiredness <= 7:
                print(f"{self.name}'s energy level is getting low")
            if self.tiredness >= 10:
                self.die()

            if self.foodQuantity == 0:
                self.die()
        else:
            print("Your pet sleeps forever")

    def feed(self):
        self.sleeping = False
        if self.isAlive:
            print(f"{self.name} is eating")
            self.foodQuantity += 3
            if 10 <= self.foodQuantity <= 17:
                print("Your pet is looking a bit tubby")
            if self.foodQuantity <= 0:
                self.die()
            if self.foodQuantity >= 20:
                self.die()
        else:
            print(f"{self.name} is in a happier place")

    def play(self):
        self.sleeping = False
        self.happiness += 2
        self.tiredness += 4
        self.foodQuantity -= 2
        if self.happy >= 40:
            print(f"CONGRATULATIONS {self.name.upper()} LOVES YOU")



    def die(self):
        self.sleeping = False
        self.isAlive = False
        print("Critter died")