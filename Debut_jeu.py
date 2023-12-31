from Input_Joueur import j1, j2, j3, j4, j5, j6, j7, j8, nom_e1, nom_e2
from Map import Carte, C1_e1, C2_e1, C1_e2, C2_e2, C2_e1_d1, C2_e2_d2, C1_e1_d1, C1_e2_d2
from Sous_marins import SousMarin, S1, S2
from Var_affichage import equipe, affichage_mode, aff_map, aff_s, start, changement


# Lancement du jeu
def lancer_jeu() :
    global nom_e1, nom_e2
    
    print(equipe)

    #définition du nombre de joueur
    nb_joueur = entre_nombre_joueur()

    #distribution des roles pour les joueurs.
    capitaine, second, mecano, detecteur = distribution_role(j1, j2, j3, j4, j5, j6, j7, j8, nb_joueur) #variable des rôles
    #Définition des capitaines des sous-marins dans une variable
    capitaine_e1 = capitaine[0] #Capitaine de l'équipe 1
    capitaine_e2 = capitaine[1] #Capitaine de l'équipe 2

    print(affichage_mode)

    #Sélection du mode de jeu
    mode = selection_mode(j1) #variable mode de jeu

    print(aff_map)

    #Selection de la map
    carte, derniere_colonne, derniere_ligne = selection_map(j1)

    C_e1 = carte[0] #Carte de l'équipe 1
    C_e2 = carte[1] #Carte de l'équipe 2

    print(aff_s)

    #Selection des sous_marins
    sous_marin_e1, sous_marin_e2 = selection_sous_marins(capitaine_e1, capitaine_e2)

    print(start)

    #1ere équipe plonge
    x1, y1 = plongerT(C_e1, sous_marin_e1, capitaine_e1, nom_e1, derniere_colonne, derniere_ligne)

    print(changement)

    #2ème équipe plonge
    x2, y2 = plongerT(C_e2, sous_marin_e2, capitaine_e2, nom_e2, derniere_colonne, derniere_ligne)

    # Le détecteur place sur le transparent l'endroit ou le sous marin ennemie a plonger
    x_t_e1, y_t_e1 = placer_transparent(detecteur_e1, nom_e1, C_e1_d1, derniere_colonne, derniere_ligne)
    x_t_e2, y_t_e2 = placer_transparent(detecteur_e2, nom_e2, C_e2_d2, derniere_colonne, derniere_ligne)

    jeu(capitaine, second, mecano, detecteur, mode, carte, sous_marin_e1, sous_marin_e2, x1, y1, x2, y2, derniere_colonne, derniere_ligne, x_t_e1, y_t_e1, x_t_e2, y_t_e2)#lancement de la boucle du jeu


#===================================#
'''Définition du nombre de joueurs'''
#===================================#

def entre_nombre_joueur():
    
    while True :
        try:
            nb_joueur = int(input("Entrez le nombre de joueur (2-8) : "))

            if 2 <= nb_joueur <= 8 :
                def_ekip(nb_joueur) #définition des équipes
                return nb_joueur

            else :
                print("\n❌ Le nombre de joueur doit être compris entre 2 et 8, recommencez.\n\n\n")

        except ValueError :
            print("\n❌ Veuillez rentrer un chiffre valide compris entre 2 et 8, recommencez.\n\n\n")



#==========================#
'''Définition des équipes'''
#==========================#

