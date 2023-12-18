#====================#
'''Class Sous-Marin'''
#====================#

class SousMarin:
    def __init__(self, nom, vie, baie_moteur, armement1, armement2, detection1, detection2, speciale, position):
        self.nom = nom
        self.vie = vie
        self.baie = baie_moteur
        self.a1 = armement1 #idée : mine à detection magnétique, 
        self.a2 = armement2 #idée : torpille Guidage par satellite, Guidage électromagnétique, Guidage par intelligence artificielle
        self.d1 = detection1 #sonar de tout les adjectifs, Magnétométrie, Capteurs électromagnétiques, Imagerie acoustique, gravimétrie
        self.d2 = detection2 #Détection optique, Capteurs infrarouges, Surveillance satellite
        self.spe = speciale #fade up, leurre, explosion
        self.pos = None
    
    def infos(self):
        print(f"\n========== Sous-marin {self.nom} ==========\n- Vie : {self.vie}\n- Armement : {self.a1}, {self.a2} \n- Moyen de detection : {self.d1}, {self.d2}\n- Spéciale : {self.spe}\n- Difficulté : {self.baie}\n")

    def definition_du_cadran(self):

        if self.baie == 1 :
            # Définition des valeurs spécifiques à chaque position
            #cadran ouest
            JAUNE_ARM = " JAUNE - ARM"
            JAUNE_SPE = " JAUNE - SPE"
            JAUNE_DET = " JAUNE - DET"
            NONE_ODET = " NONE  - DET"
            NONE1ORAD = " NONE  - RAD"
            NONE2ORAD = " NONE  - RAD"
    
            #cadran nord
            VERT__SPE = " VERT  - SPE"
            VERT__DET = " VERT  - DET"
            VERT__ARM = " VERT  - ARM"
            NONE_NDET = " NONE  - DET"
            NONE_NARM = " NONE  - ARM"
            NONE_NRAD = " NONE  - RAD"

            #cadran sud
            BLEU__DET = " BLEU  - DET"
            BLEU__SPE = " BLEU  - SPE"
            BLEU__ARM = " BLEU  - ARM"
            NONE_SARM = " NONE  - ARM"
            NONE_SSPE = " NONE  - SPE"
            NONE_SRAD = " NONE  - RAD"

            #cadran est
            JAUNE1ARM = " JAUNE - ARM"
            VERT1_SPE = " VERT  - SPE"
            BLEU1_SPE = " BLEU  - SPE"
            NONE_EDET = " NONE  - DET"
            NONE1ERAD = " NONE  - RAD"
            NONE2ERAD = " NONE  - RAD"

            # Définition des cadrans avec des listes
            cadran_ouest = [JAUNE_ARM, JAUNE_SPE, JAUNE_DET, NONE_ODET, NONE1ORAD, NONE2ORAD]
            cadran_nord = [VERT__SPE, VERT__DET, VERT__ARM, NONE_NDET, NONE_NARM, NONE_NRAD]
            cadran_sud = [BLEU__DET, BLEU__SPE, BLEU__ARM, NONE_SARM, NONE_SSPE, NONE_SRAD]
            cadran_est = [JAUNE1ARM, VERT1_SPE, BLEU1_SPE, NONE_EDET, NONE1ERAD, NONE2ERAD]

            return cadran_ouest, cadran_nord, cadran_sud, cadran_est
        
        elif self.baie == 2 : 
            #fonction d'une baie moteur numéro 2
            print(r)


    def afficher_baie_moteur(self, cadran_ouest, cadran_nord, cadran_sud, cadran_est):

        #cadran ouest
        JAUNE_ARM = cadran_ouest[0]
        JAUNE_SPE = cadran_ouest[1]
        JAUNE_DET = cadran_ouest[2]
        NONE_ODET = cadran_ouest[3]
        NONE1ORAD = cadran_ouest[4]
        NONE2ORAD = cadran_ouest[5]
    
        #cadran nord
        VERT__SPE = cadran_nord[0]
        VERT__DET = cadran_nord[1]
        VERT__ARM = cadran_nord[2]
        NONE_NDET = cadran_nord[3]
        NONE_NARM = cadran_nord[4]
        NONE_NRAD = cadran_nord[5]

        #cadran sud
        BLEU__DET = cadran_sud[0]
        BLEU__SPE = cadran_sud[1]
        BLEU__ARM = cadran_sud[2]
        NONE_SARM = cadran_sud[3]
        NONE_SSPE = cadran_sud[4]
        NONE_SRAD = cadran_sud[5]

        #cadran est
        JAUNE1ARM = cadran_est[0]
        VERT1_SPE = cadran_est[1]
        BLEU1_SPE = cadran_est[2]
        NONE_EDET = cadran_est[3]
        NONE1ERAD = cadran_est[4]
        NONE2ERAD = cadran_est[5]

        baie_moteur = f'''

                     /===\         ~         /===\         ~         /===\         ~         /===\ 
                     : O :         ~         : N :         ~         : S :         ~         : E :
                     \===/         ~         \===/         ~         \===/         ~         \===/
                /―――――――――――――\    ~    /―――――――――――――\    ~    /―――――――――――――\    ~    /―――――――――――――\ 
        1       |{ JAUNE_ARM} |    1    |{ VERT__SPE} |    1    |{ BLEU__DET} |    1    |{ JAUNE1ARM} |
        2       |{ JAUNE_SPE} |    2    |{ VERT__DET} |    2    |{ BLEU__SPE} |    2    |{ VERT1_SPE} |
        3       \{ JAUNE_DET} /    3    \{ VERT__ARM} /    3    \{ BLEU__ARM} /    3    \{ BLEU1_SPE} /
                 |―――――――――――|     ~     |―――――――――――|     ~     |―――――――――――|     ~     |―――――――――――|
        4       /{ NONE_ODET} \    4    /{ NONE_NDET} \    4    /{ NONE_SARM} \    4    /{ NONE_EDET} \ 
        5       |{ NONE1ORAD} |    5    |{ NONE_NARM} |    5    |{ NONE_SSPE} |    5    |{ NONE1ERAD} |
        6       |{ NONE2ORAD} |    6    |{ NONE_NRAD} |    6    |{ NONE_SRAD} |    6    |{ NONE2ERAD} |
                \―――――――――――――/    ~    \―――――――――――――/    ~    \―――――――――――――/    ~    \―――――――――――――/
                                   ~                       ~                       ~  
        '''

        baie_moteur = baie_moteur.replace('DET', '\033[38;5;208mDET\033[0m')\
                .replace('SPE', '\033[95mSPE\033[0m')\
                .replace('ARM', '\033[91mARM\033[0m')\
                .replace('JAUNE', '\033[38;5;228mJAUNE\033[0m')\
                .replace('BLEU', '\033[94mBLEU\033[0m')\
                .replace('VERT', '\033[92mVERT\033[0m')\
                .replace('NONE', '\033[38;5;52mNONE\033[0m')\
                .replace('RAD', '\033[38;5;52mRAD\033[0m')
                
        print(baie_moteur)


    def choisir_une_panne(self, choix_meca, cadran_ouest, cadran_nord, cadran_sud, cadran_est, cap):

        #cadran ouest
        JAUNE_ARM = cadran_ouest[0]
        JAUNE_SPE = cadran_ouest[1]
        JAUNE_DET = cadran_ouest[2]
        NONE_ODET = cadran_ouest[3]
        NONE1ORAD = cadran_ouest[4]
        NONE2ORAD = cadran_ouest[5]
    
        #cadran nord
        VERT__SPE = cadran_nord[0]
        VERT__DET = cadran_nord[1]
        VERT__ARM = cadran_nord[2]
        NONE_NDET = cadran_nord[3]
        NONE_NARM = cadran_nord[4]
        NONE_NRAD = cadran_nord[5]

        #cadran sud
        BLEU__DET = cadran_sud[0]
        BLEU__SPE = cadran_sud[1]
        BLEU__ARM = cadran_sud[2]
        NONE_SARM = cadran_sud[3]
        NONE_SSPE = cadran_sud[4]
        NONE_SRAD = cadran_sud[5]

        #cadran est
        JAUNE1ARM = cadran_est[0]
        VERT1_SPE = cadran_est[1]
        BLEU1_SPE = cadran_est[2]
        NONE_EDET = cadran_est[3]
        NONE1ERAD = cadran_est[4]
        NONE2ERAD = cadran_est[5]

        print(cap, choix_meca)
        print("début boucle : ", JAUNE1ARM)

        if cap == "OUEST" :

            if choix_meca == 1 :
                cadran_ouest[0] = " ̷J̷A̷U̷N̷E̷ ̷-̷ ̷A̷R̷M"

            elif choix_meca == 2 :
                cadran_ouest[1] = " ̷J̷A̷U̷N̷E̷ ̷-̷ ̷S̷P̷E"

            elif choix_meca == 3 :
                cadran_ouest[2] = " ̷J̷A̷U̷N̷E̷ ̷-̷ ̷D̷E̷T"

            elif choix_meca == 4 :
                cadran_ouest[3] = " ̷N̷O̷N̷E̷ ̷ ̷-̷ ̷D̷E̷T"

            elif choix_meca == 5 :
                cadran_ouest[4] = " ̷N̷O̷N̷E̷ ̷ ̷-̷ ̷R̷A̷D"

            elif choix_meca == 6 :
                cadran_ouest[5] = " ̷N̷O̷N̷E̷ ̷ ̷-̷ ̷R̷A̷D"

            else : 
                print("Sélectionner une panne comprise entre 1 et 6")

        elif cap == "NORD" :

            if choix_meca == 1 :
                cadran_nord[0] = " ̷V̷E̷R̷T̷ ̷ ̷-̷ ̷S̷P̷E"
        
            elif choix_meca == 2 :
                cadran_nord[1] = " ̷V̷E̷R̷T̷ ̷ ̷-̷ ̷D̷E̷T"

            elif choix_meca == 3 :
                cadran_nord[2] = " ̷V̷E̷R̷T̷ ̷ ̷-̷ ̷A̷R̷M"

            elif choix_meca == 4 :
                cadran_nord[3] = " ̷N̷O̷N̷E̷ ̷ ̷-̷ ̷D̷E̷T"

            elif choix_meca == 5 :
                cadran_nord[4] = " ̷N̷O̷N̷E̷ ̷ ̷-̷ ̷A̷R̷M"

            elif choix_meca == 6 :
                cadran_nord[5] = " ̷N̷O̷N̷E̷ ̷ ̷-̷ ̷R̷A̷D"

            else : 
                print("Sélectionner une panne comprise entre 1 et 6")

        elif cap == "SUD" :

            if choix_meca == 1 :
                cadran_sud[0] = " ̷B̷L̷E̷U̷ ̷ ̷-̷ ̷D̷E̷T"
        
            elif choix_meca == 2 :
                cadran_sud[1] = " ̷B̷L̷E̷U̷ ̷ ̷-̷ ̷S̷P̷E"

            elif choix_meca == 3 :
                cadran_sud[2] = " ̷B̷L̷E̷U̷ ̷ ̷-̷ ̷A̷R̷M"

            elif choix_meca == 4 :
                cadran_sud[3] = " ̷N̷O̷N̷E̷ ̷ ̷-̷ ̷A̷R̷M"

            elif choix_meca == 5 :
                cadran_sud[4] = " ̷N̷O̷N̷E̷ ̷ ̷-̷ ̷S̷P̷E"

            elif choix_meca == 6 :
                cadran_sud[5] = " ̷N̷O̷N̷E̷ ̷ ̷-̷ ̷R̷A̷D"

            else : 
                print("Sélectionner une panne comprise entre 1 et 6")

        elif cap == "EST" :

            if choix_meca == 1 :
                cadran_est[0] = " ̷J̷A̷U̷N̷E̷ ̷-̷ ̷A̷R̷M"
        
            elif choix_meca == 2 :
                cadran_est[1] = " ̷V̷E̷R̷T̷ ̷ ̷-̷ ̷S̷P̷E"

            elif choix_meca == 3 :
                cadran_est[2] = " ̷B̷L̷E̷U̷ ̷ ̷-̷ ̷S̷P̷E"

            elif choix_meca == 4 :
                cadran_est[3] = " ̷N̷O̷N̷E̷ ̷ ̷-̷ ̷D̷E̷T"

            elif choix_meca == 5 :
                cadran_est[4] = " ̷N̷O̷N̷E̷ ̷ ̷-̷ ̷R̷A̷D"

            elif choix_meca == 6 :
                cadran_est[5] = " ̷N̷O̷N̷E̷ ̷ ̷-̷ ̷R̷A̷D"

        else : 
            print("Sélectionner une panne comprise entre 1 et 6")

        print("fin boucle : ", JAUNE1ARM)
        
        print("\n\nVotre baie moteur après la panne choisis :")
        S1.afficher_baie_moteur(cadran_ouest, cadran_nord, cadran_sud, cadran_est)

        return cadran_ouest, cadran_nord, cadran_sud, cadran_est

    
    def torpiller(self, cible):
        if self == S1 :
            print(f"\nLe sous-marin {self.nom} tire une torpille sur le sous-marin {cible.nom} et prend 2 de dégats\n")
            cible.vie -= 2
            print(f"========== Sous-marin {cible.nom} ==========\n- Vie restante : {cible.vie}\n")
        elif self == S2:
            print(f"\nLe sous-marin {self.nom} tire une torpille sur le sous-marin {cible.nom} et prend 1 de dégats\n")
            cible.vie -=1
            print(f"========== Sous-marin {cible.nom} ==========\n- Vie restante : {cible.vie}\n")
        


#==========================#
'''Création de sous-marin'''
#==========================#

S1 = SousMarin("Tigre", 4, 1, "Mine a contact", "Torpille électrique a guidage acoustique actif", "Sonar passif", "Drone par magnétométrie", "Silence", None)
S2 = SousMarin("Ecureille", 3, 1, "Mine a déclanchement", "Torpille thermique a guidage acoustique passif", "Sonar actif", "Drone électomagnétiques", "Leurre", None)

