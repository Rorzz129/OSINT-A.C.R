import itertools
import os
import subprocess
import sys
from datetime import datetime

from utils import clear, pause, get_python

PYTHON = get_python()

BANNER = r"""
  ██████╗  ██████╗ ██████╗ ███████╗    ██╗    ██╗██╗
  ██╔══██╗██╔═══██╗██╔══██╗╚══███╔╝    ██║    ██║██║
  ██████╔╝██║   ██║██████╔╝  ███╔╝     ██║ █╗ ██║██║
  ██╔══██╗██║   ██║██╔══██╗ ███╔╝      ██║███╗██║██║
  ██║  ██║╚██████╔╝██║  ██║███████╗    ╚███╔███╔╝███████╗
  ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝    ╚══╝╚══╝ ╚══════╝
           [ WORDLIST GENERATOR - HACKTIVIST ]
"""

SEPARATEURS = ["", "_", "-", ".", " "]
CARACT_SPECIAUX = ["!", "@", "#", "$", "%", "&", "*", "?", ".", "-", "_"]
LEET_TABLE = str.maketrans("aAeEiIoOsStT", "4433110055++")
ANNEES = [str(a) for a in range(1970, datetime.now().year + 1)]
SUFFIXES = ["123", "1234", "12345", "0", "00", "01", "007", "69", "666", "999"]


def couleur(texte, code):
    if sys.stdout.isatty():
        return f"\033[{code}m{texte}\033[0m"
    return texte


def info(msg):
    print(couleur(f"  ✔ {msg}", "32"))


def warn(msg):
    print(couleur(f"  ⚠ {msg}", "33"))


def erreur(msg):
    print(couleur(f"  ✘ {msg}", "31"))


def titre(msg):
    print(couleur(msg, "1;36"))


def demander(prompt, obligatoire=False):
    while True:
        try:
            reponse = input(couleur(f"  {prompt}", "33")).strip()
        except (KeyboardInterrupt, EOFError):
            print("\n")
            sys.exit(0)
        if reponse or not obligatoire:
            return reponse
        warn("Ce champ est obligatoire.")


def oui_non(prompt, defaut=False):
    hint = "[O/n]" if defaut else "[o/N]"
    while True:
        try:
            r = input(couleur(f"  {prompt} {hint} : ", "33")).strip().lower()
        except (KeyboardInterrupt, EOFError):
            print("\n")
            sys.exit(0)
        if r == "":
            return defaut
        if r in ("oui", "o", "yes", "y"):
            return True
        if r in ("non", "n", "no"):
            return False
        warn("Répondez par oui ou non.")


def saisir_entier(prompt, defaut, mini=1, maxi=10_000):
    while True:
        try:
            val = input(couleur(f"    → {prompt} (défaut {defaut}) : ", "33")).strip()
            n = int(val or defaut)
            if mini <= n <= maxi:
                return n
            warn(f"Entrez un entier entre {mini} et {maxi}.")
        except ValueError:
            warn("Entier invalide.")
        except (KeyboardInterrupt, EOFError):
            print("\n")
            sys.exit(0)


def variantes_casse(mot):
    return {mot, mot.lower(), mot.upper(), mot.capitalize(), mot.title()}


def variantes_leetspeak(mot):
    transformed = mot.translate(LEET_TABLE)
    return {transformed, transformed.lower(), transformed.upper()} if transformed != mot else set()


def variantes_doubles(mot):
    return {mot + mot, mot + "_" + mot, mot + "-" + mot}


def appliquer_mutations(mots):
    enrichis = set()
    for m in mots:
        enrichis.update(variantes_casse(m))
        enrichis.update(variantes_leetspeak(m))
        enrichis.update(variantes_doubles(m))
    return enrichis


def generer_base(infos, profondeur=3):
    wordlist = set()
    for taille in range(1, profondeur + 1):
        for combo in itertools.permutations(infos, taille):
            for sep in SEPARATEURS:
                mot = sep.join(combo)
                wordlist.update(variantes_casse(mot))
    return wordlist


def ajouter_nombres(wordlist, plage=100):
    ajouts = set()
    numeros = [str(n) for n in range(plage)] + SUFFIXES + ANNEES
    snapshot = list(wordlist)
    for mot in snapshot:
        for n in numeros:
            ajouts.add(mot + n)
            ajouts.add(n + mot)
    wordlist.update(ajouts)
    return wordlist


