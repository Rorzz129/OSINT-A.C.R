import os
import subprocess
import sys
import webbrowser
from ddgs import DDGS

def pause():
    input("\nPress any keys to continue... ")

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def get_results(query):
    results = []

    with DDGS() as ddgs:
        for r in ddgs.text(query, max_results=20):
            results.append(r["href"])

    return results

def autodork(mode):
    clear()

    print("""
        MULTI DORK BUILDER
════════════════════════════════════

[1] site:           [8] intitle:
[2] filetype:       [9] allintitle:
[3] inurl:          [10] allinurl:
[4] intext:         [11] related:
[5] intitle:        [12] define:
[6] OR              [13] before:
[7] AND             [14] after:
""")

    try:
        nb = int(input("How many dorks do you want to combine ? (1-5) : ").strip())
    except:
        print("Invalid number")
        pause()
        return

    dork_map = {
        "1": "site",
        "2": "filetype",
        "3": "inurl",
        "4": "intext",
        "5": "intitle",
        "6": "OR",
        "7": "AND",
        "8": "intitle",
        "9": "allintitle",
        "10": "allinurl",
        "11": "related",
        "12": "define",
        "13": "before",
        "14": "after",
    }

    parts = []

    for i in range(nb):
        print(f"\nDork #{i+1}")

        choice = input("Choose dork number (1-14) : ").strip()
        value = input("Enter value : ").strip()

        if choice in dork_map:
            operator = dork_map[choice]

            if operator in ["OR", "AND"]:
                parts.append(operator)
            else:
                parts.append(f"{operator}:{value}")

    dork = " ".join(parts)
    url = "https://www.google.com/search?q=" + dork.replace(" ", "+")

    print("\n===== GENERATED DORK =====")
    print(dork)

    if mode == "cmd":
        print("\n===== TOP 20 RESULTS =====\n")
        results = get_results(dork)

        for i, link in enumerate(results, 1):
            print(f"{i}. {link}")

    elif mode == "browser":
        webbrowser.open(url)

    pause()

def intdork():
    clear()

    print("""
══════════════════════════════════════
        INTELLIGENCE DORKER
══════════════════════════════════════
""")

    site = input("Site            : ").strip()
    keywords = input("Keywords        : ").strip()
    title = input("Title           : ").strip()
    url_contains = input("URL Contains    : ").strip()
    text_contains = input("Page Text       : ").strip()
    filetype = input("Filetype        : ").strip()
    before = input("Before Date     : ").strip()
    after = input("After Date      : ").strip()

    dork_parts = []

    if site:
        dork_parts.append(f"site:{site}")

    if keywords:
        dork_parts.append(keywords)

    if title:
        dork_parts.append(f'intitle:"{title}"')

    if url_contains:
        dork_parts.append(f"inurl:{url_contains}")

    if text_contains:
        dork_parts.append(f'intext:"{text_contains}"')

    if filetype:
        dork_parts.append(f"filetype:{filetype}")

    if before:
        dork_parts.append(f"before:{before}")

    if after:
        dork_parts.append(f"after:{after}")

    dork = " ".join(dork_parts)

    print("\n══════════════════════════════════════")
    print("Generated Dork:")
    print(dork)
    print("══════════════════════════════════════\n")

    try:
        results = []

        with DDGS() as ddgs:
            for r in ddgs.text(dork, max_results=30):

                url = r.get("href", "")
                title = r.get("title", "No title")

                score = 0

                trusted = [
                    ".gov",
                    ".edu",
                    "github.com",
                    "arxiv.org",
                    "scholar.google",
                    "wikipedia.org",
                    "who.int",
                    "europa.eu"
                ]

                medium = [
                    "reddit.com",
                    "stackoverflow.com",
                    "medium.com"
                ]

                for domain in trusted:
                    if domain in url:
                        score += 10

                for domain in medium:
                    if domain in url:
                        score += 5

                results.append({
                    "title": title,
                    "url": url,
                    "score": score
                })

        results.sort(
            key=lambda x: x["score"],
            reverse=True
        )

        print("══════ TOP RESULTS ══════\n")

        for i, result in enumerate(results, 1):

            print(f"[{i}] Score : {result['score']}")
            print(f"Title : {result['title']}")
            print(f"URL   : {result['url']}")
            print("-" * 60)

    except Exception as e:
        print(f"Error : {e}")

    pause()

def menu():
    clear()
    print("""
    ██████╗  ██████╗ ██████╗ ██╗  ██╗███████╗██████╗    ╔═════════════════════════════════╗
    ██╔══██╗██╔═══██╗██╔══██╗██║ ██╔╝██╔════╝██╔══██╗   ║           Basic Dork            ║
    ██║  ██║██║   ██║██████╔╝█████╔╝ █████╗  ██████╔╝   ╠═════════════════════════════════╣
    ██║  ██║██║   ██║██╔══██╗██╔═██╗ ██╔══╝  ██╔══██╗   ║ - site:{site name}              ║
    ██████╔╝╚██████╔╝██║  ██║██║  ██╗███████╗██║  ██║   ║ - filetype:{file extension}     ║
    ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝   ║ - "{Precise research}"          ║
    ╔═════════════════════════════════════════╗         ║ - weather:{city or country}     ║
    ║             autoDorker                  ║         ║ - intitle:{words in title}      ║
    ╠═══════════════════╦═════════════════════╣         ║ - before:{date}                 ║
    ║ [1] autodork      ║ -Preset for dorking ║         ║ - after:{date}                  ║
    ║                   ║                     ║         ║ - allinurl:{words in url}       ║
    ║ [2] IntelResearch ║ -intelligenceDorker ║         ╠═════════════════════════════════╣
    ║                   ║                     ║         ║ discord : gg/hDE8P3f4Hy         ║
    ║ [0] Leave         ║ -Join my server     ║         ║ Github  : Rorzz129/OSINT-A.C.R  ║
    ╚═══════════════════╩═════════════════════╝         ╚═════════════════════════════════╝
""")
    
def cmd():
    clear()
    print("""
    Want a result in your cmd or browser ?

    [1] CMD
    [2] Browser
    """)

    choix = input("Make ur choice : ").strip()

    if choix == "2":
        print("u choose browser mode")
        return "browser"
    else:
        print("u choose CMD mode")
        return "cmd"

def main():
    clear()

    mode = "cmd" 

    while True:
        menu()
        choice = input("\nmake your choice : ").strip()

        if choice == "1":
            mode = cmd()     
            autodork(mode)

        elif choice == "2":
            intdork()

        elif choice == "0":
            subprocess.run(["python", "menu.py"])
            exit()

if __name__=="__main__":
    main()