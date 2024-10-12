import requests

API_URL = 'http://localhost:8081/bot7368730334:AAH9xUG8G_Ro8mvV_fDQxd5ddkwjxHnBoeg/'

def send_message(chat_id, text):
    url = f"{API_URL}sendMessage"
    payload = {
        'chat_id': chat_id,
        'text': text
    }
    response = requests.post(url, json=payload)
    return response.json()

def get_updates(offset=None):
    url = f"{API_URL}getUpdates"
    params = {'offset': offset}
    response = requests.get(url, params=params)
    return response.json()

def main():
    last_update_id = None
    greeted_users = set()  # Множество для отслеживания приветствованных пользователей

    while True:
        updates = get_updates(last_update_id).get("result", [])
        for update in updates:
            message = update.get("message")
            if message:
                chat_id = message["chat"]["id"]
                text = message.get("text", "")
                
                # Приветствие пользователя, если это его первое сообщение
                if chat_id not in greeted_users:
                    send_message(chat_id, "Привет! Добро пожаловать в нашего Telegram-бота!")
                    greeted_users.add(chat_id)  # Добавляем пользователя в множество, чтобы не приветствовать его снова

                # Ответ на сообщения пользователя
                send_message(chat_id, f"Вы сказали: {text}")
                
            last_update_id = update["update_id"] + 1

if __name__ == "__main__":
    main()
