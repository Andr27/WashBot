import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox
import threading

# Создаем класс для интерфейса
class AppGUI:
    def __init__(self, master, start_bot_callback):
        self.master = master
        self.start_bot_callback = start_bot_callback
        
        # Настройка окна
        master.title("Система записи на стирку")
        master.geometry("500x550")
        master.resizable(False, False)  # Фиксируем размер окна

        # Заголовок
        self.header = ttk.Label(master, text="Система записи на стирку", font=("Helvetica", 20, "bold"), bootstyle="primary")
        self.header.pack(pady=15)

        # Описание
        self.description = ttk.Label(master, text="Пожалуйста, выберите параметры для записи ниже:", font=("Helvetica", 12))
        self.description.pack(pady=5)

        # Фрейм для выбора машинок и интервалов
        self.frame = ttk.Frame(master, padding=20, bootstyle="secondary")
        self.frame.pack(pady=10, fill=X)

        # Элементы для первой машины
        ttk.Label(self.frame, text="Первая стиральная машина:", font=("Helvetica", 10, "bold")).grid(row=0, column=0, sticky="w", pady=10)
        self.first_machine = ttk.Combobox(self.frame, values=["Машинка №1", "Машинка №2", "Машинка №3", "Машинка №4"], bootstyle="info", state="readonly", width=20)
        self.first_machine.set("Машинка №1")
        self.first_machine.grid(row=0, column=1, padx=10)

        ttk.Label(self.frame, text="Интервал для первой машины:", font=("Helvetica", 10, "bold")).grid(row=1, column=0, sticky="w", pady=10)
        self.first_interval = ttk.Combobox(self.frame, values=["8:00 - 9:30", "9:30 - 11:00", "11:00 - 12:30", "12:30 - 14:00", "14:00 - 15:30", "15:30 - 17:00", "17:00 - 18:30", "18:30 - 20:00", "20:00 - 21:30", "21:30 - 23:00"], bootstyle="info", state="readonly", width=20)
        self.first_interval.set("8:00 - 9:30")
        self.first_interval.grid(row=1, column=1, padx=10)

        ttk.Separator(self.frame, bootstyle="info").grid(row=2, columnspan=2, pady=20, sticky="ew")

        # Элементы для второй машины
        ttk.Label(self.frame, text="Вторая стиральная машина:", font=("Helvetica", 10, "bold")).grid(row=3, column=0, sticky="w", pady=10)
        self.second_machine = ttk.Combobox(self.frame, values=["Машинка №1", "Машинка №2", "Машинка №3", "Машинка №4"], bootstyle="info", state="readonly", width=20)
        self.second_machine.set("Машинка №2")
        self.second_machine.grid(row=3, column=1, padx=10)

        ttk.Label(self.frame, text="Интервал для второй машины:", font=("Helvetica", 10, "bold")).grid(row=4, column=0, sticky="w", pady=10)
        self.second_interval = ttk.Combobox(self.frame, values=["8:00 - 9:30", "9:30 - 11:00", "11:00 - 12:30", "12:30 - 14:00", "14:00 - 15:30", "15:30 - 17:00", "17:00 - 18:30", "18:30 - 20:00", "20:00 - 21:30", "21:30 - 23:00"], bootstyle="info", state="readonly", width=20)
        self.second_interval.set("8:00 - 9:30")
        self.second_interval.grid(row=4, column=1, padx=10)

        # Кнопка для запуска бота
        self.start_button = ttk.Button(master, text="Запустить запись", bootstyle="success", command=self.start_bot)
        self.start_button.pack(pady=20)

        # Статус выполнения
        self.status_label = ttk.Label(master, text="Ожидание начала работы...", font=("Helvetica", 12), bootstyle="info")
        self.status_label.pack(pady=20)

    def start_bot(self):
        self.start_button["state"] = "disabled"  # Отключаем кнопку
        self.start_bot_callback(self.first_machine.get(), self.first_interval.get(), self.second_machine.get(), self.second_interval.get(), self.update_status, self.enable_button, self.master)

    def update_status(self, message, message_type):
        # Обновляем текст статуса в интерфейсе
        self.status_label.config(text=message, bootstyle=message_type)

    def enable_button(self):
        self.start_button["state"] = "normal"  # Включаем кнопку обратно
