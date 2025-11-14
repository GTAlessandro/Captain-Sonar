import os

from Sous_marins import chiffre_to_lettre

#===============#
'''Class Carte'''
#===============#

class Carte :
    def __init__(self, nom, hauteur, largeur, difficulte, terrain) :
        self.nom = nom
        self.hauteur = hauteur
        self.largeur = largeur
        self.difficulte = difficulte
        self.terrain = terrain
        self.pos_cible = 0, 0
        self.derniere_colonne = None
        self.derniere_ligne = None
        self.carte = [['.' for _ in range(largeur)] for _ in range(hauteur)] #gpt : premier tableau affiche . le nombre de fois = largeur et la valeur _ après le for = la largeur aussi prend

    def definition_terrain(self) :
        #Affichage des îles sur la 1ère map :
        if self.terrain == "îles épars" :
            self.carte[0][3] = "■"
            self.carte[2][1] = "■"
            self.carte[1][7] = "■"
            self.carte[3][7] = "■"
            self.carte[5][4] = "■"
            self.carte[6][6] = "■"
            self.carte[8][3] = "■"
            self.carte[8][7] = "■"

        if self.terrain == "grandes îles" :
            self.carte[5][3] = "■"
            self.carte[4][2] = "■"
            self.carte[4][3] = "■"
            self.carte[4][4] = "■"
            self.carte[4][5] = "■"
            self.carte[6][6] = "■"
            self.carte[7][6] = "■"
            self.carte[7][7] = "■"
            self.carte[7][8] = "■"
            self.carte[8][8] = "■"
        
        return 

    #on affiche la carte
    def Afficher_carte(self) :
        # Diviser la largeur et la hauteur par 2 pour obtenir les coordonnées du milieu
        milieu_largeur = self.largeur // 2
        milieu_hauteur = self.hauteur // 2


        # Afficher les lettres de l'alphabet comme libellés de colonnes
        lettres = '  ' + '  '.join([chr(65 + col) for col in range(self.largeur)])
        moitier_lettre = len(lettres) // 2
        lettres = lettres[:moitier_lettre] + " " + lettres[moitier_lettre:]
        print('  ' + lettres)  # Ajout d'un espace pour l'alignement

        print('  ' + '+-' + '-'.join(['-' for _ in range(len(lettres) // 2)]) + '-+')

        # Afficher la carte en quadrants
        for i, ligne in enumerate(self.carte):
            if i == milieu_hauteur:
                # Ajouter une ligne horizontale au milieu de la hauteur
                print(' ' * 2 + '+-' + '-'.join(['-' for _ in range(len(lettres) // 2)]) + '-+')

            if i < milieu_hauteur:
                # Afficher la première moitié des lignes
                print(str(i + 1).zfill(2) + '| ' + '  '.join(ligne[:milieu_largeur]) + ' | ' + '  '.join(ligne[milieu_largeur:])+ ' |')
            else:
                # Afficher la deuxième moitié des lignes
                print(str(i + 1).zfill(2) + '| ' + '  '.join(ligne[:milieu_largeur]) + ' | ' + '  '.join(ligne[milieu_largeur:])+ ' |')
        
        print(' ' * 2 + '+-' + '-'.join(['-' for _ in range(len(lettres) // 2)]) + '-+')

        # Retourner la première et la dernière colonne, ainsi que la première et la dernière ligne (gpt)
        self.derniere_colonne = chr(65 + self.largeur - 1)
        self.derniere_ligne = str(self.hauteur)
        
        return
    
    
    def placer_sous_marin(self, position, sous_marin):
        
        x, y = position
        self.carte[x][y] = sous_marin.nom[0]   #le sous marin est signaler par la première valeur de son nom.
        sous_marin.pos = position
        y_l = chiffre_to_lettre(y)
        print("\n-> Sous-marin placé en : ", y_l , x+1, "\n")
        self.Afficher_carte()
        
        return


    def reset_chemin(self):        
        for i in range(self.hauteur) :
            for j in range(self.largeur) :
                RED = "\033[91m"
                RESET = "\033[0m"
                
                if self.carte[i][j] in ['←', '→', '↑', '↓']:
                    self.carte[i][j] = "."

                if self.carte[i][j] == "M" :
                    self.carte[i][j] = "m"

                if self.carte[i][j] in [f"{RED}←{RESET}", f"{RED}→{RESET}", f"{RED}↑{RESET}", f"{RED}↓{RESET}"] :
                    self.carte[i][j] = "■"
        
        self.Afficher_carte()


    #on déplace le sous marin
    def deplacement_sm(self, sous_marin):
        
        x, y = sous_marin.pos

        if sous_marin.cap == "OUEST" :
            #l'emplacement avant le déplacement du sm est changer dans la direction du cap
            self.carte[x][y] = "←"

            #si une mine alliée existe sur la case du sm avant le déplacement, on la réaffiche avec un "M" majuscule.
            for i in sous_marin.emplacement_mines :
                if sous_marin.pos == i : 
                    self.carte[x][y] = "M"

            #changement de position
            y -= 1

        elif sous_marin.cap == "EST" :
            self.carte[x][y] = "→"

            for i in sous_marin.emplacement_mines :
                if sous_marin.pos == i : 
                    self.carte[x][y] = "M"

            y += 1

        elif sous_marin.cap == "NORD" :
            self.carte[x][y] = "↑"

            for i in sous_marin.emplacement_mines :
                if sous_marin.pos == i : 
                    self.carte[x][y] = "M"

            x -= 1   

        elif sous_marin.cap == "SUD" :
            self.carte[x][y] = "↓"

            for i in sous_marin.emplacement_mines :
                if sous_marin.pos == i : 
                    self.carte[x][y] = "M"

            x += 1
        
        #la nouvelle position se transforme en la première lettre du sm
        self.carte[x][y] = sous_marin.nom[0]
        #maj de la position du sm
        sous_marin.pos = x, y
        clear_terminal() 
        print("\nVoici votre nouvel emplacement : \n")
        self.Afficher_carte()
        return


    #on place la position de la cible définit dans l'initialisation de la map sur le transparent
    def start_trans(self):
        x, y = self.pos_cible
        self.carte[x][y] = "X"   #le sous marin ennemi est signalé par une croix.
        return
    

    #on déplace la cible du transparent
    def cap_cible_transpa(self) :
        h = int(self.hauteur) - 1
        l = int(self.largeur) - 1
        x, y = self.pos_cible

        while True :
            try :
                cap = input(f"\nDéplacer la cible (OUEST, NORD, EST, SUD) ou retourner en arrière (0): ")
                cap = cap.upper()

                if cap == "O" :
                    cap = "OUEST"

                elif cap == "N" :
                    cap = "NORD"

                elif cap == "E" :
                    cap = "EST"

                elif cap == "S" :
                    cap = "SUD"

                #si le cap est égale a ouest et est supérière à 0 étant la limite de la map
                if cap == "OUEST" and y > 0 :
                    #alors on déplace la cible
                    self.deplacement_transpa_valide(cap, x, y)
                    return

                elif cap == "EST" and y < l :
                    self.deplacement_transpa_valide(cap, x, y)
                    return

                elif cap == "NORD" and x > 0 :
                    self.deplacement_transpa_valide(cap, x, y)
                    return

                elif cap == "SUD" and x < h :
                    self.deplacement_transpa_valide(cap, x, y)
                    return

                elif cap == "0" :
                    return

                else :
                    print("\n\n❌ Entrez une valeur valide en restant dans la map !")

            except ValueError :
                print("\n\n❌ Entrez une valeur valide dans les limites de la map.")

    #on déplace la cible sur le transparent, fonction a l'intérieur de cap_cible_transpa
    def deplacement_transpa_valide(self, cap, x, y):
        RED = "\033[91m"
        RESET = "\033[0m"
        XR = f"{RED}X{RESET}"
        
        if cap == "OUEST" :
            #si l'emplacement actuelle de la cible est une X
            if self.carte[x][y] == "X" :
                #l'emplacement actuelle de la cible est changé dans la direction du cap.
                self.carte[x][y] = "←"

            #ou si l'emplacement actuelle de la cible est un X rouge
            elif self.carte[x][y] == XR:
                #l'ancienne emplacement est rouge, indiquant qu'il y a une ile icis
                self.carte[x][y] = f"{RED}←{RESET}"

            #si le nouvelle emplacement est une ile
            if self.carte[x][y - 1] in ["■"] :
                #la nouvelle position de la cible devient X rouge
                self.carte[x][y - 1] = XR

            else :
                self.carte[x][y - 1] = "X"

            #changement de position
            y -= 1

        elif cap == "EST" :
            if self.carte[x][y] in ["X"] :
                self.carte[x][y] = "→"

            #ou si l'emplacement actuelle de la cible est un X rouge
            elif self.carte[x][y] == XR:
                #l'ancienne emplacement est rouge, indiquant qu'il y a une ile icis
                self.carte[x][y] = f"{RED}→{RESET}"

            if self.carte[x][y + 1] in ["■"] :
                self.carte[x][y + 1] = XR

            else :
                self.carte[x][y + 1] = "X"

            y += 1

        elif cap == "NORD" :
            if self.carte[x][y] in ["X"] :
                self.carte[x][y] = "↑"

            #ou si l'emplacement actuelle de la cible est un X rouge
            elif self.carte[x][y] == XR:
                #l'ancienne emplacement est rouge, indiquant qu'il y a une ile icis
                self.carte[x][y] = f"{RED}↑{RESET}"

            if self.carte[x - 1][y] in ["■"] :
                self.carte[x - 1][y] = XR

            else :
                self.carte[x - 1][y] = "X"

            x -= 1   

        elif cap == "SUD" :
            if self.carte[x][y] in ["X"] :
                self.carte[x][y] = "↓"

            #ou si l'emplacement actuelle de la cible est un X rouge
            elif self.carte[x][y] == XR:
                #l'ancienne emplacement est rouge, indiquant qu'il y a une ile icis
                self.carte[x][y] = f"{RED}↓{RESET}"

            if self.carte[x + 1][y] in ["■"] :
                self.carte[x + 1][y] = XR

            else :
                self.carte[x + 1][y] = "X"

            x += 1
            
        clear_terminal() 
        print("\nVoici votre nouvel emplacement : \n")
        self.Afficher_carte()
        self.pos_cible = x, y
        return
    
    #Cette fonctino déplace toute les flèches de la cible du transparent
    def deplacer_all_transpa(self) :
        #demander la direction du déplacement
        h = int(self.hauteur) - 1
        l = int(self.largeur) - 1
        x, y = self.pos_cible
        direction = ""
        tableau_fleche = []
        tableau_ile = []
        tableau_all_fleche = []
        RED = "\033[91m"
        RESET = "\033[0m"

        direction_map = {
            '←': 'O',
            '→': 'E',
            '↑': 'N',
            '↓': 'S'
        }

        red_direction_map = {
            f"{RED}←{RESET}": "O",
            f"{RED}→{RESET}": "E",
            f"{RED}↑{RESET}": "N",
            f"{RED}↓{RESET}": "S"
        }

        for i in range(self.hauteur):
            for j in range(self.largeur):
                # Si il y a une flèche, on met sa position et sa direction dans un tableau
                if self.carte[i][j] in direction_map:
                    direction = direction_map[self.carte[i][j]]
                    tableau_fleche.append([i, j, direction])
                
        for i in range(self.hauteur):
            for j in range(self.largeur):
                # Si il y a une flèche rouge, on met sa position et sa direction dans un tableau spéciale île
                if self.carte[i][j] in red_direction_map:
                    direction = red_direction_map[self.carte[i][j]]
                    tableau_ile.append([i, j, direction])   
                
        tableau_all_fleche = tableau_fleche + tableau_ile

        while True :
            try :
                print("tableau fleche : ", tableau_fleche)
                print("tableau ile  : ", tableau_ile)
                print("tableau all : ", tableau_all_fleche)
                cap = input(f"\nDéplacer le tracé complé de la cible (OUEST, NORD, EST, SUD) ou retourner en arrière (0): ")
                cap = cap.upper()

                if cap == "O" :
                    cap = "OUEST"

                elif cap == "N" :
                    cap = "NORD"

                elif cap == "E" :
                    cap = "EST"

                elif cap == "S" :
                    cap = "SUD"

                #si le cap est égale a ouest, que la cible a une position y supérieur a la limite de la map et que aucune flèche ne sois a la limite aussi. la fonction all regarde pour toute variable du tableau a la position [1] de chaque variable si chacune des variables à une valeur supérieur a la limite de la map
                if cap == "OUEST" and y > 0 and all(j[1] > 0 for j in tableau_fleche): 
                    #on ajoute +1 à chaque j du tableau des flècHes qu'on met dans le new_tableau_fleche
                    for j in tableau_all_fleche :
                        j[1] -= 1 
                    #on supprime chaque ancienne flèche
                    self.reset_chemin()
                    #on affiche sur la map pour chaque valeur du new_tableau_fleche une flèche en fonction de sa direction (étant la variable[2] dans le tableau de tuple tableau_fleche)
                    for var in tableau_all_fleche :
                        if var[2] == "O" :
                            self.carte[var[1]][var[0]] = '←'
                            
                        if var[2] == "E" :
                            self.carte[var[1]][var[0]] = '→'

                        if var[2] == "N" :
                            self.carte[var[1]][var[0]] = '↑'

                        if var[2] == "S" :
                            self.carte[var[1]][var[0]] = '↓'
                    #si une des nouvelles flèches afficher à la même position qu'une ancienne flèche du tableau_ile, alors on l'affiche en rouge.

                    return

                elif cap == "EST" and y < l and all(j[1] < l for j in tableau_fleche):

                    new_tableau_all_fleche = []

                    for j in tableau_all_fleche :
                        new_pos = [j[0], j[1] + 1, j[2]]  # j[1] + 1 pour décaler à l'est
                        new_tableau_all_fleche.append(new_pos)

                    for j in tableau_all_fleche:
                        self.carte[j[1]][j[0]] = '.'

                    print(new_tableau_all_fleche)

                    for var in new_tableau_all_fleche :
                        if var[2] == "O" :
                            print("fleche ouest")
                            self.carte[var[0]][var[1]] = '←'
                            
                        if var[2] == "E" :
                            print("fleche e")
                            self.carte[var[0]][var[1]] = '→'

                        if var[2] == "N" :
                            print("fleche n")
                            self.carte[var[0]][var[1]] = '↑'

                        if var[2] == "S" :
                            print("fleche s")
                            self.carte[var[0]][var[1]] = '↓'

                    self.Afficher_carte()

                    return

                elif cap == "NORD" and x > 0 and all(i[0] > 0 for i in tableau_fleche):
                    for j in tableau_all_fleche :
                        j[0] -= 1 
                    
                    self.reset_chemin()

                    for var in tableau_all_fleche :
                        if var[2] == "O" :
                            self.carte[var[1]][var[0]] = '←'
                            
                        if var[2] == "E" :
                            self.carte[var[1]][var[0]] = '→'

                        if var[2] == "N" :
                            self.carte[var[1]][var[0]] = '↑'

                        if var[2] == "S" :
                            self.carte[var[1]][var[0]] = '↓'
                    return

                elif cap == "SUD" and x < h and all(i[0] < h for i in tableau_fleche):
                    for j in tableau_all_fleche :
                        j[0] += 1 
                    
                    self.reset_chemin()

                    for var in tableau_all_fleche :
                        if var[2] == "O" :
                            self.carte[var[1]][var[0]] = '←'
                            
                        if var[2] == "E" :
                            self.carte[var[1]][var[0]] = '→'

                        if var[2] == "N" :
                            self.carte[var[1]][var[0]] = '↑'

                        if var[2] == "S" :
                            self.carte[var[1]][var[0]] = '↓'
                    return

                elif cap == "0" :
                    return

                else :
                    print("\n\n❌ Entrez une valeur valide en restant dans la map !")

            except ValueError :
                print("\n\n❌ Entrez une valeur valide dans les limites de la map.")
        #déplacer toute les flèches et la cible par rapport a la direction

        
    def infos(self):
        print(f"\n========== Map {self.nom} ==========\n\n- Difficulté : {self.difficulte}\n- Largeur : {self.largeur}\n- Longeur : {self.hauteur}\n- Terrain : {self.terrain}\n")


#=======================#
'''Création des cartes'''
#=======================#

C1_e1 = Carte("Mer Noir", 10, 10, 1, "îles épars") #Carte mer noir de l'équipe numéro 1
C1_e1_d1 = Carte("Transparent Mer Noir", 10, 10, 1, "îles épars") #Carte transparent mer noir équipe

C1_e2 = Carte("Mer Noir", 10, 10, 1, "îles épars") #Carte mer noir de l'équipe numéro 2
C1_e2_d2 = Carte("Transparent Mer Noir", 10, 10, 1, "îles épars") #Carte transparent mer noir équipe 2

C2_e1 = Carte("Mer Rouge", 12, 12, 2, "grandes îles") #Carte numéro 2
C2_e1_d1 = Carte("Transparent Mer Rouge", 16, 16, 2, "grandes îles") #Carte transparent mer rouge équipe 1

C2_e2 = Carte("Mer Rouge", 12, 12, 2, "grandes îles") #Carte numéro 2
C2_e2_d2 = Carte("Transparent Mer Rouge", 16, 16, 2, "grandes îles") #Carte transparent mer rouge équipe 2


def clear_terminal():
    # Pour Windows
    if os.name == 'nt':
        os.system('cls')
    # Pour Unix
    else:
        os.system('clear')