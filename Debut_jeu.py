from Input_Joueur import j1, j2, j3, j4, j5, j6, j7, j8, nom_e1, nom_e2
from Map import Carte, C1_e1, C2_e1, C1_e2, C2_e2, C2_e1_d1, C2_e2_d2, C1_e1_d1, C1_e2_d2
from Sous_marins import SousMarin
from Var_affichage import equipe, affichage_mode, aff_map, aff_s, start, changement


# Lancement du jeu
def lancer_jeu() :
    global nom_e1, nom_e2
    
    print(equipe)

    #1) définition du nombre de joueurs
    nb_joueur = entre_nombre_joueur()

    #2) distribution des rôles pour les joueurs.
    capitaine, second, mecano, detecteur = distribution_role(j1, j2, j3, j4, j5, j6, j7, j8, nb_joueur) #variable des rôles
    
    #3) Définition des capitaines des sous-marins dans une variable
    capitaine_e1 = capitaine[0] #Capitaine de l'équipe 1
    capitaine_e2 = capitaine[1] #Capitaine de l'équipe 2

    detecteur_e1 = detecteur[0]
    detecteur_e2 = detecteur[1]

    print(affichage_mode)

    #4) Sélection du mode de jeu
    mode = selection_mode(j1) #variable mode de jeu

    print(aff_map)

    #5) Selection de la map
    carte, derniere_colonne, derniere_ligne = selection_map(j1)

    C_e1 = carte[0] #Carte de l'équipe 1
    C_e2 = carte[1] #Carte de l'équipe 2
    C_e1_d1 = carte[2]
    C_e2_d2 = carte[3]

    #initialisation des positions sm ennemies sur le transparent
    position_sm_d1 = C_e1_d1.start_trans()
    position_sm_d2 = C_e2_d2.start_trans()

    print(aff_s)

    #6) Selection des sous-marins
    sous_marin_e1, sous_marin_e2 = selection_sous_marins(capitaine_e1, capitaine_e2)

    print(start)

    #7) 1ere équipe plonge
    x1, y1 = plongerT(C_e1, sous_marin_e1, capitaine_e1, nom_e1, derniere_colonne, derniere_ligne)

    print(changement)

    #7) 2ème équipe plonge
    x2, y2 = plongerT(C_e2, sous_marin_e2, capitaine_e2, nom_e2, derniere_colonne, derniere_ligne)
    
    #initialisation des cadrans des sous-marins
    #intéressant de pouvoir changer de baie_moteur (plus facile / dure) en fonction du vaisseau choisie. Et donc changer de numéro en fonction du vaisseau
    cadran_ouest_e1, cadran_nord_e1, cadran_sud_e1, cadran_est_e1 = sous_marin_e1.definition_du_cadran()
    cadran_ouest_e2, cadran_nord_e2, cadran_sud_e2, cadran_est_e2 = sous_marin_e2.definition_du_cadran()

    #initialisation des compétences des sous-marins
    arme1_e1, arme2_e1, dete1_e1, dete2_e1, spe_e1 = sous_marin_e1.def_systeme()
    arme1_e2, arme2_e2, dete1_e2, dete2_e2, spe_e2 = sous_marin_e1.def_systeme()


    #9) Début de la boucle
    jeu(capitaine, second, mecano, detecteur, mode, carte, sous_marin_e1, sous_marin_e2, x1, y1, x2, y2, derniere_colonne, derniere_ligne, cadran_ouest_e1, cadran_nord_e1, cadran_sud_e1, cadran_est_e1, cadran_ouest_e2, cadran_nord_e2, cadran_sud_e2, cadran_est_e2, arme1_e1, arme2_e1, dete1_e1, dete2_e1, spe_e1, arme1_e2, arme2_e2, dete1_e2, dete2_e2, spe_e2, nb_joueur, position_sm_d1, position_sm_d2)#lancement de la boucle du jeu


