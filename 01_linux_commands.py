# Experiment 1: Basic Linux-command practice using Python
# This version also runs on Windows in VS Code.

import os
from pathlib import Path
from datetime import datetime
import getpass

while True:
    print("\n1. pwd   2. ls   3. mkdir   4. touch   5. cat")
    print("6. date  7. whoami  8. exit")
    ch = input("Choose: ")

    if ch == "1":
        print(Path.cwd())
    elif ch == "2":
        for item in Path.cwd().iterdir():
            print(item.name)
    elif ch == "3":
        name = input("Folder name: ")
        Path(name).mkdir(exist_ok=True)
        print("Folder created.")
    elif ch == "4":
        name = input("File name: ")
        Path(name).touch(exist_ok=True)
        print("File created.")
    elif ch == "5":
        name = input("File name: ")
        p = Path(name)
        if p.exists():
            print(p.read_text())
        else:
            print("File not found.")
    elif ch == "6":
        print(datetime.now())
    elif ch == "7":
        print(getpass.getuser())
    elif ch == "8":
        break
    else:
        print("Invalid choice.")
