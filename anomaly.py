from ursina import *
import random

def apply_anomaly(item):
    if not item.is_anomaly:
        item.is_anomaly = True
        # Типы аномалий
        type = random.choice(['color', 'move', 'scale'])
        
        if type == 'color':
            item.color = color.red
        elif type == 'move':
            item.y += 0.5 # Левитация
        elif type == 'scale':
            item.scale *= 1.2 # Предмет раздуло
            
        print(f"Аномалия: {item.name} изменился!")

def fix_item(item):
    item.is_anomaly = False
    item.color = item.original_color
    item.position = item.original_pos
    item.scale = (1, 1, 1) # Или вернуть исходный масштаб
    print(f"{item.name} теперь в порядке.")
  