#======================================#
'''1) Définition du nombre de joueurs'''
#======================================#

def entre_nombre_joueur():
    
    while True :
        try:
            nb_joueur = int(input("Entrer le nombre de joueurs (2-8) : "))

            if 2 <= nb_joueur <= 8 :
                def_ekip(nb_joueur) #définition des équipes
                return nb_joueur

            else :
                print("❌ Le nombre de joueurs doit être compris entre 2 et 8, recommencez.\n\n\n")

        except ValueError :
            print("❌ Veuillez rentrer un chiffre valide compris entre 2 et 8, recommencez.\n\n\n")



#=============================#
'''2) Définition des équipes'''
#=============================#

# Définition des équipe (attribution des variables joueurs et nom d'équipe en fonction du nombre totale de joueur)
def def_ekip(nb_joueur):
    
    global j1, j2, j3, j4, j5, j6, j7, j8, nom_e1, nom_e2

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

        return j1, nom_e1, j2, nom_e2

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

        return j1, nom_e1, j2, nom_e2, j3

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

        return j1, nom_e1, j2, nom_e2, j3, j4

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

        return j1, j2, j3, j4, j5, nom_e1, nom_e2

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

        return j1, j2, j3, j4, j5, j6, nom_e1, nom_e2

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

        return j1, j2, j3, j4, j5, j6, nom_e1, nom_e2, j7

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

        return j1, j2, j3, j4, j5, j6, nom_e1, nom_e2, j7, j8



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
                print("❌ Veuillez sélectionner une option valide.\n\n\n")

        except ValueError :
            print("❌ Entrez un mode de jeu valide (1 ou 2).\n\n\n")



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
                derniere_colonne, derniere_ligne = carte[0].Afficher_carte()
                input("\nSUIVANT")
                return carte, derniere_colonne, derniere_ligne

            else :
                print("❌ Veuillez entrée une carte existante.\n\n")
                
        except ValueError :
            print("❌ Veuillez entrée une carte valide.\n\n")



#================================#
'''6) Sélection des sous-marins'''
#================================#

def selection_sous_marins(capitaine_e1, capitaine_e2) :

    sous_marin_e1 = None
    sous_marin_e2 = None

    while sous_marin_e1 is None:
        try:
            choix_e1 = int(input(f"{capitaine_e1}, sélectionnez votre sous-marin : "))

            if choix_e1 == 1 :
                sous_marin_e1 = SousMarin("Tigre", 4, 1, False, False, False, False, False, None)
                break

            elif choix_e1 == 2 :
                sous_marin_e1 = SousMarin("Ecureille", 3, 1, False, False, False, False, False, None)
                break

            else:
                print("❌ Veuillez choisir un sous-marin afficher.\n\n")

        except ValueError:
            print("❌ Veuillez choisir un sous-marin valide.\n\n")

    while sous_marin_e2 is None:
        try:
            choix_e2 = int(input(f"\n{capitaine_e2}, sélectionnez votre sous-marin : "))
            
            if choix_e2 == 1 :
                sous_marin_e2 = SousMarin("Tigre", 4, 1, False, False, False, False, False, None)
                return sous_marin_e1, sous_marin_e2

            elif choix_e2 == 2 :
                sous_marin_e2 = SousMarin("Ecureille", 3, 1, False, False, False, False, False, None)
                return sous_marin_e1, sous_marin_e2

            else:
                print("❌ Veuillez choisir un sous-marin valide (1-2).\n\n")

        except ValueError:
            print("❌ Veuillez choisir un sous-marin valide (1-2).\n\n")

    print(f"\n{capitaine_e1}, vous avez sélectionné le sous-marin {sous_marin_e1.nom}.")
    print(f"\n{capitaine_e2}, vous avez sélectionné le sous-marin {sous_marin_e2.nom}.")




#============================#
'''7) Placer son sous marin'''
#============================#

