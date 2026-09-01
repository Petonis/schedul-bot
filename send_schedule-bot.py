import os
import requests

TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

def get_schedule_text() -> str:
return "Расписание на завтра:\n09:00 — Математика\n11:00 — Физика"

def send_message():
url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
payload = {"chat_id": CHAT_ID, "text": get_schedule_text()}
response = requests.post(url, data=payload)
response.raise_for_status()
print("Отправлено:", response.json())

if __name__ == "__main__":
send_message()
