import subprocess

def build():
    subprocess.run([
        "pyinstaller",
        "--noconfirm",
        "--onefile",
        "--windowed",
        "app.py"
    ])

if __name__ == "__main__":
    build()
