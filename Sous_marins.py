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


    def choisir_une_panne(self, choix_meca, cadran_ouest, cadran_nord, cadran_sud, cadran_est, cap):
        condition = False

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
    

        if cap == "OUEST" :

            if choix_meca == 1 and cadran_ouest[0] == " JAUNE 1 ARM":
                cadran_ouest[0] = " ̷J̷A̷U̷N̷E̷-̷ ̷A̷R̷M"
                condition = True

            elif choix_meca == 2 and cadran_ouest[1] == " JAUNE 2 SPE" :
                cadran_ouest[1] = " ̷J̷A̷U̷N̷E̷-̷ ̷S̷P̷E"
                condition = True

            elif choix_meca == 3 and cadran_ouest[2] == " JAUNE 3 DET" :
                cadran_ouest[2] = " ̷J̷A̷U̷N̷E̷-̷ ̷D̷E̷T"
                condition = True

            elif choix_meca == 4 and cadran_ouest[3] == " NONE  4 DET" :
                cadran_ouest[3] = " ̷N̷O̷N̷E̷ ̷ ̷-̷ ̷D̷E̷T"
                condition = True

            elif choix_meca == 5 and cadran_ouest[4] == " NONE  5 RAD" :
                cadran_ouest[4] = " ̷N̷O̷N̷E̷ ̷ ̷-̷ ̷R̷A̷D"
                condition = True

            elif choix_meca == 6 and cadran_ouest[5] == " NONE  6 RAD" :
                cadran_ouest[5] = " ̷N̷O̷N̷E̷ ̷ ̷-̷ ̷R̷A̷D"
                condition = True

            else : 
                print("Sélectionnez une panne du cadran OUEST comprise entre 1 et 6")

        elif cap == "NORD" :

            if choix_meca == 1 and cadran_nord[0] == " VERT  1 SPE" :
                cadran_nord[0] = " ̷V̷E̷R̷T̷ ̷-̷ ̷S̷P̷E"
                condition = True
        
            elif choix_meca == 2 and cadran_nord[1] == " VERT  2 DET" :
                cadran_nord[1] = " ̷V̷E̷R̷T̷ ̷-̷ ̷D̷E̷T"
                condition = True

            elif choix_meca == 3 and cadran_nord[2] == " VERT  3 ARM" :
                cadran_nord[2] = " ̷V̷E̷R̷T̷ ̷-̷ ̷A̷R̷M"
                condition = True

            elif choix_meca == 4 and cadran_nord[3] == " NONE  4 DET" :
                cadran_nord[3] = " ̷N̷O̷N̷E̷ ̷ ̷-̷ ̷D̷E̷T"
                condition = True

            elif choix_meca == 5 and cadran_nord[4] == " NONE  5 ARM" :
                cadran_nord[4] = " ̷N̷O̷N̷E̷ ̷ ̷-̷ ̷A̷R̷M"
                condition = True

            elif choix_meca == 6 and cadran_nord[5] == " NONE  6 RAD" :
                cadran_nord[5] = " ̷N̷O̷N̷E̷ ̷ ̷-̷ ̷R̷A̷D"
                condition = True

            else : 
                print("Sélectionnez une panne du cadran NORD comprise entre 1 et 6")

        elif cap == "SUD" :

            if choix_meca == 1 and cadran_sud[0] == " BLEU  1 DET" :
                cadran_sud[0] = " ̷B̷L̷E̷U̷ ̷-̷ ̷D̷E̷T"
                condition = True
        
            elif choix_meca == 2 and cadran_sud[1] == " BLEU  2 SPE" :
                cadran_sud[1] = " ̷B̷L̷E̷U̷ ̷-̷ ̷S̷P̷E"
                condition = True

            elif choix_meca == 3 and cadran_sud[2] == " BLEU  3 ARM" :
                cadran_sud[2] = " ̷B̷L̷E̷U̷ ̷-̷ ̷A̷R̷M"
                condition = True

            elif choix_meca == 4 and cadran_sud[3] == " NONE  4 ARM" :
                cadran_sud[3] = " ̷N̷O̷N̷E̷ ̷ ̷-̷ ̷A̷R̷M"
                condition = True

            elif choix_meca == 5 and cadran_sud[4] == " NONE  5 SPE" :
                cadran_sud[4] = " ̷N̷O̷N̷E̷ ̷ ̷-̷ ̷S̷P̷E"
                condition = True

            elif choix_meca == 6 and cadran_sud[5] == " NONE  6 RAD" :
                cadran_sud[5] = " ̷N̷O̷N̷E̷ ̷ ̷-̷ ̷R̷A̷D"
                condition = True

            else : 
                print("Sélectionnez une panne du cadran SUD comprise entre 1 et 6")

        elif cap == "EST" :

            if choix_meca == 1 and cadran_est[0] == " JAUNE 1 ARM" :
                cadran_est[0] = " ̷J̷A̷U̷N̷E̷-̷ ̷A̷R̷M"
                condition = True
        
            elif choix_meca == 2 and cadran_est[1] == " VERT  2 SPE" :
                cadran_est[1] = " ̷V̷E̷R̷T̷ ̷-̷ ̷S̷P̷E"
                condition = True

            elif choix_meca == 3 and cadran_est[2] == " BLEU  3 SPE" :
                cadran_est[2] = " ̷B̷L̷E̷U̷ ̷-̷ ̷S̷P̷E"
                condition = True

            elif choix_meca == 4 and cadran_est[3] == " NONE  4 DET" :
                cadran_est[3] = " ̷N̷O̷N̷E̷ ̷ ̷-̷ ̷D̷E̷T"
                condition = True

            elif choix_meca == 5 and cadran_est[4] == " NONE  5 RAD" :
                cadran_est[4] = " ̷N̷O̷N̷E̷ ̷ ̷-̷ ̷R̷A̷D"
                condition = True

            elif choix_meca == 6 and cadran_est[5] == " NONE  6 RAD" :
                cadran_est[5] = " ̷N̷O̷N̷E̷ ̷ ̷-̷ ̷R̷A̷D"
                condition = True

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
            
        self.baie_moteur = cadran_ouest, cadran_nord, cadran_sud, cadran_est
        self.afficher_baie_moteur(cadran_ouest, cadran_nord, cadran_sud, cadran_est)

        return cadran_ouest, cadran_nord, cadran_sud, cadran_est, condition

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
        
        mince = True 

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
                        mince = False
                        return mince, arme1, arme2, dete1, dete2, spe
            
            elif choix == 2 :
                for i in range(3) :
                    if arme2[i] == "0" :
                        arme2[i] = "#"
                        break

                    elif self.a2 == True : 
                        print("Votre mine est déjà chargée !")
                        mince = False
                        return mince, arme1, arme2, dete1, dete2, spe

            elif choix == 3 :
                for i in range(4) :
                    if dete1[i] == "0" :
                        dete1[i] = "#" 
                        break

                    elif self.d1 == True : 
                        print("Votre drone est déjà chargée !")
                        mince = False
                        return mince, arme1, arme2, dete1, dete2, spe

            elif choix == 4 :
                for i in range(3) :
                    if dete2[i] == "0" :
                        dete2[i] = "#" 
                        break

                    elif self.d2 == True : 
                        print("Votre sonar est déjà chargée !")
                        mince = False
                        return mince, arme1, arme2, dete1, dete2, spe

            elif choix == 5 :
                for i in range(6) :
                    if spe[i] == "0" :
                        spe[i] = "#" 
                        break

                    elif self.spe == True : 
                        print("Votre silence est déjà chargée !")
                        mince = False
                        return mince, arme1, arme2, dete1, dete2, spe

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
                        mince = False
                        return mince, arme1, arme2, dete1, dete2, spe
            
            elif choix == 2 :
                for i in range(4) :
                    if arme2[i] == "0" :
                        arme2[i] = "#"
                        break

                    elif self.a2 == True : 
                        print("Votre mine est déjà chargée !")
                        mince = False
                        return mince, arme1, arme2, dete1, dete2, spe

            elif choix == 3 :
                for i in range(4) :
                    if dete1[i] == "0" :
                        dete1[i] = "#" 
                        break

                    elif self.d1 == True : 
                        print("Votre drone est déjà chargée !")
                        mince = False
                        return mince, arme1, arme2, dete1, dete2, spe

            elif choix == 4 :
                for i in range(3) :
                    if dete2[i] == "0" :
                        dete2[i] = "#" 
                        break

                    elif self.d2 == True : 
                        print("Votre sonar est déjà chargée !")
                        mince = False
                        return mince, arme1, arme2, dete1, dete2, spe

            elif choix == 5 :
                for i in range(6) :
                    if spe[i] == "0" :
                        spe[i] = "#" 
                        break
                    
                    elif self.spe == True : 
                        print("Votre leurre est déjà chargée !")
                        mince = False
                        return mince, arme1, arme2, dete1, dete2, spe

            if arme1[0] == "#" and arme1[1] == "#" and arme1[2] == "#" :
                self.a1 = True
            
            if arme2[0] == "#" and arme2[1] == "#" and arme2[2] == "#" and arme2[3] == "#":
                self.a2 = True

            if dete1[0] == "#" and dete1[1] == "#" and dete1[2] == "#" and dete1[3] == "#":
                self.d1 = True

            if dete2[0] == "#" and dete2[1] == "#" and dete2[2] == "#" :
                self.d2 = True

            if spe[0] == "#" and spe[1] == "#" and spe[2] == "#" and spe[3] == "#" and spe[4] == "#" and spe[5] == "#" :
                self.spe = True

        self.afficher_systeme(arme1, arme2, dete1, dete2, spe)

        return mince, arme1, arme2, dete1, dete2, spe

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
                |     |  |     |          ~          | ~\ ( | o)    | - {c4}      ~          |   |/o \/|    | - {e4}
                |     |  |     | - {a3}      ~          | ~X>------    | - {c3}      ~          |    \<_/\|    | - {e3}
                |    / __ \    | - {a2}      ~          | ~/(      )   | - {c2}      ~          |     \ \ `    | - {e2}
                |    |/**\|    | - {a1}      ~          |    '-__-'    | - {c1}      ~          |      \|      | - {e1}
                ――――――――――――――――          ~          ――――――――――――――――          ~          ――――――――――――――――

                ――――――――――――――――          ~          ――――――――――――――――          ~
                |   2 - Mine   |          ~          |   4 - Sonar  |          ~
                ――――――――――――――――          ~          ――――――――――――――――          ~ 
                |              |          ~          |    ______    |          ~
                |    _.--._    |          ~          |   /     /\   |          ~
                |   ( \||/ )   | - {b4}      ~          |  /    °/  \  |          ~
                |    ―-II-―    | - {b3}      ~          | |     /    | | - {d3}      ~
                |   ( /||\ )   | - {b2}      ~          |  \        /  | - {d2}      ~
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

    def larguer_torpille(self, sous_marin_ennemi, carte, derniere_colonne, derniere_ligne, capitaine_ennemie, nom_e, nom_self, arme1):
        fin = False

        #=====================#
        '''Tigre - Ecureille'''
        #=====================#

        if self.nom == "Tigre" or self.nom == "Ecureille" :
            print("\nSelectionner un emplacement sur la map")
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

                    if 0 <= y <= ord(derniere_colonne) - ord('A') and 0 <= x <= int(derniere_ligne) :
                        if (self.nom == "Tigre" and distance_totale <= 4) or (self.nom == "Ecureille" and distance_totale <= 5) : #TOUT SEUL COMME UN GRAND DU PREMIER COUP HAHAHA
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

                                if sous_marin_ennemi.vie <= 0 :
                                    #fin de game
                                    fin = True
                            
                            #le sous marin tir sur un emplacement à côté de lui
                            elif ((x == self.pos[0]+1 or x == self.pos[0]-1) and (y == self.pos[1]+1 or y == self.pos[1]-1)) or ((x == self.pos[0]+1 or x == self.pos[0]-1) and (y == self.pos[1])) or ((y == self.pos[1]+1 or y == self.pos[1]-1) and (x == self.pos[0])) :
                                print(f"\nVous avez tirer une torpille à côté de votre propre sous-marin ! \nVous prennez 1 point de dégats !\n\n")
                                self.vie -= 1
                                print(f"========== Sous-marin '{nom_self}' ==========\n- Vie restante : {self.vie}❤️\n")

                            #si l'emplacement du tir est égale à la position du sous marin ennemi.
                            if emplacement_tir == sous_marin_ennemi.pos :
                                print(f"\n\nLe capitaine adverse '{capitaine_ennemie}' annonce : \n🚨 IMPACT DIRECT !🚨")
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
                                print(f"\n\nLe capitaine adverse '{capitaine_ennemie}' annonce : \n🚨 IMPACT INDIRECT !🚨")
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
                                print(f"\n\nLe capitaine adverse '{capitaine_ennemie}' annonce : \n🚨 RAS !🚨") 
                                print(f"\nVous avez tirer une torpille dans le vide !\n")
                                print(f"========== Sous-marin '{nom_e}' ==========\n- Vie restante : {sous_marin_ennemi.vie}❤️\n")
                                input("\nSUIVANT")
                                return fin, arme1

                        else :
                            if self.nom == "Tigre" :
                                print("❌ Votre sous-marin ne peut larguer une torpille qu'à une distance maximal de 4 cases sans diagonale !\n\n")

                            if self.nom == "Ecureille" :
                                print("❌ Votre sous-marin ne peut larguer une torpille qu'à une distance maximal de 5 cases sans diagonale !\n\n")
                    else : 
                        print("❌ Veuillez larguer votre torpille dans les limites de la map !\n\n")
                
                except ValueError :
                    print("❌ Veuillez choisir des valeurs valides.\n\n")

def lettre_to_chiffre(lettre):
        while True:
            if len(lettre) == 1 and lettre.isalpha():
                return ord(lettre.upper()) - ord('A')
            elif lettre.isdigit():
                lettre = input("Veuillez entrer une lettre existante : ")
            else:
                lettre = input("Veuillez entrer une colonne existante : ")