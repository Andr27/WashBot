import threading
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from timer import Timer

# Параметры для входа
username = "2022104180@pnu.edu.ru"  # замените на ваш логин
password = "126914ZXC"  # замените на ваш пароль
url = "https://w5.pnu.edu.ru/Account/Login"

# Время выполнения
open_time = "07:29:00"
execute_time = "07:30:00"

# Словари для машин и интервалов
machines = {
    "0": "Машинка №1",
    "1": "Машинка №2",
    "2": "Машинка №3",
    "3": "Машинка №4"
}

intervals = {
    "0": "8:00 - 9:30",
    "1": "9:30 - 11:00",
    "2": "11:00 - 12:30",
    "3": "12:30 - 14:00",
    "4": "14:00 - 15:30",
    "5": "15:30 - 17:00",
    "6": "17:00 - 18:30",
    "7": "18:30 - 20:00",
    "8": "20:00 - 21:30",
    "9": "21:30 - 23:00"
}

# Функция для выполнения записи
def run_bot(first_machine, first_interval, second_machine, second_interval, update_status, enable_button):
    driver = webdriver.Chrome()
    driver.get(url)
    
    try:
        login_field = driver.find_element(By.ID, "loginName")
        password_field = driver.find_element(By.ID, "loginPassword")
        login_button = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div/div/div/form/button")
        
        login_field.send_keys(username)
        password_field.send_keys(password)
        login_button.click()
        
        update_status("Ожидание времени для записи...", "info")
        while datetime.now().strftime("%H:%M:%S") != execute_time:
            pass
        
        machine_1_id = list(machines.keys())[list(machines.values()).index(first_machine)]
        interval_1_id = list(intervals.keys())[list(intervals.values()).index(first_interval)]
        
        machine_2_id = list(machines.keys())[list(machines.values()).index(second_machine)]
        interval_2_id = list(intervals.keys())[list(intervals.values()).index(second_interval)]

        id_slot_1 = "i" + machine_1_id + interval_1_id
        id_slot_2 = "i" + machine_2_id + interval_2_id
        
        time_slot_1 = driver.find_element(By.ID, id_slot_1)
        time_slot_1.click()
        
        time_slot_2 = driver.find_element(By.ID, id_slot_2)
        time_slot_2.click()
        
        update_status("Запись успешно завершена!", "success")
    except Exception as e:
        update_status(f"Ошибка при записи: {e}", "danger")
    finally:
        driver.quit()
        enable_button()

# Функция для запуска бота с использованием таймера
def start_bot(first_machine, first_interval, second_machine, second_interval, update_status, enable_button, root):
    # Запускаем таймер, который будет проверять время с интервалом 1000 мс (1 секунда)
    def check_time():
        current_time = datetime.now().strftime("%H:%M:%S")
        if current_time == open_time:
            update_status("Время записи началось!", "info")
            threading.Thread(target=run_bot, args=(first_machine, first_interval, second_machine, second_interval, update_status, enable_button)).start()

    timer = Timer(root, 1000, check_time)  # Таймер, проверяющий время каждую секунду
    timer.start()  # Запуск таймера
