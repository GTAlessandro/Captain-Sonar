from Input_Joueur import j1, j2, j3, j4, j5, j6, j7, j8
from Map import Carte, C1_e1, C2_e1, C1_e2, C2_e2, C2_e1_d1, C2_e2_d2, C1_e1_d1, C1_e2_d2
from Sous_marins import SousMarin, Leurre
from Var_affichage import equipe, affichage_mode, aff_map, aff_s, start, changement


# Lancement du jeu
def lancer_jeu() :
    
    print(equipe)

    #1) définition du nombre de joueurs
    nb_joueur, nom_e1, nom_e2 = entre_nombre_joueur()

    #2) distribution des rôles pour les joueurs.
    capitaine, second, mecano, detecteur = distribution_role(j1, j2, j3, j4, j5, j6, j7, j8, nb_joueur) #variable des rôles
    
    print(affichage_mode)

    #3) Sélection du mode de jeu
    mode = selection_mode(j1) #variable mode de jeu

    print(aff_map)

    #4) Selection de la map
    carte = selection_map(j1)

    #Définition des cartes
    C_e1 = carte[0] 
    C_e2 = carte[1]
    C_e1_d1 = carte[2]
    C_e2_d2 = carte[3]

    # #initialisation des positions sm ennemies sur le transparent
    # position_sm_d1 = C_e1_d1.start_trans()
    # position_sm_d2 = C_e2_d2.start_trans()

    print(aff_s)

    #5) Selection des sous-marins
    sous_marin_e1, sous_marin_e2 = selection_sous_marins(capitaine, second, mecano, detecteur)

    #if sm = écureille alors créé un leur !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    print(start)

    #6) 1ere équipe plonge
    plongerT(C_e1, sous_marin_e1, nom_e1)

    print(changement)

    #7) 2ème équipe plonge
    plongerT(C_e2, sous_marin_e2, nom_e2)

    #initialisation des cadrans des sous-marins
    sous_marin_e1.definition_du_cadran()
    sous_marin_e2.definition_du_cadran()

    #si fin == True alors le jeu est terminer 
    fin = False

    #condition pour que le tour e1 et e2 sois finito
    fin_tour_e1 = False
    fin_tour_e2 = False
    
    #condition de surface du sm
    surface_e1 = False
    surface_e2 = False

    #nombre de tour que le sm attend avant de pouvoir replonger
    nombre_tour_attendu_e1 = 0
    nombre_tour_attendu_e2 = 0

    #============================================================================================#
    '''=====================================DEBUT BOUCLE======================================='''
    #============================================================================================#

    while fin == False :
        while fin_tour_e1 == False :
            #============#
            '''EQUIPE 1'''
            #============#
            print(changement)
            print(f"\n⚠⚠⚠ Attention ⚠⚠⚠ : \nC'est au capitaine : '{sous_marin_e1.capitaine}', de l'équipe '{nom_e1}' de jouer.")
            input("\nSUIVANT\n")
            #1) le capitaine de l'équipe 1 déplace son vaisseau
            cap_e1, surface_e1, nombre_tour_attendu_e1, fin = deplacement(C_e1, sous_marin_e1, nom_e1, surface_e1, nombre_tour_attendu_e1, sous_marin_e2, fin, C_e2)
            
            #2) le mecano de l'équipe 1 rentre une panne dans le cadran associer au cap
            panne(cap_e1, nom_e1, sous_marin_e1, surface_e1, nombre_tour_attendu_e1)
            
            #3) le second de l'équipe 1 augmente la jauge d'un système
            choix_systeme(sous_marin_e1, nom_e1, cap_e1, nombre_tour_attendu_e1, surface_e1)
            
            #4) l'équipe 1 peut déclencher une compétence
            surface_e1, nombre_tour_attendu_e1, fin = declenchement_systemes(sous_marin_e1, sous_marin_e2, C_e1, nom_e2, nom_e1, fin, C_e2, nombre_tour_attendu_e1, surface_e1)
            #modifier les cadrans !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            #5) le detecteur adverse rentre le cap ennemi
            
    print(fin)
    print("BRAVO JEU FINI")



#======================================#
'''1) Définition du nombre de joueurs'''
#======================================#

def entre_nombre_joueur():
    
    while True :
        try:
            nb_joueur = int(input("Entrer le nombre de joueurs (2-8) : "))

            if 2 <= nb_joueur <= 8 :
                nom_e1, nom_e2 = def_ekip(nb_joueur) #définition des équipes
                return nb_joueur, nom_e1, nom_e2 

            else :
                print("\n\n❌ Le nombre de joueurs doit être compris entre 2 et 8, recommencez.")

        except ValueError :
            print("\n\n❌ Veuillez rentrer un chiffre valide compris entre 2 et 8, recommencez.")



#=============================#
'''2) Définition des équipes'''
#=============================#

