import os
import sys


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def pause(message="\nAppuie sur Entrée pour continuer..."):
    input(message)


def get_python():
    return sys.executable
