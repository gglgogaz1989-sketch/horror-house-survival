from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import object
import anomaly
import buttons

app = Ursina()

# Игрок
player = FirstPersonController(model='cube', z=-2, origin_y=-.5)
flashlight = Spotlight(parent=camera, world_max_depth=20)

# Мир и предметы
ground = Entity(model='plane', collider='box', scale=64, texture='white_cube', color=color.gray)
all_items = object.create_house_items()

# Связываем кнопки
def on_light(): flashlight.enabled = not flashlight.enabled
def on_interact():
    if mouse.hovered_entity and hasattr(mouse.hovered_entity, 'is_anomaly'):
        anomaly.fix_item(mouse.hovered_entity)

buttons.create_ui(on_light, on_interact)

def update():
    # Шанс появления аномалии
    if random.random() < 0.001:
        target = random.choice(all_items)
        anomaly.apply_anomaly(target)

app.run()