# Définition des équipe (attribution des variables joueurs et nom d'équipe en fonction du nombre totale de joueur)
def def_ekip(nb_joueur):
    
    global j1, j2, j3, j4, j5, j6, j7, j8, nom_e1, nom_e2

    # Partie a 2 joueurs 
    if nb_joueur == 2 :
        print("\n-> Chaques équipe ne comporte qu'un joueur.\nCe joueur cumule tout les rôles.\n")

        #Définition équipe 1
        j1 = input("Joueur 1, veuilllez rentrer votre nom : ")
        nom_e1 = input(f"{j1}, veuilllez rentrer le nom de votre équipe : ")

        #Définition équipe 2
        j2 = input("\nJoueur 2, veuilllez rentrer votre nom : ")
        nom_e2 = input(f"{j2}, veuilllez rentrer le nom de votre équipe : ")

        #Récapitulatif
        print(f"\n\n\n-> Récapitulatif : \n\n===== EQUIPE {nom_e1} =====\nCapitaine, Second, Mécano et Détecteur : {j1}\n\n===== EQUIPE {nom_e2} =====\nCapitaine, Second, Mécano et Détecteur : {j2}\n")
        input("\nSUIVANT")

        return j1, nom_e1, j2, nom_e2

    # Partie a 3 joueurs 
    elif nb_joueur == 3 :
        print("\n-> Une équipe comporte un membre, l'autre deux.\nL'équipe composé d'un joueur cumule tout les rôles. \nPour l'autre équipe, un joueur cumule le rôle de Capitaine, de Second et de Mécano.\n")
        
        #Définition équipe 1
        j1 = input("Joueur 1, vous serez seul contre deux ennemie. Veuilllez rentrer votre nom : ")
        nom_e1 = input(f"{j1}, veuilllez rentrer le nom de votre équipe : ")
        
        #Définition équipe 2
        j2 = input("\n\nJoueur 2, vous cumulerez le rôle de Capitaine, de Second et de Mécano dans votre équipe. Veuilllez rentrer votre nom : ")
        nom_e2 = input(f"{j2}, veuilllez rentrer le nom de votre équipe : ")
        j3 = input(f"Joueur 3, vous faite partie de l'équipe {nom_e2}, vous serez le détecteur a bord. Veuillez rentrer votre nom : ")

        #Récapitulatif
        print(f"\n\n\n-> Récapitulatif : \n\n===== EQUIPE {nom_e1} =====\nCapitaine, Second, Mécano et Détecteur : {j1}\n\n===== EQUIPE {nom_e2} =====\nCapitaine, Second et Mécano : {j2}\nDétecteur : {j3}\n")
        input("\nSUIVANT")

        return j1, nom_e1, j2, nom_e2, j3

    # Partie a 4 joueurs 
    elif nb_joueur == 4 :
        print("\n-> Chaques équipe comporte 2 membres.\nPour les deux équipes, un joueur cumule le rôle de Capitaine, de Second et de Mécano.\n")
    
        #Définition équipe 1
        j1 = input("\nJoueur 1, vous cumulerez le rôle de Capitaine, de Second et de Mécano dans votre équipe. Veuilllez rentrer votre nom : ")
        nom_e1 = input(f"{j1}, veuilllez rentrer le nom de votre équipe : ")
        j2 = input(f"Joueur 2, vous faite partie de l'équipe {nom_e1}, vous serez le détecteur a bord. Veuillez rentrer votre nom : ")
        
        #Définition équipe 2
        j3 = input("\n\nJoueur 3, vous cumulerez le rôle de Capitaine, de Second et de Mécano dans votre équipe. Veuilllez rentrer votre nom : ")
        nom_e2 = input(f"{j3}, veuilllez rentrer le nom de votre équipe :")
        j4 = input(f"Joueur 4, vous faite partie de l'équipe {nom_e2}, vous serez le détecteur a bord. Veuillez rentrer votre nom : ")

        #Récapitulatif
        print(f"\n\n\n-> Récapitulatif : \n\n===== EQUIPE {nom_e1} =====\nCapitaine, Second et Mécano : {j1}\nDétecteur : {j2}\n\n===== EQUIPE {nom_e2} =====\nCapitaine, Second et Mécano : {j3}\nDétecteur : {j4}\n")
        input("\nSUIVANT")

        return j1, nom_e1, j2, nom_e2, j3, j4

    # Partie a 5 joueurs 
    elif nb_joueur == 5 :
        print("\n-> Une équipe comporte deux membres, l'autre trois.\nPour l'équipe composé de 2 joueurs, un joueur cumule le rôle de Capitaine, de Second et de Mécano.\nPour l'autre équipe, un joueur cumule le rôle de Capitaine et de Second.\n")
    
        #Définition équipe 1
        j1 = input("\nJoueur 1, vous cumulerez le rôle de Capitaine, de Second et de Mécano dans votre équipe. Veuilllez rentrer votre nom : ")
        nom_e1 = input(f"{j1}, veuilllez rentrer le nom de votre équipe : ")
        j2 = input(f"Joueur 2, vous faite partie de l'équipe {nom_e1}, vous serez le détecteur a bord. Veuillez rentrer votre nom : ")
        
        #Définition équipe 2
        j3 = input("\n\nJoueur 3, vous cumulerez le rôle de Capitaine et de Second dans votre équipe. Veuilllez rentrer votre nom : ")
        nom_e2 = input(f"{j3}, veuilllez rentrer le nom de votre équipe : ")
        j4 = input(f"Joueur 4, vous faite partie de l'équipe {nom_e2}, vous serez le Mécano a bord. Veuillez rentrer votre nom : ")
        j5 = input(f"Joueur 5, vous faite partie de l'équipe {nom_e2}, vous serez le Détecteur a bord. Veuillez rentrer votre nom : ")

        #Récapitulatif
        print(f"\n\n\n-> Récapitulatif : \n\n===== EQUIPE {nom_e1} =====\nCapitaine, Second et Mécano : {j1}\nDétecteur : {j2}\n\n===== EQUIPE {nom_e2} =====\nCapitaine et Second : {j3}\nMécano : {j4}\nDétecteur : {j5}")
        input("\nSUIVANT")

        return j1, j2, j3, j4, j5, nom_e1, nom_e2

    # Partie a 6 joueurs 
    elif nb_joueur == 6 :
        print("\n-> Chaques équipe comporte 3 membres.\nPour les deux équipes, un joueur cumule le rôle de Capitaine et de Second.\n")
        
        #Définition équipe 1
        j1 = input("\nJoueur 1, vous cumulerez le rôle de Capitaine et de Second dans votre équipe. Veuilllez rentrer votre nom : ")
        nom_e1 = input(f"{j1}, veuilllez rentrer le nom de votre équipe : ")
        j2 = input(f"Joueur 2, vous faite partie de l'équipe {nom_e1}, vous serez le Mécano a bord. Veuillez rentrer votre nom : ")
        j3 = input(f"Joueur 3, vous faite partie de l'équipe {nom_e1}, vous serez le Détecteur a bord. Veuillez rentrer votre nom : ")
        
        #Définition équipe 2
        j4 = input("\n\nJoueur 4, vous cumulerez le rôle de Capitaine et de Second dans votre équipe. Veuilllez rentrer votre nom : ")
        nom_e2 = input(f"{j4}, veuilllez rentrer le nom de votre équipe : ")
        j5 = input(f"Joueur 5, vous faite partie de l'équipe {nom_e2}, vous serez le Mécano a bord. Veuillez rentrer votre nom : ")
        j6 = input(f"Joueur 6, vous faite partie de l'équipe {nom_e2}, vous serez le Détecteur a bord. Veuillez rentrer votre nom : ")

        #Récapitulatif
        print(f"\n\n\n-> Récapitulatif : \n\n===== EQUIPE {nom_e1} =====\nCapitaine et Second : {j1}\nMécano : {j2}\nDétecteur : {j3}\n\n===== EQUIPE {nom_e2} =====\nCapitaine et Second : {j4}\nMécano : {j5}\nDétecteur : {j6}")
        input("\nSUIVANT")

        return j1, j2, j3, j4, j5, j6, nom_e1, nom_e2

    # Partie a 7 joueurs 
    elif nb_joueur == 7 :
        print("\n-> Une équipe comporte trois membres, l'autre quatres.\nPour l'équipe composé de 3 joueurs, un joueur cumule le rôle de Capitaine et de Second.\nPour l'autre équipe, chaque joueur possède son propre rôle.\n")
    
        #Définition équipe 1
        j1 = input("\nJoueur 1, vous cumulerez le rôle de Capitaine et de Second dans votre équipe. Veuilllez rentrer votre nom : ")
        nom_e1 = input(f"{j1}, veuilllez rentrer le nom de votre équipe : ")
        j2 = input(f"Joueur 2, vous faite partie de l'équipe {nom_e1}, vous serez le Mécano a bord. Veuillez rentrer votre nom : ")
        j3 = input(f"Joueur 3, vous faite partie de l'équipe {nom_e1}, vous serez le Détecteur a bord. Veuillez rentrer votre nom : ")
        
        #Définition équipe 2
        j4 = input("\n\nJoueur 4, vous êtes le Capitaine de votre équipe. Veuilllez rentrer votre nom : ")
        nom_e2 = input(f"{j4}, veuilllez rentrer le nom de votre équipe : ")
        j5 = input(f"Joueur 5, vous faite partie de l'équipe {nom_e2}, vous serez le Second a bord. Veuillez rentrer votre nom : ")
        j6 = input(f"Joueur 6, vous faite partie de l'équipe {nom_e2}, vous serez le Mécano a bord. Veuillez rentrer votre nom : ")
        j7 = input(f"Joueur 7, vous faite partie de l'équipe {nom_e2}, vous serez le Détecteur a bord. Veuillez rentrer votre nom : ")
        
        #Récapitulatif
        print(f"\n\n\n-> Récapitulatif : \n\n===== EQUIPE {nom_e1} =====\nCapitaine et Second : {j1}\nMécano : {j2}\nDétecteur : {j3}\n\n===== EQUIPE {nom_e2} =====\nCapitaine :{j4}\nSecond : {j5}\nMécano : {j6}\nDétecteur : {j7}")
        input("\nSUIVANT")

        return j1, j2, j3, j4, j5, j6, nom_e1, nom_e2, j7

    # Partie a 8 joueurs 
    elif nb_joueur == 8 :
        print("\n-> Parfait, chaques équipe comporte 4 membres. Un pour chaque rôle\n")

        #Définition équipe 1
        j1 = input("\nJoueur 1, vous êtes le Capitaine de votre équipe. Veuilllez rentrer votre nom : ")
        nom_e1 = input(f"{j1}, veuilllez rentrer le nom de votre équipe : ")
        j2 = input(f"Joueur 2, vous faite partie de l'équipe {nom_e1}, vous serez le Second a bord. Veuillez rentrer votre nom : ")
        j3 = input(f"Joueur 3, vous faite partie de l'équipe {nom_e1}, vous serez le Mécano a bord. Veuillez rentrer votre nom : ")
        j4 = input(f"Joueur 4, vous faite partie de l'équipe {nom_e1}, vous serez le Détecteur a bord. Veuillez rentrer votre nom : ")
        
        #Définition équipe 2
        j5 = input("\n\nJoueur 5, vous êtes le Capitaine de votre équipe. Veuilllez rentrer votre nom : ")
        nom_e2 = input(f"{j5}, veuilllez rentrer le nom de votre équipe : ")
        j6 = input(f"Joueur 6, vous faite partie de l'équipe {nom_e2}, vous serez le Second a bord. Veuillez rentrer votre nom : ")
        j7 = input(f"Joueur 7, vous faite partie de l'équipe {nom_e2}, vous serez le Mécano a bord. Veuillez rentrer votre nom : ")
        j8 = input(f"Joueur 8, vous faite partie de l'équipe {nom_e2}, vous serez le Détecteur a bord. Veuillez rentrer votre nom : ")
        
        #Récapitulatif
        print(f"\n\n\n-> Récapitulatif : \n\n===== EQUIPE {nom_e1} =====\nCapitaine : {j1}\nSecond : {j2}\nMécano : {j3}\nDétecteur : {j4}\n\n===== EQUIPE {nom_e2} =====\nCapitaine : {j5}\nSecond : {j6}\nMécano : {j7}\nDétecteur : {j8}")
        input("\nSUIVANT")

        return j1, j2, j3, j4, j5, j6, nom_e1, nom_e2, j7, j8



