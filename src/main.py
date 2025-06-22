from tkinter import Tk
from dotenv import load_dotenv
from src.gui import CommandApp
import os

dotenv_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env')

load_dotenv(dotenv_path)

def main():
    root = Tk()
    app = CommandApp(root)
    root.mainloop()
