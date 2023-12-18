from Debut_jeu import lancer_jeu
from Var_affichage import bonjour, regles

def menu_principale():

    print(bonjour)
    entry = input("Option choisis : ")

    while True:
        try :

            entry = int(entry)

            if entry == 1 :
                lancer_jeu() # fonction du fichier jeu permettant de lancer le jeu dans Jeu.py
                break

            elif entry == 2 :
                #afficher les règles du jeu
                #code couleur pour les cadrans
                reglesc = regles.replace('DET', '\033[38;5;208mDET\033[0m')\
                                .replace('SPE', '\033[95mSPE\033[0m')\
                                .replace('ARM', '\033[91mARM\033[0m')\
                                .replace('IMPORTANT', '\033[91mIMPORTANT\033[0m')\
                                .replace('JAUNE', '\033[38;5;228mJAUNE\033[0m')\
                                .replace('BLEU', '\033[94mBLEU\033[0m')\
                                .replace('VERT', '\033[92mVERT\033[0m')\
                                .replace('NONE', '\033[38;5;52mNONE\033[0m')\
                                .replace('RAD', '\033[38;5;52mRAD\033[0m')
                                
                print(reglesc)
                input("\nSUIVANT")
                menu_principale()

            elif entry == 3 :
                #afficher paramètre du jeu
                print("3")

            else :
                print("S'il vous plait, entrez une valeur correcte comprise dans les options du menu...")
                input("\nSUIVANT")
                menu_principale()
                
        except ValueError:
            print("S'il vous plait, entrez un chiffre valide compris dans les options du menu...")  
            input("\nSUIVANT")
            menu_principale()



