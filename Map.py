
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
        self.carte = [['.' for _ in range(largeur)] for _ in range(hauteur)] #gpt : premier tableau affiche . le nombre de fois = largeur et la valeur _ après le for = la largeur aussi prend

    #on affiche la carte
    def Afficher_carte(self) :
        # Afficher les lettres de l'alphabet comme libellés de colonnes
        lettres = ' ' + ' '.join([chr(65 + col) for col in range(self.largeur)])
        print('  ' + lettres)  # Ajout d'un espace pour l'alignement

        # Afficher la carte
        for i, ligne in enumerate(self.carte): #gpt
            print(str(i + 1).zfill(2) + ' ' + ' '.join(ligne))
            
        # Retourner la première et la dernière colonne, ainsi que la première et la dernière ligne (gpt)
        derniere_colonne = chr(65 + self.largeur - 1)
        derniere_ligne = str(self.hauteur)
        
        return derniere_colonne, derniere_ligne
    
    #on place le sous marin
    def placer_sous_marin(self, position, sous_marin):
        
        x, y = position
        self.carte[x][y] = sous_marin.nom[0]   #le sous marin est signaler par la première valeur de son nom.
        y_l = chiffre_to_lettre(y)
        
        print("\n-> Sous-marin placer en : ", y_l ,x+1, "\n")
        
        self.Afficher_carte()
        
        return x, y


    def reset_chemin(self):        
        for i in range(self.hauteur) :
            for j in range(self.largeur) :
                if self.carte[i][j] in ['—', '|']:
                    self.carte[i][j] = "."
        
        self.Afficher_carte()

    #on déplace le sous marin
    def deplacement_sm(self, position, sous_marin, cap, capitaine, carte):
        from Debut_jeu import annonce_cap
        
        x, y = position
        cap = cap.upper()
        h = int(self.hauteur) - 1
        l = int(self.largeur) - 1

        if cap == "OUEST" and x > 0:
            if self.carte[x][y-1] == "." :
                self.carte[x][y] = "—"
                y -= 1
                self.carte[x][y] = sous_marin.nom[0]
                print("\nVoici votre nouvel emplacement : \n")
                self.Afficher_carte()
                return x, y #nouvelle position
            else : 
                print("\nLa nouvelle position n'est pas valide, vous ne pouvez vous déplacer que sur les '.'")
                input("\nSUIVANT")
                return x, y

        elif cap == "EST" and x < l :
            if self.carte[x][y+1] == "." :
                self.carte[x][y] = "—"
                y += 1
                self.carte[x][y] = sous_marin.nom[0]
                print("\nVoici votre nouvel emplacement : \n")
                self.Afficher_carte()
                return x, y #nouvelle position
            else : 
                print("\nLa nouvelle position n'est pas valide, vous ne pouvez vous déplacer que sur les '.'")
                input("\nSUIVANT")
                return x, y

        elif cap == "NORD" and y > 0:
            if self.carte[x-1][y] == "." :
                self.carte[x][y] = "|" 
                x -= 1   
                self.carte[x][y] = sous_marin.nom[0]
                print("\nVoici votre nouvel emplacement : \n")
                self.Afficher_carte()
                return x, y #nouvelle position
            else : 
                print("\nLa nouvelle position n'est pas valide, vous ne pouvez vous déplacer que sur les '.'")
                input("\nSUIVANT")
                return x, y

        elif cap == "SUD" and y < h :
            if self.carte[x+1][y] == "." :
                self.carte[x][y] = "|"
                x += 1
                self.carte[x][y] = sous_marin.nom[0]
                print("\nVoici votre nouvel emplacement : \n")
                self.Afficher_carte()
                return x, y #nouvelle position
            else : 
                print("\nLa nouvelle position n'est pas valide, vous ne pouvez vous déplacer que sur les '.'")
                input("\nSUIVANT")
                return x, y

        else:
            print("Déplacement invalide. Veuillez choisir un cap valide.")
            annonce_cap(position, capitaine, carte, sous_marin) #si erreur de déplacement (en dehors de la map ou sur une île) alors on redemande le cap
            return x, y

    #on place le premier cap sur le transparent
    def start_trans(self, cap, position):
        x, y = position #la première valeur place le sous marin de colonne, la deuxième de ligne
        self.carte[x][y] = "X"   #le sous marin est signaler par la première valeur de son nom.
        y_l = chiffre_to_lettre(y)
        
        print("\n-> Premier cap ennemie placer en : ", y_l ,x+1, "\n")
        
        self.Afficher_carte()
        
        return x, y

    #rentrer un cap sur le transparent.
    def continuer_trans(self, cap, position):
        x, y = position

        if cap == "NORD" or cap == "SUD":
            self.carte[x][y] = "|"

        elif cap == "EST" or cap == "OUEST":
            self.carte[x][y] = "—"

        else:
            print("Cap invalide.")


    def infos(self):
        print(f"\n========== Map {self.nom} ==========\n\n- Difficulté : {self.difficulte}\n- Largeur : {self.largeur}\n- Longeur : {self.hauteur}\n- Terrain : {self.terrain}\n")


#=======================#
'''Création des cartes'''
#=======================#

C1_e1 = Carte("Mer Noir", 15, 15, 1, "Vide") #Carte mer noir de l'équipe numéro 1
C1_e1_d1 = Carte("Transparent Mer Noir", 15, 15, 1, "Vide") #Carte transparent mer noir équipe

C1_e2 = Carte("Mer Noir", 15, 15, 1, "Vide") #Carte mer noir de l'équipe numéro 2
C1_e2_d2 = Carte("Transparent Mer Noir", 15, 15, 1, "Vide") #Carte transparent mer noir équipe 2

C2_e1 = Carte("Mer Rouge", 15, 15, 2, "île") #Carte numéro 2
C2_e1_d1 = Carte("Transparent Mer Rouge", 15, 15, 1, "Vide") #Carte transparent mer rouge équipe 1

C2_e2 = Carte("Mer Rouge", 15, 15, 2, "île") #Carte numéro 2
C2_e2_d2 = Carte("Transparent Mer Rouge", 15, 15, 1, "Vide") #Carte transparent mer rouge équipe 2


#convertie un chiffre en lettre, 0 = A etc...
def chiffre_to_lettre(chiffre):
        return chr(chiffre + ord('A')) #gpt