#convertire une lettre en chiffre, A = 0, B = 1 etc ...
def lettre_to_chiffre(lettre):
        while True:
            if len(lettre) == 1 and lettre.isalpha():
                return ord(lettre.upper()) - ord('A')
            
            elif lettre.isdigit():
                lettre = input("❌ Veuillez entrer une lettre existante : ")

            else:
                lettre = input("❌ Veuillez entrer une colonne existante : ")

def plongerT(Carte, sous_marin, capitaine, nom_e, derniere_colonne, derniere_ligne):

    print(f"⚠⚠⚠ Attention ⚠⚠⚠ : c'est à l'équipe '{nom_e}' de jouer.\n")
    print(f"Capitaine '{capitaine}' de l'équipe '{nom_e}', plongez ! ")

    Carte.Afficher_carte()

    while True :
        try :
            y_lettre = input("\nChoisissez une colonne : ")
            y = lettre_to_chiffre(y_lettre)
            x = int(input("Choisissez une ligne : ")) - 1

            if 0 <= y <= ord(derniere_colonne) - ord('A') and 0 <= x <= int(derniere_ligne) :
                x, y = Carte.placer_sous_marin((x,y), sous_marin)
                input("\nSUIVANT")
                break
            
            else : 
                print("❌ Entrer des coordonnées juste ou comprisent dans les limites de la map.\n\n")

        except ValueError :
            print("❌ Entrer des coordonnées valides.\n\n")

    return x, y




#============================================================================================#
'''=====================================DEBUT BOUCLE======================================='''
#============================================================================================#

def jeu(capitaine, second, mecano, detecteur, mode, carte, sous_marin_e1, sous_marin_e2, x1, y1, x2, y2, derniere_colonne, derniere_ligne, cadran_ouest_e1, cadran_nord_e1, cadran_sud_e1, cadran_est_e1, cadran_ouest_e2, cadran_nord_e2, cadran_sud_e2, cadran_est_e2, arme1_e1, arme2_e1, dete1_e1, dete2_e1, spe_e1, arme1_e2, arme2_e2, dete1_e2, dete2_e2, spe_e2, nb_joueur, position_sm_d1, position_sm_d2) :
    
    global nom_e1, nom_e2

    # Définition des rôles
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

    #définition des positions des sous-marins
    position_e1 = x1, y1
    position_e2 = x2, y2

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

    #initialisation des variables des systèmes
    emplacement_mines_e1 = []
    mine_cap_e1 = []
    emplacement_mines_e2 = []
    mine_cap_e2 = []

    while fin == False :
        while fin_tour_e1 == False :
            #============#
            '''EQUIPE 1'''
            #============#
            #1) le capitaine de l'équipe 1 déplace son vaisseau
            position_e1, cap_e1, surface_e1, nombre_tour_attendu_e1, fin, emplacement_mines_e2, mine_cap_e2, mine_cap_e1, emplacement_mines_e1 = deplacement(position_e1, capitaine_e1, C_e1, sous_marin_e1, nom_e1, surface_e1, nombre_tour_attendu_e1, emplacement_mines_e1, sous_marin_e2,  emplacement_mines_e1, mine_cap_e1, fin, emplacement_mines_e2, mine_cap_e2, C_e2)
            
            #2) le mecano de l'équipe 1 rentre une panne dans le cadran associer au cap
            cadran_ouest_e1, cadran_nord_e1, cadran_sud_e1, cadran_est_e1 = panne(mecano_e1, cap_e1, nom_e1, sous_marin_e1, cadran_ouest_e1, cadran_nord_e1, cadran_sud_e1, cadran_est_e1, surface_e1, nombre_tour_attendu_e1, capitaine_e1)
            
            #3) le second de l'équipe 1 augmente la jauge d'un système
            arme1_e1, arme2_e1, dete1_e1, dete2_e1, spe_e1 = choix_systeme(arme1_e1, arme2_e1, dete1_e1, dete2_e1, spe_e1, sous_marin_e1, second_e1, nom_e1, cap_e1, nombre_tour_attendu_e1, surface_e1, capitaine_e1)
            
            #4) l'équipe 1 peut déclencher une compétence
            fin, arme1_e1, emplacement_mines_e1, arme2_e1, mine_cap_e1 = declenchement_systemes(arme1_e1, arme2_e1, dete1_e1, dete2_e1, spe_e1, sous_marin_e1, sous_marin_e2, second_e1, capitaine_e1, C_e1, derniere_colonne, derniere_ligne, capitaine_e2, nom_e2, nom_e1, emplacement_mines_e1, mine_cap_e1, fin)
            
            #5) le detecteur adverse rentre le cap ennemi

    print(fin)
    print("BRAVO JEU FINI")


    


