
from ursina import *
from ursina.prefabs.health_bar import HealthBar
import time, random, os

app = Ursina()

window.title = 'Demon Slayer - 3D Arena (Enhanced)'
window.fps_counter.enabled = True
window.borderless = False
window.fullscreen = False

# Assets path helper
ASSETS = os.path.join(os.path.dirname(__file__), 'assets')

# Ground + terrain details
ground = Entity(model='plane', scale=(80,1,80), texture='grass', texture_scale=(20,20), collider='box')
# scatter some rocks/props using built-in cubes scaled
props = []
for i in range(12):
    e = Entity(model='cube', scale=(random.uniform(1,3), random.uniform(0.5,2), random.uniform(1,3)),
               color=color.rgb(90,90,90), position=(random.uniform(-25,25),0.5, random.uniform(-25,25)))
    props.append(e)

# sky + fog
Sky()
scene.fog_density = 0.01

# Player (replaceable with model files in assets/)
player = Entity(model='cube', scale=(1,2,1), position=(0,1,0), collider='box')
player.speed = 8
player.attack_power = 35
player.max_health = 180
player.health = player.max_health
player._last_attack = -10
player.attack_cooldown = 0.9

# enemy
enemy = Entity(model='cube', color=color.rgb(180,40,40), scale=(1.6,2,1), position=(8,1,0), collider='box')
enemy.speed = 3.0
enemy.attack_power = 22
enemy.max_health = 320
enemy.health = enemy.max_health
enemy._last_attack = -10
enemy.attack_cooldown = 1.2

# Health bars
player_hp = HealthBar(color=color.green, text='PLAYER')
player_hp.bar.value = player.health / player.max_health
player_hp.position = (-0.45, 0.44)
enemy_hp = HealthBar(color=color.red, text='ENEMY')
enemy_hp.bar.value = enemy.health / enemy.max_health
enemy_hp.position = (0.25, 0.44)

# Camera
camera.position = (0, 15, -22)
camera.rotation_x = 18
camera.fov = 60

# Lighting
DirectionalLight(y=2, z=3, shadows=False)
AmbientLight(color=color.rgba(100,100,100,0.5))

# Load sounds (placeholder generated wavs in assets)
try:
    hit_sfx = Audio(os.path.join(ASSETS, 'hit.wav'), autoplay=False, loop=False, volume=0.7)
    swing_sfx = Audio(os.path.join(ASSETS, 'swing.wav'), autoplay=False, loop=False, volume=0.7)
    ambient_sfx = Audio(os.path.join(ASSETS, 'ambient_loop.wav'), autoplay=True, loop=True, volume=0.4)
except Exception as e:
    print('Sound load failed:', e)
    hit_sfx = swing_sfx = ambient_sfx = None

# Particles and VFX
def hit_vfx(pos):
    for i in range(6):
        e = Entity(model='cube', scale=0.1, color=color.orange, position=pos + Vec3(random.uniform(-0.2,0.2), random.uniform(0,0.5), random.uniform(-0.2,0.2)))
        e.animate_scale(0, duration=0.4, curve=curve.linear)
        destroy(e, delay=0.45)

# combat functions
def try_player_attack():
    now = time.time()
    if now - player._last_attack < player.attack_cooldown:
        return False
    player._last_attack = now
    if distance(player.position, enemy.position) < 3.0:
        damage = player.attack_power + random.randint(-5,5)
        enemy.health -= damage
        if swing_sfx: swing_sfx.play()
        if hit_sfx: hit_sfx.play()
        enemy_hp.bar.value = max(enemy.health/enemy.max_health, 0)
        hit_vfx(enemy.position)
        enemy.animate_position(enemy.position + Vec3(0.6,0,0), duration=0.06)
        return True
    return False

def enemy_ai():
    if enemy.health <= 0 or player.health <= 0:
        return
    dir = Vec3(player.x - enemy.x, 0, player.z - enemy.z)
    if dir.length() > 1.6:
        enemy.position += dir.normalized() * enemy.speed * time.dt
    else:
        now = time.time()
        if now - enemy._last_attack >= enemy.attack_cooldown:
            enemy._last_attack = now
            damage = enemy.attack_power + random.randint(-3,3)
            player.health -= damage
            player_hp.bar.value = max(player.health/player.max_health, 0)
            if hit_sfx: hit_sfx.play()
            player.animate_position(player.position - Vec3(0.8,0,0), duration=0.08)

# UI
title = Text('Demon Slayer - 3D Arena (Enhanced)', origin=(0,0.48), scale=1.2, background=True)
instr = Text('WASD: Move   Space/Click: Attack   Q: Dodge   Esc: Quit', position=(-0.45, 0.47), scale=1.0, background=True)

# Particles for ambient (floating embers)
embers = [Entity(model='sphere', scale=0.05, color=color.orange, position=(random.uniform(-20,20), random.uniform(1,6), random.uniform(-20,20))) for _ in range(14)]
for e in embers:
    e.animate_y(e.y + random.uniform(0.6,1.8), duration=random.uniform(3,6), loop=True, curve=curve.sin)

# Win/lose handling
def check_end():
    if enemy.health <= 0:
        Text('YOU WIN', scale=2, color=color.gold, origin=(0,0), duration=4)
        application.pause()
    if player.health <= 0:
        Text('YOU LOSE', scale=2, color=color.gray, origin=(0,0), duration=4)
        application.pause()

def update():
    # movement
    if held_keys['w']:
        player.z -= player.speed * time.dt
    if held_keys['s']:
        player.z += player.speed * time.dt
    if held_keys['a']:
        player.x -= player.speed * time.dt
    if held_keys['d']:
        player.x += player.speed * time.dt
    player.x = clamp(player.x, -34, 34)
    player.z = clamp(player.z, -34, 34)

    # enemy AI
    enemy_ai()
    check_end()

def input(key):
    if key == 'space' or key == 'left mouse down':
        try_player_attack()
    if key == 'q':
        # dodge: short fast move + small invul window
        player.animate_position(player.position + Vec3(random.choice([-2,2]),0, random.choice([-1,1])), duration=0.12)
    if key == 'escape':
        application.quit()

# start ambient music if loaded
if ambient_sfx:
    ambient_sfx.play()

app.run()
