import tkinter as tk
from src.commands import run_command

class CommandApp:
    def __init__(self, root):
        self.root = root
        root.title("STE Window")

        self.text = tk.Text(root, height=20, width=60, state='disabled')
        self.text.pack(padx=10, pady=10)

        self.entry = tk.Entry(root, width=60)
        self.entry.pack(padx=10, pady=(0, 10))
        self.entry.bind("<Return>", self.execute_command)

    def execute_command(self, event=None):
        cmd = self.entry.get()
        result = run_command(cmd)
        self.entry.delete(0, tk.END)

        if result == "CLEAR":
            self.text.config(state='normal')
            self.text.delete(1.0, tk.END)
            self.text.config(state='disabled')
            return
        elif result == "EXIT":
            self.root.quit()
            return

        self.text.config(state='normal')
        self.text.insert(tk.END, f"> {cmd}\n{result}\n")
        self.text.config(state='disabled')
        self.text.see(tk.END)
