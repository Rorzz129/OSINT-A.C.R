import os
import json
import sys
import subprocess

from utils import clear, pause, get_python

PYTHON = get_python()


def ask(prompt, obligatoire=False):
    while True:
        reponse = input(f"{prompt} : ").strip()
        if obligatoire and not reponse:
            print("Ce champ est obligatoire.")
            continue
        return reponse


def list_profiles():
    dossier = "add"
    if not os.path.isdir(dossier):
        return []
    fichiers = os.listdir(dossier)
    return [f.replace(".json", "") for f in fichiers if f.endswith(".json")]


def safe_path(filename):
    safe = filename.strip().replace(" ", "_")
    safe = safe.replace("..", "").replace("/", "").replace("\\", "")
    return f"add/{safe}.json"


def add():
    champs = {
        "profil_name": ask("[+] profil_name"),
        "nom": ask("[+] Nom"),
        "prenom": ask("[+] Prenom"),
        "age": ask("[+] Age"),
        "mail": ask("[+] Mail"),
        "num": ask("[+] Phone Number"),
        "birthday": ask("[+] Birthday"),
        "ville_de_naissance": ask("[+] Ville de naissance"),
        "bio": ask("[+] Bio"),
        "pseudo": ask("[+] Pseudo"),
        "adresse": ask("[+] Adresse"),
        "compte": ask("[+] Compte"),
        "sexe": ask("[+] Sexe"),
        "nationalite": ask("[+] Nationalité"),
        "discord": ask("[+] Discord"),
        "instagram": ask("[+] Instagram"),
        "telegram": ask("[+] Telegram"),
        "job": ask("[+] Travail"),
        "etudes": ask("[+] Études"),
        "hobbies": ask("[+] Hobbies"),
        "mot_de_passe": ask("[+] Mot de passe"),
        "email_backup": ask("[+] Email de secours"),
    }

    print("profil create successfully")

    os.makedirs("add", exist_ok=True)
    path = safe_path(champs["profil_name"])

    with open(path, "w", encoding="utf-8") as file:
        json.dump(champs, file, indent=4, ensure_ascii=False)

    print(f"\nProfil sauvegardé dans {path}")
    pause()


def show():
    clear()
    profils = list_profiles()

    if not profils:
        print("Aucun profil trouvé.")
        pause()
        return

    print("\n===== PROFILS DISPONIBLES =====\n")
    for i, p in enumerate(profils, 1):
        print(f"[{i}] {p}")

    try:
        choix = int(input("\nChoisis un profil : ").strip())
    except ValueError:
        print("Choix invalide.")
        pause()
        return

    if choix < 1 or choix > len(profils):
        print("Profil inexistant.")
        pause()
        return

    profil_name = profils[choix - 1]
    path = f"add/{profil_name}.json"

    with open(path, "r", encoding="utf-8") as file:
        data = json.load(file)

    clear()
    print("\n===== PROFIL =====\n")
    for key, value in data.items():
        print(f"{key:<20} : {value}")
    print("\n====================")
    pause()


def delete_profile():
    clear()
    profils = list_profiles()

    if not profils:
        print("Aucun profil à supprimer.")
        pause()
        return

    print("\n===== PROFILS =====\n")
    for i, p in enumerate(profils, 1):
        print(f"[{i}] {p}")

    try:
        choix = int(input("\nChoisis le profil à supprimer : ").strip())
    except ValueError:
        print("Choix invalide.")
        pause()
        return

    if choix < 1 or choix > len(profils):
        print("Profil inexistant.")
        pause()
        return

    profil_choisi = profils[choix - 1]
    confirmation = input(f"\nSupprimer '{profil_choisi}' ? (o/n) : ").strip().lower()

    if confirmation == "o":
        path = f"add/{profil_choisi}.json"
        os.remove(path)
        print("Profil supprimé avec succès.")
    else:
        print("Suppression annulée.")

    pause()


def main():
    while True:
        clear()
        print("""\n

⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣶⣿⣿⣿⣿⣿⣶⡀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠆       Osint - Identities
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣽⣿⣿⣿⣿⣿⣿⣿⡟⠀            By Rorz X Offset
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⡿⠁
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣾⢻⣿⣿⣿⣿⣿⣿⡀
⠀⠀⠀⠀⢀⣠⣤⣴⣾⣿⣿⣿⠛⠀⠙⡿⠟⠋⠀⣿⣿⣦⣄⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⡟⠀⣰⣿⣿⣆⠀⢰⣿⣿⣿⣿⣿⣷⣶⣄⡀⠀⠀
⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⣰⣿⣷⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⠀
⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⢰⣿⣿⣿⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀
⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⣿⣿⣿⣿⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
 """)
        print("\n1 - Add Profiles")
        print("2 - show Profiles")
        print("3 - Delete Profiles")
        print("4 - Revenir en arriere")

        choix = input("\n Choose an Option: ").strip()

        if choix == "1":
            add()
        elif choix == "2":
            show()
        elif choix == "3":
            delete_profile()
        elif choix == '4':
            subprocess.run([PYTHON, "menu.py"])
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()
