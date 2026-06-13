import requests
import socket
import subprocess
import os

def pause():
    input("\nAppuie sur Entrée pour continuer...")


def clear():
    os.system("cls" if os.name == "nt" else "clear")

import socket

def port():
    clear()

    target = input("IP ou domaine : ").strip()

    try:
        ip = socket.gethostbyname(target)
    except:
        print("Erreur : cible invalide.")
        pause()
        return

    ports = {
        21: "FTP",
        22: "SSH",
        23: "Telnet",
        25: "SMTP",
        53: "DNS",
        80: "HTTP",
        110: "POP3",
        443: "HTTPS",
        3306: "MySQL",
        8080: "HTTP-ALT"
    }

    clear()
    print("===== PORT ANALYZER =====\n")
    print(f"Cible : {target}")
    print(f"IP    : {ip}\n")

    print("PORT     STATUS      SERVICE")
    print("-" * 35)

    for port, service in ports.items():
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.7)

        result = sock.connect_ex((ip, port))

        if result == 0:
            status = "OPEN"
        else:
            status = "CLOSED"

        print(f"{port:<8} {status:<10} {service}")

        sock.close()

    print("\nScan terminé")
    pause()

def dns():
    clear()

    domain = input("Domaine (ex: google.com) : ").strip()

    try:
        clear()
        print("===== DNS LOOKUP =====\n")

        # IP principale
        ip = socket.gethostbyname(domain)
        print(f"Domaine        : {domain}")
        print(f"IP principale  : {ip}")

        # Reverse lookup (IP -> hostname)
        try:
            host = socket.gethostbyaddr(ip)
            print(f"Hostname       : {host[0]}")
        except:
            print("Hostname       : introuvable")

        # Toutes les IPs (si plusieurs serveurs)
        try:
            all_ips = socket.gethostbyname_ex(domain)[2]
            print("\n--- Toutes les IPs ---")
            for i, ip_addr in enumerate(all_ips, 1):
                print(f"{i}. {ip_addr}")
        except:
            pass

    except:
        print("Erreur : domaine introuvable ou DNS invalide.")

    pause()

def ip():
    clear()

    ip = input("IP à analyser : ").strip()

    try:
        r = requests.get(f"http://ip-api.com/json/{ip}")
        data = r.json()

        clear()
        print("===== IP LOOKUP =====\n")

        print(f"IP        : {data.get('query')}")
        print(f"Pays      : {data.get('country')}")
        print(f"Région    : {data.get('regionName')}")
        print(f"Ville     : {data.get('city')}")
        print(f"ISP       : {data.get('isp')}")
        print(f"Organisation : {data.get('org')}")
        print(f"Latitude  : {data.get('lat')}")
        print(f"Longitude : {data.get('lon')}")

    except:
        print("Erreur lors de la requête.")

    pause()

def main():
    while True:
        print("""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠀⠤⠴⠶⡇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣶⣾⣿⡟
⠀⠀⠀⠀⠀⠀⠀⠂⠉⡇⠀⠀⠀⢰⣿⣿⣿⣿⣧⠀⠀⢀⣄⣀
⠀⠀⠀⠀⠀⠀⢠⣶⣶⣷⠀⠀⠀⠸⠟⠁⠀⡇⠀⠀⠀⠀⠀⢹
⠀⠀⠀⠀⠀⠀⠘⠟⢹⣋⣀⡀⢀⣤⣶⣿⣿⣿⣿⣿⡿⠛⣠⣼⣿⡟
⠀⠀⠀⠀⠀⣴⣾⣿⣿⣿⣿⢁⣾⣿⣿⣿⣿⣿⣿⡿⢁⣾⣿⣿⣿⠁         Look Up - IP / DNS / Port
⠀⠀⠀⠀⠸⣿⣿⣿⣿⣿⣿⢸⣿⣿⣿⣿⣿⣿⣿⡇⢸⣿⣿⣿⠿⠇             By Rorz X Offset
⠀⠀⠀⠳⣤⣙⠟⠛⢻⠿⣿⠸⣿⣿⣿⣿⣿⣿⣿⣇⠘⠉⠀⢸⠀⢀⣠
⠀⠀⠀⠀⠈⠻⣷⣦⣼⠀⠀⠀⢻⣿⣿⠿⢿⡿⠿⣿⡄⠀⠀⣼⣷⣿⣿
⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⣶⣄⡈⠉⠀⠀⢸⡇⠀⠀⠉⠂⠀⣿⣿⣿⣧
⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣷⣤⣀⣸⣧⣠⣤⣴⣶⣾⣿⣿⣿⡿
⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇
⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠟⠛⠉
    """)
    
        print("\n[1] - Port Analyser")
        print("[2] - DNS LookUp")
        print("[3] - IP LookUp")
        print("[4] - Quitter")

        choix = input("\n Choose an Option: ").strip()

        if choix == "1":
            port()

        elif choix == "2":
            dns()

        elif choix == "3":
            ip()

        elif choix == '4':
            subprocess.run(["python", "menu.py"])

        else:
            print("Invalid option.")

if __name__=="__main__":
    main()