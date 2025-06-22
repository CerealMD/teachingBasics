from datetime import datetime
import os

def run_command(cmd):
    api_key = os.getenv("API_KEY")
    password = os.getenv("PASSWORD")
    print(password)
    print(api_key)
    cmd = cmd.strip().lower()
    if cmd == "hello":
        return password
    elif cmd == "time":
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    elif cmd == "clear":
        return "CLEAR"
    elif cmd == "exit":
        return "EXIT"
    return f"Unknown command: {cmd}"
