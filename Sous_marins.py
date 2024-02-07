import random

from Var_affichage import changement

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
        self.pos = position
    
    def infos(self):
        print(f"\n========== Sous-marin {self.nom} ==========\n- Vie : {self.vie}\n- Armement : {self.a1}, {self.a2} \n- Moyen de detection : {self.d1}, {self.d2}\n- Spéciale : {self.spe}\n- Difficulté : {self.baie}\n")

    #===================================#
    '''============CADRAN============='''
    #===================================#

    def definition_du_cadran(self):

        if self.baie == 1 :
            # Définition des valeurs spécifiques à chaque position
            #cadran ouest
            JAUNE_ARM = " JAUNE 1 ARM"
            JAUNE_SPE = " JAUNE 2 SPE"
            JAUNE_DET = " JAUNE 3 DET"
            NONE_ODET = " NONE  4 DET"
            NONE1ORAD = " NONE  5 RAD"
            NONE2ORAD = " NONE  6 RAD"
    
            #cadran nord
            VERT__SPE = " VERT  1 SPE"
            VERT__DET = " VERT  2 DET"
            VERT__ARM = " VERT  3 ARM"
            NONE_NDET = " NONE  4 DET"
            NONE_NARM = " NONE  5 ARM"
            NONE_NRAD = " NONE  6 RAD"

            #cadran sud
            BLEU__DET = " BLEU  1 DET"
            BLEU__SPE = " BLEU  2 SPE"
            BLEU__ARM = " BLEU  3 ARM"
            NONE_SARM = " NONE  4 ARM"
            NONE_SSPE = " NONE  5 SPE"
            NONE_SRAD = " NONE  6 RAD"

            #cadran est
            JAUNE1ARM = " JAUNE 1 ARM"
            VERT1_SPE = " VERT  2 SPE"
            BLEU1_SPE = " BLEU  3 SPE"
            NONE_EDET = " NONE  4 DET"
            NONE1ERAD = " NONE  5 RAD"
            NONE2ERAD = " NONE  6 RAD"

            # Définition des cadrans avec des listes
            cadran_ouest = [JAUNE_ARM, JAUNE_SPE, JAUNE_DET, NONE_ODET, NONE1ORAD, NONE2ORAD]
            cadran_nord = [VERT__SPE, VERT__DET, VERT__ARM, NONE_NDET, NONE_NARM, NONE_NRAD]
            cadran_sud = [BLEU__DET, BLEU__SPE, BLEU__ARM, NONE_SARM, NONE_SSPE, NONE_SRAD]
            cadran_est = [JAUNE1ARM, VERT1_SPE, BLEU1_SPE, NONE_EDET, NONE1ERAD, NONE2ERAD]

            self.baie_moteur = cadran_ouest, cadran_nord, cadran_sud, cadran_est

            return cadran_ouest, cadran_nord, cadran_sud, cadran_est
        
        elif self.baie == 2 : 
            #fonction d'une baie moteur numéro 2
            print("r pour le moment")


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
        ============================================= Baie moteur ====================================================

                     /===\         ~         /===\         ~         /===\         ~         /===\ 
                     : O :         ~         : N :         ~         : S :         ~         : E :
                     \===/         ~         \===/         ~         \===/         ~         \===/
                /―――――――――――――\    ~    /―――――――――――――\    ~    /―――――――――――――\    ~    /―――――――――――――\ 
                |{ JAUNE_ARM} |    ~    |{ VERT__SPE} |    ~    |{ BLEU__DET} |    ~    |{ JAUNE1ARM} |
                |{ JAUNE_SPE} |    ~    |{ VERT__DET} |    ~    |{ BLEU__SPE} |    ~    |{ VERT1_SPE} |
                \{ JAUNE_DET} /    ~    \{ VERT__ARM} /    ~    \{ BLEU__ARM} /    ~    \{ BLEU1_SPE} /
                 |―――――――――――|     ~     |―――――――――――|     ~     |―――――――――――|     ~     |―――――――――――|
                /{ NONE_ODET} \    ~    /{ NONE_NDET} \    ~    /{ NONE_SARM} \    ~    /{ NONE_EDET} \ 
                |{ NONE1ORAD} |    ~    |{ NONE_NARM} |    ~    |{ NONE_SSPE} |    ~    |{ NONE1ERAD} |
                |{ NONE2ORAD} |    ~    |{ NONE_NRAD} |    ~    |{ NONE_SRAD} |    ~    |{ NONE2ERAD} |
                \―――――――――――――/    ~    \―――――――――――――/    ~    \―――――――――――――/    ~    \―――――――――――――/
                                   ~                       ~                       ~  
        '''

        baie_moteur = baie_moteur.replace('DET', '\033[38;5;208mDET\033[0m')\
                                  .replace('SPE', '\033[95mSPE\033[0m')\
                                  .replace('ARM', '\033[91mARM\033[0m')\
                                  .replace('J̷A̷U̷N̷E', '\033[38;5;228mJ̷A̷U̷N̷E\033[0m')\
                                  .replace('JAUNE', '\033[38;5;228mJAUNE\033[0m')\
                                  .replace('BLEU', '\033[94mBLEU\033[0m')\
                                  .replace('V̷E̷R̷T', '\033[92mV̷E̷R̷T\u200D\033[0m')\
                                  .replace('B̷L̷E̷U', '\033[94mB̷L̷E̷U\u200D\033[0m')\
                                  .replace('VERT', '\033[92mVERT\033[0m')\
                                  .replace('NONE', '\033[38;5;52mNONE\033[0m')\
                                  .replace('RAD', '\033[38;5;52mRAD\033[0m')
                
        print(baie_moteur)


    def choisir_une_panne(self, choix_meca, cadran_ouest, cadran_nord, cadran_sud, cadran_est, cap, condition_panne_arm, condition_panne_spe, condition_panne_det):
        condition_voyant = False

        if cap == "OUEST" :

            if choix_meca == 1 and cadran_ouest[0] == " JAUNE 1 ARM":
                cadran_ouest[0] = " ̷J̷A̷U̷N̷E̷-̷ ̷A̷R̷M"
                condition_panne_arm = True
                condition_voyant = True

            elif choix_meca == 2 and cadran_ouest[1] == " JAUNE 2 SPE" :
                cadran_ouest[1] = " ̷J̷A̷U̷N̷E̷-̷ ̷S̷P̷E"
                condition_panne_spe = True
                condition_voyant = True

            elif choix_meca == 3 and cadran_ouest[2] == " JAUNE 3 DET" :
                cadran_ouest[2] = " ̷J̷A̷U̷N̷E̷-̷ ̷D̷E̷T"
                condition_panne_det = True
                condition_voyant = True

            elif choix_meca == 4 and cadran_ouest[3] == " NONE  4 DET" :
                cadran_ouest[3] = " ̷N̷O̷N̷E̷ ̷ ̷-̷ ̷D̷E̷T"
                condition_panne_det = True
                condition_voyant = True

            elif choix_meca == 5 and cadran_ouest[4] == " NONE  5 RAD" :
                cadran_ouest[4] = " ̷N̷O̷N̷E̷ ̷ ̷-̷ ̷R̷A̷D"
                condition_voyant = True

            elif choix_meca == 6 and cadran_ouest[5] == " NONE  6 RAD" :
                cadran_ouest[5] = " ̷N̷O̷N̷E̷ ̷ ̷-̷ ̷R̷A̷D"
                condition_voyant = True

            else : 
                print("Sélectionnez une panne du cadran OUEST comprise entre 1 et 6")

        elif cap == "NORD" :

            if choix_meca == 1 and cadran_nord[0] == " VERT  1 SPE" :
                cadran_nord[0] = " ̷V̷E̷R̷T̷ ̷-̷ ̷S̷P̷E"
                condition_panne_spe = True
                condition_voyant = True
        
            elif choix_meca == 2 and cadran_nord[1] == " VERT  2 DET" :
                cadran_nord[1] = " ̷V̷E̷R̷T̷ ̷-̷ ̷D̷E̷T"
                condition_panne_det = True
                condition_voyant = True

            elif choix_meca == 3 and cadran_nord[2] == " VERT  3 ARM" :
                cadran_nord[2] = " ̷V̷E̷R̷T̷ ̷-̷ ̷A̷R̷M"
                condition_panne_arm = True
                condition_voyant = True

            elif choix_meca == 4 and cadran_nord[3] == " NONE  4 DET" :
                cadran_nord[3] = " ̷N̷O̷N̷E̷ ̷ ̷-̷ ̷D̷E̷T"
                condition_panne_det = True
                condition_voyant = True

            elif choix_meca == 5 and cadran_nord[4] == " NONE  5 ARM" :
                cadran_nord[4] = " ̷N̷O̷N̷E̷ ̷ ̷-̷ ̷A̷R̷M"
                condition_panne_arm = True
                condition_voyant = True

            elif choix_meca == 6 and cadran_nord[5] == " NONE  6 RAD" :
                cadran_nord[5] = " ̷N̷O̷N̷E̷ ̷ ̷-̷ ̷R̷A̷D"
                condition_voyant = True

            else : 
                print("Sélectionnez une panne du cadran NORD comprise entre 1 et 6")

        elif cap == "SUD" :

            if choix_meca == 1 and cadran_sud[0] == " BLEU  1 DET" :
                cadran_sud[0] = " ̷B̷L̷E̷U̷ ̷-̷ ̷D̷E̷T"
                condition_panne_det = True
                condition_voyant = True
        
            elif choix_meca == 2 and cadran_sud[1] == " BLEU  2 SPE" :
                cadran_sud[1] = " ̷B̷L̷E̷U̷ ̷-̷ ̷S̷P̷E"
                condition_panne_spe = True
                condition_voyant = True

            elif choix_meca == 3 and cadran_sud[2] == " BLEU  3 ARM" :
                cadran_sud[2] = " ̷B̷L̷E̷U̷ ̷-̷ ̷A̷R̷M"
                condition_panne_arm = True
                condition_voyant = True

            elif choix_meca == 4 and cadran_sud[3] == " NONE  4 ARM" :
                cadran_sud[3] = " ̷N̷O̷N̷E̷ ̷ ̷-̷ ̷A̷R̷M"
                condition_panne_arm = True
                condition_voyant = True

            elif choix_meca == 5 and cadran_sud[4] == " NONE  5 SPE" :
                cadran_sud[4] = " ̷N̷O̷N̷E̷ ̷ ̷-̷ ̷S̷P̷E"
                condition_panne_spe = True
                condition_voyant = True

            elif choix_meca == 6 and cadran_sud[5] == " NONE  6 RAD" :
                cadran_sud[5] = " ̷N̷O̷N̷E̷ ̷ ̷-̷ ̷R̷A̷D"
                condition_voyant = True

            else : 
                print("Sélectionnez une panne du cadran SUD comprise entre 1 et 6")

        elif cap == "EST" :

            if choix_meca == 1 and cadran_est[0] == " JAUNE 1 ARM" :
                cadran_est[0] = " ̷J̷A̷U̷N̷E̷-̷ ̷A̷R̷M"
                condition_panne_arm = True
                condition_voyant = True
        
            elif choix_meca == 2 and cadran_est[1] == " VERT  2 SPE" :
                cadran_est[1] = " ̷V̷E̷R̷T̷ ̷-̷ ̷S̷P̷E"
                condition_panne_spe = True
                condition_voyant = True

            elif choix_meca == 3 and cadran_est[2] == " BLEU  3 SPE" :
                cadran_est[2] = " ̷B̷L̷E̷U̷ ̷-̷ ̷S̷P̷E"
                condition_panne_spe = True
                condition_voyant = True

            elif choix_meca == 4 and cadran_est[3] == " NONE  4 DET" :
                cadran_est[3] = " ̷N̷O̷N̷E̷ ̷ ̷-̷ ̷D̷E̷T"
                condition_panne_det = True
                condition_voyant = True

            elif choix_meca == 5 and cadran_est[4] == " NONE  5 RAD" :
                cadran_est[4] = " ̷N̷O̷N̷E̷ ̷ ̷-̷ ̷R̷A̷D"
                condition_voyant = True

            elif choix_meca == 6 and cadran_est[5] == " NONE  6 RAD" :
                cadran_est[5] = " ̷N̷O̷N̷E̷ ̷ ̷-̷ ̷R̷A̷D"
                condition_voyant = True

            else : 
                print("Sélectionnez une panne du cadran EST comprise entre 1 et 6")

        # Si le sous marin fait surface, toutes les pannes sont réparées.
        elif cap == "AUCUN" :
            cadran_ouest[0] = " JAUNE 1 ARM"
            cadran_ouest[1] = " JAUNE 2 SPE"
            cadran_ouest[2] = " JAUNE 3 DET"
            cadran_ouest[3] = " NONE  4 DET"
            cadran_ouest[4] = " NONE  5 RAD"
            cadran_ouest[5] = " NONE  6 RAD"

            cadran_nord[0] = " VERT  1 SPE"
            cadran_nord[1] = " VERT  2 DET"
            cadran_nord[2] = " VERT  3 ARM"
            cadran_nord[3] = " NONE  4 DET"
            cadran_nord[4] = " NONE  5 ARM"
            cadran_nord[5] = " NONE  6 RAD"

            cadran_sud[0] = " BLEU  1 DET"
            cadran_sud[1] = " BLEU  2 SPE"
            cadran_sud[2] = " BLEU  3 ARM"
            cadran_sud[3] = " NONE  4 ARM"
            cadran_sud[4] = " NONE  5 SPE"
            cadran_sud[5] = " NONE  6 RAD"

            cadran_est[0] = " JAUNE 1 ARM"
            cadran_est[1] = " VERT  2 SPE"
            cadran_est[2] = " BLEU  3 SPE"
            cadran_est[3] = " NONE  4 DET"
            cadran_est[4] = " NONE  5 RAD"
            cadran_est[5] = " NONE  6 RAD"


        # Si toutes les pannes des couleurs sont cochés, alors tout est réparé
        if cadran_est[0] == " ̷J̷A̷U̷N̷E̷-̷ ̷A̷R̷M" and cadran_ouest[2] == " ̷J̷A̷U̷N̷E̷-̷ ̷D̷E̷T" and cadran_ouest[1] == " ̷J̷A̷U̷N̷E̷-̷ ̷S̷P̷E" and cadran_ouest[0] == " ̷J̷A̷U̷N̷E̷-̷ ̷A̷R̷M" :
            cadran_est[0] = " JAUNE 1 ARM"
            cadran_ouest[0] = " JAUNE 1 ARM"
            cadran_ouest[1] = " JAUNE 2 SPE"
            cadran_ouest[2] = " JAUNE 3 DET"
            print("\n\nVous avez réparé les pannes jaune !")
        
        if cadran_nord[0] == " ̷V̷E̷R̷T̷ ̷-̷ ̷S̷P̷E" and cadran_nord[1] == " ̷V̷E̷R̷T̷ ̷-̷ ̷D̷E̷T" and cadran_nord[2] == " ̷V̷E̷R̷T̷ ̷-̷ ̷A̷R̷M" and cadran_est[1] == " ̷V̷E̷R̷T̷ ̷-̷ ̷S̷P̷E" :
            cadran_nord[0] = " VERT  1 SPE"
            cadran_nord[1] = " VERT  2 DET"
            cadran_nord[2] = " VERT  3 ARM"
            cadran_est[1] = " VERT  2 SPE"
            print("\n\nVous avez réparé les pannes vertes !")

        if cadran_sud[0] != " BLEU  1 DET" and cadran_sud[1] != " BLEU  2 SPE" and cadran_sud[2] != " BLEU  3 ARM" and cadran_est[2] != " BLEU  3 SPE" :
            cadran_sud[0] = " BLEU  1 DET"
            cadran_sud[1] = " BLEU  2 SPE"
            cadran_sud[2] = " BLEU  3 ARM"
            cadran_est[2] = " BLEU  3 SPE"
            print("\n\nVous avez réparé les pannes bleu !")
        
        # Si toutes les pannes d'un cadran son coché, alors elles sont toutes réparé mais le sous marin prend un de dégat !
        if cadran_ouest[0] == " ̷J̷A̷U̷N̷E̷-̷ ̷A̷R̷M" and cadran_ouest[1] == " ̷J̷A̷U̷N̷E̷-̷ ̷S̷P̷E" and cadran_ouest[2] == " ̷J̷A̷U̷N̷E̷-̷ ̷D̷E̷T" and cadran_ouest[3] == " ̷N̷O̷N̷E̷ ̷ ̷-̷ ̷D̷E̷T" and cadran_ouest[4] == " ̷N̷O̷N̷E̷ ̷ ̷-̷ ̷R̷A̷D" and cadran_ouest[5] == " ̷N̷O̷N̷E̷ ̷ ̷-̷ ̷R̷A̷D" :
            cadran_ouest[0] = " JAUNE 1 ARM"
            cadran_ouest[1] = " JAUNE 2 SPE"
            cadran_ouest[2] = " JAUNE 3 DET"
            cadran_ouest[3] = " NONE  4 DET"
            cadran_ouest[4] = " NONE  5 RAD"
            cadran_ouest[5] = " NONE  6 RAD"
            print("\n\nToutes les pannes du cadran OUEST ont été cochées, toutes vos pannes de ce cadran sont réparées mais vous subissez un de dégât !")
            self.vie -= 1
            print(f"\n========== Sous-marin {self.nom} ==========\n- Vie : {self.vie}")

        if cadran_nord[0] == " ̷V̷E̷R̷T̷ ̷-̷ ̷S̷P̷E" and cadran_nord[1] == " ̷V̷E̷R̷T̷ ̷-̷ ̷D̷E̷T" and cadran_nord[2] == " ̷V̷E̷R̷T̷ ̷-̷ ̷A̷R̷M" and cadran_nord[3] == " ̷N̷O̷N̷E̷ ̷ ̷-̷ ̷D̷E̷T" and cadran_nord[4] == " ̷N̷O̷N̷E̷ ̷ ̷-̷ ̷A̷R̷M" and cadran_nord[5] == " ̷N̷O̷N̷E̷ ̷ ̷-̷ ̷R̷A̷D" :
            cadran_nord[0] = " VERT  1 SPE"
            cadran_nord[1] = " VERT  2 DET"
            cadran_nord[2] = " VERT  3 ARM"
            cadran_nord[3] = " NONE  4 DET"
            cadran_nord[4] = " NONE  5 ARM"
            cadran_nord[5] = " NONE  6 RAD"
            print("\n\nToutes les pannes du cadran NORD ont été cochées, toutes vos pannes de ce cadran sont réparées mais vous subissez un de dégât !")
            self.vie -= 1
            print(f"\n========== Sous-marin {self.nom} ==========\n- Vie : {self.vie}")

        if cadran_sud[0] == " ̷B̷L̷E̷U̷ ̷-̷ ̷D̷E̷T" and cadran_sud[1] == " ̷B̷L̷E̷U̷ ̷-̷ ̷S̷P̷E" and cadran_sud[2] == " ̷B̷L̷E̷U̷ ̷-̷ ̷A̷R̷M" and cadran_sud[3] == " ̷N̷O̷N̷E̷ ̷ ̷-̷ ̷A̷R̷M" and cadran_sud[4] == " ̷N̷O̷N̷E̷ ̷ ̷-̷ ̷S̷P̷E" and cadran_sud[5] == " ̷N̷O̷N̷E̷ ̷ ̷-̷ ̷R̷A̷D" :
            cadran_sud[0] = " BLEU  1 DET"
            cadran_sud[1] = " BLEU  2 SPE"
            cadran_sud[2] = " BLEU  3 ARM"
            cadran_sud[3] = " NONE  4 ARM"
            cadran_sud[4] = " NONE  5 SPE"
            cadran_sud[5] = " NONE  6 RAD"
            print("\n\nToutes les pannes du cadran SUD ont été cochées, toutes vos pannes de ce cadran sont réparées mais vous subissez un de dégât !")
            self.vie -= 1
            print(f"\n========== Sous-marin {self.nom} ==========\n- Vie : {self.vie}")

        if cadran_est[0] == " ̷J̷A̷U̷N̷E̷-̷ ̷A̷R̷M" and cadran_est[1] == " ̷V̷E̷R̷T̷ ̷-̷ ̷S̷P̷E" and cadran_est[2] == " ̷B̷L̷E̷U̷ ̷-̷ ̷S̷P̷E" and cadran_est[3] == " ̷N̷O̷N̷E̷ ̷ ̷-̷ ̷D̷E̷T" and cadran_est[4] == " ̷N̷O̷N̷E̷ ̷ ̷-̷ ̷R̷A̷D" and cadran_est[5] == " ̷N̷O̷N̷E̷ ̷ ̷-̷ ̷R̷A̷D" :
            cadran_est[0] = " JAUNE 1 ARM"
            cadran_est[1] = " VERT  2 SPE"
            cadran_est[2] = " BLEU  3 SPE"
            cadran_est[3] = " NONE  4 DET"
            cadran_est[4] = " NONE  5 RAD"
            cadran_est[5] = " NONE  6 RAD"
            print("\n\nToutes les pannes du cadran SUD ont été cochées, toutes vos pannes de ce cadran sont réparées mais vous subissez un de dégât !")
            self.vie -= 1
            print(f"\n========== Sous-marin {self.nom} ==========\n- Vie : {self.vie}")

        # Si toutes les pannes RAD sont cochées, alors elles sont réparées et le sous-marin perd 1 pv
        if cadran_ouest[4] == " ̷N̷O̷N̷E̷ ̷ ̷-̷ ̷R̷A̷D" and cadran_ouest[5] == " ̷N̷O̷N̷E̷ ̷ ̷-̷ ̷R̷A̷D" and cadran_nord[5] == " ̷N̷O̷N̷E̷ ̷ ̷-̷ ̷R̷A̷D" and cadran_sud[5] == " ̷N̷O̷N̷E̷ ̷ ̷-̷ ̷R̷A̷D" and cadran_est[4] == " ̷N̷O̷N̷E̷ ̷ ̷-̷ ̷R̷A̷D" and cadran_est[5] == " ̷N̷O̷N̷E̷ ̷ ̷-̷ ̷R̷A̷D":
            cadran_ouest[4] = " NONE  5 RAD"
            cadran_ouest[5] = " NONE  6 RAD"
            cadran_nord[5] = " NONE  6 RAD"
            cadran_sud[5] = " NONE  6 RAD"
            cadran_est[4] = " NONE  5 RAD"
            cadran_est[5] = " NONE  6 RAD"
            print("\n\nToutes les pannes RAD ont été cochées, toutes vos pannes RAD sont réparées mais vous subissez un de dégât !")
            self.vie -= 1
            print(f"\n========== Sous-marin {self.nom} ==========\n- Vie : {self.vie}")

        #Changement d'état des variables de conditions pour savoir si l'on peut lancer ou non une capacité
        #ARM
        if cadran_ouest[0] == " JAUNE 1 ARM" and cadran_nord[2] == " VERT  3 ARM" and cadran_nord[4] == " NONE  5 ARM" and cadran_sud[2] == " BLEU  3 ARM" and cadran_sud[3] == " NONE  4 ARM" and cadran_est[0] == " JAUNE 1 ARM" :
            condition_panne_arm = False
        
        if cadran_ouest[1] == " JAUNE 2 SPE" and cadran_nord[0] == " VERT  1 SPE" and cadran_sud[1] == " BLEU  2 SPE" and cadran_sud[4] == " NONE  5 SPE" and cadran_est[1] == " VERT  2 SPE" and cadran_est[2] == " BLEU  3 SPE" :
            condition_panne_spe = False
        
        if cadran_ouest[2] == " JAUNE 3 DET" and cadran_ouest[3] == " NONE  4 DET" and cadran_nord[1] == " VERT  2 DET" and cadran_nord[3] == " NONE  4 DET" and cadran_sud[0] == " BLEU  1 DET" and cadran_est[3] == " NONE  4 DET" :
            condition_panne_det = False

        self.baie_moteur = cadran_ouest, cadran_nord, cadran_sud, cadran_est
        self.afficher_baie_moteur(cadran_ouest, cadran_nord, cadran_sud, cadran_est)

        return cadran_ouest, cadran_nord, cadran_sud, cadran_est, condition_panne_arm, condition_panne_spe, condition_panne_det, condition_voyant

    #=====================================#
    '''=============SYSTEMES============'''
    #=====================================#

    def def_systeme(self) :
        a1 = "0"
        a2 = "0"
        a3 = "0"
        a4 = "0"
        a5 = "0"
        a6 = "0"

        b1 = "0"
        b2 = "0"
        b3 = "0"
        b4 = "0"
        b5 = "0"
        b6 = "0"

        c1 = "0"
        c2 = "0"
        c3 = "0"
        c4 = "0"
        c5 = "0"
        c6 = "0"

        d1 = "0"
        d2 = "0"
        d3 = "0"
        d4 = "0"
        d5 = "0"
        d6 = "0"

        e1 = "0"
        e2 = "0"
        e3 = "0"
        e4 = "0"
        e5 = "0"
        e6 = "0"

        f1 = "0"
        f2 = "0"
        f3 = "0"
        f4 = "0"
        f5 = "0"
        f6 = "0"

        arme1 = [a1, a2, a3, a4, a5, a6]
        arme2 = [b1, b2, b3, b4, b5, b6]
        dete1 = [c1, c2, c3, c4, c5, c6]
        dete2 = [d1, d2, d3, d4, d5, d6]
        spe = [e1, e2, e3, e4, e5, e6]
        spe2 = [f1, f2, f3, f4, f5, f6]

        return arme1, arme2, dete1, dete2, spe


    def charger_systeme(self, choix, arme1, arme2, dete1, dete2, spe):
        
        condition_charge = True 

        #=========#
        '''Tigre'''
        #=========#
        
        if self.nom == "Tigre" :
            if choix == 1 :
                for i in range(3) :
                    if arme1[i] == "0" :
                        arme1[i] = "#"
                        break

                    elif self.a1 == True : 
                        print("Votre torpille est déjà chargée !")
                        condition_charge = False
                        return condition_charge, arme1, arme2, dete1, dete2, spe
            
            elif choix == 2 :
                for i in range(3) :
                    if arme2[i] == "0" :
                        arme2[i] = "#"
                        break

                    elif self.a2 == True : 
                        print("Votre mine est déjà chargée !")
                        condition_charge = False
                        return condition_charge, arme1, arme2, dete1, dete2, spe

            elif choix == 3 :
                for i in range(4) :
                    if dete1[i] == "0" :
                        dete1[i] = "#" 
                        break

                    elif self.d1 == True : 
                        print("Votre drone est déjà chargée !")
                        condition_charge = False
                        return condition_charge, arme1, arme2, dete1, dete2, spe

            elif choix == 4 :
                for i in range(3) :
                    if dete2[i] == "0" :
                        dete2[i] = "#" 
                        break

                    elif self.d2 == True : 
                        print("Votre sonar est déjà chargée !")
                        condition_charge = False
                        return condition_charge, arme1, arme2, dete1, dete2, spe

            elif choix == 5 :
                for i in range(6) :
                    if spe[i] == "0" :
                        spe[i] = "#" 
                        break

                    elif self.spe == True : 
                        print("Votre silence est déjà chargée !")
                        condition_charge = False
                        return condition_charge, arme1, arme2, dete1, dete2, spe

            if arme1[0] == "#" and arme1[1] == "#" and arme1[2] == "#" :
                self.a1 = True
            
            if arme2[0] == "#" and arme2[1] == "#" and arme2[2] == "#" :
                self.a2 = True

            if dete1[0] == "#" and dete1[1] == "#" and dete1[2] == "#" and dete1[3] == "#":
                self.d1 = True

            if dete2[0] == "#" and dete2[1] == "#" and dete2[2] == "#" :
                self.d2 = True

            if spe[0] == "#" and spe[1] == "#" and spe[2] == "#" and spe[3] == "#" and spe[4] == "#" and spe[5] == "#" :
                self.spe = True

        #=============#
        '''Ecureille'''
        #=============#

        if self.nom == "Ecureille" :
            if choix == 1 :
                for i in range(3) :
                    if arme1[i] == "0" :
                        arme1[i] = "#"
                        break

                    elif self.a1 == True : 
                        print("Votre torpille est déjà chargée !")
                        condition_charge = False
                        return condition_charge, arme1, arme2, dete1, dete2, spe
            
            elif choix == 2 :
                for i in range(4) :
                    if arme2[i] == "0" :
                        arme2[i] = "#"
                        break

                    elif self.a2 == True : 
                        print("Votre mine est déjà chargée !")
                        condition_charge = False
                        return condition_charge, arme1, arme2, dete1, dete2, spe

            elif choix == 3 :
                for i in range(4) :
                    if dete1[i] == "0" :
                        dete1[i] = "#" 
                        break

                    elif self.d1 == True : 
                        print("Votre drone est déjà chargée !")
                        condition_charge = False
                        return condition_charge, arme1, arme2, dete1, dete2, spe

            elif choix == 4 :
                for i in range(3) :
                    if dete2[i] == "0" :
                        dete2[i] = "#" 
                        break

                    elif self.d2 == True : 
                        print("Votre sonar est déjà chargée !")
                        condition_charge = False
                        return condition_charge, arme1, arme2, dete1, dete2, spe

            elif choix == 5 :
                for i in range(6) :
                    if spe[i] == "0" :
                        spe[i] = "#" 
                        break
                    
                    elif self.spe == True : 
                        print("Votre leurre est déjà chargée !")
                        condition_charge = False
                        return condition_charge, arme1, arme2, dete1, dete2, spe

            if arme1[0] == "#" and arme1[1] == "#" and arme1[2] == "#" :
                self.a1 = True
            
            if arme2[0] == "#" and arme2[1] == "#" and arme2[2] == "#" and arme2[3] == "#":
                self.a2 = True

            if dete1[0] == "#" and dete1[1] == "#" and dete1[2] == "#" :
                self.d1 = True

            if dete2[0] == "#" and dete2[1] == "#" and dete2[2] == "#" :
                self.d2 = True

            if spe[0] == "#" and spe[1] == "#" and spe[2] == "#" and spe[3] == "#" and spe[4] == "#" and spe[5] == "#" :
                self.spe = True

        if choix == 1 :
            choix = "la torpille"
            
        if choix == 2 :
            choix = "la mine"

        if choix == 3 :
            choix = "le drone"

        if choix == 4 :
            choix = "le sonar"

        if self.nom == "Tigre" and choix == 5 :
            choix = "le silence"

        if self.nom == "Ecureille" and choix == 5 :
            choix = "le leurre"

        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print(f"Vous avez chargé {choix} :")
        self.afficher_systeme(arme1, arme2, dete1, dete2, spe)

        return condition_charge, arme1, arme2, dete1, dete2, spe


    def afficher_systeme(self, arme1, arme2, dete1, dete2, spe) :
        a1 = arme1[0]
        a2 = arme1[1]
        a3 = arme1[2]
        a4 = arme1[3]
        a5 = arme1[4]
        a6 = arme1[5]

        b1 = arme2[0]
        b2 = arme2[1]
        b3 = arme2[2]
        b4 = arme2[3]
        b5 = arme2[4]
        b6 = arme2[5]

        c1 = dete1[0]
        c2 = dete1[1]
        c3 = dete1[2]
        c4 = dete1[3]
        c5 = dete1[4]
        c6 = dete1[5]

        d1 = dete2[0]
        d2 = dete2[1]
        d3 = dete2[2]
        d4 = dete2[3]
        d5 = dete2[4]
        d6 = dete2[5]

        e1 = spe[0]
        e2 = spe[1]
        e3 = spe[2]
        e4 = spe[3]
        e5 = spe[4]
        e6 = spe[5]


        if self.nom == "Tigre" :
            systemes = f'''\n        
            ============================================= Systèmes ====================================================

                ――――――――――――――――          ~          ――――――――――――――――          ~          ――――――――――――――――
                | 1 - Torpille |          ~          |  3 - Drone   |          ~          | 5 - Silence  |
                ――――――――――――――――          ~          ――――――――――――――――          ~          ――――――――――――――――
                |      __      |          ~          |     .--.     |          ~          |              | - {e6}
                |     /  \     |          ~          |    ( | o)    |          ~          |     .--.     | - {e5}
                |     |  |     |          ~          |  *>------    | - {c4}      ~          |    (o  o)    | - {e4}
                |     |  |     | - {a3}      ~          |   (      )   | - {c3}      ~          |   /_ O  _\   | - {e3}
                |    / == \    | - {a2}      ~          |    |/^^\|    | - {c2}      ~          |     \   \    | - {e2}
                |    |/**\|    | - {a1}      ~          |     ****     | - {c1}      ~          |      `~~~'   | - {e1}
                ――――――――――――――――          ~          ――――――――――――――――          ~          ――――――――――――――――

                ――――――――――――――――          ~          ――――――――――――――――          ~
                |   2 - Mine   |          ~          |   4 - Sonar  |          ~
                ――――――――――――――――          ~          ――――――――――――――――          ~
                |              |          ~          |    ______    |          ~
                |     _--_     |          ~          |   /     /\   |          ~
                |    ( || )    |          ~          |  /    °/  \  |          ~
                |    ―-II-―    | - {b3}      ~          | (     /    ) | - {d3}      ~
                |    ( || )    | - {b2}      ~          |  \        /  | - {d2}      ~
                |     '――'     | - {b1}      ~          |   \______/   | - {d1}      ~
                ――――――――――――――――          ~          ――――――――――――――――          ~
                '''

        
        #=============#
        '''Ecureille'''
        #=============#
        
        if self.nom == "Ecureille" :
            systemes = f'''            
            ============================================= Systèmes ====================================================

                ――――――――――――――――          ~          ――――――――――――――――          ~          ――――――――――――――――
                | 1 - Torpille |          ~          |  3 - Drone   |          ~          | 5 - Leurre   |
                ――――――――――――――――          ~          ――――――――――――――――          ~          ___/|―――――――――――
                |      /\      |          ~          |              |          ~          |   |  /|      | - {e6}
                |     /..\     |          ~          |     .--.     |          ~          |   | /_/ ,    | - {e5}
                |     |  |     |          ~          | ~\ ( | o)    |          ~          |   |/o \/|    | - {e4}
                |     |  |     | - {a3}      ~          | ~X>------    | - {c3}      ~          |    \<_/\|    | - {e3}
                |    / __ \    | - {a2}      ~          | ~/(      )   | - {c2}      ~          |     \ \ `    | - {e2}
                |    |/**\|    | - {a1}      ~          |    '-__-'    | - {c1}      ~          |      \|      | - {e1}
                ――――――――――――――――          ~          ――――――――――――――――          ~          ――――――――――――――――

                ――――――――――――――――          ~          ――――――――――――――――          ~
                |   2 - Mine   |          ~          |   4 - Sonar  |          ~
                ――――――――――――――――          ~          ――――――――――――――――          ~ 
                |              |          ~          |    ______    |          ~
                |    _.--._    |          ~          |   /     /\   |          ~
                |   ( \||/ )   | - {b4}      ~          |  /     /  \  |          ~
                |    ―-II-―    | - {b3}      ~          | |     /    | | - {d3}      ~
                |   ( /||\ )   | - {b2}      ~          |  \ °      /  | - {d2}      ~
                |    '-――-'    | - {b1}      ~          |   \______/   | - {d1}      ~
                ――――――――――――――――          ~          ――――――――――――――――          ~
            '''

        systemes = systemes.replace('Drone', '\033[38;5;208mDrone\033[0m')\
                            .replace('Silence', '\033[95mSilence\033[0m')\
                            .replace('Leurre', '\033[95mLeurre\033[0m')\
                            .replace('Sonar', '\033[38;5;208mSonar\033[0m')\
                            .replace('Torpille', '\033[91mTorpille\033[0m')\
                            .replace('Mine', '\033[91mMine\033[0m')\
                            .replace('#', '\033[92m#\033[0m')\
                            
        print(systemes)


    #================================================#
    '''============ACTIVATION SYSTEMES============='''
    #================================================#

    def larguer_torpille(self, sous_marin_ennemi, carte, derniere_colonne, derniere_ligne, capitaine_ennemi, nom_e, nom_self, arme1, fin):

        #=====================#
        '''Tigre - Ecureille'''
        #=====================#

        if self.nom == "Tigre" or self.nom == "Ecureille" :
            print("\nSelectionner un emplacement sur la map :")
            carte.Afficher_carte()
            
            while True :
                try :
                    y_lettre = input("\nChoisissez une colonne : ")
                    y = lettre_to_chiffre(y_lettre)
                    x = int(input("Choisissez une ligne : ")) - 1
                    emplacement_tir = x, y
                    distance_x = abs(self.pos[0] - x) 
                    distance_y = abs(self.pos[1] - y)
                    #distance totale parcouru par le missile
                    distance_totale = distance_x + distance_y

                    if y != "alpha" :
                        if 0 <= y <= ord(derniere_colonne) - ord('A') and 0 <= x <= int(derniere_ligne) :
                            if (self.nom == "Tigre" and distance_totale <= 4) or (self.nom == "Ecureille" and distance_totale <= 5) :
                                #on reset graphiquement le chargement de l'arme
                                for i in range(6):
                                    arme1[i] = "0"

                                #on reset la valeur de l'armement1 à False pour que le jeu comprenne que la torpille a été tirée
                                self.a1 = False

                                print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

                                #le sous-marin se tir dessus
                                if emplacement_tir == self.pos :
                                    print(f"\nVous avez tirer une torpille en plein sur VOTRE SOUS-MARIN !!! \nVous prennez 2 points de dégats !!!\nVous entendez votre équipage crier : 'LE CAPITAINE EST DEVENU FOU ?!'\n")
                                    self.vie -= 2
                                    print(f"========== Sous-marin '{nom_self}' ==========\n- Vie restante : {self.vie}❤️\n")

                                    if self.vie <= 0 :
                                        #fin de game
                                        fin = True
                                
                                #le sous marin tir sur un emplacement à côté de lui
                                elif ((x == self.pos[0]+1 or x == self.pos[0]-1) and (y == self.pos[1]+1 or y == self.pos[1]-1)) or ((x == self.pos[0]+1 or x == self.pos[0]-1) and (y == self.pos[1])) or ((y == self.pos[1]+1 or y == self.pos[1]-1) and (x == self.pos[0])) :
                                    print(f"\nVous avez tirer une torpille à côté de votre propre sous-marin ! \nVous prennez 1 point de dégats !\n\n")
                                    self.vie -= 1
                                    print(f"========== Sous-marin '{nom_self}' ==========\n- Vie restante : {self.vie}❤️\n")
                                    
                                    if self.vie <= 0 :
                                        #fin de game
                                        fin = True

                                #si l'emplacement du tir est égale à la position du sous marin ennemi.
                                if emplacement_tir == sous_marin_ennemi.pos :
                                    print(f"\n\nLe capitaine adverse '{capitaine_ennemi}' annonce : \n🚨 IMPACT DIRECT !🚨")
                                    print(f"\nVous avez tirer une torpille en plein sur le sous-marin ennemi '{nom_e}' ! \nIl prend 2 points de dégats !!!\n")
                                    sous_marin_ennemi.vie -= 2
                                    print(f"========== Sous-marin '{nom_e}' ==========\n- Vie restante : {sous_marin_ennemi.vie}❤️\n")
                                    
                                    if sous_marin_ennemi.vie <= 0 :
                                        #fin de game
                                        fin = True

                                    input("SUIVANT")
                                    return fin, arme1

                                #La première condition and (les deux premières parenthèses) vérifie si l'emplacement du tir est dans la diagonale du sous marin ennemi. Le deux suivante check si le tir se situe à côté horizontalement du sm ennemi. Et les deux dernières check si le tir a été fait à côté verticalement du sm ennemi. Un peu indigeste, mais ca marche
                                elif ((x == sous_marin_ennemi.pos[0]+1 or x == sous_marin_ennemi.pos[0]-1) and (y == sous_marin_ennemi.pos[1]+1 or y == sous_marin_ennemi.pos[1]-1)) or ((x == sous_marin_ennemi.pos[0]+1 or x == sous_marin_ennemi.pos[0]-1) and (y == sous_marin_ennemi.pos[1])) or ((y == sous_marin_ennemi.pos[1]+1 or y == sous_marin_ennemi.pos[1]-1) and (x == sous_marin_ennemi.pos[0])):
                                    print(f"\n\nLe capitaine adverse '{capitaine_ennemi}' annonce : \n🚨 IMPACT INDIRECT !🚨")
                                    print(f"\nVous avez tirer une torpille juste à côté sous-marin ennemi '{nom_e}' ! \nIl prend tout de même 1 point de dégats !\n")
                                    sous_marin_ennemi.vie -= 1
                                    print(f"========== Sous-marin '{nom_e}' ==========\n- Vie restante : {sous_marin_ennemi.vie}❤️\n")
                                    
                                    if sous_marin_ennemi.vie <= 0 :
                                        #fin de game
                                        fin = True
                                    
                                    input("SUIVANT")
                                    return fin, arme1

                                #l'emplacement du tir est ni sur le sous-marin ennemi ni à ses alentours.
                                else :
                                    print(f"\n\nLe capitaine adverse '{capitaine_ennemi}' annonce : \n🚨 RAS !🚨") 
                                    print(f"\nVous avez tirer une torpille dans le vide !\n")
                                    print(f"========== Sous-marin '{nom_e}' ==========\n- Vie restante : {sous_marin_ennemi.vie}❤️\n")
                                    input("\nSUIVANT")
                                    return fin, arme1

                            else :
                                if self.nom == "Tigre" :
                                    print("\n\n❌ Votre sous-marin ne peut larguer une torpille qu'à une distance maximal de 4 cases sans diagonale !")

                                if self.nom == "Ecureille" :
                                    print("\n\n❌ Votre sous-marin ne peut larguer une torpille qu'à une distance maximal de 5 cases sans diagonale !")
                        else : 
                            print("\n\n❌ Veuillez larguer votre torpille dans les limites de la map !")
                
                except ValueError :
                    print("\n\n❌ Veuillez choisir des valeurs valides.")


    def larguer_mine(self, carte, derniere_colonne, derniere_ligne, arme2):
        print("\nSelectionner un emplacement sur la map :")
        carte.Afficher_carte()
        
        while True :
            try :
                y_lettre = input("\nChoisissez une colonne : ")
                y = lettre_to_chiffre(y_lettre)
                x = int(input("Choisissez une ligne : ")) - 1
                
                if y != "alpha" :
                    emplacement_mine = x, y

                    if 0 <= y <= ord(derniere_colonne) - ord('A') and 0 <= x <= int(derniere_ligne) :
                        if ((x == self.pos[0]+1 or x == self.pos[0]-1) and (y == self.pos[1]+1 or y == self.pos[1]-1)) or ((x == self.pos[0]+1 or x == self.pos[0]-1) and (y == self.pos[1])) or ((y == self.pos[1]+1 or y == self.pos[1]-1) and (x == self.pos[0])) :
                            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

                            for i in range(6):
                                    arme2[i] = "0"
                            
                            #Si le sm a déjà naviguer là ou la mine est posé, alors le signalement de la mine sera en majuscule est le sm ne pourra pas naviguer dessus;
                            if carte.carte[x][y] == '←':
                                mine_cap = "OUEST"
                                carte.carte[x][y] = "M"

                            elif carte.carte[x][y] == '→':
                                mine_cap = "EST"
                                carte.carte[x][y] = "M"

                            elif carte.carte[x][y] == '↑':
                                mine_cap = "NORD"
                                carte.carte[x][y] = "M"

                            elif carte.carte[x][y] == '↓':
                                mine_cap = "SUD"
                                carte.carte[x][y] = "M"
                            
                            else :
                                carte.carte[x][y] = "m"
                                mine_cap = None

                            self.a2 = False
                            print("\nVotre mine a été placé en : ", y_lettre, x+1, "\n")
                            carte.Afficher_carte()
                            input("SUIVANT")

                            return emplacement_mine, arme2, mine_cap
                        
                        else :
                            print("\n\n❌ Veuillez choisir des valeurs autour de votre sous-marin sur des cases de mer qui ne sont déjà pas occupé par l'une de vos mines.")

                    else :
                        print("\n\n❌ Veuillez choisir des valeurs dans la limite de la map.")

                else : 
                    print("\n\n❌ Entrez une colonne valide.")

            except ValueError : 
                print("\n\n❌ Veuillez choisir des valeurs valides.")


    def exploser_mine(self, sous_marin_ennemi,  capitaine_ennemi, nom_e, nom_self, emplacement_mines, mine_cap, carte, fin) :
        nb_mines = len(emplacement_mines)
        print("\n")
        carte.Afficher_carte()

        #afficher l'emplacement des mines à exploser et le lier à un numéro de mine
        for i in range(nb_mines) :
            x, y = emplacement_mines[i - 1]
            y_l = chiffre_to_lettre(y)
            print(f"{i + 1} - Faire exploser la mine placée en {y_l}{x + 1}")

        while True :
            try :
                choix = int(input(f"\nChoisissez la mine que vous voulez faire exploser (1 - {nb_mines}). Annuler l'explosion (0) : "))

                if 0 < choix <= nb_mines :

                    for i in range(nb_mines) :
                    #selection de la position de la mine selectionnée et de son cap
                        emplacement_mine_choisis = emplacement_mines[i - 1]
                        mine_cap_choisis = mine_cap[i - 1]

                    #si le cap associé à la mine posée égale une valeur de cap alors on remet sur la carte la fléche du cap pour prévenir que le sm est déjà passer par la
                    if mine_cap[choix - 1] == "OUEST" :
                        carte.carte[x][y] = '←'

                    elif mine_cap[choix - 1] == "EST" :
                        carte.carte[x][y] = '→'

                    elif mine_cap[choix - 1] == "NORD" :
                        carte.carte[x][y] = '↑'

                    elif mine_cap[choix - 1] == "SUD" :
                        carte.carte[x][y] = '↓'

                    else :
                        carte.carte[x][y] = '.'

                    # i, j = self.pos
                    # carte.carte[i][j] = self.nom[0]

                    #on retire la mine qui a explosée dans le tableau des emplacement_mines ainsi que son cap associé.
                    emplacement_mines.remove(emplacement_mine_choisis)
                    mine_cap.remove(mine_cap_choisis)

                    #le sous-marin explose une mine sur sois
                    if emplacement_mine_choisis == self.pos :
                        print(f"\nVous avez fait exploser une mine en plein sur VOTRE SOUS-MARIN !!! \nVous prennez 2 points de dégats !!!\nVous entendez votre équipage crier : 'MUTINERIE, CHANGEONS DE CAPITAINE !!!'\n")
                        self.vie -= 2
                        print(f"========== Sous-marin '{nom_self}' ==========\n- Vie restante : {self.vie}❤️\n")

                        if self.vie <= 0 :
                            #fin de game
                            fin = True
                            
                    #le sous marin explose la mine sur un emplacement à côté de lui
                    elif ((x == self.pos[0]+1 or x == self.pos[0]-1) and (y == self.pos[1]+1 or y == self.pos[1]-1)) or ((x == self.pos[0]+1 or x == self.pos[0]-1) and (y == self.pos[1])) or ((y == self.pos[1]+1 or y == self.pos[1]-1) and (x == self.pos[0])) :
                        print(f"\nVous avez fait exploser une mine à côté de votre propre sous-marin ! \nVous prennez 1 point de dégats !\n\n")
                        self.vie -= 1
                        print(f"========== Sous-marin '{nom_self}' ==========\n- Vie restante : {self.vie}❤️\n")

                        if self.vie <= 0 :
                            #fin de game
                            fin = True

                    if emplacement_mine_choisis == sous_marin_ennemi.pos :
                        print(f"\n\nLe capitaine adverse '{capitaine_ennemi}' annonce : \n🚨 IMPACT DIRECT !🚨")
                        print(f"\nVotre mine a explosé en plein sur le sous-marin ennemi '{nom_e}' ! \nIl prend 2 points de dégats !!!\n")
                        sous_marin_ennemi.vie -= 2
                        print(f"========== Sous-marin '{nom_e}' ==========\n- Vie restante : {sous_marin_ennemi.vie}❤️\n")
                                
                        if sous_marin_ennemi.vie <= 0 :
                            #fin de game
                            fin = True

                        input("SUIVANT")
                        return fin, emplacement_mines, mine_cap

                    #La première condition and (les deux premières parenthèses) vérifie si l'emplacement du tir est dans la diagonale du sous marin ennemi. Le deux suivante check si le tir se situe à côté horizontalement du sm ennemi. Et les deux dernières check si le tir a été fait à côté verticalement du sm ennemi. Un peu indigeste, mais ca marche
                    elif ((x == sous_marin_ennemi.pos[0]+1 or x == sous_marin_ennemi.pos[0]-1) and (y == sous_marin_ennemi.pos[1]+1 or y == sous_marin_ennemi.pos[1]-1)) or ((x == sous_marin_ennemi.pos[0]+1 or x == sous_marin_ennemi.pos[0]-1) and (y == sous_marin_ennemi.pos[1])) or ((y == sous_marin_ennemi.pos[1]+1 or y == sous_marin_ennemi.pos[1]-1) and (x == sous_marin_ennemi.pos[0])):
                        print(f"\n\nLe capitaine adverse '{capitaine_ennemi}' annonce : \n🚨 IMPACT INDIRECT !🚨")
                        print(f"\nVotre mine a explosé juste à côté sous-marin ennemi '{nom_e}' ! \nIl prend tout de même 1 point de dégats !\n")
                        sous_marin_ennemi.vie -= 1
                        print(f"========== Sous-marin '{nom_e}' ==========\n- Vie restante : {sous_marin_ennemi.vie}❤️\n")
                                
                        if sous_marin_ennemi.vie <= 0 :
                            #fin de game
                            fin = True
                                
                        input("SUIVANT")
                        return fin, emplacement_mines, mine_cap

                    #l'emplacement du tir est ni sur le sous-marin ennemi ni à ses alentours.
                    else :
                        print(f"\n\nLe capitaine adverse '{capitaine_ennemi}' annonce : \n🚨 RAS !🚨") 
                        print(f"\nVous avez fait exploser une mine dans le vide !\n")
                        print(f"========== Sous-marin '{nom_e}' ==========\n- Vie restante : {sous_marin_ennemi.vie}❤️\n")
                        input("\nSUIVANT")
                        return fin, emplacement_mines, mine_cap

                if choix == 0 :
                    return fin, emplacement_mines, mine_cap
            
            except ValueError :
                print("\n\n❌ choisissez une valeur valide.")


    def explosion_auto(self, sous_marin_ennemi, nom_self, emplacement_mines_self, mine_cap_self, carte, fin, emplacement_mines_ennemi, mine_cap_ennemi, carte_ennemi):

        if sous_marin_ennemi.nom == "Ecureille" :
            if emplacement_mines_ennemi :
                for i in range(len(emplacement_mines_ennemi)) :
                    x, y = emplacement_mines_ennemi[i - 1]
                    
                    if self.pos == emplacement_mines_ennemi[i - 1] :
                        
                        if mine_cap_ennemi[i - 1] == "OUEST" :
                            carte_ennemi.carte[x][y] = '←'

                        elif mine_cap_ennemi[i - 1] == "EST" :
                            carte_ennemi.carte[x][y] = '→'

                        elif mine_cap_ennemi[i - 1] == "NORD" :
                            carte_ennemi.carte[x][y] = '↑'

                        elif mine_cap_ennemi[i - 1] == "SUD" :
                            carte_ennemi.carte[x][y] = '↓'

                        emplacement_mine_explose = emplacement_mines_ennemi[i - 1]
                        mine_cap_explose = mine_cap_ennemi[i - 1]
                        emplacement_mines_ennemi.remove(emplacement_mine_explose)
                        mine_cap_ennemi.remove(mine_cap_explose)

                        print(f"\nUne mine ennemi à déjà été larguée sur votre nouvelle position et celle-ci à exploser au contact de votre sous-marin !  \nVous prenez 1 point de dégats !\n")
                        self.vie -= 1
                        print(f"========== Sous-marin '{nom_self}' ==========\n- Vie restante : {self.vie}❤️\n")
                                
                        if self.vie <= 0 :
                            #fin de game
                            fin = True
                                
                        return fin, emplacement_mines_ennemi, mine_cap_ennemi, mine_cap_self, emplacement_mines_self

        if self.nom == "Ecureille" :
            if emplacement_mines_self :
                for i in range(len(emplacement_mines_self)) :
                    x, y = emplacement_mines_self[i - 1]

                    if self.pos == emplacement_mines_self[i - 1] :

                        if mine_cap_self[i - 1] == "OUEST" :
                            carte.carte[x][y] = '←'

                        elif mine_cap_self[i - 1] == "EST" :
                            carte.carte[x][y] = '→'

                        elif mine_cap_self[i - 1] == "NORD" :
                            carte.carte[x][y] = '↑'

                        elif mine_cap_self[i - 1] == "SUD" :
                            carte.carte[x][y] = '↓'

                        emplacement_mine_explose = emplacement_mines_self[i - 1]
                        mine_cap_explose = mine_cap_self[i - 1]
                        emplacement_mines_self.remove(emplacement_mine_explose)
                        mine_cap_self.remove(mine_cap_explose)

                        print(f"\nVous aviez déjà posé une mine sur cette position et celle-ci à exploser au contact de votre sous-marin !  \nVous prenez 1 point de dégats !\n")
                        self.vie -= 1
                        print(f"========== Sous-marin '{nom_self}' ==========\n- Vie restante : {self.vie}❤️\n")
                                
                        if self.vie <= 0 :
                            #fin de game
                            fin = True
                                
                        return fin, emplacement_mines_ennemi, mine_cap_ennemi, mine_cap_self, emplacement_mines_self
        
        return fin, emplacement_mines_ennemi, mine_cap_ennemi, mine_cap_self, emplacement_mines_self
    

    def larguer_drone(self, carte, sous_marin_ennemi, dete1) :
        while True :
            try : 
                choix = int(input("Vous larguez votre drone secteur (1 - 4) : "))
                if 1 <= choix <= 4 :
                    self.d1 = False
                    #on reset graphiquement le chargement du drone
                    for i in range(6):
                        dete1[i] = "0"

                    milieu_largeur = carte.largeur // 2
                    milieu_hauteur = carte.hauteur // 2
                    x, y = sous_marin_ennemi.pos
                    
                    #le joueur a selectionner le secteur 1 et la position du sm ennemi est dans le secteur 1
                    if choix == 1 and x < milieu_hauteur and y < milieu_largeur :
                        print("\nVotre drone vous retourne : 'OUI' ")
                        return dete1
                    
                    #le joueur a selectionner le secteur 2 et la position du sm ennemi est dans le secteur 2
                    elif choix == 2 and x < milieu_hauteur and y >= milieu_largeur:
                        print("\nVotre drone vous retourne : 'OUI' ")
                        return dete1

                    elif choix == 3 and x >= milieu_hauteur and y < milieu_largeur :
                        print("\nVotre drone vous retourne : 'OUI' ")
                        return dete1

                    elif choix == 4 and x >= milieu_hauteur and y >= milieu_largeur :
                        print("\nVotre drone vous retourne : 'OUI' ")
                        return dete1

                    else :
                        print("\nVotre drone vous retourne : 'NON' ")
                        return dete1

                else :
                    print("\n\n❌ choisissez un secteur existant.")

            except ValueError :
                print("\n\n❌ choisissez une valeur valide.")

    def lancer_sonar(self, carte, sous_marin_ennemi, dete2, capitaine_ennemi, nom_ennemi, derniere_colonne, derniere_ligne, capitaine_self, nom_self, carte_ennemi) :
        print(changement)
        print(f"\n⚠⚠⚠ Attention ⚠⚠⚠ : \nC'est au Capitaine : '{capitaine_ennemi}', de l'équipe '{nom_ennemi}' de jouer.")
        input("\nSUIVANT")

        print("\n\nLe sous-marin adverse a lancé un sonar, vous êtes obligé de leur communiquer DEUX informations concernant la position de votre sous-marin. \nLa première information à choisir sera la bonne et la deuxième sera la mauvaise. \nLes informations seront communiquées aux ennemis dans un ordre aléatoire.")
        #on met dans x et y les valeurs de la colonne et de la ligne du sm pour pouvoir l'afficher
        x, y = sous_marin_ennemi.pos
        y_lettre = chiffre_to_lettre(y)
        y_self = y_lettre

        #on met dans la variable secteur la valeur de la position du secteur du sous-marin
        milieu_largeur = carte.largeur // 2
        milieu_hauteur = carte.hauteur // 2
                    
        if x < milieu_hauteur and y < milieu_largeur :
            secteur = 1
                    
        elif x < milieu_hauteur and y >= milieu_largeur:
            secteur = 2

        elif x >= milieu_hauteur and y < milieu_largeur :
            secteur = 3

        elif x >= milieu_hauteur and y >= milieu_largeur :
            secteur = 4

        else :
            print("Si on voit ce message, c'est qu'il y à un problème quelque part...")

        while True :
            try :
                print(f"\n\nVoici actuellement vos coordonnées :\n1 - Colonne : {y_lettre}\n2 - Ligne : {x + 1}\n3 - Secteur : {secteur}")
                vrai = int(input("\nVeuillez fournir une information véridique concernant votre position (1 - 3) que le sonar ennemi captera : "))
                
                if vrai == 1 :
                    vrai = "Le sous-marin ennemi se trouve en colonne : " + y_lettre
                    condition_vrai = 1
                    break

                elif vrai == 2 :
                    vrai = "Le sous-marin ennemi se trouve en ligne : " + str(x)
                    condition_vrai = 2
                    break

                elif vrai == 3 :
                    vrai = "Le sous-marin ennemi se trouve en secteur : " + str(secteur)
                    condition_vrai = 3
                    break

                else :
                    print("\n\n❌ Veuillez choisir une colonne, une ligne ou un secteur correspondant à votre position\n\n")

            except ValueError :
                print("\n\n❌ Veuillez choisir une option parmi celles qui vous sont proposées.")

        while True:
            try :
                faux = int(input("\nVoici le type de coordonnées trompeuse que vous pouvez choisir : \n1 - Colonne\n2 - Ligne\n3 - Secteur\n\nVeuillez maintenant sélectionné celle que le sonar ennemi captera  (1 - 3) :"))

                if faux != condition_vrai :
                    print("\n\n")
                    carte_ennemi.Afficher_carte()
                    print("\n")

                    if faux == 1 :
                        while faux == 1 :
                            try :
                                y_lettre = input(f"Choisissez une colonne sur laquelle votre sous-marin n'est pas (A - {derniere_colonne}) ou revenir en arrière (0) : ")
                                
                                if y_lettre == "0" :
                                    break
                                
                                y_given = lettre_to_chiffre(y_lettre)
                                
                                if y_given != "alpha" :
                                    if y_lettre != y_self :
                                        if 0 <= y_given <= ord(derniere_colonne) - ord('A') : 
                                            faux = "Le sous-marin ennemi se trouve en colonne : " + y_lettre
                                            break
                                        
                                        else :
                                            print("\n\n❌ Veuillez donner une colonne comprise dans les limites de la map.")
                                        
                                    else :
                                        print("\n\n❌ Vous venez de donner la véritable colonne de votre sous-marin alors que vous devez en donner une fausse.")
                                else :
                                    print("\n\n❌ Entrez une colonne valide.")
                            
                            except ValueError :
                                print("\n\n❌ Veuillez saisir une colonne de la map.")

                        if y_lettre != "0" :
                            break

                    elif faux == 2 :
                        while faux == 2 :
                            try :
                                x_given = int(input(f"Choisissez une ligne sur laquelle votre sous-marin n'est pas (1 - {derniere_ligne}) ou revenir en arrière (0) : "))
                                
                                if x_given == 0 :
                                    break

                                elif x_given != x + 1 :
                                    if 0 <= x_given <= int(derniere_ligne) : 
                                        faux = "Le sous-marin ennemi se trouve en ligne : " + str(x_given)
                                        break
                                    
                                    else :
                                        print("\n\n❌ Veuillez entrer une ligne comprise dans les limites de la map.")
                                    
                                else :
                                    print("\n\n❌ Vous venez de donner la véritable ligne de votre sous-marin alors que vous devez en donner une fausse.")
                            
                            except ValueError :
                                print("\n\n❌ Veuillez saisir une ligne de la map.")

                        if x_given != 0 :
                            break

                    elif faux == 3 :
                        while faux == 3 :
                            try :
                                secteur_given = int(input("Choisissez un secteur sur lequelle votre sous-marin n'est pas (1 - 4) ou revenir en arrière (0) :"))

                                if secteur_given == 0 :
                                    break

                                if secteur_given != secteur :
                                    if  0 < secteur_given < 5 :
                                        faux = "Le sous-marin ennemi se trouve en secteur : " + str(secteur_given)
                                        break
                                    
                                    else :
                                        print("\n\n❌ Veuillez saisir un secteur existant.")

                                else :
                                    print("\n\n❌ Vous venez de donner le véritable secteur de votre sous-marin alors que vous devez en donner un faux.")

                            except ValueError :
                                print("\n\n❌ Veuillez saisir un secteur de la map.")

                        if secteur_given != 0 :
                            break

                else :
                    print("\n\n❌ Vous ne pouvez pas sélectionner deux fois le même type de coordonnée.")
            
            except ValueError :
                print("\n\n❌ Veuillez choisir une option parmi celles qui vous sont proposées.")

        #reset de la compétence
        for i in range(6):
            dete2[i] = "0"

        self.dete2 = False

        #On renvoie la réponse de l'ennemi aléatoirement.
        print(changement)
        print(f"\n⚠⚠⚠ Attention ⚠⚠⚠ : \nC'est au Capitaine : '{capitaine_self}', de l'équipe '{nom_self}' de jouer.")
        input("\nSUIVANT")

        print("\n\nVoici le résultat de votre drone :")

        #alea_1 est égale à vrai ou à faux choisis aléatoirement
        alea_1 = random.choice([vrai, faux])
        #si alea_1 est égale à vrai alors alea_2 est égale à faux et vise versa
        alea_2 = faux if alea_1 == vrai else vrai

        print("\n" + alea_1 + "\nOU\n" + alea_2) 
        print("\nVous ne savez pas laquelle est vrai ou fausse...")
        input("\n\nSUIVANT")

        return dete2


def lettre_to_chiffre(lettre):
    if len(lettre) == 1 and lettre.isalpha() :
        return ord(lettre.upper()) - ord('A')
    
    else :
        return False 

def chiffre_to_lettre(chiffre):
    return chr(chiffre + ord('A'))