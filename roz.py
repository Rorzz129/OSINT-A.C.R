import asyncio
import aiohttp
import subprocess
import webbrowser
import os

HEADERS = {"User-Agent": "Mozilla/5.0"}

NEGATIVE = [
    "not found",
    "doesn't exist",
    "page not found",
    "error",
    "404"
]

TIMEOUT = 10
CONCURRENT = 20

SITES = {

    "GitHub":"https://github.com/{}",
    "GitLab":"https://gitlab.com/{}",
    "Bitbucket":"https://bitbucket.org/{}",
    "Twitter/X":"https://x.com/{}",
    "Instagram":"https://www.instagram.com/{}/",
    "Facebook":"https://www.facebook.com/{}",
    "Reddit":"https://www.reddit.com/user/{}",
    "TikTok":"https://www.tiktok.com/@{}",
    "YouTube":"https://www.youtube.com/@{}",
    "Twitch":"https://www.twitch.tv/{}",
    "Snapchat":"https://www.snapchat.com/add/{}",
    "Pinterest":"https://www.pinterest.com/{}/",
    "LinkedIn":"https://www.linkedin.com/in/{}",
    "StackOverflow":"https://stackoverflow.com/users/{}",
    "StackExchange":"https://stackexchange.com/users/{}",
    "Dev.to":"https://dev.to/{}",
    "Hashnode":"https://hashnode.com/@{}",
    "CodePen":"https://codepen.io/{}",
    "Replit":"https://replit.com/@{}",
    "Kaggle":"https://www.kaggle.com/{}",
    "HackerRank":"https://www.hackerrank.com/{}",
    "LeetCode":"https://leetcode.com/{}",
    "Codewars":"https://www.codewars.com/users/{}",
    "Glitch":"https://glitch.com/@{}",
    "JSFiddle":"https://jsfiddle.net/user/{}/",
    "Steam":"https://steamcommunity.com/id/{}",
    "EpicGames":"https://www.epicgames.com/id/{}",
    "Xbox":"https://www.xboxgamertag.com/search/{}",
    "PlayStation":"https://psnprofiles.com/{}",
    "Roblox":"https://www.roblox.com/users/profile?username={}",
    "Battle.net":"https://worldofwarcraft.com/en-us/character/{}",
    "Origin":"https://www.ea.com/games/library/pc/{}",
    "Chess.com":"https://www.chess.com/member/{}",
    "Lichess":"https://lichess.org/@/{}",
    "DeviantArt":"https://www.deviantart.com/{}",
    "Behance":"https://www.behance.net/{}",
    "Dribbble":"https://dribbble.com/{}",
    "ArtStation":"https://www.artstation.com/{}",
    "500px":"https://500px.com/p/{}",
    "Flickr":"https://www.flickr.com/people/{}",
    "SoundCloud":"https://soundcloud.com/{}",
    "Bandcamp":"https://{}.bandcamp.com",
    "Mixcloud":"https://www.mixcloud.com/{}",
    "LastFM":"https://www.last.fm/user/{}",
    "Spotify":"https://open.spotify.com/user/{}",
    "AppleMusic":"https://music.apple.com/profile/{}",
    "Vimeo":"https://vimeo.com/{}",
    "Dailymotion":"https://www.dailymotion.com/{}",
    "Coursera":"https://www.coursera.org/user/{}",
    "Udemy":"https://www.udemy.com/user/{}",
    "Duolingo":"https://www.duolingo.com/profile/{}",
    "edX":"https://www.edx.org/user/{}",
    "Skillshare":"https://www.skillshare.com/profile/{}",
    "ProductHunt":"https://www.producthunt.com/@{}",
    "AngelList":"https://angel.co/u/{}",
    "About.me":"https://about.me/{}",
    "Crunchbase":"https://www.crunchbase.com/person/{}",
    "Patreon":"https://www.patreon.com/{}",
    "Ko-fi":"https://ko-fi.com/{}",
    "BuyMeACoffee":"https://www.buymeacoffee.com/{}",
    "OpenSea":"https://opensea.io/{}",
    "TradingView":"https://www.tradingview.com/u/{}",
    "Binance":"https://www.binance.com/en/user/{}",
    "CoinMarketCap":"https://coinmarketcap.com/community/profile/{}",
    "WordPress":"https://{}.wordpress.com",
    "Blogger":"https://{}.blogspot.com",
    "Medium":"https://medium.com/@{}",
    "Ghost":"https://{}.ghost.io",
    "Trello":"https://trello.com/{}",
    "Asana":"https://app.asana.com/0/{}",
    "Notion":"https://www.notion.so/{}",
    "Slack":"https://{}.slack.com",
    "Discord":"https://discord.com/users/{}",
    "Zoom":"https://zoom.us/profile/{}",
    "Strava":"https://www.strava.com/athletes/{}",
    "MyFitnessPal":"https://www.myfitnesspal.com/profile/{}",
    "Garmin":"https://connect.garmin.com/modern/profile/{}",
    "Goodreads":"https://www.goodreads.com/{}",
    "MyAnimeList":"https://myanimelist.net/profile/{}",
    "AniList":"https://anilist.co/user/{}",
    "ComicVine":"https://comicvine.gamespot.com/profile/{}",
    "Gravatar":"https://en.gravatar.com/{}",
    "Keybase":"https://keybase.io/{}",
    "About.me":"https://about.me/{}",
    "Pastebin":"https://pastebin.com/u/{}",
    "Imgur":"https://imgur.com/user/{}",
    "Linktree":"https://linktr.ee/{}",
    "SlideShare":"https://www.slideshare.net/{}",
    "Issuu":"https://issuu.com/{}",
    "ReverbNation":"https://www.reverbnation.com/{}",
    "TripAdvisor":"https://www.tripadvisor.com/members/{}",
    "PinterestBoards":"https://www.pinterest.com/{}/",

}

