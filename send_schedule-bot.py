import os
import requests
from datetime import datetime, timedelta

TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

# Расписание для каждого дня недели (0 = понедельник, 6 = воскресенье)
SCHEDULE = {
    0: "Расписание на завтра (понедельник):\n09:00 - 10:35 — Психология (361 лекции)\n10:50 - 12:25 — Квантовая теория (362 лекции)\n13:10 - 14:45 — Основы радиоэлектроники (430 лекции)\n15:00 - 16:35 — Основы радиоэлектроники (430 практика)",
    1: "Расписание на завтра (вторник):\n16:50 - 18:25 — Механика сплошных сред (608 практика)",
    2: "Расписание на завтра (среда):\n09:00-10:35  — Основы радиоэлектроники (172)\n10:50 - 12:25 — радиоэлектроники (172)",
    3: "Расписание на завтра (четверг):\n13:10 - 14:45 — Прикладные пакеты и подготовка публикаций (287)\n11:00 — Гравитация (510)",
    4: "Расписание на завтра (пятница):\n09:00 - 10:35 — Механика сплошных сред (402 лекции)\n13:10 - 14:45 — Квантовая теория (362 практика)",
    5: "Расписание на завтра (суббота):\n09:00 — Дополнительные занятия",
    6: "Завтра воскресенье — выходной, занятий нет!",
}

def get_schedule_text() -> str:
    tomorrow = datetime.now() + timedelta(days=1)
    weekday = tomorrow.weekday()
    return SCHEDULE[weekday]

def send_message():
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": get_schedule_text()}
    response = requests.post(url, data=payload)
    response.raise_for_status()
    print("Отправлено:", response.json())

if __name__ == "__main__":
    send_message()