# Définition des équipe (attribution des variables joueurs et nom d'équipe en fonction du nombre totale de joueur)
def def_ekip(nb_joueur):
    
    global j1, j2, j3, j4, j5, j6, j7, j8

    # Partie a 2 joueurs 
    if nb_joueur == 2 :
        print("\n-> Chaque équipe ne comporte qu'un joueur.\nCe joueur cumule tous les rôles.\n")

        #Définition équipe 1
        j1 = input("Joueur 1, veuillez rentrer votre nom : ")
        nom_e1 = input(f"{j1}, veuillez rentrer le nom de votre équipe : ")

        #Définition équipe 2
        j2 = input("\nJoueur 2, veuillez rentrer votre nom : ")
        nom_e2 = input(f"{j2}, veuillez rentrer le nom de votre équipe : ")

        #Récapitulatif
        print(f"\n\n\n-> Récapitulatif : \n\n===== EQUIPE {nom_e1} =====\nCapitaine, Second, Mécano et Détecteur : {j1}\n\n===== EQUIPE {nom_e2} =====\nCapitaine, Second, Mécano et Détecteur : {j2}\n")
        input("\nSUIVANT")


    # Partie a 3 joueurs 
    elif nb_joueur == 3 :
        print("\n-> Une équipe comporte un membre, l'autre deux.\nL'équipe composé d'un joueur cumule tous les rôles. \nPour l'autre équipe, un joueur cumule le rôle de Capitaine, de Second et de Mécano.\n")
        
        #Définition équipe 1
        j1 = input("Joueur 1, vous serez seul contre deux ennemis. Veuillez rentrer votre nom : ")
        nom_e1 = input(f"{j1}, veuillez rentrer le nom de votre équipe : ")
        
        #Définition équipe 2
        j2 = input("\n\nJoueur 2, vous cumulerez le rôle de Capitaine, de Second et de Mécano dans votre équipe. Veuillez rentrer votre nom : ")
        nom_e2 = input(f"{j2}, veuillez rentrer le nom de votre équipe : ")
        j3 = input(f"Joueur 3, vous faites partie de l'équipe '{nom_e2}', vous serez le détecteur à bord. Veuillez rentrer votre nom : ")

        #Récapitulatif
        print(f"\n\n\n-> Récapitulatif : \n\n===== EQUIPE {nom_e1} =====\nCapitaine, Second, Mécano et Détecteur : {j1}\n\n===== EQUIPE {nom_e2} =====\nCapitaine, Second et Mécano : {j2}\nDétecteur : {j3}\n")
        input("\nSUIVANT")


    # Partie a 4 joueurs 
    elif nb_joueur == 4 :
        print("\n-> Chaque équipe comporte 2 membres.\nPour les deux équipes, un joueur cumule le rôle de Capitaine, de Second et de Mécano.\n")
    
        #Définition équipe 1
        j1 = input("\nJoueur 1, vous cumulerez le rôle de Capitaine, de Second et de Mécano dans votre équipe. Veuillez rentrer votre nom : ")
        nom_e1 = input(f"{j1}, veuillez rentrer le nom de votre équipe : ")
        j2 = input(f"Joueur 2, vous faites partie de l'équipe '{nom_e1}', vous serez le détecteur à bord. Veuillez rentrer votre nom : ")
        
        #Définition équipe 2
        j3 = input("\n\nJoueur 3, vous cumulerez le rôle de Capitaine, de Second et de Mécano dans votre équipe. Veuillez rentrer votre nom : ")
        nom_e2 = input(f"{j3}, veuillez rentrer le nom de votre équipe :")
        j4 = input(f"Joueur 4, vous faites partie de l'équipe '{nom_e2}', vous serez le détecteur à bord. Veuillez rentrer votre nom : ")

        #Récapitulatif
        print(f"\n\n\n-> Récapitulatif : \n\n===== EQUIPE {nom_e1} =====\nCapitaine, Second et Mécano : {j1}\nDétecteur : {j2}\n\n===== EQUIPE {nom_e2} =====\nCapitaine, Second et Mécano : {j3}\nDétecteur : {j4}\n")
        input("\nSUIVANT")


    # Partie a 5 joueurs 
    elif nb_joueur == 5 :
        print("\n-> Une équipe comporte deux membres, l'autre trois.\nPour l'équipe composé de 2 joueurs, un joueur cumule le rôle de Capitaine, de Second et de Mécano.\nPour l'autre équipe, un joueur cumule le rôle de Capitaine et de Second.\n")
    
        #Définition équipe 1
        j1 = input("\nJoueur 1, vous cumulerez le rôle de Capitaine, de Second et de Mécano dans votre équipe. Veuillez rentrer votre nom : ")
        nom_e1 = input(f"{j1}, veuillez rentrer le nom de votre équipe : ")
        j2 = input(f"Joueur 2, vous faites partie de l'équipe '{nom_e1}', vous serez le détecteur à bord. Veuillez rentrer votre nom : ")
        
        #Définition équipe 2
        j3 = input("\n\nJoueur 3, vous cumulerez le rôle de Capitaine et de Second dans votre équipe. Veuillez rentrer votre nom : ")
        nom_e2 = input(f"{j3}, veuillez rentrer le nom de votre équipe : ")
        j4 = input(f"Joueur 4, vous faites partie de l'équipe '{nom_e2}', vous serez le Mécano à bord. Veuillez rentrer votre nom : ")
        j5 = input(f"Joueur 5, vous faites partie de l'équipe '{nom_e2}', vous serez le Détecteur à bord. Veuillez rentrer votre nom : ")

        #Récapitulatif
        print(f"\n\n\n-> Récapitulatif : \n\n===== EQUIPE {nom_e1} =====\nCapitaine, Second et Mécano : {j1}\nDétecteur : {j2}\n\n===== EQUIPE {nom_e2} =====\nCapitaine et Second : {j3}\nMécano : {j4}\nDétecteur : {j5}")
        input("\nSUIVANT")

    # Partie a 6 joueurs 
    elif nb_joueur == 6 :
        print("\n-> Chaque équipe comporte 3 membres.\nPour les deux équipes, un joueur cumule le rôle de Capitaine et de Second.\n")
        
        #Définition équipe 1
        j1 = input("\nJoueur 1, vous cumulerez le rôle de Capitaine et de Second dans votre équipe. Veuillez rentrer votre nom : ")
        nom_e1 = input(f"{j1}, veuillez rentrer le nom de votre équipe : ")
        j2 = input(f"Joueur 2, vous faites partie de l'équipe '{nom_e1}', vous serez le Mécano à bord. Veuillez rentrer votre nom : ")
        j3 = input(f"Joueur 3, vous faites partie de l'équipe '{nom_e1}', vous serez le Détecteur à bord. Veuillez rentrer votre nom : ")
        
        #Définition équipe 2
        j4 = input("\n\nJoueur 4, vous cumulerez le rôle de Capitaine et de Second dans votre équipe. Veuillez rentrer votre nom : ")
        nom_e2 = input(f"{j4}, veuillez rentrer le nom de votre équipe : ")
        j5 = input(f"Joueur 5, vous faites partie de l'équipe '{nom_e2}', vous serez le Mécano à bord. Veuillez rentrer votre nom : ")
        j6 = input(f"Joueur 6, vous faites partie de l'équipe '{nom_e2}', vous serez le Détecteur à bord. Veuillez rentrer votre nom : ")

        #Récapitulatif
        print(f"\n\n\n-> Récapitulatif : \n\n===== EQUIPE {nom_e1} =====\nCapitaine et Second : {j1}\nMécano : {j2}\nDétecteur : {j3}\n\n===== EQUIPE {nom_e2} =====\nCapitaine et Second : {j4}\nMécano : {j5}\nDétecteur : {j6}")
        input("\nSUIVANT")

    # Partie a 7 joueurs 
    elif nb_joueur == 7 :
        print("\n-> Une équipe comporte trois membres, l'autre quatres.\nPour l'équipe composé de 3 joueurs, un joueur cumule le rôle de Capitaine et de Second.\nPour l'autre équipe, chaque joueur possède son propre rôle.\n")
    
        #Définition équipe 1
        j1 = input("\nJoueur 1, vous cumulerez le rôle de Capitaine et de Second dans votre équipe. Veuillez rentrer votre nom : ")
        nom_e1 = input(f"{j1}, veuillez rentrer le nom de votre équipe : ")
        j2 = input(f"Joueur 2, vous faites partie de l'équipe '{nom_e1}', vous serez le Mécano à bord. Veuillez rentrer votre nom : ")
        j3 = input(f"Joueur 3, vous faites partie de l'équipe '{nom_e1}', vous serez le Détecteur à bord. Veuillez rentrer votre nom : ")
        
        #Définition équipe 2
        j4 = input("\n\nJoueur 4, vous êtes le Capitaine de votre équipe. Veuillez rentrer votre nom : ")
        nom_e2 = input(f"{j4}, veuillez rentrer le nom de votre équipe : ")
        j5 = input(f"Joueur 5, vous faites partie de l'équipe '{nom_e2}', vous serez le Second à bord. Veuillez rentrer votre nom : ")
        j6 = input(f"Joueur 6, vous faites partie de l'équipe '{nom_e2}', vous serez le Mécano à bord. Veuillez rentrer votre nom : ")
        j7 = input(f"Joueur 7, vous faites partie de l'équipe '{nom_e2}', vous serez le Détecteur à bord. Veuillez rentrer votre nom : ")
        
        #Récapitulatif
        print(f"\n\n\n-> Récapitulatif : \n\n===== EQUIPE {nom_e1} =====\nCapitaine et Second : {j1}\nMécano : {j2}\nDétecteur : {j3}\n\n===== EQUIPE {nom_e2} =====\nCapitaine :{j4}\nSecond : {j5}\nMécano : {j6}\nDétecteur : {j7}")
        input("\nSUIVANT")

    # Partie a 8 joueurs 
    elif nb_joueur == 8 :
        print("\n-> Parfait, chaque équipe comporte 4 membres. Un pour chaque rôle\n")

        #Définition équipe 1
        j1 = input("\nJoueur 1, vous êtes le Capitaine de votre équipe. Veuillez rentrer votre nom : ")
        nom_e1 = input(f"{j1}, veuillez rentrer le nom de votre équipe : ")
        j2 = input(f"Joueur 2, vous faites partie de l'équipe '{nom_e1}', vous serez le Second à bord. Veuillez rentrer votre nom : ")
        j3 = input(f"Joueur 3, vous faites partie de l'équipe '{nom_e1}', vous serez le Mécano à bord. Veuillez rentrer votre nom : ")
        j4 = input(f"Joueur 4, vous faites partie de l'équipe '{nom_e1}', vous serez le Détecteur à bord. Veuillez rentrer votre nom : ")
        
        #Définition équipe 2
        j5 = input("\n\nJoueur 5, vous êtes le Capitaine de votre équipe. Veuillez rentrer votre nom : ")
        nom_e2 = input(f"{j5}, veuillez rentrer le nom de votre équipe : ")
        j6 = input(f"Joueur 6, vous faites partie de l'équipe '{nom_e2}', vous serez le Second à bord. Veuillez rentrer votre nom : ")
        j7 = input(f"Joueur 7, vous faites partie de l'équipe '{nom_e2}', vous serez le Mécano à bord. Veuillez rentrer votre nom : ")
        j8 = input(f"Joueur 8, vous faites partie de l'équipe '{nom_e2}', vous serez le Détecteur à bord. Veuillez rentrer votre nom : ")
        
        #Récapitulatif
        print(f"\n\n\n-> Récapitulatif : \n\n===== EQUIPE {nom_e1} =====\nCapitaine : {j1}\nSecond : {j2}\nMécano : {j3}\nDétecteur : {j4}\n\n===== EQUIPE {nom_e2} =====\nCapitaine : {j5}\nSecond : {j6}\nMécano : {j7}\nDétecteur : {j8}")
        input("\nSUIVANT")

    return nom_e1, nom_e2