def pause():
    input("\nPress")


def clear():
    os.system("cls" if os.name == "nt" else "clear")

async def check(session, sem, site, url, username):
    async with sem:
        full_url = url.replace("{}", username)

        try:
            async with session.get(full_url, timeout=TIMEOUT) as r:
                text = await r.text()
                text_lower = text.lower()

                if r.status == 200:

                    if username.lower() in text_lower:
                        print(f"[+] FOUND -> {site}")
                        return site, full_url
                    
                    if any(x in text_lower for x in NEGATIVE):
                        print(f"[-] NOT FOUND -> {site}")
                        return None

                    print(f"[?] UNKNOWN -> {site}")
                    return None

                print(f"[!] STATUS {r.status} -> {site}")

        except asyncio.TimeoutError:
            print(f"[!] TIMEOUT -> {site}")
        except:
            print(f"[!] ERROR -> {site}")

        return None

async def run(username):
    connector = aiohttp.TCPConnector(limit=CONCURRENT)
    sem = asyncio.Semaphore(CONCURRENT)

    async with aiohttp.ClientSession(headers=HEADERS, connector=connector) as session:
        tasks = [
            check(session, sem, site, url, username)
            for site, url in SITES.items()
        ]

        results = await asyncio.gather(*tasks)
        return [r for r in results if r]


def banner():
    clear()
    print("""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣶⣿⣿⣿⣿⣿⣶⡀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠆       Osint - Usernames check
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣽⣿⣿⣿⣿⣿⣿⣿⡟⠀            s By Rorz X Offset
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⡿⠁
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣾⢻⣿⣿⣿⣿⣿⣿⡀
⠀⠀⠀⠀⢀⣠⣤⣴⣾⣿⣿⣿⠛⠀⠙⡿⠟⠋⠀⣿⣿⣦⣄⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⡟⠀⣰⣿⣿⣆⠀⢰⣿⣿⣿⣿⣿⣷⣶⣄⡀⠀⠀
⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⣰⣿⣷⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⠀
⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⢰⣿⣿⣿⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀
⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⣿⣿⣿⣿⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇     ⠀⠀⠀⠀⠀⠀
""")

def main():
    banner()

    username = input("[👤] Username > ").strip()

    print("\n[-] Scanning...\n")

    results = asyncio.run(run(username))

    print("\nResultat :\n")

    for site, link in results:
        print(f"{site} -> {link}")

    print(f"\nTotal : {len(results)}")

    # option ouverture navigateur
    if results:
        open_choice = input("\nOpen all profils ? (y/n): ").lower()
        if open_choice == 'y':
            for _, link in results:
                webbrowser.open(link)



if __name__ == "__main__":
    main()