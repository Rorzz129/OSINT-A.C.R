import os
import subprocess

banner = """                             
⠀ 
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣶⣿⣿⣿⣿⣿⣶⡀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠆       Osint - DoxTemplate
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

# 🔧 Fonction pour aligner proprement
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

why = input("[+] Pourquoi Cette Fiche : ")

print("Cible Principal")
print("-------------------------------------")

nom = input("[+] Nom : ")
Prenom = input("[+] Prenom : ")
Pseudo = input("[+] Pseudo : ")
Pseudo2 = input("[+] Pseudo 2 : ")
Ville = input("[+] Ville : ")
pays = input("[+] Pays : ")
adress = input("[+] Adress : ")

print("\nReseaux sociaux")
print("-------------------------------------")

insta = input("[+] instagram : ")
tiktok = input("[+] tiktok : ")
youtube = input("[+] Youtube : ")
X = input("[+] Twitter : ")
facebook = input("[+] facebook : ")

print("\nFamilles")
print("-------------------------------------")

Pn = input("[+] Nom,Prenom père : ")
Mn = input("[+] Nom,Prenom mère : ")
Adressen = input("[+] Adresse Parent : ")
NP = input("[+] Numero père : ")
NM = input("[+] Numero mère : ")

print("\nInformations de contact")
print("-------------------------------------")

mail = input("[+] Mail : ")
num = input("[+] Numero : ")
maill = input("[+] Ancien Mail : ")

print("\nInfo +")
print("-------------------------------------")

password = input("[+] Password : ")
compte = input("[+] Compte liée au Mail : ")
ID = input("[+] ID Discord: ")
IDD = input("[+] ID Site: ")
animal = input("[+] Animal Name: ")
Pass = input("[+] Passion : ")
Jeux = input("[+] Jeux préférés : ")

print("\nNote +")
print("-------------------------------------")

note = input("des choses en + ? ")

# 📄 Texte final avec alignement + banner
texte = f"""{banner}

{ligne("Pourquoi Cette Fiche ? ", why)}

================= CIBLE PRINCIPALE =================

{ligne("Nom", nom)}
{ligne("Prenom", Prenom)}
{ligne("Pseudo", Pseudo)}
{ligne("Pseudo Secondaire", Pseudo2)}
{ligne("Ville", Ville)}
{ligne("Pays", pays)}
{ligne("Adresse", adress)}

================= RESEAUX SOCIAUX =================

{ligne("Instagram", insta)}
{ligne("TikTok", tiktok)}
{ligne("YouTube", youtube)}
{ligne("Twitter", X)}
{ligne("Facebook", facebook)}

================= FAMILLE =================

{ligne("Pere", Pn)}
{ligne("Mere", Mn)}
{ligne("Adresse parents", Adressen)}
{ligne("Numero pere", NP)}
{ligne("Numero mere", NM)}

=================CONTACT =================

{ligne("Mail", mail)}
{ligne("Numero", num)}
{ligne("Mail 2", maill)}

================= INFO + =================

{ligne("Password", password)}
{ligne("Compte lie", compte)}
{ligne("ID Discord", ID)}
{ligne("ID Sites", IDD)}
{ligne("Animal", animal)}
{ligne("Passion", Pass)}
{ligne("Jeux Pref", Jeux)}

================= Note + =================

{ligne("des choses en + ?  ", note)}
"""

# 📁 Nom du fichier basé sur le prénom
nom_fichier = f"{Prenom}.txt"
chemin = os.path.join(os.path.dirname(__file__), nom_fichier)

# 💾 Écriture
with open(chemin, "w", encoding="utf-8") as fichier:
    fichier.write(texte)

print(f"\n✅ Données enregistrées dans {nom_fichier}")
