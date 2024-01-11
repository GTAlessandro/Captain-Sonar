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

            if choix_meca == 1 :
                cadran_ouest[0] = " ̷J̷A̷U̷N̷E̷-̷ ̷A̷R̷M"

            elif choix_meca == 2 :
                cadran_ouest[1] = " ̷J̷A̷U̷N̷E̷-̷ ̷S̷P̷E"

            elif choix_meca == 3 :
                cadran_ouest[2] = " ̷J̷A̷U̷N̷E̷-̷ ̷D̷E̷T"

            elif choix_meca == 4 :
                cadran_ouest[3] = " ̷N̷O̷N̷E̷ ̷ ̷-̷ ̷D̷E̷T"

            elif choix_meca == 5 :
                cadran_ouest[4] = " ̷N̷O̷N̷E̷ ̷ ̷-̷ ̷R̷A̷D"

            elif choix_meca == 6 :
                cadran_ouest[5] = " ̷N̷O̷N̷E̷ ̷ ̷-̷ ̷R̷A̷D"

            else : 
                print("Sélectionner une panne du cadran OUEST comprise entre 1 et 6")

        elif cap == "NORD" :

            if choix_meca == 1 :
                cadran_nord[0] = " ̷V̷E̷R̷T̷ ̷-̷ ̷S̷P̷E"
        
            elif choix_meca == 2 :
                cadran_nord[1] = " ̷V̷E̷R̷T̷ ̷-̷ ̷D̷E̷T"

            elif choix_meca == 3 :
                cadran_nord[2] = " ̷V̷E̷R̷T̷ ̷-̷ ̷A̷R̷M"

            elif choix_meca == 4 :
                cadran_nord[3] = " ̷N̷O̷N̷E̷ ̷ ̷-̷ ̷D̷E̷T"

            elif choix_meca == 5 :
                cadran_nord[4] = " ̷N̷O̷N̷E̷ ̷ ̷-̷ ̷A̷R̷M"

            elif choix_meca == 6 :
                cadran_nord[5] = " ̷N̷O̷N̷E̷ ̷ ̷-̷ ̷R̷A̷D"

            else : 
                print("Sélectionner une panne du cadran NORD comprise entre 1 et 6")

        elif cap == "SUD" :

            if choix_meca == 1 :
                cadran_sud[0] = " ̷B̷L̷E̷U̷ ̷-̷ ̷D̷E̷T"
        
            elif choix_meca == 2 :
                cadran_sud[1] = " ̷B̷L̷E̷U̷ ̷-̷ ̷S̷P̷E"

            elif choix_meca == 3 :
                cadran_sud[2] = " ̷B̷L̷E̷U̷ ̷-̷ ̷A̷R̷M"

            elif choix_meca == 4 :
                cadran_sud[3] = " ̷N̷O̷N̷E̷ ̷ ̷-̷ ̷A̷R̷M"

            elif choix_meca == 5 :
                cadran_sud[4] = " ̷N̷O̷N̷E̷ ̷ ̷-̷ ̷S̷P̷E"

            elif choix_meca == 6 :
                cadran_sud[5] = " ̷N̷O̷N̷E̷ ̷ ̷-̷ ̷R̷A̷D"

            else : 
                print("Sélectionner une panne du cadran SUD comprise entre 1 et 6")

        elif cap == "EST" :

            if choix_meca == 1 :
                cadran_est[0] = " ̷J̷A̷U̷N̷E̷-̷ ̷A̷R̷M"
        
            elif choix_meca == 2 :
                cadran_est[1] = " ̷V̷E̷R̷T̷ ̷-̷ ̷S̷P̷E"

            elif choix_meca == 3 :
                cadran_est[2] = " ̷B̷L̷E̷U̷ ̷-̷ ̷S̷P̷E"

            elif choix_meca == 4 :
                cadran_est[3] = " ̷N̷O̷N̷E̷ ̷ ̷-̷ ̷D̷E̷T"

            elif choix_meca == 5 :
                cadran_est[4] = " ̷N̷O̷N̷E̷ ̷ ̷-̷ ̷R̷A̷D"

            elif choix_meca == 6 :
                cadran_est[5] = " ̷N̷O̷N̷E̷ ̷ ̷-̷ ̷R̷A̷D"

            else : 
                print("Sélectionner une panne du cadran EST comprise entre 1 et 6")

        # Si le sous marin fait surface, toute les pannes sont réparées.
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

            print("\n\nVous faite surface ! Toute vos pannes sont réparés !")


        # Si toute les pannes des couleurs sont cochés, alors tout est réparé
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
        
        # Si toute les pannes d'un cadran son coché, alors elles sont toutes réparé mais le sous marin prend un de dégat !
        if cadran_ouest[0] == " ̷J̷A̷U̷N̷E̷-̷ ̷A̷R̷M" and cadran_ouest[1] == " ̷J̷A̷U̷N̷E̷-̷ ̷S̷P̷E" and cadran_ouest[2] == " ̷J̷A̷U̷N̷E̷-̷ ̷D̷E̷T" and cadran_ouest[3] == " ̷N̷O̷N̷E̷ ̷ ̷-̷ ̷D̷E̷T" and cadran_ouest[4] == " ̷N̷O̷N̷E̷ ̷ ̷-̷ ̷R̷A̷D" and cadran_ouest[5] == " ̷N̷O̷N̷E̷ ̷ ̷-̷ ̷R̷A̷D" :
            cadran_ouest[0] = " JAUNE 1 ARM"
            cadran_ouest[1] = " JAUNE 2 SPE"
            cadran_ouest[2] = " JAUNE 3 DET"
            cadran_ouest[3] = " NONE  4 DET"
            cadran_ouest[4] = " NONE  5 RAD"
            cadran_ouest[5] = " NONE  6 RAD"
            print("\n\nToute les pannes du cadran OUEST ont été cochées, toute vos pannes de ce cadran sont réparés mais vous subissez un de dégât !")
            self.vie -= 1
            print(f"\n========== Sous-marin {self.nom} ==========\n- Vie : {self.vie}")

        if cadran_nord[0] == " ̷V̷E̷R̷T̷ ̷-̷ ̷S̷P̷E" and cadran_nord[1] == " ̷V̷E̷R̷T̷ ̷-̷ ̷D̷E̷T" and cadran_nord[2] == " ̷V̷E̷R̷T̷ ̷-̷ ̷A̷R̷M" and cadran_nord[3] == " ̷N̷O̷N̷E̷ ̷ ̷-̷ ̷D̷E̷T" and cadran_nord[4] == " ̷N̷O̷N̷E̷ ̷ ̷-̷ ̷A̷R̷M" and cadran_nord[5] == " ̷N̷O̷N̷E̷ ̷ ̷-̷ ̷R̷A̷D" :
            cadran_nord[0] = " VERT  1 SPE"
            cadran_nord[1] = " VERT  2 DET"
            cadran_nord[2] = " VERT  3 ARM"
            cadran_nord[3] = " NONE  4 DET"
            cadran_nord[4] = " NONE  5 ARM"
            cadran_nord[5] = " NONE  6 RAD"
            print("\n\nToute les pannes du cadran NORD ont été cochées, toute vos pannes de ce cadran sont réparés mais vous subissez un de dégât !")
            self.vie -= 1
            print(f"\n========== Sous-marin {self.nom} ==========\n- Vie : {self.vie}")

        if cadran_sud[0] == " ̷B̷L̷E̷U̷ ̷-̷ ̷D̷E̷T" and cadran_sud[1] == " ̷B̷L̷E̷U̷ ̷-̷ ̷S̷P̷E" and cadran_sud[2] == " ̷B̷L̷E̷U̷ ̷-̷ ̷A̷R̷M" and cadran_sud[3] == " ̷N̷O̷N̷E̷ ̷ ̷-̷ ̷A̷R̷M" and cadran_sud[4] == " ̷N̷O̷N̷E̷ ̷ ̷-̷ ̷S̷P̷E" and cadran_sud[5] == " ̷N̷O̷N̷E̷ ̷ ̷-̷ ̷R̷A̷D" :
            cadran_sud[0] = " BLEU  1 DET"
            cadran_sud[1] = " BLEU  2 SPE"
            cadran_sud[2] = " BLEU  3 ARM"
            cadran_sud[3] = " NONE  4 ARM"
            cadran_sud[4] = " NONE  5 SPE"
            cadran_sud[5] = " NONE  6 RAD"
            print("\n\nToute les pannes du cadran SUD ont été cochées, toute vos pannes de ce cadran sont réparés mais vous subissez un de dégât !")
            self.vie -= 1
            print(f"\n========== Sous-marin {self.nom} ==========\n- Vie : {self.vie}")

        if cadran_est[0] == " ̷J̷A̷U̷N̷E̷-̷ ̷A̷R̷M" and cadran_est[1] == " ̷V̷E̷R̷T̷ ̷-̷ ̷S̷P̷E" and cadran_est[2] == " ̷B̷L̷E̷U̷ ̷-̷ ̷S̷P̷E" and cadran_est[3] == " ̷N̷O̷N̷E̷ ̷ ̷-̷ ̷D̷E̷T" and cadran_est[4] == " ̷N̷O̷N̷E̷ ̷ ̷-̷ ̷R̷A̷D" and cadran_est[5] == " ̷N̷O̷N̷E̷ ̷ ̷-̷ ̷R̷A̷D" :
            cadran_est[0] = " JAUNE 1 ARM"
            cadran_est[1] = " VERT  2 SPE"
            cadran_est[2] = " BLEU  3 SPE"
            cadran_est[3] = " NONE  4 DET"
            cadran_est[4] = " NONE  5 RAD"
            cadran_est[5] = " NONE  6 RAD"
            print("\n\nToute les pannes du cadran SUD ont été cochées, toute vos pannes de ce cadran sont réparés mais vous subissez un de dégât !")
            self.vie -= 1
            print(f"\n========== Sous-marin {self.nom} ==========\n- Vie : {self.vie}")

        # Si toute les pannes RAD sont cochées, alors elles sont réparés et le sous-marin perd 1 pv
        if cadran_ouest[4] == " ̷N̷O̷N̷E̷ ̷ ̷-̷ ̷R̷A̷D" and cadran_ouest[5] == " ̷N̷O̷N̷E̷ ̷ ̷-̷ ̷R̷A̷D" and cadran_nord[5] == " ̷N̷O̷N̷E̷ ̷ ̷-̷ ̷R̷A̷D" and cadran_sud[5] == " ̷N̷O̷N̷E̷ ̷ ̷-̷ ̷R̷A̷D" and cadran_est[4] == " ̷N̷O̷N̷E̷ ̷ ̷-̷ ̷R̷A̷D" and cadran_est[5] == " ̷N̷O̷N̷E̷ ̷ ̷-̷ ̷R̷A̷D":
            cadran_ouest[4] = " NONE  5 RAD"
            cadran_ouest[5] = " NONE  6 RAD"
            cadran_nord[5] = " NONE  6 RAD"
            cadran_sud[5] = " NONE  6 RAD"
            cadran_est[4] = " NONE  5 RAD"
            cadran_est[5] = " NONE  6 RAD"
            print("\n\nToute les pannes RAD ont été cochées, toute vos pannes RAD sont réparés mais vous subissez un de dégât !")
            self.vie -= 1
            print(f"\n========== Sous-marin {self.nom} ==========\n- Vie : {self.vie}")
            
        
        S1.afficher_baie_moteur(cadran_ouest, cadran_nord, cadran_sud, cadran_est)

        return cadran_ouest, cadran_nord, cadran_sud, cadran_est

    
    def def_capacite(self) :
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

        self.a1 = [a1, a2, a3, a4, a5, a6]
        self.a2 = [b1, b2, b3, b4, b5, b6]
        self.d1 = [c1, c2, c3, c4, c5, c6]
        self.d2 = [d1, d2, d3, d4, d5, d6]
        self.spe = [e1, e2, e3, e4, e5, e6]

        return self.a1, self.a2, self.d1, self.d2, self.spe

    def afficher_capacite():
        if choix == 1 :
            a1 = "#"
            
        if self.name == "Tigre" :

            capacite = f'''            
                ――――――――――――――――          ~          ――――――――――――――――          ~          ――――――――――――――――
                | 1 - Torpille |          ~          |  3 - Drone   |          ~          | 5 - Silence  |
                ――――――――――――――――          ~          ――――――――――――――――          ~          ――――――――――――――――
                |      __      |          ~          |              |          ~          |              | - {e6}
                |     /  \     |          ~          |      .--.    |          ~          |     .--.     | - {e5}
                |     |  |     |          ~          |  ~\ ( | o)   | - {c4}      ~          |    (o  o)    | - {e4}
                |     |  |     | - {a3}      ~          |  ~X>------   | - {c3}      ~          |   /_ O  _\   | - {e3}
                |    / == \    | - {a2}      ~          |  ~/(      )  | - {c2}      ~          |     \   \    | - {e2}
                |    |/**\|    | - {a1}      ~          |     '-__-'   | - {c1}      ~          |      `~~~'   | - {e1}
                ――――――――――――――――          ~          ――――――――――――――――          ~          ――――――――――――――――

                ――――――――――――――――          ~          ――――――――――――――――          ~
                |   2 - Mine   |          ~          |   4 - Sonar  |          ~
                ――――――――――――――――          ~          ――――――――――――――――          ~
                |              |          ~          |    ______    |          ~
                |     _--_     |          ~          |   /     /\   |          ~
                |    (\||/)    |          ~          |  /    °/  \  |          ~
                |    ―-II-―    | - {b3}      ~          | |     /    | | - {d3}      ~
                |    (/||\)    | - {b2}      ~          |  \        /  | - {d2}      ~
                |     '――'     | - {b1}      ~          |   \______/   | - {d1}      ~
                ――――――――――――――――          ~          ――――――――――――――――          ~
                '''

            capacite = capacite.replace('Drone', '\033[38;5;208mDrone\033[0m')\
                            .replace('Silence', '\033[95mSilence\033[0m')\
                            .replace('Sonar', '\033[38;5;208mSonar\033[0m')\
                            .replace('Torpille', '\033[91mTorpille\033[0m')\
                            .replace('Mine', '\033[91mMine\033[0m')\
            
            print(capacite)
            return self.a1, self.a2, self.d1, self.d2, self.spe


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