#=============================#
'''3) Distribution des roles'''
#=============================#

def distribution_role(j1, j2, j3, j4, j5, j6, j7, j8, nb_joueur):
    
    if nb_joueur == 2 :
        capitaine = [j1, j2]
        second = [j1, j2]
        mecano = [j1, j2]
        detecteur = [j1, j2]
        return capitaine, second, mecano, detecteur


    elif nb_joueur == 3 :
        capitaine = [j1, j2]
        second = [j1, j2]
        mecano = [j1, j2]
        detecteur = [j1, j3]
        return capitaine, second, mecano, detecteur

    elif nb_joueur == 4 :
        capitaine = [j1, j3]
        second = [j1, j3]
        mecano = [j1, j3]
        detecteur = [j2, j4]
        return capitaine, second, mecano, detecteur

    elif nb_joueur == 5 :
        capitaine = [j1, j3]
        second = [j1, j3]
        mecano = [j1, j4]
        detecteur = [j2, j5]
        return capitaine, second, mecano, detecteur

    elif nb_joueur == 6 :
        capitaine = [j1, j4]
        second = [j1, j4]
        mecano = [j2, j5]
        detecteur = [j3, j6]
        return capitaine, second, mecano, detecteur

    elif nb_joueur == 7 :
        capitaine = [j1, j4]
        second = [j1, j5]
        mecano = [j2, j6]
        detecteur = [j3, j7]
        return capitaine, second, mecano, detecteur

    elif nb_joueur == 8 :
        capitaine = [j1, j5]
        second = [j2, j6]
        mecano = [j3, j7]
        detecteur = [j4, j8]
        
        return capitaine, second, mecano, detecteur



