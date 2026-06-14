import os
import subprocess

def pause():
    input("\n[-] Press any keys to continue...")


def clear():
    os.system("cls" if os.name == "nt" else "clear")

clear()
banner = """                             
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣶⣿⣿⣿⣿⣿⣶⡀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠆       Osint - Dox Template
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣽⣿⣿⣿⣿⣿⣿⣿⡟⠀            By Rorz X Offset
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⡿⠁
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣾⢻⣿⣿⣿⣿⣿⣿⡀
⠀⠀⠀⠀⢀⣠⣤⣴⣾⣿⣿⣿⠛⠀⠙⡿⠟⠋⠀⣿⣿⣦⣄⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⡟⠀⣰⣿⣿⣆⠀⢰⣿⣿⣿⣿⣿⣷⣶⣄⡀⠀⠀
⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⣰⣿⣷⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⠀
⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⢰⣿⣿⣿⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀
⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⣿⣿⣿⣿⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇     
                                            
"""

print(banner)



def ligne(label, valeur):
    return f"{label:<22} : {valeur}"

choice = input(
    "0 - Return Launcher\n"
    "1 - Stay on the tool\n" \
    "choix 0 OR 1 :"
)

if choice == '0':
    subprocess.run(["python", "menu.py"])
    exit()

why = input("[+] Why This Sheet : ")

print("Main Target")
print("-------------------------------------")

nom = input("[+] Name : ")
Prenom = input("[+] First name : ")
Pseudo = input("[+] Pseudo : ")
Pseudo2 = input("[+] Pseudo 2 : ")
Ville = input("[+] Ville : ")
pays = input("[+] Country : ")
adress = input("[+] Adress : ")

print("\nSocial Media")
print("-------------------------------------")

insta = input("[+] instagram : ")
tiktok = input("[+] tiktok : ")
youtube = input("[+] Youtube : ")
X = input("[+] Twitter : ")
facebook = input("[+] facebook : ")

print("\nFamilles")
print("-------------------------------------")

Pn = input("[+] Dad name : ")
Mn = input("[+] Mom name : ")
Adressen = input("[+] Parent Adress : ")
NP = input("[+] Dad Phone : ")
NM = input("[+] Mom Phone : ")

print("\nContact information")
print("-------------------------------------")

mail = input("[+] Mail : ")
num = input("[+] Phone Number : ")
maill = input("[+] old eMail : ")

print("\nInfo +")
print("-------------------------------------")

password = input("[+] Password : ")
compte = input("[+] account link to the Mail : ")
ID = input("[+] ID Discord: ")
IDD = input("[+] ID Site: ")
animal = input("[+] Animal Name: ")
Pass = input("[+] Passion : ")
Jeux = input("[+] Favorite Game : ")

print("\nNote +")
print("-------------------------------------")

note = input("things in + ? ")

texte = f"""{banner}

{ligne("[+] Why This Sheet : ", why)}

================= Main target =================

{ligne("Last name", nom)}
{ligne("First name", Prenom)}
{ligne("Username", Pseudo)}
{ligne("Secondary username", Pseudo2)}
{ligne("City", Ville)}
{ligne("Country", pays)}
{ligne("Address", adress)}

================= SOCIAL NETWORKS =================

{ligne("Instagram", insta)}
{ligne("TikTok", tiktok)}
{ligne("YouTube", youtube)}
{ligne("Twitter", X)}
{ligne("Facebook", facebook)}

================= FAMILY =================

{ligne("Father", Pn)}
{ligne("Mother", Mn)}
{ligne("Parents' address", Adressen)}
{ligne("Father's number", NP)}
{ligne("Mother's number", NM)}

================= CONTACT =================

{ligne("Email", mail)}
{ligne("Phone number", num)}
{ligne("Secondary email", maill)}

================= INFO + =================

{ligne("Password", password)}
{ligne("Account link", compte)}
{ligne("Discord ID", ID)}
{ligne("Website IDs", IDD)}
{ligne("Animal", animal)}
{ligne("Hobby", Pass)}
{ligne("Favorite game", Jeux)}
================= Note + =================

{ligne("thing more ?  ", note)}
"""

nom_fichier = f"{Prenom}.txt"
chemin = os.path.join(os.path.dirname(__file__), nom_fichier)

# 💾 Écriture
with open(chemin, "w", encoding="utf-8") as fichier:
    fichier.write(texte)

print(f"\nDate saved in {nom_fichier}")
pause()