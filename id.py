import os
import subprocess
import json
import random

dossier = "id"

def ask(prompt: str, obligatoire: bool = False):
    while True:
        reponse = input(f"{prompt} : ").strip()

        if obligatoire and not reponse:
            print("Ce champ est obligatoire.")
            continue

        return reponse
    
def pause():
    input("\n[-] Appuie sur Entrée pour continuer...")


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

    print("[-] profil create successfully")

    os.makedirs("add", exist_ok=True)

    filename = champs["profil_name"].strip().replace(" ", "_")
    path = f"add/{filename}.json"

    with open(path, "w", encoding="utf-8") as file:
        json.dump(champs, file, indent=4, ensure_ascii=False)

    print(f"\n[-] Profil sauvegardé dans {path}")

    pause()

def show():
    clear()

    profils = list_profiles()

    if not profils:
        print("Aucun profil trouvé.")
        pause()
        return

    print("\n[-] PROFILS DISPONIBLES [-]\n")

    for i, p in enumerate(profils, 1):
        print(f"[{i}] {p}")

    try:
        choix = int(input("\n[-] Choisis un profil : ").strip())
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

    print("\n[-] PROFIL [-]\n")

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

def profil_gen():
    dossier = "id"

    def lire_fichier(fichier):
        chemin = os.path.join(dossier, fichier)
        if not os.path.exists(chemin):
            print(f"[ERREUR] Fichier manquant : {chemin}")
            return []

        with open(chemin, "r", encoding="utf-8") as f:
            return [line.strip() for line in f if line.strip()]

    ages = lire_fichier("age.txt")
    jobs = lire_fichier("jobs.txt")
    nationalites = lire_fichier("nationalite.txt")
    noms = lire_fichier("nom.txt")
    prenoms = lire_fichier("prenom.txt")
    pseudos = lire_fichier("pseudo.txt")

    # sécurité si fichiers vides
    if not all([ages, jobs, nationalites, noms, prenoms, pseudos]):
        print("Erreur : un ou plusieurs fichiers sont vides.")
        pause()
        return

    def creer_profil():
        return {
            "prenom": random.choice(prenoms),
            "nom": random.choice(noms),
            "age": random.choice(ages),
            "job": random.choice(jobs),
            "nationalite": random.choice(nationalites),
            "pseudo": random.choice(pseudos)
        }

    # génération propre
    nombre = int(input("[-] Combien de profils générer ? : ").strip())

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