#=============================#
'''4) Choix du mode de jeu'''
#=============================#

def selection_mode(j1):

    while True :
        try :
            mode = int(input(f"{j1}, veuillez selectionner le mode de jeu : "))

            if mode == 1 :
                print("\nVous avez sélectionner le mode de jeu : 'Tour par tour'")
                return mode
            
            elif mode == 2 :
                print("\nCette option n'est pas encore disponible, veuillez sélectionner le mode tour par tour.")
            
            else :
                print("\n\n❌ Veuillez sélectionner une option valide.")

        except ValueError :
            print("\n\n❌ Entrez un mode de jeu valide (1 ou 2).")



#======================#
'''5) Choix de la map'''
#======================#

def selection_map(j1) :
    
    #pool des cartes dispo
    cartes_disponibles = {
        1: [C1_e1, C1_e2, C1_e1_d1, C1_e2_d2],
        2: [C2_e1, C2_e2, C2_e1_d1, C2_e2_d2]
    }

    while True :
        try :
            choix = int(input(f"{j1}, sélectionnez la carte du jeu : "))

            if choix in cartes_disponibles:
                carte = cartes_disponibles[choix]
                print(f"\nVous avez sélectionné la carte {carte[0].nom} :")
                carte[0].Afficher_carte()
                input("\nSUIVANT")
                return carte

            else :
                print("\n\n❌ Veuillez entrée une carte existante.")
                
        except ValueError :
            print("\n\n❌ Veuillez entrée une carte valide.")



#================================#
'''6) Sélection des sous-marins'''
#================================#

def selection_sous_marins(capitaine, second, mecano, detecteur) :

    sous_marin_e1 = None
    sous_marin_e2 = None

    while sous_marin_e1 is None:
        try:
            choix_e1 = int(input(f"{capitaine[0]}, sélectionnez votre sous-marin : "))

            if choix_e1 == 1 :
                sous_marin_e1 = SousMarin(capitaine[0], second[0], mecano[0], detecteur[0], "Tigre", 4, 1)
                break

            elif choix_e1 == 2 :
                sous_marin_e1 = SousMarin(capitaine[0], second[0], mecano[0], detecteur[0], "Ecureille", 3, 1)
                break

            else:
                print("\n\n❌ Veuillez choisir un sous-marin afficher.")

        except ValueError:
            print("\n\n❌ Veuillez choisir un sous-marin valide.")

    while sous_marin_e2 is None:
        try:
            choix_e2 = int(input(f"\n{capitaine[1]}, sélectionnez votre sous-marin : "))
            
            if choix_e2 == 1 :
                sous_marin_e2 = SousMarin(capitaine[1], second[1], mecano[1], detecteur[1], "Tigre", 4, 1)

            elif choix_e2 == 2 :
                sous_marin_e2 = SousMarin(capitaine[1], second[1], mecano[1], detecteur[1], "Ecureille", 3, 1)

            else:
                print("\n\n❌ Veuillez choisir un sous-marin valide (1-2).")

        except ValueError:
            print("\n\n❌ Veuillez choisir un sous-marin valide (1-2).")

    return sous_marin_e1, sous_marin_e2


#============================#
'''7) Placer son sous marin'''
#============================#

#convertire une lettre en chiffre, A = 0, B = 1 etc ...
def lettre_to_chiffre(lettre):
    return ord(lettre.upper()) - ord('A')

