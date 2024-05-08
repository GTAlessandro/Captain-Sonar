
#===============#
'''Class Carte'''
#===============#

class Carte :
    def __init__(self, nom, hauteur, largeur, difficulte, terrain, pos_cible) :
        self.nom = nom
        self.hauteur = hauteur
        self.largeur = largeur
        self.difficulte = difficulte
        self.terrain = terrain
        self.pos_cible = pos_cible
        self.derniere_colonne = None
        self.derniere_ligne = None
        self.carte = [['.' for _ in range(largeur)] for _ in range(hauteur)] #gpt : premier tableau affiche . le nombre de fois = largeur et la valeur _ après le for = la largeur aussi prend

    #on affiche la carte
    def Afficher_carte(self) :
        # Diviser la largeur et la hauteur par 2 pour obtenir les coordonnées du milieu
        milieu_largeur = self.largeur // 2
        milieu_hauteur = self.hauteur // 2

        #Affichage des îles sur la 1ère map :
        if self.nom == "Mer Noir" or self.nom == "Transparent Mer Noir" :
            self.carte[0][3] = "■"
            self.carte[2][1] = "■"
            self.carte[1][7] = "■"
            self.carte[3][7] = "■"
            self.carte[5][4] = "■"
            self.carte[6][6] = "■"
            self.carte[8][3] = "■"
            self.carte[8][7] = "■"

        if self.nom == "Mer Rouge" or self.nom == "Transparent Mer Rouge" :
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
                if self.carte[i][j] in ['←', '→', '↑', '↓']:
                    self.carte[i][j] = "."

                if self.carte[i][j] == "M" :
                    self.carte[i][j] = "m"
        
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
            #la nouvelle position se transforme en la première lettre du sm
            self.carte[x][y] = sous_marin.nom[0]
            #maj de la position du sm
            sous_marin.pos = x, y
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            print("\nVoici votre nouvel emplacement : \n")
            self.Afficher_carte()
            return x, y #retour de la nouvelle position

        elif sous_marin.cap == "EST" :
            self.carte[x][y] = "→"

            for i in sous_marin.emplacement_mines :
                if sous_marin.pos == i : 
                    self.carte[x][y] = "M"

            y += 1
            self.carte[x][y] = sous_marin.nom[0]
            sous_marin.pos = x, y
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            print("\nVoici votre nouvel emplacement : \n")
            self.Afficher_carte()
            return x, y #nouvelle position

        elif sous_marin.cap == "NORD" :
            self.carte[x][y] = "↑"

            for i in sous_marin.emplacement_mines :
                if sous_marin.pos == i : 
                    self.carte[x][y] = "M"

            x -= 1   
            self.carte[x][y] = sous_marin.nom[0]
            sous_marin.pos = x, y
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            print("\nVoici votre nouvel emplacement : \n")
            self.Afficher_carte()
            return x, y #nouvelle position

        elif sous_marin.cap == "SUD" :
            self.carte[x][y] = "↓"

            for i in sous_marin.emplacement_mines :
                if sous_marin.pos == i : 
                    self.carte[x][y] = "M"

            x += 1
            self.carte[x][y] = sous_marin.nom[0]
            sous_marin.pos = x, y
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            print("\nVoici votre nouvel emplacement : \n")
            self.Afficher_carte()
            return x, y #nouvelle position

       
    #on place le premier cap sur le transparent
    def start_trans(self):
        self.carte[0][0] = "X"   #le sous marin ennemi est signalé par une croix.
        self.pos_cible = 0, 0
        
        return 0, 0

    def infos(self):
        print(f"\n========== Map {self.nom} ==========\n\n- Difficulté : {self.difficulte}\n- Largeur : {self.largeur}\n- Longeur : {self.hauteur}\n- Terrain : {self.terrain}\n")


#=======================#
'''Création des cartes'''
#=======================#

C1_e1 = Carte("Mer Noir", 10, 10, 1, "îles épars", None) #Carte mer noir de l'équipe numéro 1
C1_e1_d1 = Carte("Transparent Mer Noir", 10, 10, 1, "îles épars", None) #Carte transparent mer noir équipe

C1_e2 = Carte("Mer Noir", 10, 10, 1, "île épars", None) #Carte mer noir de l'équipe numéro 2
C1_e2_d2 = Carte("Transparent Mer Noir", 10, 10, 1, "îles épars", None) #Carte transparent mer noir équipe 2

C2_e1 = Carte("Mer Rouge", 12, 12, 2, "grandes îles", None) #Carte numéro 2
C2_e1_d1 = Carte("Transparent Mer Rouge", 16, 16, 2, "grandes îles", None) #Carte transparent mer rouge équipe 1

C2_e2 = Carte("Mer Rouge", 12, 12, 2, "grandes îles", None) #Carte numéro 2
C2_e2_d2 = Carte("Transparent Mer Rouge", 16, 16, 2, "grandes îles", None) #Carte transparent mer rouge équipe 2


#convertie un chiffre en lettre, 0 = A etc...
def chiffre_to_lettre(chiffre):
        return chr(chiffre + ord('A')) #gpt