#=====================#
'''1) Annonce de cap'''
#=====================#

def annonce_cap(position, capitaine, carte, sous_marin, emplacement_mines) : 
    x, y = position
    h = int(carte.hauteur) - 1
    l = int(carte.largeur) - 1

    while True :
        try :
            cap = input(f"\n{capitaine}, annoncez un cap à votre équipe (OUEST, NORD, EST, SUD) ou retourner en arrière (0): ")
            cap = cap.upper()

            #si le cap est = a ouest et est supérière à 0 étant la limite de la map
            if cap == "OUEST" and y > 0 :
                #si le nouvelle emplacement du sous-marin contient la string "." étant un emplacement valide pour le sous-marin
                if carte.carte[x][y - 1] in [".", "m"] :
                    #alors on est autorisé a déplacer le sm et mettre a jour sa position
                    position = carte.deplacement_sm(position, sous_marin, cap, emplacement_mines)
                    return position, cap #retour de la nouvelle position contenant x, y ainsi que son cap pour les fonctions panne et choix_systeme
                    
                else : 
                    print("\nLa nouvelle position n'est pas valide, vous ne pouvez vous déplacer que sur les '.' OU 'm'")

            elif cap == "EST" and y < l :
                if carte.carte[x][y + 1] in [".", "m"] :
                    position = carte.deplacement_sm(position, sous_marin, cap, emplacement_mines)
                    return position, cap #nouvelle position contenant x, y
                    
                else : 
                    print("\nLa nouvelle position n'est pas valide, vous ne pouvez vous déplacer que sur les '.' OU 'm'")

            elif cap == "NORD" and x > 0 :
                if carte.carte[x - 1][y] in [".", "m"] :
                    position = carte.deplacement_sm(position, sous_marin, cap, emplacement_mines)
                    return position, cap #nouvelle position contenant x, y

                else : 
                    print("\nLa nouvelle position n'est pas valide, vous ne pouvez vous déplacer que sur les '.' OU 'm'")

            elif cap == "SUD" and x < h :
                if carte.carte[x + 1][y] in [".", "m"] :
                    position = carte.deplacement_sm(position, sous_marin, cap, emplacement_mines)
                    return position, cap #nouvelle position contenant x, y

                else : 
                    print("\nLa nouvelle position n'est pas valide, vous ne pouvez vous déplacer que sur les '.' OU 'm'")

            elif cap == "0" :
                return position, cap

            else :
                print("❌ Entrez une valeur valide !\n\n\n")

        except ValueError :
            print("❌ Entrez une valeur valide.\n\n\n")

#====================#
'''1) Faire surface'''
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

