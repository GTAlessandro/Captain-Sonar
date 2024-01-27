
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
        self.carte = [['.' for _ in range(largeur)] for _ in range(hauteur)] #gpt : premier tableau affiche . le nombre de fois = largeur et la valeur _ après le for = la largeur aussi prend

    #on affiche la carte
    def Afficher_carte(self) :
        # Afficher les lettres de l'alphabet comme libellés de colonnes
        lettres = ' ' + ' '.join([chr(65 + col) for col in range(self.largeur)])
        print('  ' + lettres)  # Ajout d'un espace pour l'alignement

        # Diviser la largeur et la hauteur par 2 pour obtenir les coordonnées du milieu
        milieu_largeur = self.largeur // 2
        milieu_hauteur = self.hauteur // 2

        # Afficher la carte en quadrants (GPT 80%)
        for i, ligne in enumerate(self.carte):
            if i == milieu_hauteur:
                # Ajouter une ligne horizontale au milieu de la hauteur
                print(' ' * 2 + '+-' + '-'.join(['-' for _ in range(self.largeur - 1)]) + '-+')

            if i < milieu_hauteur:
                # Afficher la première moitié des lignes
                print(str(i + 1).zfill(2) + '|' + ' '.join(ligne[:milieu_largeur]) + '|' + ' '.join(ligne[milieu_largeur:]))
            else:
                # Afficher la deuxième moitié des lignes
                print(str(i + 1).zfill(2) + '|' + ' '.join(ligne[:milieu_largeur]) + '|' + ' '.join(ligne[milieu_largeur:]))
            
        # Retourner la première et la dernière colonne, ainsi que la première et la dernière ligne (gpt)
        derniere_colonne = chr(65 + self.largeur - 1)
        derniere_ligne = str(self.hauteur)
        
        return derniere_colonne, derniere_ligne
    
    
    def placer_sous_marin(self, position, sous_marin):
        
        x, y = position
        self.carte[x][y] = sous_marin.nom[0]   #le sous marin est signaler par la première valeur de son nom.
        sous_marin.pos = position
        y_l = chiffre_to_lettre(y)
        print("\n-> Sous-marin placé en : ", y_l ,x+1, "\n")
        self.Afficher_carte()
        
        return x, y


    def reset_chemin(self):        
        for i in range(self.hauteur) :
            for j in range(self.largeur) :
                if self.carte[i][j] in ['←', '→', '↑', '↓']:
                    self.carte[i][j] = "."

                if self.carte[i][j] == "M" :
                    self.carte[i][j] = "m"
        
        self.Afficher_carte()

    #on déplace le sous marin
    def deplacement_sm(self, position, sous_marin, cap, emplacement_mines):
        
        x, y = position
        cap = cap.upper()   

        if cap == "OUEST" :
            #l'emplacement avant le déplacement du sm est changer dans la direction du cap
            self.carte[x][y] = "←"

            #si une mine alliée existe sur la case du sm avant le déplacement, on la réaffiche avec un "M" majuscule.
            for i in emplacement_mines :
                if position == i : 
                    self.carte[x][y] = "M"

            #changement de position
            y -= 1
            #la nouvelle position se transforme en la première lettre du sm
            self.carte[x][y] = sous_marin.nom[0]
            #maj de la position du sm
            sous_marin.pos = x, y
            print("\nVoici votre nouvel emplacement : \n")
            self.Afficher_carte()
            return x, y #retour de la nouvelle position

        elif cap == "EST" :
            self.carte[x][y] = "→"

            for i in emplacement_mines :
                if position == i : 
                    self.carte[x][y] = "M"

            y += 1
            self.carte[x][y] = sous_marin.nom[0]
            sous_marin.pos = x, y
            print("\nVoici votre nouvel emplacement : \n")
            self.Afficher_carte()
            return x, y #nouvelle position

        elif cap == "NORD" :
            self.carte[x][y] = "↑"

            for i in emplacement_mines :
                if position == i : 
                    self.carte[x][y] = "M"

            x -= 1   
            self.carte[x][y] = sous_marin.nom[0]
            sous_marin.pos = x, y
            print("\nVoici votre nouvel emplacement : \n")
            self.Afficher_carte()
            return x, y #nouvelle position

        elif cap == "SUD" :
            self.carte[x][y] = "↓"

            for i in emplacement_mines :
                if position == i : 
                    self.carte[x][y] = "M"

            x += 1
            self.carte[x][y] = sous_marin.nom[0]
            sous_marin.pos = x, y
            print("\nVoici votre nouvel emplacement : \n")
            self.Afficher_carte()
            return x, y #nouvelle position

       
    #on place le premier cap sur le transparent
    def start_trans(self):
        self.carte[0][0] = "X"   #le sous marin ennemi est signalé par une croix.
        self.pos_cible = 0, 0
        
        return 0, 0

    #rentrer un cap sur le transparent.
    def continuer_trans(self, cap, position):
        x, y = position

        if cap == "NORD" or cap == "SUD":
            if cap == "NORD" :
                self.carte[x][y] = "↑"
            
            if cap == "SUD" :
                self.carte[x][y] = "↓"
            
            self.pos_cible = x, y
            return x, y

        elif cap == "EST" or cap == "OUEST":
            if cap == "EST" :
                self.carte[x][y] = "→"
            
            if cap == "OUEST" :
                self.carte[x][y] = "←"
            self.pos_cible = x, y
            return x, y

        else:
            print("Cap invalide.")


    def infos(self):
        print(f"\n========== Map {self.nom} ==========\n\n- Difficulté : {self.difficulte}\n- Largeur : {self.largeur}\n- Longeur : {self.hauteur}\n- Terrain : {self.terrain}\n")


#=======================#
'''Création des cartes'''
#=======================#

C1_e1 = Carte("Mer Noir", 16, 16, 1, "Vide", None) #Carte mer noir de l'équipe numéro 1
C1_e1_d1 = Carte("Transparent Mer Noir", 16, 16, 1, "Vide", None) #Carte transparent mer noir équipe

C1_e2 = Carte("Mer Noir", 16, 16, 1, "Vide", None) #Carte mer noir de l'équipe numéro 2
C1_e2_d2 = Carte("Transparent Mer Noir", 16, 16, 1, "Vide", None) #Carte transparent mer noir équipe 2

C2_e1 = Carte("Mer Rouge", 16, 16, 2, "île", None) #Carte numéro 2
C2_e1_d1 = Carte("Transparent Mer Rouge", 16, 16, 1, "Vide", None) #Carte transparent mer rouge équipe 1

C2_e2 = Carte("Mer Rouge", 16, 16, 2, "île", None) #Carte numéro 2
C2_e2_d2 = Carte("Transparent Mer Rouge", 16, 16, 1, "Vide", None) #Carte transparent mer rouge équipe 2


#convertie un chiffre en lettre, 0 = A etc...
def chiffre_to_lettre(chiffre):
        return chr(chiffre + ord('A')) #gpt