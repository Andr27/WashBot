import tkinter as tk
from gui import AppGUI
from bot import start_bot

if __name__ == "__main__":
    root = tk.Tk()
    app = AppGUI(root, start_bot)
    root.mainloop()
