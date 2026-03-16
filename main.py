from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

# --- НАСТРОЙКИ ---
window.fps_counter.enabled = False
window.exit_button.enabled = False

# --- ИГРОК ---
player = FirstPersonController(model='cube', z=-2, origin_y=-.5, speed=5)
player.cursor.visible = True # Оставим курсор для прицеливания во взаимодействия

# --- ФОНАРИК ---
flashlight = Spotlight(parent=camera, world_max_depth=20, color=color.light_gray)
flashlight.enabled = True

# --- ВЗАИМОДЕЙСТВИЕ ---
interact_text = Text(text='', origin=(0,0), y=-0.1, scale=1.5, color=color.yellow)

# --- КЛАСС ДЕКОРА (МЕБЕЛИ) ---
class Furniture(Entity):
    def __init__(self, position=(0,0,0), model='cube', scale=(1,1,1), is_anomaly=False):
        super().__init__(
            model=model,
            position=position,
            scale=scale,
            collider='box',
            color=color.white
        )
        self.is_anomaly = is_anomaly
        self.description = "Обычный предмет"

    def interact(self):
        if self.is_anomaly:
            print("О НЕТ! Это аномалия!")
            self.shake() # Предмет начинает трястись
            self.color = color.red
        else:
            print("Это просто мебель.")

# --- СОЗДАЕМ ДОМ ---
ground = Entity(model='plane', collider='box', scale=64, texture='white_cube', color=color.gray)

# Пример мебели
table = Furniture(position=(2, 0.5, 3), scale=(2, 1, 1), model='cube')
table.description = "Стол"

cursed_chair = Furniture(position=(-2, 0.5, 3), scale=(0.5, 1, 0.5), is_anomaly=True)
cursed_chair.description = "Странный стул"

# --- ИГРОВОЙ ЦИКЛ ---
def update():
    # Проверка взаимодействия (куда смотрит игрок)
    if mouse.hovered_entity and isinstance(mouse.hovered_entity, Furniture):
        interact_text.text = f"Нажмите [E] чтобы изучить: {mouse.hovered_entity.description}"
    else:
        interact_text.text = ""

def input(key):
    # 1. Включение/выключение фонарика
    if key == 'f':
        flashlight.enabled = not flashlight.enabled
        # Звук щелчка можно добавить тут: Audio('click.wav')
    
    # 2. Взаимодействие
    if key == 'e':
        if mouse.hovered_entity and hasattr(mouse.hovered_entity, 'interact'):
            mouse.hovered_entity.interact()

app.run()