def deplacement(position, capitaine, Carte, sous_marin, nom, surface, nombre_tour_attendu, emplacement_mines, sous_marin_ennemi, emplacement_mines_self, mine_cap_self, fin, emplacement_mines_ennemi, mine_cap_ennemi, carte_ennemi) :
    print(changement)
    print(f"\n⚠⚠⚠ Attention ⚠⚠⚠ : \nC'est au capitaine : '{capitaine}', de l'équipe '{nom}' de jouer.")
    input("\nSUIVANT\n")

    Carte.Afficher_carte()

    #tant que la var surface est égale à False, le sm est sous la mer et peut donc se déplacer
    while surface == False :
        try :
            entete_deplacement = int(input("\n  1 - Choisir un cap\n  2 - Faire surface\n\n  Sélectionner une action : "))

            if entete_deplacement == 1 :
                position, cap = annonce_cap(position, capitaine, Carte, sous_marin, emplacement_mines)
                
                if cap != "0" : 
                    #si le  sous marin se déplace sur une mine posé par un sm Ecureille
                    if sous_marin_ennemi.nom == "Ecureille" or sous_marin.nom == "Ecureille" :
                        fin, emplacement_mines_ennemi, mine_cap_ennemi, mine_cap_self, emplacement_mines_self = sous_marin.explosion_auto(sous_marin_ennemi, nom, emplacement_mines_self, mine_cap_self, Carte, fin, emplacement_mines_ennemi, mine_cap_ennemi, carte_ennemi)
                    
                    input("\nSUIVANT")
                    return position, cap.upper(), surface, nombre_tour_attendu, fin, emplacement_mines_ennemi, mine_cap_ennemi, mine_cap_self, emplacement_mines_self
                
            elif entete_deplacement == 2 :
                surface = faire_surface(Carte)
                cap = "AUCUN"
                return position, cap, surface, nombre_tour_attendu, fin, emplacement_mines_ennemi, mine_cap_ennemi, mine_cap_self, emplacement_mines_self
                
            else :
                print("❌ Sélectionnez une action comprise entre 1 et 2.\n\n\n")

        except ValueError :
            print("❌ Sélectionnez une action valide.\n\n\n")

    #si la var surface est True, alors le sm est en surface et doit attendre trois tours avant de pouvoir se redéplacer
    if surface == True :
            nombre_tour_attendu = nombre_tour_attendu + 1
            cap = "AUCUN"

            if nombre_tour_attendu == 1 :
                print("\nVous passez votre 2ème tour à la surface, plus qu'un seul !")
                input("\nSUIVANT")

            if nombre_tour_attendu == 2 :
                nombre_tour_attendu = 0
                surface = False
                print("\nVous avez passez vos 3 tours à la surface et vous replongez dans les eaux profondes !\n")
                input("SUIVANT")
                return position, cap, surface, nombre_tour_attendu

            else :
                return position, cap, surface, nombre_tour_attendu


#==============================#
'''2) Mécano rentre une panne'''
#==============================#

