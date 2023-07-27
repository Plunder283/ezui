from colorama import Back, Fore, Style
from keyboard import is_pressed
from os import system, get_terminal_size
import platform
from time import sleep
import threading

syst = platform.system()

def clear():
    if syst == 'Windows':
        system('cls')
    else:
        system("clear")

def set_default_surbrillance(text):
    t_size = len(text)
    rest = get_terminal_size()[0] - t_size
    return (Back.WHITE + Fore.BLACK + Style.BRIGHT + " " + text + " "*(rest-1) + Back.RESET + Fore.RESET + Style.RESET_ALL)


def simple_menu(elements, custom_banner=None, mode="default"):
    global active
    """Create a simple menu"""
    selection = 0
    last_sel = 0
    items = []
    
    # Gestion du nombre max d'éléments et récuperation des items
    elements_len = len(elements) - 1
    for e in elements:
        items.append(e[0])

    # Fonction pour mettre à jour la frame à l'écran
    def update_frame():
        
        clear()
        # Mettre le titre et les items
        frame = custom_banner + "\n" if custom_banner != None else ""
        for i in items:
            if i != items[selection]:
                frame += i + "\n"
            else:
                if mode == "simple":
                    frame += Back.WHITE + Fore.BLACK + Style.BRIGHT + i + "" + Back.RESET + Fore.RESET + Style.RESET_ALL + "\n"
                else:
                    frame += set_default_surbrillance(i) + "\n"

        # Mettre les aides
        print(frame)

    update_frame()
    size = get_terminal_size()
    last_size = size

    while True:
        
        # Rendre l'affichage dynamique au changement de taille du shell
        if size != last_size:
            last_size = size
            update_frame()
        

        if is_pressed('down'):
            if selection < elements_len:
                selection += 1
            else:
                selection = 0 # Remet en haut de la liste si le bas est atteint

            update_frame()
            sleep(0.2)

        elif is_pressed('up'):
            if selection > 0:
                selection -= 1
            else:
                selection = elements_len # Remet tout en haut

            update_frame()
            sleep(0.2)
        
        elif is_pressed('enter'):
            input() # Ce input sert à handle l'appui sur la touche entré sinon il reste un appui de touche dans le std::cin
            clear()
            elements[selection][1]()
            break
        