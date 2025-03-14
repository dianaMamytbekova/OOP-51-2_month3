import datetime
import flet as ft

HISTORY_FILE = "greetings_history.txt"

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
    elif 12 <= hour < 18:
        greeting = f"Добрый день, {name}!"
    elif 18 <= hour < 24:
        greeting = f"Добрый вечер, {name}!"
    else:
        greeting = f"Доброй ночи, {name}!"
    return greeting

def main(page: ft.Page):
    page.title = "Приветствие с историей"
    greeting_history = load_greeting_history()

    def button_click(e):
        name = name_field.value.strip()
        if not name:
            text.value = "Введите имя!"
        else:
            greeting = get_greeting(name)
            text.value = greeting
            history_entry = save_greeting_to_file(greeting)
            history.value += history_entry
        page.update()

    name_field = ft.TextField(label="Введите имя")
    text = ft.Text()
    button = ft.ElevatedButton("Поздороваться", on_click=button_click)
    history = ft.Text(value="История приветствий:\n" + "".join(greeting_history), selectable=True)

    page.add(name_field, button, text, history)

ft.app(target=main)