def panne(mecano, cap, nom, sous_marin, cadran_ouest, cadran_nord, cadran_sud, cadran_est, surface, nombre_tour_attendu, capitaine) :
    #le capitaine a choisis un cap
    print(changement)
    print(f"\n⚠⚠⚠ Attention ⚠⚠⚠ : \nC'est au Mécano : '{mecano}', de l'équipe '{nom}' de jouer.")
    
    if mecano != capitaine :
        input("\nSUIVANT")

    if cap == "SUD" or cap == "NORD" or cap == "OUEST" or cap == "EST" :
        print(f"\nVotre capitaine à annoncé le cap : {cap}\n")

        # Affichage de la baie moteur
        sous_marin.afficher_baie_moteur(cadran_ouest, cadran_nord, cadran_sud, cadran_est)

        while True :
            try :
                choix_meca = int(input(f"{mecano}, choisissez une panne dans le cadran du cap '{cap}' annoncé par le capitaine (1-6) : "))

                if 1 <= choix_meca <= 6 :
                    print(f"\n\nVous avez choisis la panne {choix_meca} du cadran '{cap}' ")
                    cadran_ouest, cadran_nord, cadran_sud, cadran_est, condition = sous_marin.choisir_une_panne(choix_meca, cadran_ouest, cadran_nord, cadran_sud, cadran_est, cap)
                    
                    if condition :    
                        input("\nSUIVANT")
                        return cadran_ouest, cadran_nord, cadran_sud, cadran_est

                    print("❌ Selectionnez un voyant qui n'est pas déjà en panne.\n\n")

                else :
                    print("❌ Selectionnez un voyant entre 1 et 6.\n\n")

            except ValueError :
                print("❌ Entrez un voyant valide.\n\n")

    #le capitaine a décider de faire surface
    else :
        if surface == True and nombre_tour_attendu == 0:
            print(f"\n\nVotre capitaine a fait surface et n'annoncera pas de cap pendant 3 tours !\n{mecano}, vous n'avez pas besoin de choisir une panne et celles-ci sont toutes réparées.")
            choix_meca = "AUCUN"
            cadran_ouest, cadran_nord, cadran_sud, cadran_est, condition = sous_marin.choisir_une_panne(choix_meca, cadran_ouest, cadran_nord, cadran_sud, cadran_est, cap)
        
        if nombre_tour_attendu >= 1 :
            print(f"\n\nVotre sous-marin est à la surface et votre capitaine ne peut annoncer de cap !\n{mecano}, vous n'avez pas besoin de choisir une panne et celles-ci sont déjà toutes réparées.")
        
        #0 car il est reset avec le déplacement donc c'est le dernier tour
        if surface == False and nombre_tour_attendu == 0 :
            print(f"\n\nVotre sous-marin replonge dans les eaux profondes !\n{mecano}, lors de ce tour vous n'avez toujours pas besoin de choisir une panne.")

        input("\nSUIVANT")

        return cadran_ouest, cadran_nord, cadran_sud, cadran_est

    
#===============================================#
'''3) Le second augmente la jauge d'un système'''
#===============================================#

def choix_systeme(arme1, arme2, dete1, dete2, spe, sous_marin, second, nom, cap, nombre_tour_attendu, surface, capitaine):
    print(changement)
    print(f"\n⚠⚠⚠ Attention ⚠⚠⚠ : \nC'est au Second : '{second}', de l'équipe '{nom}' de jouer.")

    if second != capitaine :
        input("\nSUIVANT")

    if cap == "SUD" or cap == "NORD" or cap == "OUEST" or cap == "EST" :
        sous_marin.afficher_systeme(arme1, arme2, dete1, dete2, spe)

        while True :
            try :
                choix_second = int(input(f"\n'{second}', choisissez un système à charger (1-5) : "))
                
                if 1 <= choix_second <= 5 :
                    mince, arme1, arme2, dete1, dete2, spe = sous_marin.charger_systeme(choix_second, arme1, arme2, dete1, dete2, spe)
                    
                    while mince != True :
                        try : 
                            choix_second = int(input(f"\n{second}, choisissez un système qui n'est pas déjà chargée (1-5) : "))
                            
                            if 1 <= choix_second <= 5 :
                                mince, arme1, arme2, dete1, dete2, spe = sous_marin.charger_systeme(choix_second, arme1, arme2, dete1, dete2, spe)
                            
                            else :
                                print("❌ Veuillez entrer un chiffre compris dans les systèmes du vaisseau.\n\n")

                        except ValueError : 
                            print("❌ Veuillez choisir un chiffre compris dans les systèmes du vaisseau.\n\n")    

                    input("\nSUIVANT")
                    return arme1, arme2, dete1, dete2, spe
                
                else :
                    print("❌ Veuillez entrer un chiffre compris entre 1 et 5.\n\n")

            except ValueError : 
                print("❌ Veuillez choisir un chiffre compris dans les compétences du vaisseau.\n\n")

    else :
        if nombre_tour_attendu == 0 and surface == True:
            print(f"\n\nVotre capitaine a fait surface et n'annoncera pas de cap pendant 3 tours !\n{second}, vous ne pouvez pas charger un système durant ce tour et les 2 prochains.")
            input("\nSUIVANT")

        if nombre_tour_attendu >= 1 :
            print(f"\n\nVotre sous-marin est à la surface et votre capitaine ne peut annoncer de cap !\n{second}, vous ne pouvez pas charger un système durant ce tour.")
            input("\nSUIVANT")
            
        #0 car il est reset avec le déplacement donc c'est le dernier tour
        if surface == False and nombre_tour_attendu == 0 :
            print(f"\n\nVotre sous-marin replonge dans les eaux profondes !\n{second}, lors de ce tour vous ne pouvez toujours pas charger un système.")
            input("\nSUIVANT")
        
        return arme1, arme2, dete1, dete2, spe

