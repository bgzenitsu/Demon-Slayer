
from slayers_core import DemonSlayer
import random
class Tanjiro(DemonSlayer):
    def __init__(self):
        super().__init__("Tanjiro", "Su Nefesi", health=120, attack_power=25)

    def special_move(self, target):
        damage = 40
        target.health -= damage
        print(f"{self.name} Özel Hamle: Su Ejderhası ile {target.name}'a {damage} hasar verdi!")

from slayers_core import DemonSlayer
import random
class Zenitsu(DemonSlayer):
    def __init__(self):
        super().__init__("Zenitsu", "Yıldırım Nefesi", health=100, attack_power=30)

    def special_move(self, target):
        damage = 50
        target.health -= damage
        print(f"{self.name} Özel Hamle: Tanrı'nın Hızı ile {target.name}'a {damage} hasar verdi!")

from slayers_core import DemonSlayer
import random
class Inosuke(DemonSlayer):
    def __init__(self):
        super().__init__("Inosuke", "Canavar Nefesi", health=130, attack_power=22)

    def special_move(self, target):
        damage = 35
        target.health -= damage
        print(f"{self.name} Özel Hamle: Çifte Kılıç Çılgınlığı ile {target.name}'a {damage} hasar verdi!")

from slayers_core import DemonSlayer
import random
class Nezuko(DemonSlayer):
    def __init__(self):
        super().__init__("Nezuko", "İblis Gücü", health=150, attack_power=28)

    def special_move(self, target):
        damage = 45
        target.health -= damage
        print(f"{self.name} Özel Hamle: İblis Pençesi ile {target.name}'a {damage} hasar verdi!")
