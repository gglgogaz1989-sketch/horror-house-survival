from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

# --- ОКРУЖЕНИЕ ---
# Пол
ground = Entity(model='plane', collider='box', scale=64, texture='white_cube', texture_scale=(64,64), color=color.gray)

# Простая комната (стены)
wall_1 = Entity(model='cube', collider='box', position=(0, 2.5, 5), scale=(10, 5, 0.1), color=color.dark_gray)
wall_2 = Entity(model='cube', collider='box', position=(0, 2.5, -5), scale=(10, 5, 0.1), color=color.dark_gray)
wall_3 = Entity(model='cube', collider='box', position=(5, 2.5, 0), scale=(0.1, 5, 10), color=color.dark_gray)
wall_4 = Entity(model='cube', collider='box', position=(-5, 2.5, 0), scale=(0.1, 5, 10), color=color.dark_gray)

# --- ИГРОК И ФОНАРИК ---
player = FirstPersonController(model='cube', z=-2, origin_y=-.5, speed=5)
player.cursor.visible = False

# Фонарик (привязан к камере игрока)
flashlight = Spotlight(parent=camera, world_max_depth=15, color=color.light_gray)
flashlight.enabled = True

# --- СИСТЕМА ВРЕМЕНИ ---
time_text = Text(text='00:00', position=(0.7, 0.45), scale=2, color=color.yellow)
game_minutes = 0
game_hours = 0

def update():
    global game_minutes, game_hours
    
    # Каждые 2 секунды реального времени прибавляем 1 игровую минуту
    game_minutes += time.dt / 2
    
    if game_minutes >= 60:
        game_minutes = 0
        game_hours += 1
        
    # Отображение времени
    time_text.text = f"{int(game_hours):02d}:{int(game_minutes):02d}"
    
    # Условие победы
    if game_hours >= 6:
        time_text.text = "6:00 - ТЫ ВЫЖИЛ!"
        time_text.color = color.green
        application.pause()

# Включение/выключение фонарика на клавишу 'f'
def input(key):
    if key == 'f':
        flashlight.enabled = not flashlight.enabled

app.run()