#==========================#
'''Distribution des roles'''
#==========================#

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



#==========================#
'''Choix du mode de jeu'''
#==========================#

def selection_mode(j1):

    while True :
        try :
            mode = int(input(f"{j1}, veuillez selectionner le mode de jeu : "))

            if mode == 1 :
                print("\nVous avez sélectionner le mode de jeu tour par tour.")
                return mode
            
            elif mode == 2 :
                print("\nCette option n'est pas encore disponible, veuillez sélectionner le mode tour par tour.")
                selection_mode(j1)
            
            else :
                print("\n❌ Veuillez sélectionner une option valide.\n\n\n")

        except ValueError :
            print("\n❌ Entrez un mode de jeu valide (1 ou 2).\n\n\n")



#===================#
'''Choix de la map'''
#===================#

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
                print(f"\nVous avez sélectionné la carte {carte[0].nom} :\n")
                derniere_colonne, derniere_ligne = carte[0].Afficher_carte()
                input("\nSUIVANT")
                return carte, derniere_colonne, derniere_ligne

            else :
                print("\n❌ Veuillez entrée une carte existante.\n\n")
                
        except ValueError :
            print("\n❌ Veuillez entrée une carte valide.\n\n")



#=============================#
'''Sélection des sous-marins'''
#=============================#

