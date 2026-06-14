import webbrowser
import subprocess
import exifread
import os

def pause():
    input("\nPress any keys to continue... ")


def clear():
    os.system("cls" if os.name == "nt" else "clear")

def extract_exif(image_path):
    with open(image_path, 'rb') as f:
        tags = exifread.process_file(f)
    return tags


def convert_to_degrees(value):
    d = float(value.values[0].num) / float(value.values[0].den)
    m = float(value.values[1].num) / float(value.values[1].den)
    s = float(value.values[2].num) / float(value.values[2].den)
    return d + (m / 60.0) + (s / 3600.0)


def get_gps(exif_data):
    try:
        lat = convert_to_degrees(exif_data["GPS GPSLatitude"])
        lon = convert_to_degrees(exif_data["GPS GPSLongitude"])

        if exif_data.get("GPS GPSLatitudeRef") != "N":
            lat = -lat
        if exif_data.get("GPS GPSLongitudeRef") != "E":
            lon = -lon

        return lat, lon
    except:
        return None


def open_maps(lat, lon):
    print(f"\nOpening maps for: {lat}, {lon}")
    webbrowser.open(f"https://www.google.com/maps?q={lat},{lon}")
    webbrowser.open(f"https://www.openstreetmap.org/?mlat={lat}&mlon={lon}")

choice = input(
    "0 - Return Launcher\n"
    "1 - Stay on the tool\n" \
    "choix 0 OR 1 :"
)

if choice == '0':
    subprocess.run(["python", "menu.py"])
    exit()

clear()
print('''
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣶⣿⣿⣿⣿⣿⣶⡀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠆       Osint - Exif
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣽⣿⣿⣿⣿⣿⣿⣿⡟⠀            By Rorz X Offset
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⡿⠁
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣾⢻⣿⣿⣿⣿⣿⣿⡀
⠀⠀⠀⠀⢀⣠⣤⣴⣾⣿⣿⣿⠛⠀⠙⡿⠟⠋⠀⣿⣿⣦⣄⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⡟⠀⣰⣿⣿⣆⠀⢰⣿⣿⣿⣿⣿⣷⣶⣄⡀⠀⠀
⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⣰⣿⣷⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⠀
⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⢰⣿⣿⣿⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀
⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⣿⣿⣿⣿⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇     
''')

print("""
1 - Photo EXIF
2 - Open StreetMaps
""")

try:
    choix = int(input("choose an Option : "))
except:
    print("invalid Enter")
    exit()

if choix == 1:
    image_path = input("Enter image path: ").strip().strip('"')

    if not os.path.exists(image_path):
        print("! File not found")
        exit()

    exif_data = extract_exif(image_path)

    print(f"\n! Tags found: {len(exif_data)}\n")

    if not exif_data:
        print("[+] No EXIF data (image probably stripped)")
    else:
        for tag in exif_data:
            print(f"{tag}: {exif_data[tag]}")

        gps = get_gps(exif_data)

        if gps:
            lat, lon = gps
            print(f"\nGPS FOUND: {lat}, {lon}")

            open_choice = input("Open in maps? (y/n): ").lower()
            if open_choice == 'y':
                open_maps(lat, lon)
        else:
            print("No GPS data found")

elif choix == 2:
    lat = input("Latitude : ")
    lon = input("Longitude : ")

    try:
        lat = float(lat)
        lon = float(lon)
        open_maps(lat, lon)
    except:
        print("Invalid coordinates")


else:
    print("Invalid Choice")