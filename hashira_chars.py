
from slayers_core import DemonSlayer
import random
class Giyu(DemonSlayer):
    def __init__(self):
        super().__init__("Giyu Tomioka", "Su Nefesi", health=160, attack_power=32)
    def special_move(self, target):
        damage = 55
        target.health -= damage
        print(f"{self.name} Özel Hamle: Sessizlik Tekniği ile {target.name}'a {damage} hasar verdi!")

class Rengoku(DemonSlayer):
    def __init__(self):
        super().__init__("Rengoku Kyojuro", "Alev Nefesi", health=170, attack_power=35)
    def special_move(self, target):
        damage = 60
        target.health -= damage
        print(f"{self.name} Özel Hamle: Alev Ejderhası ile {target.name}'a {damage} hasar verdi!")

class Shinobu(DemonSlayer):
    def __init__(self):
        super().__init__("Shinobu Kocho", "Böcek Nefesi", health=110, attack_power=20)
    def special_move(self, target):
        damage = 40
        target.health -= damage
        print(f"{self.name} Özel Hamle: Zehirli İğne ile {target.name}'a {damage} hasar verdi!")

class Tengen(DemonSlayer):
    def __init__(self):
        super().__init__("Uzui Tengen", "Ses Nefesi", health=180, attack_power=30)
    def special_move(self, target):
        damage = 55
        target.health -= damage
        print(f"{self.name} Özel Hamle: Patlayıcı Performans ile {target.name}'a {damage} hasar verdi!")

class Muichiro(DemonSlayer):
    def __init__(self):
        super().__init__("Muichiro Tokito", "Sis Nefesi", health=140, attack_power=28)
    def special_move(self, target):
        damage = 50
        target.health -= damage
        print(f"{self.name} Özel Hamle: Sonsuz Sis ile {target.name}'a {damage} hasar verdi!")

class Mitsuri(DemonSlayer):
    def __init__(self):
        super().__init__("Mitsuri Kanroji", "Aşk Nefesi", health=150, attack_power=33)
    def special_move(self, target):
        damage = 52
        target.health -= damage
        print(f"{self.name} Özel Hamle: Aşk Kılıcı Dansı ile {target.name}'a {damage} hasar verdi!")

class Sanemi(DemonSlayer):
    def __init__(self):
        super().__init__("Sanemi Shinazugawa", "Rüzgar Nefesi", health=160, attack_power=34)
    def special_move(self, target):
        damage = 58
        target.health -= damage
        print(f"{self.name} Özel Hamle: Fırtına Kesik ile {target.name}'a {damage} hasar verdi!")

class Gyomei(DemonSlayer):
    def __init__(self):
        super().__init__("Gyomei Himejima", "Taş Nefesi", health=200, attack_power=40)
    def special_move(self, target):
        damage = 70
        target.health -= damage
        print(f"{self.name} Özel Hamle: Taş Dağ Ezici ile {target.name}'a {damage} hasar verdi!")

class Obanai(DemonSlayer):
    def __init__(self):
        super().__init__("Obanai Iguro", "Yılan Nefesi", health=145, attack_power=29)
    def special_move(self, target):
        damage = 48
        target.health -= damage
        print(f"{self.name} Özel Hamle: Yılan Dansı ile {target.name}'a {damage} hasar verdi!")
