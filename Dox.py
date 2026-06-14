import os
import sys
import subprocess

from utils import clear, pause, get_python

BANNER = """\
                             
⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⣰⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⡀⠀⢀⠒⠑⣴⣦⣾⣧⣤⢀⡤⠀⠀⠀⡀⠀⠀⠀
⠀⠀⠀⠀⢀⠀⢀⡘⠉⠁⣰⣾⣿⣿⣿⣿⣿⣿⣷⢀⡤⠊⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢱⠊⡄⠒⠾⣿⣿⣿⣿⣿⣿⠿⠛⢹⣿⣯⣤⠤⠄⠀⠀
⠀⠀⠀⠀⠔⢦⠂⠀⣇⠀⠸⠟⢈⣿⣿⡁⠺⠗⠀⣸⣿⣿⣃⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢘⢀⣼⠻⢷⣶⣶⣿⣿⣿⣿⣶⣶⣾⠟⣻⣿⡯⠁⠀⠀⠀
⠀⠀⠀⠀⠉⠱⢾⣿⡀⠀⠈⠉⠙⠛⠛⠛⠉⠉⠀⢀⣿⣿⠿⠛⠒⠀⠀
⠀⠀⠀⠀⠀⠔⢛⣿⣷⡈⠒⠀⠀⠀⠔⠁⠊⠒⢈⣾⣿⡏⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠜⠛⠿⣿⣶⣤⣀⣀⣀⣀⣤⣶⣿⠿⣿⠉⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⡸⠛⢉⡿⠻⠟⣿⢿⡟⣏⠁⠀⠘⠄⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⡜⠀⠀⠀⠁⠀⠃⠘⡀⠀⠀⠀⠀⠀
                                 
                        TOOL BY RORZ - OSINT Recap
                      [N'hésitez pas à DOX des FAFS]
"""

PYTHON = get_python()


def ligne(label, valeur):
    return f"{label:<22} : {valeur}"


def main():
    print(BANNER)

    choice = input(
        "0 - Return Launcher\n"
        "1 - Stay on the tool\n"
        "choix 0 OR 1 :"
    )

    if choice == '0':
        subprocess.run([PYTHON, "menu.py"])
        return

    why = input("[+] Pourquoi Cette Fiche : ")

    print("Cible Principal")
    print("-------------------------------------")

    nom = input("[+] Nom : ")
    prenom = input("[+] Prenom : ")
    pseudo = input("[+] Pseudo : ")
    pseudo2 = input("[+] Pseudo 2 : ")
    ville = input("[+] Ville : ")
    pays = input("[+] Pays : ")
    adress = input("[+] Adress : ")

    print("\nReseaux sociaux")
    print("-------------------------------------")

    insta = input("[+] instagram : ")
    tiktok = input("[+] tiktok : ")
    youtube = input("[+] Youtube : ")
    twitter = input("[+] Twitter : ")
    facebook = input("[+] facebook : ")

    print("\nFamilles")
    print("-------------------------------------")

    pere = input("[+] Nom,Prenom père : ")
    mere = input("[+] Nom,Prenom mère : ")
    adress_parents = input("[+] Adresse Parent : ")
    num_pere = input("[+] Numero père : ")
    num_mere = input("[+] Numero mère : ")

    print("\nInformations de contact")
    print("-------------------------------------")

    mail = input("[+] Mail : ")
    num = input("[+] Numero : ")
    ancien_mail = input("[+] Ancien Mail : ")

    print("\nInfo +")
    print("-------------------------------------")

    password = input("[+] Password : ")
    compte = input("[+] Compte liée au Mail : ")
    discord_id = input("[+] ID Discord: ")
    site_id = input("[+] ID Site: ")
    animal = input("[+] Animal Name: ")
    passion = input("[+] Passion : ")
    jeux = input("[+] Jeux préférés : ")

    print("\nNote +")
    print("-------------------------------------")

    note = input("des choses en + ? ")

    texte = f"""{BANNER}

{ligne("Pourquoi Cette Fiche ? ", why)}

================= CIBLE PRINCIPALE =================

{ligne("Nom", nom)}
{ligne("Prenom", prenom)}
{ligne("Pseudo", pseudo)}
{ligne("Pseudo Secondaire", pseudo2)}
{ligne("Ville", ville)}
{ligne("Pays", pays)}
{ligne("Adresse", adress)}

================= RESEAUX SOCIAUX =================

{ligne("Instagram", insta)}
{ligne("TikTok", tiktok)}
{ligne("YouTube", youtube)}
{ligne("Twitter", twitter)}
{ligne("Facebook", facebook)}

================= FAMILLE =================

{ligne("Pere", pere)}
{ligne("Mere", mere)}
{ligne("Adresse parents", adress_parents)}
{ligne("Numero pere", num_pere)}
{ligne("Numero mere", num_mere)}

=================CONTACT =================

{ligne("Mail", mail)}
{ligne("Numero", num)}
{ligne("Mail 2", ancien_mail)}

================= INFO + =================

{ligne("Password", password)}
{ligne("Compte lie", compte)}
{ligne("ID Discord", discord_id)}
{ligne("ID Sites", site_id)}
{ligne("Animal", animal)}
{ligne("Passion", passion)}
{ligne("Jeux Pref", jeux)}

================= Note + =================

{ligne("des choses en + ?  ", note)}
"""

    nom_fichier = f"{prenom}.txt" if prenom else "output.txt"
    chemin = os.path.join(os.path.dirname(__file__), nom_fichier)

    if os.path.exists(chemin):
        overwrite = input(f"\n[!] {nom_fichier} existe déjà. Écraser ? (o/n) : ").strip().lower()
        if overwrite != "o":
            print("Annulé.")
            return

    with open(chemin, "w", encoding="utf-8") as fichier:
        fichier.write(texte)

    print(f"\n✅ Données enregistrées dans {nom_fichier}")


if __name__ == "__main__":
    main()