def traiter_entree(entree):
    if len(entree) < 2:
        return 1  # Si l'entrée est trop courte, retourne 1

    lettre = entree[0].upper()  # Première lettre de l'entrée
    nombre_str = entree[1:]  # Le reste de l'entrée

    if not lettre.isalpha() :
        return 2 # Si la lettre n'est pas une lettre 

    if not nombre_str.isdigit() :
        return 3  #si le nombre n'est pas un nombre

    nombre = int(nombre_str) - 1  # Convertit le nombre en entier
    position = [lettre, nombre]
    return position

def plongerT(carte, sous_marin, nom_e):

    print(f"⚠⚠⚠ Attention ⚠⚠⚠ : c'est à l'équipe '{nom_e}' de jouer.\n")
    print(f"Capitaine '{sous_marin.capitaine}' de l'équipe '{nom_e}', plongez ! ")

    carte.Afficher_carte()

    while True :
        try :
            yx = input("Entrez une position (par exemple A3) : ")
            position = traiter_entree(yx)

            if position != 1 :
                if position != 2 :
                    if position != 3 :
                        y = lettre_to_chiffre(position[0])
                        x = position[1]

                        if 0 <= y <= ord(carte.derniere_colonne) - ord('A') and 0 <= x <= int(carte.derniere_ligne) - 1 :
                            if carte.carte[x][y] == "." :
                                carte.placer_sous_marin((x,y), sous_marin)
                                input("\nSUIVANT")
                                return

                            else : 
                                print("\n\n❌ Vous ne pouvez pas plonger sur une île.")

                        else : 
                            print("\n\n❌ Entrer des coordonnées comprisent dans les limites de la map.")

                    else :
                        print("\n\n❌ Entrée une ligne correcte.")

                else :
                    print("\n\n❌ Entrée une colonne correcte.")

            else :
                print("\n\n❌ Entrée des coordonnées correcte.")

        except ValueError :
            print("\n\n❌ Entrer des coordonnées valides.")


#=====================#
'''8) Annonce de cap'''
#=====================#

def annonce_cap(carte, sous_marin) : 
    h = int(carte.hauteur) - 1
    l = int(carte.largeur) - 1
    x, y = sous_marin.pos

    while True :
        try :
            cap = input(f"\n{sous_marin.capitaine}, annoncez un cap à votre équipe (OUEST, NORD, EST, SUD) ou retourner en arrière (0): ")
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
                #si le nouvelle emplacement du sous-marin contient la string "." étant un emplacement valide pour le sous-marin
                if carte.carte[x][y - 1] in [".", "m"] :
                    #alors on est autorisé a déplacer le sm et mettre a jour sa position
                    carte.deplacement_sm(sous_marin, cap)
                    return cap #retour de la nouvelle position contenant x, y ainsi que son cap pour les fonctions panne et choix_systeme
                    
                else : 
                    print("\nLa nouvelle position n'est pas valide, vous ne pouvez vous déplacer que sur les '.' OU 'm'")

            elif cap == "EST" and y < l :
                if carte.carte[x][y + 1] in [".", "m"] :
                    carte.deplacement_sm(sous_marin, cap)
                    return cap #nouvelle position contenant x, y
                    
                else : 
                    print("\nLa nouvelle position n'est pas valide, vous ne pouvez vous déplacer que sur les '.' OU 'm'")

            elif cap == "NORD" and x > 0 :
                if carte.carte[x - 1][y] in [".", "m"] :
                    carte.deplacement_sm(sous_marin, cap)
                    return cap #nouvelle position contenant x, y

                else : 
                    print("\nLa nouvelle position n'est pas valide, vous ne pouvez vous déplacer que sur les '.' OU 'm'")

            elif cap == "SUD" and x < h :
                if carte.carte[x + 1][y] in [".", "m"] :
                    carte.deplacement_sm(sous_marin, cap)
                    return cap #nouvelle position contenant x, y

                else : 
                    print("\nLa nouvelle position n'est pas valide, vous ne pouvez vous déplacer que sur les '.' OU 'm'")

            elif cap == "0" :
                return cap

            else :
                print("\n\n❌ Entrez une valeur valide en restant dans la map !")

        except ValueError :
            print("\n\n❌ Entrez une valeur valide dans les limites de la map.")

#====================#
'''8) Faire surface'''
#====================#

def faire_surface(carte) :
    surface = True
    print("\nVous faites surface et passez votre tour 3 fois.\n")
    #continuer la fonction pour faire en sorte que l'équipe passe son tour 3 fois
    carte.reset_chemin()
    input("\nSUIVANT")
    return surface 


#=============================#
'''1) Déplacement 1er équipe'''
#=============================#

