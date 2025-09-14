
from ursina import *
from ursina.prefabs.health_bar import HealthBar
import time, random, os

app = Ursina()
ASSETS = os.path.join(os.path.dirname(__file__), 'assets')
MODELS = os.path.join(ASSETS, 'models')

# --- Window ---
window.title = 'Demon Slayer - Advanced 3D Arena'
window.fps_counter.enabled = True
window.borderless = False
window.fullscreen = False

# --- Sounds ---
def load_sfx(name):
    try:
        return Audio(os.path.join(ASSETS, name), autoplay=False, loop=False, volume=0.7)
    except: return None
swing_sfx = load_sfx('swing.wav')
hit_sfx = load_sfx('hit.wav')
block_sfx = load_sfx('block.wav')
special_sfx = load_sfx('special.wav')
ambient_sfx = load_sfx('ambient_loop.wav')
menu_music = load_sfx('menu_music.wav')
if ambient_sfx: ambient_sfx.play()
if menu_music: menu_music.play()

# --- Environment ---
ground = Entity(model='plane', scale=(80,1,80), texture='grass', texture_scale=(20,20), collider='box')
Sky()
scene.fog_density = 0.01
props = [Entity(model='cube', scale=(random.uniform(1,3),random.uniform(0.5,2),random.uniform(1,3)),
               color=color.rgb(90,90,90), position=(random.uniform(-25,25),0.5,random.uniform(-25,25))) for _ in range(12)]
Directionallight(y=2,z=3)
AmbientLight(color=color.rgba(100,100,100,0.5))

# --- Player / Enemy ---
player = Entity(model=os.path.join(MODELS,'player.obj'), scale=1, position=(0,1,0), collider='box', color=color.cyan)
player.speed = 8
player.attack_power = 35
player.max_health = 200
player.health = player.max_health
player.stamina = 100
player.max_stamina = 100
player.combo_count = 0
player._last_attack = -10
player.attack_cooldown = 0.8

enemy = Entity(model=os.path.join(MODELS,'enemy.obj'), scale=1, position=(8,1,0), collider='box', color=color.red)
enemy.speed = 3.0
enemy.attack_power = 25
enemy.max_health = 320
enemy.health = enemy.max_health
enemy._last_attack = -10
enemy.attack_cooldown = 1.2

player_hp = HealthBar(color=color.green, text='PLAYER'); player_hp.bar.value = player.health/player.max_health; player_hp.position=(-0.45,0.44)
enemy_hp = HealthBar(color=color.red, text='ENEMY'); enemy_hp.bar.value = enemy.health/enemy.max_health; enemy_hp.position=(0.25,0.44)

# --- Camera ---
camera.position=(0,15,-22); camera.rotation_x=18; camera.fov=60

# --- HUD ---
title = Text('Demon Slayer - Advanced Arena', origin=(0,0.48), scale=1.2, background=True)
instr = Text('WASD: Move  Space: Attack  Shift: Block  Q: Dodge', position=(-0.45,0.47), scale=1.0, background=True)
stamina_text = Text(f'Stamina: {player.stamina}', position=(-0.45,0.41), scale=1.0, background=True)

# --- Functions ---
def hit_vfx(pos):
    for i in range(6):
        e = Entity(model='cube', scale=0.1, color=color.orange, position=pos + Vec3(random.uniform(-0.2,0.2),random.uniform(0,0.5),random.uniform(-0.2,0.2)))
        e.animate_scale(0,duration=0.4); destroy(e,delay=0.45)

def try_player_attack():
    now=time.time()
    if now-player._last_attack<player.attack_cooldown: return False
    if player.stamina<10: return False
    player._last_attack=now; player.stamina-=10
    if distance(player.position,enemy.position)<3.0:
        damage=player.attack_power + random.randint(-5,5)
        enemy.health-=damage
        enemy_hp.bar.value=max(enemy.health/enemy.max_health,0)
        if swing_sfx: swing_sfx.play()
        if hit_sfx: hit_sfx.play()
        hit_vfx(enemy.position)
        player.combo_count+=1
        if player.combo_count%3==0 and special_sfx: special_sfx.play()
        enemy.animate_position(enemy.position + Vec3(0.6,0,0), duration=0.06)
        return True
    return False

def enemy_ai():
    if enemy.health<=0 or player.health<=0: return
    dir=Vec3(player.x-enemy.x,0,player.z-enemy.z)
    if dir.length()>1.6:
        enemy.position+=dir.normalized()*enemy.speed*time.dt
    else:
        now=time.time()
        if now-enemy._last_attack>=enemy.attack_cooldown:
            enemy._last_attack=now
            damage=enemy.attack_power + random.randint(-3,3)
            if held_keys['shift']: damage//=2; player.stamina+=5; if block_sfx: block_sfx.play()
            player.health-=damage; player_hp.bar.value=max(player.health/player.max_health,0)

def check_end():
    if enemy.health<=0:
        Text('YOU WIN',scale=2,color=color.gold,origin=(0,0),duration=4); application.pause()
    if player.health<=0:
        Text('YOU LOSE',scale=2,color=color.gray,origin=(0,0),duration=4); application.pause()

# --- Update Loop ---
def update():
    # movement
    if held_keys['w']: player.z-=player.speed*time.dt
    if held_keys['s']: player.z+=player.speed*time.dt
    if held_keys['a']: player.x-=player.speed*time.dt
    if held_keys['d']: player.x+=player.speed*time.dt
    player.x=clamp(player.x,-34,34); player.z=clamp(player.z,-34,34)
    # regenerate stamina
    player.stamina=min(player.stamina+10*time.dt,player.max_stamina)
    stamina_text.text=f'Stamina: {int(player.stamina)}'
    # AI & check end
    enemy_ai(); check_end()

def input(key):
    if key=='space' or key=='left mouse down': try_player_attack()
    if key=='q': player.animate_position(player.position+Vec3(random.choice([-2,2]),0,random.choice([-1,1])),duration=0.12)
    if key=='escape': application.quit()

# Ambient embers
embers=[Entity(model='sphere',scale=0.05,color=color.orange,position=(random.uniform(-20,20),random.uniform(1,6),random.uniform(-20,20))) for _ in range(14)]
for e in embers: e.animate_y(e.y+random.uniform(0.6,1.8),duration=random.uniform(3,6),loop=True,curve=curve.sin)

app.run()
