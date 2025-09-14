
import random
class Demon:
    def __init__(self, name, health=200, attack_power=25):
        self.name = name
        self.health = health
        self.attack_power = attack_power
    def attack(self, target):
        damage = random.randint(self.attack_power - 5, self.attack_power + 5)
        target.health -= damage
        print(f"{self.name}, {target.name}'a {damage} hasar verdi!")
    def is_alive(self):
        return self.health > 0

class Muzan(Demon):
    def __init__(self):
        super().__init__("Muzan Kibutsuji", health=500, attack_power=45)
    def special_move(self, target):
        damage = 80
        target.health -= damage
        print(f"{self.name} Özel Hamle: Hücre Yok Etme ile {target.name}'a {damage} hasar verdi!")

class Akaza(Demon):
    def __init__(self):
        super().__init__("Akaza", health=300, attack_power=35)
    def special_move(self, target):
        damage = 60
        target.health -= damage
        print(f"{self.name} Özel Hamle: Yokedici Ölüm Sanatı ile {target.name}'a {damage} hasar verdi!")

class Doma(Demon):
    def __init__(self):
        super().__init__("Doma", health=350, attack_power=33)
    def special_move(self, target):
        damage = 65
        target.health -= damage
        print(f"{self.name} Özel Hamle: Buz Lotus'u ile {target.name}'a {damage} hasar verdi!")

class Kokushibo(Demon):
    def __init__(self):
        super().__init__("Kokushibo", health=400, attack_power=40)
    def special_move(self, target):
        damage = 75
        target.health -= damage
        print(f"{self.name} Özel Hamle: Ay Nefesi Tekniği ile {target.name}'a {damage} hasar verdi!")

class Gyutaro(Demon):
    def __init__(self):
        super().__init__("Gyutaro", health=220, attack_power=28)
    def special_move(self, target):
        damage = 50
        target.health -= damage
        print(f"{self.name} Özel Hamle: Kanlı Tırpan ile {target.name}'a {damage} hasar verdi!")

class Daki(Demon):
    def __init__(self):
        super().__init__("Daki", health=180, attack_power=26)
    def special_move(self, target):
        damage = 45
        target.health -= damage
        print(f"{self.name} Özel Hamle: Obi Kuşağı Kesişi ile {target.name}'a {damage} hasar verdi!")
