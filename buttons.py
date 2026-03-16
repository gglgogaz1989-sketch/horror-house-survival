from ursina import *

def create_ui(flashlight_func, interact_func):
    # Контейнер для кнопок, чтобы было удобно их позиционировать
    # Кнопка фонарика (снизу справа)
    btn_f = Button(
        text='Light (F)', 
        color=color.rgba(1, 1, 1, 0.2), # Белый, но почти прозрачный
        highlight_color=color.yellow,   # Подсветка при нажатии
        scale=(0.15, 0.1), 
        position=(0.6, -0.4),
        radius=0.1
    )
    
    # Кнопка взаимодействия (чуть правее и выше)
    btn_e = Button(
        text='Action (E)', 
        color=color.rgba(0, 1, 0, 0.2), # Зеленоватый оттенок для действий
        highlight_color=color.green,
        scale=(0.15, 0.1), 
        position=(0.8, -0.3),
        radius=0.1
    )

    # Привязываем функции, которые мы передали из main.py
    btn_f.on_click = flashlight_func
    btn_e.on_click = interact_func

    # Добавим индикатор «прицела» в центр экрана
    crosshair = Entity(
        model='quad', 
        texture='circle', 
        scale=0.01, 
        color=color.white,
        add_to_scene_control=False # Чтобы не мешал физике
    )

    return btn_f, btn_e, crosshair
  
