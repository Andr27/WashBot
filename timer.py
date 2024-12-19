import tkinter as tk
from datetime import datetime

class Timer:
    def __init__(self, root, interval, callback):
        """
        Инициализация таймера, который будет запускать callback через заданный интервал.
        :param root: основное окно Tkinter.
        :param interval: интервал в миллисекундах.
        :param callback: функция, которая будет вызываться.
        """
        self.root = root
        self.interval = interval
        self.callback = callback
        self.running = False

    def start(self):
        """Запуск таймера."""
        if not self.running:
            self.running = True
            self._schedule()

    def stop(self):
        """Остановка таймера."""
        self.running = False

    def _schedule(self):
        """Запланировать выполнение callback через заданный интервал."""
        if self.running:
            self.callback()  # Вызываем функцию обратного вызова
            self.root.after(self.interval, self._schedule)  # Повторяем таймер
