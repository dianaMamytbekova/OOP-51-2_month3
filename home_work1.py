import datetime
import random
import flet as ft

HISTORY_FILE = "greetings_history.txt"

RANDOM_NAMES = ["Алексей", "Мария", "Иван", "Ольга", "Дмитрий", "Елена"]

def load_greeting_history():
    try:
        with open(HISTORY_FILE, "r", encoding="utf-8") as file:
            return file.readlines()
    except FileNotFoundError:
        return []

def save_greeting_to_file(greeting):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = f"{timestamp} - {greeting}\n"
    with open(HISTORY_FILE, "a", encoding="utf-8") as file:
        file.write(entry)
    return entry  

def get_greeting(name):
    hour = datetime.datetime.now().hour
    if 6 <= hour < 12:
        greeting = f"Доброе утро, {name}!"
        color = "yellow"
    elif 12 <= hour < 18:
        greeting = f"Добрый день, {name}!"
        color = "orange"
    elif 18 <= hour < 24:
        greeting = f"Добрый вечер, {name}!"
        color = "red"
    else:
        greeting = f"Доброй ночи, {name}!"
        color = "blue"
    return greeting, color

def main(page: ft.Page):
    page.title = "Приветствие с историей"
    greeting_history = load_greeting_history()

    def button_click(e):
        name = name_field.value.strip()
        if not name:
            text.value = "Введите имя!"
            text.color = "black"
        else:
            greeting, color = get_greeting(name)
            text.value = greeting
            text.color = color
            history_entry = save_greeting_to_file(greeting)
            history.value += history_entry
            name_field.value = ""
        page.update()
    
    def random_name(e):
        name_field.value = random.choice(RANDOM_NAMES)
        page.update()
    
    def toggle_history(e):
        history.visible = not history.visible
        page.update()
    
    name_field = ft.TextField(label="Введите имя", on_submit=button_click)
    text = ft.Text()
    button = ft.ElevatedButton("Поздороваться", on_click=button_click)
    random_button = ft.ElevatedButton("Случайное имя", on_click=random_name)
    toggle_button = ft.ElevatedButton("Скрыть/Показать историю", on_click=toggle_history)
    history = ft.Text(value="История приветствий:\n" + "".join(greeting_history), selectable=True, visible=True)

    page.add(name_field, button, random_button, toggle_button, text, history)

ft.app(target=main)
