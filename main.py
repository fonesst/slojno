import os
import subprocess

REPO_URL = "https://github.com/YOUR_USERNAME/telegram-bot.git"
REPO_DIR = "telegram-bot"

def clone_and_install():
    # Клонирование репозитория
    if not os.path.exists(REPO_DIR):
        print("Клонирование репозитория...")
        subprocess.run(["git", "clone", REPO_URL])
    else:
        print("Репозиторий уже существует. Выполняется обновление...")
        os.chdir(REPO_DIR)
        subprocess.run(["git", "pull"])
        os.chdir("..")

    # Установка зависимостей
    print("Установка зависимостей...")
    subprocess.run(["pip", "install", "-r", f"{REPO_DIR}/requirements.txt"])

def run_bot():
    # Запуск бота
    print("Запуск бота...")
    subprocess.run(["python3", f"{REPO_DIR}/bot.py"])

if __name__ == "__main__":
    clone_and_install()
    run_bot()