def selection_sous_marins(capitaine_e1, capitaine_e2) :
    
    #pool des sous-marins dispo
    sous_marins_disponibles = {
        1: S1,
        2: S2,
    }

    sous_marin_e1 = None
    sous_marin_e2 = None

    while sous_marin_e1 is None:
        try:
            choix_e1 = int(input(f"{capitaine_e1}, sélectionnez votre sous-marin : "))
            sous_marin_e1 = sous_marins_disponibles.get(choix_e1)

            if sous_marin_e1 is None:
                print("\n❌ Veuillez choisir un sous-marin valide (1-2).\n\n")

        except ValueError:
            print("\n❌ Veuillez choisir un sous-marin valide (1-2).\n\n")

    while sous_marin_e2 is None:
        try:
            choix_e2 = int(input(f"\n{capitaine_e2}, sélectionnez votre sous-marin : "))
            sous_marin_e2 = sous_marins_disponibles.get(choix_e2)

            if sous_marin_e2 is None:
                print("\n❌ Veuillez choisir un sous-marin valide (1-2).\n\n")

        except ValueError:
            print("\n❌ Veuillez choisir un sous-marin valide (1-2).\n\n")

    print(f"\n{capitaine_e1}, vous avez sélectionné le sous-marin {sous_marin_e1.nom}.")
    print(f"\n{capitaine_e2}, vous avez sélectionné le sous-marin {sous_marin_e2.nom}.")

    return sous_marin_e1, sous_marin_e2