def deplacement(carte, sous_marin, nom, surface, nombre_tour_attendu, sous_marin_ennemi, fin, carte_ennemi) :

    carte.Afficher_carte()

    #tant que la var surface est égale à False, le sm est sous la mer et peut donc se déplacer
    while surface == False :
        try :
            entete_deplacement = int(input("\n  1 - Choisir un cap\n  2 - Faire surface\n  3 - Demander au Mecano d'afficher la baie moteur\n\n  Sélectionner une action : "))

            if entete_deplacement == 1 :
                cap = annonce_cap(carte, sous_marin)
                
                if cap != "0" : 
                    #si le  sous marin se déplace sur une mine posé par un sm Ecureille
                    if sous_marin_ennemi.nom == "Ecureille" or sous_marin.nom == "Ecureille" :
                        fin = sous_marin.explosion_auto(sous_marin_ennemi, nom, Carte, fin, carte_ennemi)
                    input("\nSUIVANT")

                # if leurre_larguer == True :
                #     #définition du cap du leurre
                #     if cap == "OUEST" :
                #         cap_leurre = "EST"

                #     elif cap == "NORD" :
                #         cap_leurre = "SUD"

                #     elif cap == "EST" :
                #         cap_leurre = "OUEST"

                #     elif cap == "SUD" :
                #         cap_leurre = "NORD"

                    # #on déplace le leurre en fonction de son cap
                    # position_leurre = carte.deplacement_sm(position_leurre, leurre, cap_leurre)
                    # #si le leurre se déplace sur une mine automatique
                    # if sous_marin_ennemi.nom == "Ecureille" or sous_marin.nom == "Ecureille" :
                    #     fin, leurre_larguer = leurre.explosion_auto(sous_marin_ennemi, nom, carte, fin, carte_ennemi, self)
                
                    return cap.upper(), surface, nombre_tour_attendu, fin
                
            elif entete_deplacement == 2 :
                surface = faire_surface(carte)
                cap = "AUCUN"
                return cap.upper(), surface, nombre_tour_attendu, fin
            
            elif entete_deplacement == 3 :
                sous_marin.afficher_baie_moteur()
                
            else :
                print("\n\n❌ Sélectionnez une action comprise entre 1 et 2.")

        except ValueError :
            print("\n\n❌ Sélectionnez une action valide.")

    #si la var surface est True, alors le sm est en surface et doit attendre trois tours avant de pouvoir se redéplacer
    if surface == True :
            nombre_tour_attendu += 1
            cap = "AUCUN"

            if nombre_tour_attendu == 1 :
                print("\nVous passez votre 2ème tour à la surface, plus qu'un seul !")
                input("\nSUIVANT")

            if nombre_tour_attendu == 2 :
                print("\nVous avez passez vos 3 tours à la surface et vous replongez dans les eaux profondes !\n")
                input("SUIVANT")
                return cap.upper(), surface, nombre_tour_attendu, fin
            else :
                return cap.upper(), surface, nombre_tour_attendu, fin


#===============================#
'''10) Mécano rentre une panne'''
#===============================#

def panne(cap, nom, sous_marin, surface, nombre_tour_attendu) :
    #le capitaine a choisis un cap
    print(changement)
    print(f"\n⚠⚠⚠ Attention ⚠⚠⚠ : \nC'est au Mécano : '{sous_marin.mecano}', de l'équipe '{nom}' de jouer.")
    
    if sous_marin.mecano != sous_marin.capitaine :
        input("\nSUIVANT")

    if cap == "SUD" or cap == "NORD" or cap == "OUEST" or cap == "EST" :
        print(f"\nVotre capitaine à annoncé le cap : {cap}\n")

        # Affichage de la baie moteur
        sous_marin.afficher_baie_moteur()

        while True :
            try :
                choix_meca = int(input(f"{sous_marin.mecano}, choisissez une panne dans le cadran du cap '{cap}' annoncé par le capitaine (1-6) : "))

                if 1 <= choix_meca <= 6 :
                    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                    print(f"\n\nVous avez choisis la panne {choix_meca} du cadran '{cap}' ")
                    voyant_deja_panne = sous_marin.choisir_une_panne(choix_meca, cap)
                    
                    if voyant_deja_panne :    
                        input("\nSUIVANT")
                        return 

                    else :
                        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                        print("\n\n❌ Selectionnez un voyant qui n'est pas déjà en panne.")
                        sous_marin.afficher_baie_moteur()

                else :
                    print("\n\n❌ Selectionnez un voyant entre 1 et 6.")

            except ValueError :
                print("\n\n❌ Entrez un voyant valide.")

    #le capitaine a décider de faire surface
    else :
        if surface == True and nombre_tour_attendu == 0:
            print(f"\n\nVotre capitaine a fait surface et n'annoncera pas de cap pendant 3 tours !\n{sous_marin.mecano}, vous n'avez pas besoin de choisir une panne et celles-ci sont toutes réparées.")
            choix_meca = "AUCUN"
            voyant_deja_panne = sous_marin.choisir_une_panne(choix_meca, cap)
        
        if nombre_tour_attendu >= 1 :
            print(f"\n\nVotre sous-marin est à la surface et votre capitaine ne peut annoncer de cap !\n{sous_marin.mecano}, vous n'avez pas besoin de choisir une panne et celles-ci sont déjà toutes réparées.")
        
        #0 car il est reset avec le déplacement donc c'est le dernier tour
        if surface == False and nombre_tour_attendu == 0 :
            print(f"\n\nVotre sous-marin replonge dans les eaux profondes !\n{sous_marin.mecano}, lors de ce tour vous n'avez toujours pas besoin de choisir une panne.")

        input("\nSUIVANT")

        return

    
#================================================#
'''11) Le second augmente la jauge d'un système'''
#================================================#

