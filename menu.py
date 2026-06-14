import subprocess
import sys

from utils import clear, get_python

PYTHON = get_python()


def banner():
    clear()
    print("""
                                                                                     
             .@@@@@@@@*.               .:@@@@@@@@@@@@@@@@=.       .*@@@@@@@@@@@@@@@@@@@@:..  
            :@@@@@@@@@@@.             :@@@@@@@@@@@@@@@@@@@@*.     .*@@@@@@@@@@@@@@@@@@@@@@.  
          .*@@@@@@:@@@@@@.           .@@@@@@@=.    ..@@@@@@@*     .*@@@@@@+.      .%@@@@@@=  
         .@@@@@@%. .@@@@@@=         .#@@@@@@+.                    .*@@@@@@+.....:+@@@@@@@@:  
        .@@@@@@*.....@@@@@@%..      .#@@@@@@*                    ..*@@@@@@@@@@@@@@@@@@@@@.   
      .-@@@@@@@@@@@@@@@@@@@@@.       .@@@@@@@%..   .=@@@@@@@-.    .*@@@@@@@@@@@@@@@@@@@@-.   
     .#@@@@@@@@@@@@@@@@@@@@@@@:  +++. .@@@@@@@@@@@@@@@@@@@@-  +++..*@@@@@@+.     .+@@@@@@%.. 
     @@@@@@@.           #@@@@@@* @@@.   .#@@@@@@@@@@@@@@@..  .@@@..*@@@@@@+.      .@@@@@@@.  
                             
                .-*.                           @@                                  
             ...@@@                          .*@@%.                                         
        ..@@@@@@@@@@-.                        #..*:                   .#@@@@##%@@@@@:       
      .=@@*..-@@*@@-@@@-                  .=@.    ..+=.                .*@@%.    .:@@@=    
      @@#.  +@@  @@: .@@@.              .%@     .-@@@@@@@.             .*@@%.      .@@@     
    .*@%. .@@@   @@%. .+@=.            .@@:       :@@%@@@.             .*@@%.      .@@@    
 +**%@@@%@@@@=+**@@@+==*@%.==@        .#@@.     .%@@                   .*@@%.     .@@@*    
 -%@@@@%@@@@++++=+@@@..@@+:@==          @@@%.  .-@@+.                  .=#@@@====%@@@*      
     :@@@@=      .@@@=@@+.             -@@@@:.@@@.  .==.               .*@@%. -@@@.          
     .@@@@-..    .*@@@@:                =@@@@@@@@@@@@@@@#-.    ....    .*@@%.  .@@@-         
   .*@@%.%@@@@@@@@@@@@*.                 .%@@@@@@@@*. .@@@@=   %@@*.   .*@@%.   .@@@#.       
  .#@*-.   ........:@@@                 .*@@@:::..      ....   :--:    .*@@%.    .#@@@     
                    ..*                  .+.                          .@@@@@@-    @@@@@@                                                     
""")


def menu():
    print("Toujours En Dev !")
    print()
    print("[1] - Sherlock Equivalent ")
    print("[2] - Dox.TXT")
    print("[3] - wordlist Generator")
    print("[4] - Analyse d'Image")
    print("[5] - ID creator")
    print("[6] - LookUp")
    print("[0] - Quitter ! ")


def main():
    while True:
        banner()
        menu()
        choice = input("\nChoix > ").strip()

        if choice == "1":
            subprocess.run([PYTHON, "roz.py"])
        elif choice == "2":
            subprocess.run([PYTHON, "Dox.py"])
        elif choice == "3":
            subprocess.run([PYTHON, "worldlistgen.py"])
        elif choice == "4":
            subprocess.run([PYTHON, "image.py"])
        elif choice == "5":
            subprocess.run([PYTHON, "id.py"])
        elif choice == "6":
            subprocess.run([PYTHON, "lookup.py"])
        elif choice == "0":
            break
        else:
            print("Choix invalide")


if __name__ == "__main__":
    main()