#=========================#
'''Placer son sous marin'''
#=========================#

#convertie une lettre en chiffre, A = 0, B = 1 etc ...
def lettre_to_chiffre(lettre):
        while True:
            if len(lettre) == 1:
                return ord(lettre.upper()) - ord('A')
            else:
                lettre = input("Veuillez entrer une colonne existante : ")

def plongerT(Carte, sous_marin, capitaine, nom_e, derniere_colonne, derniere_ligne):

    print(f"⚠⚠⚠ Attention ⚠⚠⚠ : c'est à l'équipe {nom_e} de jouer.\n")
    print(f"Capitaine {capitaine} de l'équipe '{nom_e}', plongez ! \n")

    Carte.Afficher_carte()

    while True :
        try :
            y_lettre = input("\nChoississez une colonne : ")
            y = lettre_to_chiffre(y_lettre)
            x = int(input("Choississez une ligne : ")) - 1

            if 0 <= y <= ord(derniere_colonne) - ord('A') and 0 <= x <= int(derniere_ligne) :
                x, y = Carte.placer_sous_marin((x,y), sous_marin)
                input("\nSUIVANT")
                break
            
            else : 
                print("\n❌ Entrez des coordonnées comprisent dans les limites de la map.\n\n")

        except ValueError :
            print("\n❌ Entrez des coordonnées valides.\n\n")

    return x, y

#=====================================#
'''Placer transparent équipe énnemie'''
#=====================================#

def placer_transparent(detecteur, nom, cap, Carte, derniere_colonne, derniere_ligne) :
    # Si le capitaine ennemie a annoncer un cap
    if cap == "SUD" or cap == "NORD" or cap == "OUEST" or cap == "EST" :
        print(changement)
        print(f"\n⚠⚠⚠ Attention ⚠⚠⚠ : \nC'est au détecteur {detecteur}, de l'équipe {nom} de jouer.\n")
        input("\nSUIVANT")

        print(f"\nLe capitaine ennemie à annoncer son cap : '{cap}' !")

        while True :
            try :
                y_lettre = input("\nChoississez une colonne pour placer le cap ennemie : ")
                y = lettre_to_chiffre(y_lettre)
                x = int(input("Choississez une ligne pour placer le cap ennemie : ")) - 1
                position = x, y

                if 0 <= y <= ord(derniere_colonne) - ord('A') and 0 <= x <= int(derniere_ligne) :
                    x_transparent, y_transparent = Carte.start_trans(cap, position) #ici, x et y corresponde au coordonnée de l'empacement du premier déplacement du sous marin ennemie sur le transparent adverse.
                    input("\nSUIVANT")
                    return x_transparent, y_transparent
                            
                else : 
                    print("\n❌ Entrez des coordonnées comprisent dans les limites de la map.\n\n")

            except ValueError :
                print("\n❌ Entrez des coordonnées valides.\n\n")

    else :
        print(f"Le capitaine ennemie a fait surface et n'annoncera pas de cap pendant 3 tours !")