def ajouter_speciaux(wordlist):
    ajouts = set()
    snapshot = list(wordlist)
    for mot in snapshot:
        for s in CARACT_SPECIAUX:
            ajouts.add(mot + s)
            ajouts.add(s + mot)
        for s1, s2 in itertools.product(CARACT_SPECIAUX[:5], repeat=2):
            ajouts.add(mot + s1 + s2)
    wordlist.update(ajouts)
    return wordlist


def ajouter_mutations(wordlist):
    wordlist.update(appliquer_mutations(wordlist))
    return wordlist


def filtrer_longueur(wordlist, mini=4, maxi=32):
    return {m for m in wordlist if mini <= len(m) <= maxi}


def sauvegarder(wordlist, chemin):
    mots_tries = sorted(wordlist, key=lambda x: (len(x), x))
    with open(chemin, "w", encoding="utf-8") as f:
        f.write("\n".join(mots_tries) + "\n")
    return len(mots_tries)


def main():
    print(BANNER)
    print("=" * 60)

    titre("\n Informations cible \n")

    champs = {
        "prenom": demander("[+] Prénom          : "),
        "nom": demander("[+] Nom             : "),
        "pseudo": demander("[+] Pseudo / login  : "),
        "annee": demander("[+] Année naissance : "),
        "animal": demander("[+] Animal préféré  : "),
        "ville": demander("[+] Ville / pays    : "),
        "mot_cle": demander("[+] Mot clé (hobby) : "),
        "extra": demander("[+] Info bonus      : "),
    }

    print()
    avec_nombres = oui_non("[+] Ajouter des nombres ?", defaut=True)
    avec_speciaux = oui_non("[+] Ajouter des caractères spéciaux ?", defaut=True)
    avec_mutations = oui_non("[+] Appliquer mutations (leet, doublons…) ?", defaut=True)
    avec_filtre = oui_non("[+] Filtrer longueurs hors [4-32] ?", defaut=True)

    plage = saisir_entier("[+] Plage de nombres (0 → N)", 100, 1, 9999) if avec_nombres else 100
    profondeur = saisir_entier("[+] Profondeur des combinaisons (2-4)", 3, 2, 4)

    infos = [v for v in champs.values() if v]
    if not infos:
        erreur("Aucune information fournie. Abandon.")
        sys.exit(1)

    print()
    titre("[+] Génération en cours…\n")

    wordlist = generer_base(infos, profondeur=profondeur)
    info(f"Base                : {len(wordlist):>12,} mots")

    if avec_mutations:
        wordlist = ajouter_mutations(wordlist)
        info(f"+ Mutations (leet)  : {len(wordlist):>12,} mots")

    if avec_nombres:
        wordlist = ajouter_nombres(wordlist, plage)
        info(f"+ Nombres           : {len(wordlist):>12,} mots")

    if avec_speciaux:
        wordlist = ajouter_speciaux(wordlist)
        info(f"+ Spéciaux          : {len(wordlist):>12,} mots")

    if avec_filtre:
        avant = len(wordlist)
        wordlist = filtrer_longueur(wordlist)
        info(f"Filtre longueur     : -{avant - len(wordlist):,} → {len(wordlist):>12,} mots")

    horodatage = datetime.now().strftime("%Y%m%d_%H%M%S")
    nom_fichier = f"wordlist_{horodatage}.txt"
    nb_mots = sauvegarder(wordlist, nom_fichier)
    taille_mo = os.path.getsize(nom_fichier) / (1024 * 1024)

    print(f"""
╔══════════════════════════════════════════════════
║           ✅  GÉNÉRATION TERMINÉE
╠══════════════════════════════════════════════════
║  Mots générés  : {nb_mots:>12,}
║  Fichier       : {nom_fichier:<30}
║  Taille        : {taille_mo:>11.2f} Mo
╚══════════════════════════════════════════════════
""")


if __name__ == "__main__":
    choice = input(
        "0 - Return Launcher\n"
        "1 - Stay on the tool\n"
        "choix 0 OR 1 :"
    )

    if choice == '0':
        subprocess.run([PYTHON, "menu.py"])
    else:
        main()