#====================================#
'''4) déclenchement de compétencee'''
#====================================#

def declenchement_systemes(arme1, arme2, dete1, dete2, spe, sous_marin, sous_marin_ennemi, second, capitaine, carte, derniere_colonne, derniere_ligne, capitaine_ennemie, nom_ennemi, nom_self, emplacement_mines, mine_cap, fin) :

    #si aucun système n'est déclanchable
    if (sous_marin.nom == "Tigre" or sous_marin.nom == "Ecureille") and sous_marin.a1 == False and sous_marin.a2 == False and sous_marin.d1 == False and sous_marin.d2 == False and sous_marin.spe == False and emplacement_mines == False : 
        print("\n\nAucun système ne peut être déclencher\n")
        input("SUIVANT")
        return fin, arme1, emplacement_mines, arme2

    while True :
        try : 
            print(f"\n\nCapitaine : '{capitaine}' ou Second : '{second}', voulez-vous déclancher un système ?\n1 - non\n2 - oui\n")
            choix = int(input("Sélectionnez une option (1 ou 2) : "))

            if choix == 2 :
                print("\n")
                #afficher les systèmes prêts a être larguer
                if (sous_marin.nom == "Tigre" or sous_marin.nom == "Ecureille") and sous_marin.a1 == True :
                    print("1 - Votre torpille est prête à être larguer !")
                
                if (sous_marin.nom == "Tigre" or sous_marin.nom == "Ecureille") and sous_marin.a2 == True :
                    print("2 - Votre mine est prête à être larguer !")

                if (sous_marin.nom == "Tigre" or sous_marin.nom == "Ecureille") and sous_marin.d1 == True :
                    print("3 - Votre drone est prêt à être larguer !")

                if (sous_marin.nom == "Tigre" or sous_marin.nom == "Ecureille") and sous_marin.d2 == True :
                    print("4 - Votre sonar est prêt à être lancer !")

                if sous_marin.nom == "Tigre" and sous_marin.spe == True :
                    print("5 - Votre silence est prêt à être lancer !")

                if sous_marin.nom == "Ecureille" and sous_marin.spe == True :
                    print("5 - Votre leurre est prêt à être lancer !")

                if (sous_marin.nom == "Tigre" or sous_marin.nom == "Ecureille") and emplacement_mines :
                    print("10 - Vous pouvez faire exploser votre mine !")

                #activer les systèmes à larguer
                while True :
                    try :
                        choix_systeme = int(input("\nSelectionner le système que vous voulez utiliser ou retourner en arrière (0): "))
                        
                        #torpille larguable
                        if (sous_marin.nom == "Tigre" or sous_marin.nom == "Ecureille") and sous_marin.a1 == True and choix_systeme == 1 :
                            fin, arme1 = sous_marin.larguer_torpille(sous_marin_ennemi, carte, derniere_colonne, derniere_ligne, capitaine_ennemie, nom_ennemi, nom_self, arme1, fin)
                            return fin, arme1, emplacement_mines, arme2, mine_cap

                        #mine largable
                        if (sous_marin.nom == "Tigre" or sous_marin.nom == "Ecureille") and sous_marin.a2 == True and choix_systeme == 2 :
                            x_y_mine, arme2, cap_m = sous_marin.larguer_mine(carte, derniere_colonne, derniere_ligne, arme2)
                            emplacement_mines.append(x_y_mine) #on ajoute les coordonnées de la mine larguer au tableau emplacement_mines
                            mine_cap.append(cap_m)
                            return fin, arme1, emplacement_mines, arme2, mine_cap

                        #explosion mine
                        if (sous_marin.nom == "Tigre" or sous_marin.nom == "Ecureille") and emplacement_mines and choix_systeme == 10 :
                            fin, emplacement_mines, mine_cap = sous_marin.exploser_mine(sous_marin_ennemi,  capitaine_ennemie, nom_ennemi, nom_self, emplacement_mines, mine_cap, carte, fin)
                            return fin, arme1, emplacement_mines, arme2, mine_cap

                        #
                        if (sous_marin.nom == "Tigre" or sous_marin.nom == "Ecureille") and sous_marin.d1 == True and choix_systeme == 3 :
                            #fonction lancer drone
                            print("sous_marin.larguer_drone()")
                            return fin, arme1, emplacement_mines, arme2, mine_cap

                        if (sous_marin.nom == "Tigre" or sous_marin.nom == "Ecureille") and sous_marin.d2 == True and choix_systeme == 4 :
                            #fonction lancer sonar
                            print("sous_marin.lancer_sonar()")
                            return fin, arme1, emplacement_mines, arme2, mine_cap

                        if sous_marin.nom == "Tigre" and sous_marin.spe == True and choix_systeme == 5 :
                            #fonction lancer silence
                            print("sous_marin.lancer_silence()")
                            return fin, arme1, emplacement_mines, arme2, mine_cap

                        if sous_marin.nom == "Ecureille" and sous_marin.spe == True and choix_systeme == 5 :
                            #fonction lancer leurre
                            print("sous_marin.lancer_leurre()")
                            return fin, arme1, emplacement_mines, arme2, mine_cap

                        if choix_systeme == 0 :
                            break

                        else :
                            print("❌ Veuillez sélectionner un système chargé !\n\n")

                    except ValueError :
                        print("❌ Veuillez entrer un chiffre valide !\n\n")

            elif choix == 1 :
                return fin, arme1, emplacement_mines, arme2, mine_cap
            
            else :
                print("❌ Veuillez entrer une option valide (1-2) !\n\n")

        except ValueError :
            print("❌ Veuillez sélectionner une option valide !\n\n")


        

