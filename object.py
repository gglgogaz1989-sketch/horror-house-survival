from ursina import *

# Базовый класс для всех вещей в доме
class Furniture(Entity):
    def __init__(self, name="Объект", **kwargs):
        super().__init__(model='cube', collider='box', **kwargs)
        self.name = name
        self.is_anomaly = False
        self.original_color = self.color
        self.original_pos = self.position

# Создаем список всех предметов в доме
def create_house_items():
    items = []
    
    # Расставляем мебель (сюда потом подставишь свои .obj из Blockbench)
    items.append(Furniture(name="Обеденный стол", position=(2, 0.5, 2), scale=(2, 1, 2), color=color.brown))
    items.append(Furniture(name="Старый шкаф", position=(-4, 1.5, 3), scale=(1.5, 3, 0.5), color=color.orange))
    items.append(Furniture(name="Стул", position=(2, 0.5, 0), scale=(0.5, 1, 0.5), color=color.light_gray))
    
    return items
  