def choix_systeme(sous_marin, nom, cap, nombre_tour_attendu, surface):
    print(changement)
    print(f"\n⚠⚠⚠ Attention ⚠⚠⚠ : \nC'est au Second : '{sous_marin.second}', de l'équipe '{nom}' de jouer.")

    if sous_marin.second != sous_marin.capitaine :
        input("\nSUIVANT")

    if cap == "SUD" or cap == "NORD" or cap == "OUEST" or cap == "EST" :
        sous_marin.afficher_systeme()

        while True :
            try :
                choix_second = int(input(f"\n'{sous_marin.second}', choisissez un système à charger (1-5) : "))
                
                if 1 <= choix_second <= 5 :
                    sous_marin.charger_systeme(choix_second)
                    sous_marin.check_systeme_charger(choix_second)
                    
                    while sous_marin.competence_charger != True :
                        try : 
                            choix_second = int(input(f"\n{sous_marin.second}, choisissez un système qui n'est pas déjà chargée (1-5) : "))
                            
                            if 1 <= choix_second <= 5 :
                                sous_marin.charger_systeme(choix_second)
                                sous_marin.check_systeme_charger(choix_second)
                            
                            else :
                                print("\n\n❌ Veuillez entrer un chiffre compris dans les systèmes du vaisseau.")

                        except ValueError : 
                            print("\n\n❌ Veuillez choisir un chiffre compris dans les systèmes du vaisseau.")    

                    input("\nSUIVANT")
                    return
                
                else :
                    print("\n\n❌ Veuillez entrer un chiffre compris entre 1 et 5.")

            except ValueError : 
                print("\n\n❌ Veuillez choisir un chiffre compris dans les compétences du vaisseau.")

    else :
        if nombre_tour_attendu == 0 and surface == True:
            print(f"\n\nVotre capitaine a fait surface et n'annoncera pas de cap pendant 3 tours !\n{sous_marin.second}, vous ne pouvez pas charger un système durant ce tour et les 2 prochains.")
            input("\nSUIVANT")

        if nombre_tour_attendu >= 1 :
            print(f"\n\nVotre sous-marin est à la surface et votre capitaine ne peut annoncer de cap !\n{sous_marin.second}, vous ne pouvez pas charger un système durant ce tour.")
            input("\nSUIVANT")
            
        #0 car il est reset avec le déplacement donc c'est le dernier tour
        if surface == False and nombre_tour_attendu == 0 :
            print(f"\n\nVotre sous-marin replonge dans les eaux profondes !\n{sous_marin.second}, lors de ce tour vous ne pouvez toujours pas charger un système.")
            input("\nSUIVANT")
        
        return

#=====================================#
'''12) déclenchement de compétencee'''
#=====================================#

