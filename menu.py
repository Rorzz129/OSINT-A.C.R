import subprocess
import os
import sys

def pause():
    input("\nPress any keys to continue... ")


def clear():
    os.system("cls" if os.name == "nt" else "clear")

def banner():
    clear()
    print("""
                                                                                    
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣶⣿⣿⣿⣿⣿⣶⡀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠆        A.C.R / MarxWare
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣽⣿⣿⣿⣿⣿⣿⣿⡟⠀               By Rorz X Offset
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⡿⠁
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣾⢻⣿⣿⣿⣿⣿⣿⡀
    ⠀⠀⠀⠀⢀⣠⣤⣴⣾⣿⣿⣿⠛⠀⠙⡿⠟⠋⠀⣿⣿⣦⣄⡀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⡟⠀⣰⣿⣿⣆⠀⢰⣿⣿⣿⣿⣿⣷⣶⣄⡀⠀⠀
    ⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⣰⣿⣷⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⠀
    ⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⢰⣿⣿⣿⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀
    ⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⣿⣿⣿⣿⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇                                                     
""")

def menu():
    print("""
╔═══════════════════════════════════════╗
║             OSINT BASE                ║
╠═════════════════╦═════════════════════╣
║ [1] Sherlock    ║ [5] ID creator      ║
║                 ║                     ║
║ [2] nothing     ║ [6] LookUp          ║
║                 ║                     ║
║ [3] WordlistGen ║ [7] AutoDorker      ║
║                 ║                     ║
║ [4] Image       ║ [0] Leave           ║
╚═════════════════╩═════════════════════╝
(Pls dont leave...)

""")

def main():
    while True:
        banner()
        menu()
        choice=input("\nChoice > ").strip()

        if choice=="1":
            subprocess.run(["python","roz.py"])
        elif choice=="2":
            subprocess.run(["python","Dox.py"])
        elif choice=="3":
            subprocess.run(["python","worldlistgen.py"])
        elif choice=="4":
            subprocess.run(["python","image.py"])
        elif choice=="5":
            subprocess.run(["python","id.py"])
        elif choice=="6":
            subprocess.run(["python","lookup.py"])  
        elif choice=="7":
            subprocess.run(["python","dorker.py"])  
        elif choice=="0":
            sys.exit()
        else:
            print("Choix invalide")

if __name__=="__main__":
    main()