#===============================================================================================#
'''============================================TOUR==========================================='''
#===============================================================================================#

def jeu(capitaine, second, mecano, detecteur, mode, carte, sous_marin_e1, sous_marin_e2, x1, y1, x2, y2, derniere_colonne, derniere_ligne, x_t_e1, y_t_e1, x_t_e2, y_t_e2) :
    
    global nom_e1, nom_e2

    capitaine_e1 = capitaine[0]
    capitaine_e2 = capitaine[1]

    detecteur_e1 = detecteur[0]
    detecteur_e2 = detecteur[1]

    mecano_e1 = mecano[0]
    mecano_e2 = mecano[1]

    second_e1 = second[0]
    second_e2 = second[1]

    C_e1 = carte[0] #Carte de l'équipe 1
    C_e2 = carte[1] #Carte de l'équipe 2
    C_e1_d1 = carte[2] #Transparent de l'équipe 1
    C_e2_d2 = carte[3] #Transparent de l'équipe 2

    position_e1 = x1, y1
    position_e2 = x2, y2

    #initialisation des cadrans des sous_marins
    #intéressant de pouvoir changer de baie_moteur (plus facile / dure) en fonction du vaisseaux choisie. et donc changer de numéro en fonction du vaisseau
    cadran_ouest_e1, cadran_nord_e1, cadran_sud_e1, cadran_est_e1 = sous_marin_e1.definition_du_cadran()
    cadran_ouest_e2, cadran_nord_e2, cadran_sud_e2, cadran_est_e2 = sous_marin_e2.definition_du_cadran()

    #1) la première équipe se déplace
    position_e1, cap_e1 = deplacement(position_e1, capitaine_e1, C_e1, sous_marin_e1, nom_e1)

    #2) le mecano rentre une panne dans le cadran associer au cap
    cadran_ouest_e1, cadran_nord_e1, cadran_sud_e1, cadran_est_e1 = panne(mecano_e1, cap_e1, nom_e1, sous_marin_e1, cadran_ouest_e1, cadran_nord_e1, cadran_sud_e1, cadran_est_e1)

    #3) le second augmente la jauge d'un système
    


#==================#
'''Annonce de cap'''
#==================#

def annonce_cap(position, capitaine, carte, sous_marin) : 
    while True :
        try :
            cap = input(f"\n{capitaine}, annoncez un cap à votre équipe (OUEST, NORD, EST, SUD): ")
            cap = cap.upper()

            if cap == "SUD" or cap == "NORD" or cap == "OUEST" or cap == "EST" :
                position = carte.deplacement_sm(position, sous_marin, cap, capitaine, carte)
                return position, cap #nouvelle position contenant x, y

            else :
                print("❌ Annoncez un cap valide !\n\n\n")

        except ValueError :
            print("❌ Entrez une valeur valide.\n\n\n")

#=================#
'''Faire surface'''
#=================#

def faire_surface(carte, sous_marin) :
    print("\nVous faite surface et passer votre tour 3 fois.\n")
    #continuer la fonction pour faire en sorte que l'équipe passe son tour 3 fois
    carte.reset_chemin()


#==========================#
'''Déplacement 1er équipe'''
#==========================#

def deplacement(position, capitaine, Carte, sous_marin, nom) :
    print(changement)
    print(f"\n⚠⚠⚠ Attention ⚠⚠⚠ : \nC'est au capitaine {capitaine} de l'équipe {nom} de jouer.")
    input("\nSUIVANT\n")
    Carte.Afficher_carte()

    while True :
        try :
            entete_deplacement = int(input("\n  1 - Choisir un cap\n  2 - Faire surface\n\n  Sélectionner une action : "))

            if entete_deplacement == 1 :
                position, cap = annonce_cap(position, capitaine, Carte, sous_marin)
                input("\nSUIVANT")
                return position, cap.upper()
                
            elif entete_deplacement == 2 :
                faire_surface(Carte, sous_marin)
                cap = "AUCUN"
                return position, cap
                
            else :
                print("\n❌ Sélectionner une action comprise entre 1 et 2.\n\n\n")

        except ValueError :
            print("\n❌ Sélectionner une action valide.\n\n\n")


