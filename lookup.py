import requests
import socket
import subprocess
import os
import whois

def pause():
    input("\nPress any keys to continue...")


def clear():
    os.system("cls" if os.name == "nt" else "clear")

def port():
    clear()

    target = input("IP or domaine : ").strip()

    try:
        ip = socket.gethostbyname(target)
    except:
        print("Erreur : invalid target")
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

    print("\nScan finished.. ")
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

        try:
            host = socket.gethostbyaddr(ip)
            print(f"Hostname       : {host[0]}")
        except:
            print("Hostname       : introuvable")

        try:
            all_ips = socket.gethostbyname_ex(domain)[2]
            print("\n--- Toutes les IPs ---")
            for i, ip_addr in enumerate(all_ips, 1):
                print(f"{i}. {ip_addr}")
        except:
            pass

    except:
        print("Error: Domain not found or DNS invalid")

    pause()

def ip():
    clear()

    ip = input("IP to analyze : ").strip()

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
        print("Error during query")

    pause()

def header():
    clear()

    url = input("URL (https://...) : ").strip()

    try:
        r = requests.get(url, timeout=5)

        print("\n===== WEBSITE HEADERS =====\n")

        for key, value in r.headers.items():
            print(f"{key:<20} : {value}")

        interesting = {
            "Server": "Web server",
            "X-Powered-By": "Technology",
            "Content-Type": "Content type",
            "Content-Length": "Size",
            "Strict-Transport-Security": "HSTS",
            "Content-Security-Policy": "CSP",
            "X-Frame-Options": "Frame protection",
            "Set-Cookie": "Cookies",
        }
        for header, desc in interesting.items():
            value = r.headers.get(header)

        if value:
            print(f"{desc:<25}: {value}")

    except Exception as e:
        print(f"ERROR : {e}")

    pause()

def whoiss():
    clear()

    domain = input("Domaine : ").strip()

    try:
        w = whois.whois(domain)

        print("\n------ WHOIS LOOKUP -----\n")

        print(f"Domain         : {w.domain_name}")
        print(f"Registrar      : {w.registrar}")
        print(f"WHOIS Server   : {w.whois_server}")
        print(f"Status         : {w.status}")
        print(f"Created on     : {w.creation_date}")
        print(f"Updated on     : {w.updated_date}")
        print(f"Expires on     : {w.expiration_date}")
        print(f"Emails         : {w.emails}")
        print(f"DNS            : {w.name_servers}")
        print(f"DNSSEC         : {w.dnssec}")
        print(f"Organization   : {w.org}")
        print(f"Country        : {w.country}")

    except Exception as e:
        print(f"Erreur : {e}")

    pause()

def main():
    while True:
        print("""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣶⣿⣿⣿⣿⣿⣶⡀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠆       Osint - LookUp
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣽⣿⣿⣿⣿⣿⣿⣿⡟⠀            By Rorz X Offset
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⡿⠁
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣾⢻⣿⣿⣿⣿⣿⣿⡀
⠀⠀⠀⠀⢀⣠⣤⣴⣾⣿⣿⣿⠛⠀⠙⡿⠟⠋⠀⣿⣿⣦⣄⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⡟⠀⣰⣿⣿⣆⠀⢰⣿⣿⣿⣿⣿⣷⣶⣄⡀⠀⠀
⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⣰⣿⣷⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⠀
⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⢰⣿⣿⣿⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀
⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⣿⣿⣿⣿⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇     
    """)
    
        print("\n[1] - Port Analyser")
        print("[2] - DNS LookUp")
        print("[3] - IP LookUp")
        print("[4] - Website Header LookUp")
        print("[5] - Whois LookUp")
        print("[6] - Leave")

        choix = input("\n Choose an Option: ").strip()

        if choix == "1":
            port()

        elif choix == "2":
            dns()

        elif choix == "3":
            ip()

        elif choix == "4":
            header()

        elif choix == "5":
            whoiss()

        elif choix == '6':
            subprocess.run(["python", "menu.py"])

        else:
            print("Invalid option.")

if __name__=="__main__":
    main()