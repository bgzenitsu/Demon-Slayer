
from slayers_core import DemonSlayer
from slayer_chars import Tanjiro, Zenitsu, Inosuke, Nezuko
from hashira_chars import Giyu, Rengoku, Shinobu, Tengen, Muichiro, Mitsuri, Sanemi, Gyomei, Obanai
from demons import Muzan, Akaza, Doma, Kokushibo, Gyutaro, Daki
import random

slayer_options = [
    Tanjiro(), Zenitsu(), Inosuke(), Nezuko(),
    Giyu(), Rengoku(), Shinobu(), Tengen(),
    Muichiro(), Mitsuri(), Sanemi(), Gyomei(), Obanai()
]
demon_options = [Muzan(), Akaza(), Doma(), Kokushibo(), Gyutaro(), Daki()]

print('Demon Slayer - Team Fight (Text)')
print('Choose 3 slayers for your team:')
for i, s in enumerate(slayer_options, start=1):
    print(f"{i}. {s.name} ({s.breathing_style})")

team = []
while len(team) < 3:
    idx = int(input(f"Choose #{len(team)+1}: ")) - 1
    if 0 <= idx < len(slayer_options):
        chosen = slayer_options[idx]
        if chosen in team:
            print('Already chosen')
        else:
            team.append(chosen)
            print(f'Added {chosen.name}')
    else:
        print('Invalid')

print('Choose demon:')
for i, d in enumerate(demon_options, start=1):
    print(f"{i}. {d.name}")
choice = int(input('demon: ')) - 1
enemy = demon_options[choice] if 0 <= choice < len(demon_options) else random.choice(demon_options)
print(f'Enemy: {enemy.name} (HP {enemy.health})')

while enemy.is_alive() and any(s.is_alive() for s in team):
    for i, s in enumerate(team, start=1):
        if s.is_alive():
            print(f"{i}. {s.name} HP:{s.health}")
    choice = int(input('Which slayer attacks? ')) - 1
    if not (0 <= choice < len(team) and team[choice].is_alive()):
        print('invalid')
        continue
    fighter = team[choice]
    print('1 normal, 2 special')
    move = input('> ')
    if move == '1':
        fighter.attack(enemy)
    else:
        fighter.special_move(enemy)
    if enemy.is_alive():
        target = random.choice([s for s in team if s.is_alive()])
        if random.random() < 0.4:
            enemy.special_move(target)
        else:
            enemy.attack(target)
print('Battle finished')