#===========================#
'''Mécano rentre une panne'''
#===========================#

def panne(mecano, cap, nom, sous_marin, cadran_ouest, cadran_nord, cadran_sud, cadran_est) :
    if cap == "SUD" or cap == "NORD" or cap == "OUEST" or cap == "EST" :
        print(changement)
        print(f"\n⚠⚠⚠ Attention ⚠⚠⚠ : \nC'est au mécano {mecano}, de l'équipe {nom} de jouer.")
        input("\nSUIVANT")
        print(f"\nVotre capitaine à annoncer le cap : {cap}\n")

        # Affichage de la baie moteur
        sous_marin.afficher_baie_moteur(cadran_ouest, cadran_nord, cadran_sud, cadran_est)

        while True :
            try :
                choix_meca = int(input(f"{mecano}, choississez une panne dans le cadran du cap (1-6) : "))

                if 1 <= choix_meca <= 6 :
                    cadran_ouest, cadran_nord, cadran_sud, cadran_est = sous_marin.choisir_une_panne(choix_meca, cadran_ouest, cadran_nord, cadran_sud, cadran_est, cap)
                    input("\nSUIVANT")
                    return cadran_ouest, cadran_nord, cadran_sud, cadran_est

                else :
                    print("❌ Selectionnez une panne entre 1 et 6.\n\n")

            except ValueError :
                    print("❌ Entrez une panne valide.\n\n")

    else :
        print(changement)
        print(f"\n⚠⚠⚠ Attention ⚠⚠⚠ : \nC'est au mécano {mecano}, de l'équipe {nom} de jouer.")
        input("\nSUIVANT")
        print(f"\n\nLe capitaine ennemie a fait surface et n'annoncera pas de cap pendant 3 tours !\nLe mecano n'a pas besoin de choisir une panne et celle-ci sont toutes réparées.")
        
        choix_meca = "AUCUN"
        
        cadran_ouest, cadran_nord, cadran_sud, cadran_est = sous_marin.choisir_une_panne(choix_meca, cadran_ouest, cadran_nord, cadran_sud, cadran_est, cap)
        
        input("\nSUIVANT")

        return cadran_ouest, cadran_nord, cadran_sud, cadran_est


#garder pour le déplacement du transparent :
def placer_transparent(detecteur, nom, cap, Carte, derniere_colonne, derniere_ligne) :
    # Si le capitaine ennemie a annoncer un cap
    if cap == "SUD" or cap == "NORD" or cap == "OUEST" or cap == "EST" :
        print(changement)
        print(f"\n⚠⚠⚠ Attention ⚠⚠⚠ : \nC'est au détecteur {detecteur}, de l'équipe {nom} de jouer.\n")
        input("\nSUIVANT")

        print(f"\nLe capitaine ennemie à annoncer son cap : '{cap}' !")

        while True :
            try :
                cap = input(f"\n{detecteur}, entrez le cap ennemi (Nord, Sud, Est, Ouest) : ")
                cap = cap.upper()

                if cap == "SUD" or cap == "NORD" or cap == "OUEST" or cap == "EST" :
                    Carte.Afficher_carte()

                    while True :
                        try :
                            y_lettre = input("\nChoississez une colonne pour placer le cap ennemie : ")
                            y = lettre_to_chiffre(y_lettre)
                            x = int(input("Choississez une ligne pour placer le cap ennemie : ")) - 1
                            position = x, y

                            if 0 <= y <= ord(derniere_colonne) - ord('A') and 0 <= x <= int(derniere_ligne) :
                                x_transparent, y_transparent = Carte.start_trans(cap, position) #ici, x et y corresponde au coordonnée de l'empacement du premier déplacement du sous marin ennemie sur le transparent adverse.
                                input("\nSUIVANT")
                                return x_transparent, y_transparent
                            
                            else : 
                                print("\n❌ Entrez des coordonnées comprisent dans les limites de la map.\n\n")

                        except ValueError :
                            print("\n❌ Entrez des coordonnées valides.\n\n")
                            
                    break

                else :
                    print("❌ Annoncez un cap valide !\n\n")

            except ValueError :
                print("❌ Entrez une valeur valide.\n\n")

        return 

    else :
        print(f"Le capitaine ennemie a fait surface et n'annoncera pas de cap pendant 3 tours !")