# 🔎 OSINT Toolkit

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Version](https://img.shields.io/badge/Status-Active-success)
![License](https://img.shields.io/badge/License-MIT-green)

## 📖 Description

OSINT Toolkit est une suite d'outils Open Source dédiée à l'Open Source Intelligence (OSINT). Le projet regroupe plusieurs fonctionnalités permettant de collecter, analyser et exploiter des informations accessibles publiquement.

L'objectif est de fournir une plateforme simple, rapide et évolutive pour les passionnés de cybersécurité, chercheurs, étudiants et professionnels souhaitant effectuer des recherches OSINT depuis une seule interface.

Le projet est activement maintenu et recevra régulièrement des mises à jour, de nouvelles fonctionnalités et des améliorations afin d'élargir ses capacités.

---

## ✨ Fonctionnalités

### 📸 Analyse EXIF
Extraction et analyse des métadonnées d'images :

- Date de création
- Coordonnées GPS
- Modèle d'appareil photo
- Paramètres de prise de vue
- Informations techniques du fichier

---

### 🌐 Sherlock
Recherche de noms d'utilisateur sur de nombreuses plateformes :

- Réseaux sociaux
- Forums
- Services en ligne
- Plateformes communautaires

Permet de retrouver rapidement la présence numérique d'un utilisateur.

---

### 📝 Wordlist Generator
Génération de wordlists personnalisées à partir d'informations fournies par l'utilisateur.

Exemples :

- Nom
- Prénom
- Date de naissance
- Pseudonymes
- Informations personnalisées

---

## 🚀 Installation

### Cloner le projet

```bash
git clone https://github.com/VOTRE-PSEUDO/osint-toolkit.git
cd osint-toolkit
```

### Installer les dépendances

```bash
pip install -r requirements.txt
```

### Requirements

```txt
aiohttp
exifread
```

---

## ▶️ Utilisation

Lancer simplement le programme :

```bash
python main.py
```

Puis sélectionner l'outil souhaité dans le menu.

---

## 📂 Structure du projet

```text
OSINT-Toolkit/
│
├── main.py
├── requirements.txt
├── README.md
│
├── modules/
│   ├── exif.py
│   ├── sherlock.py
│   └── wordlistgen.py
│
└── assets/
```

---

## 🔮 Fonctionnalités prévues

Le projet est en développement actif.

Prochaines fonctionnalités :

- Analyse d'adresses e-mail
- Lookup IP
- Analyse de domaines
- Recherche WHOIS
- Géolocalisation
- Vérification de fuites de données
- Recherche avancée réseaux sociaux
- Export des résultats
- API intégrée

---

## 🤝 Contributions

Les contributions sont les bienvenues.

Pour contribuer :

1. Fork le projet
2. Crée une branche

```bash
git checkout -b feature/nouvelle-fonction
```

3. Commit tes modifications

```bash
git commit -m "Ajout d'une nouvelle fonctionnalité"
```

4. Push la branche

```bash
git push origin feature/nouvelle-fonction
```

5. Ouvre une Pull Request

---

## ⚠️ Avertissement

Cet outil est destiné à des fins :

- Éducatives
- De recherche
- D'audit autorisé
- De formation en cybersécurité

L'utilisateur est entièrement responsable de l'utilisation qu'il fait du logiciel.

Les développeurs ne pourront être tenus responsables d'une utilisation illégale ou abusive du projet.

---

## 📜 Licence

Ce projet est distribué sous licence MIT.

---

## ⭐ Support

Si ce projet vous est utile :

- ⭐ Laissez une étoile sur GitHub
- 🐛 Signalez les bugs
- 💡 Proposez des idées d'amélioration

Le projet continuera d'évoluer avec de nouveaux modules et fonctionnalités OSINT au fil des mises à jour.
