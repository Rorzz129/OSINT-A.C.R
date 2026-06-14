import os
import subprocess
import json
import random

dossier = "id"

def ask(prompt: str, obligatoire: bool = False):
    while True:
        reponse = input(f"{prompt} : ").strip()

        if obligatoire and not reponse:
            print("This field is mandatory.")
            continue

        return reponse
    
def pause():
    input("\n[-] Press any keys to continue...")


def clear():
    os.system("cls" if os.name == "nt" else "clear")
    
def list_profiles():
    dossier = "add"

    fichiers = os.listdir(dossier)

    profils = []

    for f in fichiers:
        if f.endswith(".json"):
            profils.append(f.replace(".json", ""))

    return profils


def add():
    champs = {
        "profile_name": ask("[+] Profile name"),
        "last_name": ask("[+] Last name"),
        "first_name": ask("[+] First name"),
        "age": ask("[+] Age"),
        "email": ask("[+] Email"),
        "phone_number": ask("[+] Phone number"),
        "birthday": ask("[+] Birthday"),
        "place_of_birth": ask("[+] Place of birth"),
        "bio": ask("[+] Bio"),
        "username": ask("[+] Username"),
        "address": ask("[+] Address"),
        "account": ask("[+] Account"),
        "gender": ask("[+] Gender"),
        "nationality": ask("[+] Nationality"),
        "discord": ask("[+] Discord"),
        "instagram": ask("[+] Instagram"),
        "telegram": ask("[+] Telegram"),
        "job": ask("[+] Job"),
        "studies": ask("[+] Studies"),
        "hobbies": ask("[+] Hobbies"),
        "password": ask("[+] Password"),
        "backup_email": ask("[+] Backup email"),
    }

    print("[-] profil create successfully")

    os.makedirs("add", exist_ok=True)

    filename = champs["profil_name"].strip().replace(" ", "_")
    path = f"add/{filename}.json"

    with open(path, "w", encoding="utf-8") as file:
        json.dump(champs, file, indent=4, ensure_ascii=False)

    print(f"\n[-] Profil Saved in {path}")

    pause()

def show():
    clear()

    profils = list_profiles()

    if not profils:
        print(" Nothing Found ( 0 Profils )")
        pause()
        return

    print("\n[-] PROFILES AVAILABLE [-]\n")

    for i, p in enumerate(profils, 1):
        print(f"[{i}] {p}")

    try:
        choix = int(input("\n[-] Choose a profile : ").strip())
    except ValueError:
        print("Invalid Choice ! ")
        pause()
        return

    if choix < 1 or choix > len(profils):
        print("Non-existent profile")
        pause()
        return

    profil_name = profils[choix - 1]
    path = f"add/{profil_name}.json"

    with open(path, "r", encoding="utf-8") as file:
        data = json.load(file)

    clear()

    print("\n[-] PROFIL [-]\n")

    for key, value in data.items():
        print(f"{key:<20} : {value}")

    print("\n====================")

    pause()

def delete_profile():
    clear()

    profils = list_profiles()

    if not profils:
        print("No profiles to delete")
        pause()
        return

    print("\n===== PROFILES =====\n")

    for i, p in enumerate(profils, 1):
        print(f"[{i}] {p}")

    try:
        choix = int(input("\nChoose the profile to delete : ").strip())
    except ValueError:
        print("Invalid choice")
        pause()
        return

    if choix < 1 or choix > len(profils):
        print("Non-existent profile")
        pause()
        return

    profil_choisi = profils[choix - 1]

    confirmation = input(f"\nDelete '{profil_choisi}' ? (o/n) : ").strip().lower()

    if confirmation == "o":
        path = f"add/{profil_choisi}.json"
        os.remove(path)
        print("Profile successfully deleted")
    else:
        print("Deletion canceled")

    pause()

def profil_gen():
    dossier = "id"

    def lire_fichier(fichier):
        chemin = os.path.join(dossier, fichier)
        if not os.path.exists(chemin):
            print(f"[ERREUR] midding file : {chemin}")
            return []

        with open(chemin, "r", encoding="utf-8") as f:
            return [line.strip() for line in f if line.strip()]

    ages = lire_fichier("age.txt")
    jobs = lire_fichier("jobs.txt")
    nationalites = lire_fichier("nationalite.txt")
    name = lire_fichier("nom.txt")
    firstname = lire_fichier("prenom.txt")
    pseudos = lire_fichier("pseudo.txt")

    # sécurité si fichiers vides
    if not all([ages, jobs, nationalites, name, firstname, pseudos]):
        print("Error: One or more files are empty")
        pause()
        return

    def creer_profil():
        return {
            "FirstName": random.choice(firstname),
            "name": random.choice(name),
            "age": random.choice(ages),
            "job": random.choice(jobs),
            "nationalite": random.choice(nationalites),
            "pseudo": random.choice(pseudos)
        }

    # génération propre
    nombre = int(input("[-] Chow many profiles to generate ?: ").strip())

    for _ in range(nombre):
        print(creer_profil())

    pause()


def main(): 
    while True:
        clear()
        print("""\n

⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣶⣿⣿⣿⣿⣿⣶⡀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠆       Osint - Identities
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣽⣿⣿⣿⣿⣿⣿⣿⡟⠀            By Rorz X Offset
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⡿⠁
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣾⢻⣿⣿⣿⣿⣿⣿⡀
⠀⠀⠀⠀⢀⣠⣤⣴⣾⣿⣿⣿⠛⠀⠙⡿⠟⠋⠀⣿⣿⣦⣄⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⡟⠀⣰⣿⣿⣆⠀⢰⣿⣿⣿⣿⣿⣷⣶⣄⡀⠀⠀
⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⣰⣿⣷⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⠀
⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⢰⣿⣿⣿⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀
⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⣿⣿⣿⣿⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇           
 """)
        print("\n1 - Add Profiles")
        print("2 - show Profiles")
        print("3 - Delete Profiles")
        print("4 - Generator ID")
        print("5 - Menu.py")

        choix = input("\n[-] Choose an Option: ").strip()

        if choix == "1":
            add()

        elif choix == "2":
            show()

        elif choix == "3":
            delete_profile()

        elif choix == "4":
            profil_gen()

        elif choix == '5':
            subprocess.run(["python", "menu.py"])

        else:
            print("Invalid option.")

if __name__=="__main__":
    main()