def declenchement_systemes(sous_marin, sous_marin_ennemi, carte, nom_ennemi, nom_self, fin, carte_ennemi, nombre_tour_attendu, surface) :
    if nombre_tour_attendu != 0 or surface == True :
        if nombre_tour_attendu == 2 :
            nombre_tour_attendu = 0
            surface = False
        return surface, nombre_tour_attendu, fin

    #si aucun système n'est déclanchable
    if (sous_marin.nom == "Tigre" or sous_marin.nom == "Ecureille") and sous_marin.a1_charge == False and sous_marin.a2_charge == False and sous_marin.d1_charge == False and sous_marin.d2_charge == False and sous_marin.spe_charge == False and not sous_marin.emplacement_mines : 
        print("\n\nAucun système ne peut être déclencher\n")
        input("SUIVANT")
        return surface, nombre_tour_attendu, fin

    while True :
        try : 
            print(f"\n\nCapitaine : '{sous_marin.capitaine}' ou Second : '{sous_marin.second}', voulez-vous déclancher un système ?\n1 - non\n2 - oui\n")
            choix = int(input("Sélectionnez une option (1 ou 2) : "))

            if choix == 2 :
                #activer les systèmes à larguer
                while True :
                    try :
                        print("\n")
                        #afficher les systèmes prêts a être larguer
                        if (sous_marin.nom == "Tigre" or sous_marin.nom == "Ecureille") and sous_marin.a1_charge == True :
                            print("1 - Votre torpille est prête à être larguer ! 🚀")
                        
                        if (sous_marin.nom == "Tigre" or sous_marin.nom == "Ecureille") and sous_marin.a2_charge == True :
                            print("2 - Votre mine est prête à être larguer ! 💣")

                        if (sous_marin.nom == "Tigre" or sous_marin.nom == "Ecureille") and sous_marin.d1_charge == True :
                            print("3 - Votre drone est prêt à être larguer ! 🤖")

                        if (sous_marin.nom == "Tigre" or sous_marin.nom == "Ecureille") and sous_marin.d2_charge == True :
                            print("4 - Votre sonar est prêt à être lancer ! 🔍")

                        if sous_marin.nom == "Tigre" and sous_marin.spe_charge == True :
                            print("5 - Votre silence est prêt à être lancer ! 🌟")

                        if sous_marin.nom == "Ecureille" and sous_marin.spe_charge == True :
                            print("5 - Votre leurre est prêt à être lancer ! 🌟")

                        if (sous_marin.nom == "Tigre" or sous_marin.nom == "Ecureille") and sous_marin.emplacement_mines :
                            print("10 - Vous pouvez faire exploser votre mine ! 💥")

                        choix_systeme = int(input("\nSelectionner le système que vous voulez utiliser ou retourner en arrière (0) : "))
                        
                        #torpille larguable
                        if (sous_marin.nom == "Tigre" or sous_marin.nom == "Ecureille") and sous_marin.a1_charge == True and choix_systeme == 1 :
                            if sous_marin.condition_panne_arm == False :
                                fin = sous_marin.larguer_torpille(sous_marin_ennemi, carte, nom_ennemi, nom_self, fin)
                                return surface, nombre_tour_attendu, fin
                            
                            else :
                                print("\n\n❌ Votre système ARM détient une ou plusieurs pannes ! Vous ne pouvez par conséquent pas larguer une torpille !")

                        #mine largable
                        elif (sous_marin.nom == "Tigre" or sous_marin.nom == "Ecureille") and sous_marin.a2_charge == True and choix_systeme == 2 :
                            if sous_marin.condition_panne_arm == False :
                                sous_marin.larguer_mine(carte)
                                return surface, nombre_tour_attendu, fin
                            
                            else :
                                print("\n\n❌ Votre système ARM détient une ou plusiers pannes ! Vous ne pouvez par conséquent pas larguer de mine !")

                        #explosion mine
                        elif (sous_marin.nom == "Tigre" or sous_marin.nom == "Ecureille") and sous_marin.emplacement_mines and choix_systeme == 10 :
                            fin, condition_boucle_explo = sous_marin.exploser_mine(sous_marin_ennemi, nom_ennemi, nom_self, carte, fin)
                            if condition_boucle_explo == False :
                                return surface, nombre_tour_attendu, fin

                        #Larguage du drone
                        elif (sous_marin.nom == "Tigre" or sous_marin.nom == "Ecureille") and sous_marin.d1_charge == True and choix_systeme == 3 :
                            if sous_marin.condition_panne_det == False :
                                condition_boucle_det1 = sous_marin.larguer_drone(carte, sous_marin_ennemi)
                                if condition_boucle_det1 == False :
                                    input("SUIVANT")
                                    return surface, nombre_tour_attendu, fin
                            
                            else :
                                print("\n\n❌ Votre système DET détient une ou plusiers pannes ! Vous ne pouvez par conséquent pas larguer de drone !")

                        #lancer le sonar
                        elif (sous_marin.nom == "Tigre" or sous_marin.nom == "Ecureille") and sous_marin.d2_charge == True and choix_systeme == 4 :
                            if sous_marin.condition_panne_det == False :
                                print("Vous lancer votre sonar à la recherche du sous-marin ennemi !\nC'est au capitaine ennemi de jouer.")
                                input("\nSUIVANT")
                                dete2 = sous_marin.lancer_sonar(carte, sous_marin_ennemi, dete2, nom_ennemi, nom_self, carte_ennemi)
                                return surface, nombre_tour_attendu, fin
                            
                            else :
                                print("\n\n❌ Votre système DET détient une ou plusiers pannes ! Vous ne pouvez par conséquent pas déclencher de sonar !")

                        #lancer le silence
                        elif sous_marin.nom == "Tigre" and sous_marin.spe_charge == True and choix_systeme == 5 :
                            if sous_marin.condition_panne_spe == False :
                                condition_boucle_spe = sous_marin.lancer_silence(carte)
                                if condition_boucle_spe == False :
                                    print("\n\nVoici votre nouvelle emplacement :\n")
                                    carte.Afficher_carte()
                                    input("\nSUIVANT")
                                    return surface, nombre_tour_attendu, fin
                            
                            else : 
                                print("\n\n❌ Votre système SPE détient une ou plusiers pannes ! Vous ne pouvez par conséquent pas déclencher votre silence !")

                        #larguer le leurre
                        elif sous_marin.nom == "Ecureille" and sous_marin.spe_charge == True and choix_systeme == 5 :
                            if sous_marin.condition_panne_spe == False :
                                sous_marin.lancer_leurre()
                                
                                return surface, nombre_tour_attendu, fin
                            
                            else :
                                print("\n\n❌ Votre système SPE détient une ou plusiers pannes ! Vous ne pouvez par conséquent pas larguer votre leurre !")

                        elif choix_systeme == 0 :
                            break

                        else :
                            print("\n\n❌ Veuillez sélectionner un système chargé !")

                    except ValueError :
                        print("\n\n❌ Veuillez entrer un chiffre valide !")

            elif choix == 1 :
                return surface, nombre_tour_attendu, fin
            
            else :
                print("\n\n❌ Veuillez entrer une option valide (1-2) !")

        except ValueError :
            print("\n\n❌ Veuillez sélectionner une option valide !")


        

#===========================================#
'''13) déplacer transparent équipe énnemie'''
#===========================================#

def deplacer_transparent(nom, cap, Carte) :
    # Si le capitaine ennemi a annoncer un cap
    if cap == "SUD" or cap == "NORD" or cap == "OUEST" or cap == "EST" :
        print(changement)
        print(f"\n⚠⚠⚠ Attention ⚠⚠⚠ : \nC'est au détecteur {sous_marin.detecteur}, de l'équipe {nom} de jouer.\n")
        input("\nSUIVANT")

        print(f"\nLe capitaine ennemi à annoncer son cap : '{cap}' !")

        while True :
            try :
                y_lettre = input("\nChoisissez une colonne pour placer le cap ennemi : ")
                y = lettre_to_chiffre(y_lettre)
                x = int(input("Choisissez une ligne pour placer le cap ennemi : ")) - 1

                if y != "alpha" :
                    if 0 <= y <= ord(carte.derniere_colonne) - ord('A') and 0 <= x <= int(carte.derniere_ligne) - 1 :
                        x_transparent, y_transparent = Carte.start_trans(cap) #ici, x et y corresponde au coordonnée de l'empacement du premier déplacement du sous marin ennemi sur le transparent adverse.
                        input("\nSUIVANT")
                        return x_transparent, y_transparent
                                
                    else : 
                        print("\n\n❌ Entrez des coordonnées comprisent dans les limites de la map.")
                
                else :
                    print("\n\n❌ Entrez une colonne valide.")

            except ValueError :
                print("\n\n❌ Entrez des coordonnées valides.")

    else :
        print(f"Le capitaine ennemi a fait surface et n'annoncera pas de cap pendant 3 tours !")