#==========================================#
'''5) déplacer transparent équipe énnemie'''
#==========================================#

def deplacer_transparent(detecteur, nom, cap, Carte, derniere_colonne, derniere_ligne) :
    # Si le capitaine ennemi a annoncer un cap
    if cap == "SUD" or cap == "NORD" or cap == "OUEST" or cap == "EST" :
        print(changement)
        print(f"\n⚠⚠⚠ Attention ⚠⚠⚠ : \nC'est au détecteur {detecteur}, de l'équipe {nom} de jouer.\n")
        input("\nSUIVANT")

        print(f"\nLe capitaine ennemi à annoncer son cap : '{cap}' !")

        while True :
            try :
                y_lettre = input("\nChoisissez une colonne pour placer le cap ennemi : ")
                y = lettre_to_chiffre(y_lettre)
                x = int(input("Choisissez une ligne pour placer le cap ennemi : ")) - 1
                position = x, y

                if 0 <= y <= ord(derniere_colonne) - ord('A') and 0 <= x <= int(derniere_ligne) :
                    x_transparent, y_transparent = Carte.start_trans(cap, position) #ici, x et y corresponde au coordonnée de l'empacement du premier déplacement du sous marin ennemi sur le transparent adverse.
                    input("\nSUIVANT")
                    return x_transparent, y_transparent
                            
                else : 
                    print("❌ Entrez des coordonnées comprisent dans les limites de la map.\n\n")

            except ValueError :
                print("❌ Entrez des coordonnées valides.\n\n")

    else :
        print(f"Le capitaine ennemi a fait surface et n'annoncera pas de cap pendant 3 tours !")