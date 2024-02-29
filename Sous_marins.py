import random

from Var_affichage import changement

#====================#
'''Class Sous-Marin'''
#====================#

class SousMarin:
    def __init__(self, capitaine, second, mecano, detecteur, nom, vie, baie_moteur):
        self.capitaine = capitaine
        self.second = second
        self.mecano = mecano
        self.detecteur = detecteur
        self.nom = nom
        self.vie = vie
        self.baie = baie_moteur
        self.cadran_ouest = None
        self.cadran_est = None
        self.cadran_nord = None
        self.cadran_sud = None
        self.condition_panne_arm = None
        self.condition_panne_det = None
        self.condition_panne_spe = None
        self.a1_charge = False #idée : mine à detection magnétique, 
        self.a2_charge = False #idée : torpille Guidage par satellite, Guidage électromagnétique, Guidage par intelligence artificielle
        self.d1_charge = False #sonar de tout les adjectifs, Magnétométrie, Capteurs électromagnétiques, Imagerie acoustique, gravimétrie
        self.d2_charge = False #Détection optique, Capteurs infrarouges, Surveillance satellite
        self.spe_charge = False #fade up, leurre
        self.arme1 = ["0", "0", "0", "0", "0", "0"]
        self.arme2 = ["#", "#", "#", "0", "0", "0"]
        self.dete1 = ["0", "0", "0", "0", "0", "0"]
        self.dete2 = ["0", "0", "0", "0", "0", "0"]
        self.spe1 = ["0", "0", "0", "0", "0", "0"]
        self.competence_charger = None
        self.emplacement_mines = []
        self.mine_cap = []
        self.pos = [None, None]
    
    def infos(self):
        print(f"\n========== Sous-marin {self.nom} ==========\n- Vie : {self.vie}\n- Armement : {self.a1_charge}, {self.a2_charge} \n- Moyen de detection : {self.d1_charge}, {self.d2_charge}\n- Spéciale : {self.spe_charge}\n- Difficulté : {self.baie}\n")

    #===================================#
    '''============CADRAN============='''
    #===================================#

    def definition_du_cadran(self):

        if self.baie == 1 :
            # Définition des valeurs spécifiques à chaque position
            self.cadran_ouest = [" JAUNE 1 ARM", " JAUNE 2 SPE", " JAUNE 3 DET", " NONE  4 DET", " NONE  5 RAD", " NONE  6 RAD"]
            self.cadran_nord = [" VERT  1 SPE", " VERT  2 DET", " VERT  3 ARM", " NONE  4 DET", " NONE  5 ARM", " NONE  6 RAD"]
            self.cadran_sud = [" BLEU  1 DET", " BLEU  2 SPE", " BLEU  3 ARM", " NONE  4 ARM", " NONE  5 SPE", " NONE  6 RAD"]
            self.cadran_est = [" JAUNE 1 ARM", " VERT  2 SPE",  " BLEU  3 SPE", " NONE  4 DET", " NONE  5 RAD", " NONE  6 RAD"]
        
        elif self.baie == 2 : 
            #fonction d'une baie moteur numéro 2
            print("r pour le moment")


    def afficher_baie_moteur(self):

        baie_moteur = f'''
        ============================================= Baie moteur ====================================================

                     /===\         ~         /===\         ~         /===\         ~         /===\ 
                     : O :         ~         : N :         ~         : S :         ~         : E :
                     \===/         ~         \===/         ~         \===/         ~         \===/
                /―――――――――――――\    ~    /―――――――――――――\    ~    /―――――――――――――\    ~    /―――――――――――――\ 
                |{ self.cadran_ouest[0]} |    ~    |{ self.cadran_nord[0]} |    ~    |{ self.cadran_sud[0]} |    ~    |{ self.cadran_est[0]} |
                |{ self.cadran_ouest[1]} |    ~    |{ self.cadran_nord[1]} |    ~    |{ self.cadran_sud[1]} |    ~    |{ self.cadran_est[1]} |
                \{ self.cadran_ouest[2]} /    ~    \{ self.cadran_nord[2]} /    ~    \{ self.cadran_sud[2]} /    ~    \{ self.cadran_est[2]} /
                 |―――――――――――|     ~     |―――――――――――|     ~     |―――――――――――|     ~     |―――――――――――|
                /{ self.cadran_ouest[3]} \    ~    /{ self.cadran_nord[3]} \    ~    /{ self.cadran_sud[3]} \    ~    /{ self.cadran_est[3]} \ 
                |{ self.cadran_ouest[4]} |    ~    |{ self.cadran_nord[4]} |    ~    |{ self.cadran_sud[4]} |    ~    |{ self.cadran_est[4]} |
                |{ self.cadran_ouest[5]} |    ~    |{ self.cadran_nord[5]} |    ~    |{ self.cadran_sud[5]} |    ~    |{ self.cadran_est[5]} |
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


    def choisir_une_panne(self, choix_meca, cap):
        voyant_deja_panne = False

        if cap == "OUEST" :
            if choix_meca == 1 and self.cadran_ouest[0] == " JAUNE 1 ARM":
                self.cadran_ouest[0] = " ̷J̷A̷U̷N̷E̷-̷ ̷A̷R̷M"
                self.condition_panne_arm = True
                voyant_deja_panne = True

            elif choix_meca == 2 and self.cadran_ouest[1] == " JAUNE 2 SPE" :
                self.cadran_ouest[1] = " ̷J̷A̷U̷N̷E̷-̷ ̷S̷P̷E"
                self.condition_panne_spe = True
                voyant_deja_panne = True

            elif choix_meca == 3 and self.cadran_ouest[2] == " JAUNE 3 DET" :
                self.cadran_ouest[2] = " ̷J̷A̷U̷N̷E̷-̷ ̷D̷E̷T"
                self.condition_panne_det = True
                voyant_deja_panne = True

            elif choix_meca == 4 and self.cadran_ouest[3] == " NONE  4 DET" :
                self.cadran_ouest[3] = " ̷N̷O̷N̷E̷ ̷ ̷-̷ ̷D̷E̷T"
                self.condition_panne_det = True
                voyant_deja_panne = True

            elif choix_meca == 5 and self.cadran_ouest[4] == " NONE  5 RAD" :
                self.cadran_ouest[4] = " ̷N̷O̷N̷E̷ ̷ ̷-̷ ̷R̷A̷D"
                voyant_deja_panne = True

            elif choix_meca == 6 and self.cadran_ouest[5] == " NONE  6 RAD" :
                self.cadran_ouest[5] = " ̷N̷O̷N̷E̷ ̷ ̷-̷ ̷R̷A̷D"
                voyant_deja_panne = True

            else : 
                print("Sélectionnez une panne du cadran OUEST comprise entre 1 et 6")

        elif cap == "NORD" :

            if choix_meca == 1 and self.cadran_nord[0] == " VERT  1 SPE" :
                self.cadran_nord[0] = " ̷V̷E̷R̷T̷ ̷-̷ ̷S̷P̷E"
                self.condition_panne_spe = True
                voyant_deja_panne = True
        
            elif choix_meca == 2 and self.cadran_nord[1] == " VERT  2 DET" :
                self.cadran_nord[1] = " ̷V̷E̷R̷T̷ ̷-̷ ̷D̷E̷T"
                self.condition_panne_det = True
                voyant_deja_panne = True

            elif choix_meca == 3 and self.cadran_nord[2] == " VERT  3 ARM" :
                self.cadran_nord[2] = " ̷V̷E̷R̷T̷ ̷-̷ ̷A̷R̷M"
                self.condition_panne_arm = True
                voyant_deja_panne = True

            elif choix_meca == 4 and self.cadran_nord[3] == " NONE  4 DET" :
                self.cadran_nord[3] = " ̷N̷O̷N̷E̷ ̷ ̷-̷ ̷D̷E̷T"
                self.condition_panne_det = True
                voyant_deja_panne = True

            elif choix_meca == 5 and self.cadran_nord[4] == " NONE  5 ARM" :
                self.cadran_nord[4] = " ̷N̷O̷N̷E̷ ̷ ̷-̷ ̷A̷R̷M"
                self.condition_panne_arm = True
                voyant_deja_panne = True

            elif choix_meca == 6 and self.cadran_nord[5] == " NONE  6 RAD" :
                self.cadran_nord[5] = " ̷N̷O̷N̷E̷ ̷ ̷-̷ ̷R̷A̷D"
                voyant_deja_panne = True

            else : 
                print("Sélectionnez une panne du cadran NORD comprise entre 1 et 6")

        elif cap == "SUD" :

            if choix_meca == 1 and self.cadran_sud[0] == " BLEU  1 DET" :
                self.cadran_sud[0] = " ̷B̷L̷E̷U̷ ̷-̷ ̷D̷E̷T"
                self.condition_panne_det = True
                voyant_deja_panne = True
        
            elif choix_meca == 2 and self.cadran_sud[1] == " BLEU  2 SPE" :
                self.cadran_sud[1] = " ̷B̷L̷E̷U̷ ̷-̷ ̷S̷P̷E"
                self.condition_panne_spe = True
                voyant_deja_panne = True

            elif choix_meca == 3 and self.cadran_sud[2] == " BLEU  3 ARM" :
                self.cadran_sud[2] = " ̷B̷L̷E̷U̷ ̷-̷ ̷A̷R̷M"
                self.condition_panne_arm = True
                voyant_deja_panne = True

            elif choix_meca == 4 and self.cadran_sud[3] == " NONE  4 ARM" :
                self.cadran_sud[3] = " ̷N̷O̷N̷E̷ ̷ ̷-̷ ̷A̷R̷M"
                self.condition_panne_arm = True
                voyant_deja_panne = True

            elif choix_meca == 5 and self.cadran_sud[4] == " NONE  5 SPE" :
                self.cadran_sud[4] = " ̷N̷O̷N̷E̷ ̷ ̷-̷ ̷S̷P̷E"
                self.condition_panne_spe = True
                voyant_deja_panne = True

            elif choix_meca == 6 and self.cadran_sud[5] == " NONE  6 RAD" :
                self.cadran_sud[5] = " ̷N̷O̷N̷E̷ ̷ ̷-̷ ̷R̷A̷D"
                voyant_deja_panne = True

            else : 
                print("Sélectionnez une panne du cadran SUD comprise entre 1 et 6")

        elif cap == "EST" :

            if choix_meca == 1 and self.cadran_est[0] == " JAUNE 1 ARM" :
                self.cadran_est[0] = " ̷J̷A̷U̷N̷E̷-̷ ̷A̷R̷M"
                self.condition_panne_arm = True
                voyant_deja_panne = True
        
            elif choix_meca == 2 and self.cadran_est[1] == " VERT  2 SPE" :
                self.cadran_est[1] = " ̷V̷E̷R̷T̷ ̷-̷ ̷S̷P̷E"
                self.condition_panne_spe = True
                voyant_deja_panne = True

            elif choix_meca == 3 and self.cadran_est[2] == " BLEU  3 SPE" :
                self.cadran_est[2] = " ̷B̷L̷E̷U̷ ̷-̷ ̷S̷P̷E"
                self.condition_panne_spe = True
                voyant_deja_panne = True

            elif choix_meca == 4 and self.cadran_est[3] == " NONE  4 DET" :
                self.cadran_est[3] = " ̷N̷O̷N̷E̷ ̷ ̷-̷ ̷D̷E̷T"
                self.condition_panne_det = True
                voyant_deja_panne = True

            elif choix_meca == 5 and self.cadran_est[4] == " NONE  5 RAD" :
                self.cadran_est[4] = " ̷N̷O̷N̷E̷ ̷ ̷-̷ ̷R̷A̷D"
                voyant_deja_panne = True

            elif choix_meca == 6 and self.cadran_est[5] == " NONE  6 RAD" :
                self.cadran_est[5] = " ̷N̷O̷N̷E̷ ̷ ̷-̷ ̷R̷A̷D"
                voyant_deja_panne = True

            else : 
                print("Sélectionnez une panne du cadran EST comprise entre 1 et 6")

        # Si le sous marin fait surface, toutes les pannes sont réparées.
        elif cap == "AUCUN" :
            self.cadran_ouest[0] = " JAUNE 1 ARM"
            self.cadran_ouest[1] = " JAUNE 2 SPE"
            self.cadran_ouest[2] = " JAUNE 3 DET"
            self.cadran_ouest[3] = " NONE  4 DET"
            self.cadran_ouest[4] = " NONE  5 RAD"
            self.cadran_ouest[5] = " NONE  6 RAD"

            self.cadran_nord[0] = " VERT  1 SPE"
            self.cadran_nord[1] = " VERT  2 DET"
            self.cadran_nord[2] = " VERT  3 ARM"
            self.cadran_nord[3] = " NONE  4 DET"
            self.cadran_nord[4] = " NONE  5 ARM"
            self.cadran_nord[5] = " NONE  6 RAD"

            self.cadran_sud[0] = " BLEU  1 DET"
            self.cadran_sud[1] = " BLEU  2 SPE"
            self.cadran_sud[2] = " BLEU  3 ARM"
            self.cadran_sud[3] = " NONE  4 ARM"
            self.cadran_sud[4] = " NONE  5 SPE"
            self.cadran_sud[5] = " NONE  6 RAD"

            self.cadran_est[0] = " JAUNE 1 ARM"
            self.cadran_est[1] = " VERT  2 SPE"
            self.cadran_est[2] = " BLEU  3 SPE"
            self.cadran_est[3] = " NONE  4 DET"
            self.cadran_est[4] = " NONE  5 RAD"
            self.cadran_est[5] = " NONE  6 RAD"


        # Si toutes les pannes des couleurs sont cochés, alors tout est réparé
        if self.cadran_est[0] == " ̷J̷A̷U̷N̷E̷-̷ ̷A̷R̷M" and self.cadran_ouest[2] == " ̷J̷A̷U̷N̷E̷-̷ ̷D̷E̷T" and self.cadran_ouest[1] == " ̷J̷A̷U̷N̷E̷-̷ ̷S̷P̷E" and self.cadran_ouest[0] == " ̷J̷A̷U̷N̷E̷-̷ ̷A̷R̷M" :
            self.cadran_est[0] = " JAUNE 1 ARM"
            self.cadran_ouest[0] = " JAUNE 1 ARM"
            self.cadran_ouest[1] = " JAUNE 2 SPE"
            self.cadran_ouest[2] = " JAUNE 3 DET"
            print("\n\nVous avez réparé les pannes jaune !")
        
        if self.cadran_nord[0] == " ̷V̷E̷R̷T̷ ̷-̷ ̷S̷P̷E" and self.cadran_nord[1] == " ̷V̷E̷R̷T̷ ̷-̷ ̷D̷E̷T" and self.cadran_nord[2] == " ̷V̷E̷R̷T̷ ̷-̷ ̷A̷R̷M" and self.cadran_est[1] == " ̷V̷E̷R̷T̷ ̷-̷ ̷S̷P̷E" :
            self.cadran_nord[0] = " VERT  1 SPE"
            self.cadran_nord[1] = " VERT  2 DET"
            self.cadran_nord[2] = " VERT  3 ARM"
            self.cadran_est[1] = " VERT  2 SPE"
            print("\n\nVous avez réparé les pannes vertes !")

        if self.cadran_sud[0] != " BLEU  1 DET" and self.cadran_sud[1] != " BLEU  2 SPE" and self.cadran_sud[2] != " BLEU  3 ARM" and self.cadran_est[2] != " BLEU  3 SPE" :
            self.cadran_sud[0] = " BLEU  1 DET"
            self.cadran_sud[1] = " BLEU  2 SPE"
            self.cadran_sud[2] = " BLEU  3 ARM"
            self.cadran_est[2] = " BLEU  3 SPE"
            print("\n\nVous avez réparé les pannes bleu !")
        
        # Si toutes les pannes d'un cadran son coché, alors elles sont toutes réparé mais le sous marin prend un de dégat !
        if self.cadran_ouest[0] == " ̷J̷A̷U̷N̷E̷-̷ ̷A̷R̷M" and self.cadran_ouest[1] == " ̷J̷A̷U̷N̷E̷-̷ ̷S̷P̷E" and self.cadran_ouest[2] == " ̷J̷A̷U̷N̷E̷-̷ ̷D̷E̷T" and self.cadran_ouest[3] == " ̷N̷O̷N̷E̷ ̷ ̷-̷ ̷D̷E̷T" and self.cadran_ouest[4] == " ̷N̷O̷N̷E̷ ̷ ̷-̷ ̷R̷A̷D" and self.cadran_ouest[5] == " ̷N̷O̷N̷E̷ ̷ ̷-̷ ̷R̷A̷D" :
            self.cadran_ouest[0] = " JAUNE 1 ARM"
            self.cadran_ouest[1] = " JAUNE 2 SPE"
            self.cadran_ouest[2] = " JAUNE 3 DET"
            self.cadran_ouest[3] = " NONE  4 DET"
            self.cadran_ouest[4] = " NONE  5 RAD"
            self.cadran_ouest[5] = " NONE  6 RAD"
            print("\n\nToutes les pannes du cadran OUEST ont été cochées, toutes vos pannes de ce cadran sont réparées mais vous subissez un de dégât ! 💥")
            self.vie -= 1
            print(f"\n========== Sous-marin {self.nom} ==========\n- Vie : {self.vie}")

        if self.cadran_nord[0] == " ̷V̷E̷R̷T̷ ̷-̷ ̷S̷P̷E" and self.cadran_nord[1] == " ̷V̷E̷R̷T̷ ̷-̷ ̷D̷E̷T" and self.cadran_nord[2] == " ̷V̷E̷R̷T̷ ̷-̷ ̷A̷R̷M" and self.cadran_nord[3] == " ̷N̷O̷N̷E̷ ̷ ̷-̷ ̷D̷E̷T" and self.cadran_nord[4] == " ̷N̷O̷N̷E̷ ̷ ̷-̷ ̷A̷R̷M" and self.cadran_nord[5] == " ̷N̷O̷N̷E̷ ̷ ̷-̷ ̷R̷A̷D" :
            self.cadran_nord[0] = " VERT  1 SPE"
            self.cadran_nord[1] = " VERT  2 DET"
            self.cadran_nord[2] = " VERT  3 ARM"
            self.cadran_nord[3] = " NONE  4 DET"
            self.cadran_nord[4] = " NONE  5 ARM"
            self.cadran_nord[5] = " NONE  6 RAD"
            print("\n\nToutes les pannes du cadran NORD ont été cochées, toutes vos pannes de ce cadran sont réparées mais vous subissez un de dégât ! 💥")
            self.vie -= 1
            print(f"\n========== Sous-marin {self.nom} ==========\n- Vie : {self.vie}")

        if self.cadran_sud[0] == " ̷B̷L̷E̷U̷ ̷-̷ ̷D̷E̷T" and self.cadran_sud[1] == " ̷B̷L̷E̷U̷ ̷-̷ ̷S̷P̷E" and self.cadran_sud[2] == " ̷B̷L̷E̷U̷ ̷-̷ ̷A̷R̷M" and self.cadran_sud[3] == " ̷N̷O̷N̷E̷ ̷ ̷-̷ ̷A̷R̷M" and self.cadran_sud[4] == " ̷N̷O̷N̷E̷ ̷ ̷-̷ ̷S̷P̷E" and self.cadran_sud[5] == " ̷N̷O̷N̷E̷ ̷ ̷-̷ ̷R̷A̷D" :
            self.cadran_sud[0] = " BLEU  1 DET"
            self.cadran_sud[1] = " BLEU  2 SPE"
            self.cadran_sud[2] = " BLEU  3 ARM"
            self.cadran_sud[3] = " NONE  4 ARM"
            self.cadran_sud[4] = " NONE  5 SPE"
            self.cadran_sud[5] = " NONE  6 RAD"
            print("\n\nToutes les pannes du cadran SUD ont été cochées, toutes vos pannes de ce cadran sont réparées mais vous subissez un de dégât ! 💥")
            self.vie -= 1
            print(f"\n========== Sous-marin {self.nom} ==========\n- Vie : {self.vie}")

        if self.cadran_est[0] == " ̷J̷A̷U̷N̷E̷-̷ ̷A̷R̷M" and self.cadran_est[1] == " ̷V̷E̷R̷T̷ ̷-̷ ̷S̷P̷E" and self.cadran_est[2] == " ̷B̷L̷E̷U̷ ̷-̷ ̷S̷P̷E" and self.cadran_est[3] == " ̷N̷O̷N̷E̷ ̷ ̷-̷ ̷D̷E̷T" and self.cadran_est[4] == " ̷N̷O̷N̷E̷ ̷ ̷-̷ ̷R̷A̷D" and self.cadran_est[5] == " ̷N̷O̷N̷E̷ ̷ ̷-̷ ̷R̷A̷D" :
            self.cadran_est[0] = " JAUNE 1 ARM"
            self.cadran_est[1] = " VERT  2 SPE"
            self.cadran_est[2] = " BLEU  3 SPE"
            self.cadran_est[3] = " NONE  4 DET"
            self.cadran_est[4] = " NONE  5 RAD"
            self.cadran_est[5] = " NONE  6 RAD"
            print("\n\nToutes les pannes du cadran EST ont été cochées, toutes vos pannes de ce cadran sont réparées mais vous subissez un de dégât ! 💥")
            self.vie -= 1
            print(f"\n========== Sous-marin {self.nom} ==========\n- Vie : {self.vie}")

        # Si toutes les pannes RAD sont cochées, alors elles sont réparées et le sous-marin perd 1 pv
        if self.cadran_ouest[4] == " ̷N̷O̷N̷E̷ ̷ ̷-̷ ̷R̷A̷D" and self.cadran_ouest[5] == " ̷N̷O̷N̷E̷ ̷ ̷-̷ ̷R̷A̷D" and self.cadran_nord[5] == " ̷N̷O̷N̷E̷ ̷ ̷-̷ ̷R̷A̷D" and self.cadran_sud[5] == " ̷N̷O̷N̷E̷ ̷ ̷-̷ ̷R̷A̷D" and self.cadran_est[4] == " ̷N̷O̷N̷E̷ ̷ ̷-̷ ̷R̷A̷D" and self.cadran_est[5] == " ̷N̷O̷N̷E̷ ̷ ̷-̷ ̷R̷A̷D":
            self.cadran_ouest[4] = " NONE  5 RAD"
            self.cadran_ouest[5] = " NONE  6 RAD"
            self.cadran_nord[5] = " NONE  6 RAD"
            self.cadran_sud[5] = " NONE  6 RAD"
            self.cadran_est[4] = " NONE  5 RAD"
            self.cadran_est[5] = " NONE  6 RAD"
            print("\n\nToutes les pannes RAD ont été cochées, toutes vos pannes RAD sont réparées mais vous subissez un de dégât ! 💥")
            self.vie -= 1
            print(f"\n========== Sous-marin {self.nom} ==========\n- Vie : {self.vie}")

        #Changement d'état des variables de conditions pour savoir si l'on peut lancer ou non une capacité
        #ARM
        if self.cadran_ouest[0] == " JAUNE 1 ARM" and self.cadran_nord[2] == " VERT  3 ARM" and self.cadran_nord[4] == " NONE  5 ARM" and self.cadran_sud[2] == " BLEU  3 ARM" and self.cadran_sud[3] == " NONE  4 ARM" and self.cadran_est[0] == " JAUNE 1 ARM" :
            self.condition_panne_arm = False
        
        if self.cadran_ouest[1] == " JAUNE 2 SPE" and self.cadran_nord[0] == " VERT  1 SPE" and self.cadran_sud[1] == " BLEU  2 SPE" and self.cadran_sud[4] == " NONE  5 SPE" and self.cadran_est[1] == " VERT  2 SPE" and self.cadran_est[2] == " BLEU  3 SPE" :
            self.condition_panne_spe = False
        
        if self.cadran_ouest[2] == " JAUNE 3 DET" and self.cadran_ouest[3] == " NONE  4 DET" and self.cadran_nord[1] == " VERT  2 DET" and self.cadran_nord[3] == " NONE  4 DET" and self.cadran_sud[0] == " BLEU  1 DET" and self.cadran_est[3] == " NONE  4 DET" :
            self.condition_panne_det = False

        self.afficher_baie_moteur()

        return voyant_deja_panne

    #=====================================#
    '''=============SYSTEMES============'''
    #=====================================#

    def charger_systeme(self, choix):
        
        self.competence_charger = True 

        #=========#
        '''Tigre'''
        #=========#
        
        if self.nom == "Tigre" :
            if choix == 1 :
                for i in range(3) :
                    if self.arme1[i] == "0" :
                        self.arme1[i] = "#"
                        return

                    elif self.a1_charge == True : 
                        print("Votre torpille est déjà chargée !")
                        input("\nSUIVANT")
                        self.competence_charger = False
                        return
            
            elif choix == 2 :
                for i in range(3) :
                    if self.arme2[i] == "0" :
                        self.arme2[i] = "#"
                        return

                    elif self.a2_charge == True : 
                        print("Votre mine est déjà chargée !")
                        input("\nSUIVANT")
                        self.competence_charger = False
                        return

            elif choix == 3 :
                for i in range(4) :
                    if self.dete1[i] == "0" :
                        self.dete1[i] = "#" 
                        return

                    elif self.d1_charge == True : 
                        print("Votre drone est déjà chargée !")
                        input("\nSUIVANT")
                        self.competence_charger = False
                        return

            elif choix == 4 :
                for i in range(3) :
                    if self.dete2[i] == "0" :
                        self.dete2[i] = "#" 
                        return

                    elif self.d2_charge == True : 
                        print("Votre sonar est déjà chargée !")
                        input("\nSUIVANT")
                        self.competence_charger = False
                        return

            elif choix == 5 :
                for i in range(6) :
                    if self.spe1[i] == "0" :
                        self.spe1[i] = "#" 
                        return

                    elif self.spe_charge == True : 
                        print("Votre silence est déjà chargée !")
                        input("\nSUIVANT")
                        self.competence_charger = False
                        return

        #=============#
        '''Ecureille'''
        #=============#

        if self.nom == "Ecureille" :
            if choix == 1 :
                for i in range(3) :
                    if self.arme1[i] == "0" :
                        self.arme1[i] = "#"
                        return

                    elif self.a1_charge == True : 
                        print("Votre torpille est déjà chargée !")
                        input("\nSUIVANT")
                        self.competence_charger = False
                        return
            
            elif choix == 2 :
                for i in range(4) :
                    if self.arme2[i] == "0" :
                        self.arme2[i] = "#"
                        return

                    elif self.a2_charge == True : 
                        print("Votre mine est déjà chargée !")
                        input("\nSUIVANT")
                        self.competence_charger = False
                        return 

            elif choix == 3 :
                for i in range(4) :
                    if self.dete1[i] == "0" :
                        self.dete1[i] = "#" 
                        return

                    elif self.d1_charge == True : 
                        print("Votre drone est déjà chargée !")
                        input("\nSUIVANT")
                        self.competence_charger = False
                        return 

            elif choix == 4 :
                for i in range(3) :
                    if self.dete2[i] == "0" :
                        self.dete2[i] = "#" 
                        return

                    elif self.d2_charge == True : 
                        print("Votre sonar est déjà chargée !")
                        input("\nSUIVANT")
                        self.competence_charger = False
                        return

            elif choix == 5 :
                for i in range(6) :
                    if self.spe1[i] == "0" :
                        self.spe1[i] = "#" 
                        return
                    
                    elif self.spe_charge == True : 
                        print("Votre leurre est déjà chargée !")
                        input("\nSUIVANT")
                        self.competence_charger = False
                        return 

            
    def check_systeme_charger(self, choix) :

        if self.nom == "Tigre" :
            if self.arme1[0] == "#" and self.arme1[1] == "#" and self.arme1[2] == "#" :
                self.a1_charge = True
            
            if self.arme2[0] == "#" and self.arme2[1] == "#" and self.arme2[2] == "#" :
                self.a2_charge = True

            if self.dete1[0] == "#" and self.dete1[1] == "#" and self.dete1[2] == "#" and self.dete1[3] == "#" :
                self.d1_charge = True

            if self.dete2[0] == "#" and self.dete2[1] == "#" and self.dete2[2] == "#" :
                self.d2_charge = True

            if self.spe1[0] == "#" and self.spe1[1] == "#" and self.spe1[2] == "#" and self.spe1[3] == "#" and self.spe1[4] == "#" and self.spe1[5] == "#" :
                self.spe_charge = True


        if self.nom == "Ecureille" :
            if self.arme1[0] == "#" and self.arme1[1] == "#" and self.arme1[2] == "#" :
                self.a1_charge = True
            
            if self.arme2[0] == "#" and self.arme2[1] == "#" and self.arme2[2] == "#" and self.arme2[3] == "#" :
                self.a2_charge = True

            if self.dete1[0] == "#" and self.dete1[1] == "#" and self.dete1[2] == "#" and self.dete1[3] == "#" :
                self.d1_charge = True

            if self.dete2[0] == "#" and self.dete2[1] == "#" and self.dete2[2] == "#" :
                self.d2_charge = True

            if self.spe1[0] == "#" and self.spe1[1] == "#" and self.spe1[2] == "#" and self.spe1[3] == "#" and self.spe1[4] == "#" and self.spe1[5] == "#" :
                self.spe_charge = True

        if choix == 1 :
            choix = "la torpille 🚀"
            
        if choix == 2 :
            choix = "la mine 💣"

        if choix == 3 :
            choix = "le drone 🤖"

        if choix == 4 :
            choix = "le sonar 🔍"

        if self.nom == "Tigre" and choix == 5 :
            choix = "le silence 🌟"

        if self.nom == "Ecureille" and choix == 5 :
            choix = "le leurre 🌟"

        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print(f"Vous avez chargé {choix} :")
        self.afficher_systeme()

        return


    def afficher_systeme(self) :
        a1 = self.arme1[0]
        a2 = self.arme1[1]
        a3 = self.arme1[2]
        a4 = self.arme1[3]
        a5 = self.arme1[4]
        a6 = self.arme1[5]

        b1 = self.arme2[0]
        b2 = self.arme2[1]
        b3 = self.arme2[2]
        b4 = self.arme2[3]
        b5 = self.arme2[4]
        b6 = self.arme2[5]

        c1 = self.dete1[0]
        c2 = self.dete1[1]
        c3 = self.dete1[2]
        c4 = self.dete1[3]
        c5 = self.dete1[4]
        c6 = self.dete1[5]

        d1 = self.dete2[0]
        d2 = self.dete2[1]
        d3 = self.dete2[2]
        d4 = self.dete2[3]
        d5 = self.dete2[4]
        d6 = self.dete2[5]

        e1 = self.spe1[0]
        e2 = self.spe1[1]
        e3 = self.spe1[2]
        e4 = self.spe1[3]
        e5 = self.spe1[4]
        e6 = self.spe1[5]


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
                |   ( \||/ )   | - {b4}      ~          |  /     /  \  |          ~
                |    ―-II-―    | - {b3}      ~          | (    °/    ) | - {d3}      ~
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

    def larguer_torpille(self, sous_marin_ennemi, carte, nom_ennemi, nom_self, fin):

        #=====================#
        '''Tigre - Ecureille'''
        #=====================#

        if self.nom == "Tigre" or self.nom == "Ecureille" :
            print("\nSelectionner un emplacement sur la map :")
            carte.Afficher_carte()
            
            while True :
                try :
                    yx = input("Entrez une position : ")
                    position = traiter_entree(yx)

                    if position != 1 :
                        if position != 2 :
                            if position != 3 :
                                y = lettre_to_chiffre(position[0])
                                x = position[1]

                                emplacement_tir = x, y
                                distance_x = abs(self.pos[0] - x) 
                                distance_y = abs(self.pos[1] - y)
                                #distance totale parcouru par le missile
                                distance_totale = distance_x + distance_y
                                traverser_ile = False

                                #si le sm est une tigre, qu'il y a une île au nord, au sud, a l'ouest ou a l'est (dans l'ordre des parenthèses), alors le sm ne peut pas tiré derrière l'ile +1 et +2 car sinon le missile traverserais l'île
                                if self.nom == "Tigre" :
                                    #nord
                                    #une île se trouve au nord dans un rayon de 1 OU 2 cases explorable
                                    #le try sert a passer l'erreur d'index car au bord haut de la map (pour la partie nord) on ne peut pas accéder à l'index -1 ou -2 par exemple
                                    try :
                                        if carte.carte[self.pos[0] - 1][self.pos[1]] == "■" or carte.carte[self.pos[0] - 2][self.pos[1]] == "■" :
                                            #si la position du tir nord se trouve de l'autre coté de l'ile
                                            if (x == self.pos[0] - 3 or x == self.pos[0] - 4) and y == self.pos[1] :
                                                traverser_ile = True
                                    
                                        if carte.carte[self.pos[0] - 3][self.pos[1]] == "■" :
                                            if x == self.pos[0] - 4 and y == self.pos[1] :
                                                traverser_ile = True

                                    except IndexError :
                                        pass

                                    #sud
                                    try :
                                        if carte.carte[self.pos[0] + 1][self.pos[1]] == "■" or carte.carte[self.pos[0] + 2][self.pos[1]] == "■" :
                                            if (x == self.pos[0] + 3 or x == self.pos[0] + 4) and y == self.pos[1] :
                                                traverser_ile = True
                                            
                                        if carte.carte[self.pos[0] + 3][self.pos[1]] == "■" :
                                            if x == self.pos[0] + 4 and y == self.pos[1] :
                                                traverser_ile = True
                                        
                                    except IndexError :
                                        pass

                                    #ouest
                                    try :
                                        if carte.carte[self.pos[0]][self.pos[1] - 1] == "■" or carte.carte[self.pos[0]][self.pos[1] - 2] == "■" :
                                            if (y == self.pos[1] - 2 or y == self.pos[1] - 3) and x == self.pos[0] :
                                                traverser_ile = True
                                                        
                                        if carte.carte[self.pos[0]][self.pos[1] - 3] == "■" :
                                            if y == self.pos[1] - 3 and x == self.pos[0] :
                                                traverser_ile = True
                                            
                                    except IndexError :
                                        pass

                                    #est
                                    try :
                                        if carte.carte[self.pos[0]][self.pos[1] + 1] == "■" or carte.carte[self.pos[0]][self.pos[1] + 2] == "■" :
                                            if (y == self.pos[1] + 2 or y == self.pos[1] + 3) and x == self.pos[0] :
                                                traverser_ile = True
                                                            
                                        if carte.carte[self.pos[0]][self.pos[1] + 3] == "■" :
                                            if y == self.pos[1] + 3 and x == self.pos[0] :
                                                traverser_ile = True

                                    except IndexError :
                                        pass
                                    
                                #pareil pour le sm ecureille
                                if self.nom == "Ecureille" :
                                    #nord
                                    try :
                                        if carte.carte[self.pos[0] - 1][self.pos[1]] == "■" or carte.carte[self.pos[0] - 2][self.pos[1]] == "■" or carte.carte[self.pos[0] - 3][self.pos[1]] == "■" :
                                            if (x == self.pos[0] - 4 or x == self.pos[0] - 5) and y == self.pos[1] :
                                                traverser_ile = True
                                    
                                        if carte.carte[self.pos[0] - 4][self.pos[1]] == "■" :
                                            if x == self.pos[0] - 5 and y == self.pos[1] :
                                                traverser_ile = True

                                    except IndexError :
                                        pass
                                    
                                    #sud
                                    try :
                                        if carte.carte[self.pos[0] + 1][self.pos[1]] == "■" or carte.carte[self.pos[0] + 2][self.pos[1]] == "■" or carte.carte[self.pos[0] + 3][self.pos[1]] == "■" : 
                                            if (x == self.pos[0] + 4 or x == self.pos[0] + 5) and y == self.pos[1] :
                                                traverser_ile = True
                                        
                                        if carte.carte[self.pos[0] + 4][self.pos[1]] == "■" :
                                            if x == self.pos[0] + 5 and y == self.pos[1] :
                                                traverser_ile = True

                                    except IndexError :
                                        pass
                                    
                                    #ouest
                                    try :
                                        if carte.carte[self.pos[0]][self.pos[1] - 1] == "■"  or carte.carte[self.pos[0]][self.pos[1] - 2] == "■" or carte.carte[self.pos[0]][self.pos[1] - 3] == "■" : 
                                            if (y == self.pos[1] - 4 or y == self.pos[1] - 5) and x == self.pos[0] :
                                                traverser_ile = True
                                                
                                        if carte.carte[self.pos[0]][self.pos[1] - 4] == "■" :
                                            if y == self.pos[1] - 5 and x == self.pos[0] :
                                                traverser_ile = True

                                    except IndexError :
                                        pass

                                    #est
                                    try :
                                        if carte.carte[self.pos[0]][self.pos[1] + 1] == "■"  or carte.carte[self.pos[0]][self.pos[1] + 2] == "■"  or carte.carte[self.pos[0]][self.pos[1] + 3] == "■" :
                                            if (y == self.pos[1] + 4 or y == self.pos[1] + 5) and x == self.pos[0] :
                                                traverser_ile = True 
                                                
                                        if carte.carte[self.pos[0]][self.pos[1] + 4] == "■" :
                                            if y == self.pos[1] + 5 and x == self.pos[0] :
                                                traverser_ile = True

                                    except IndexError :
                                        pass


                                if traverser_ile == False :
                                    if 0 <= y <= ord(carte.derniere_colonne) - ord('A') and 0 <= x <= int(carte.derniere_ligne) - 1 :
                                        if (self.nom == "Tigre" and distance_totale <= 4) or (self.nom == "Ecureille" and distance_totale <= 5) :
                                            #on reset graphiquement le chargement de l'arme
                                            for i in range(6):
                                                self.arme1[i] = "0"

                                            #on reset la valeur de l'armement1 à False pour que le jeu comprenne que la torpille a été tirée
                                            self.a1_charge = False

                                            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

                                            #le sous-marin tir sur une île
                                            if carte.carte[x][y] == "■" :
                                                print(f"\nVous avez tirer une torpille sur une île ! 💥\nElle explose dessus et ne fait aucun dégât alentour...\n")
                                                input("\nSUIVANT")
                                                return fin

                                            #le sous-marin se tir dessus
                                            if emplacement_tir == self.pos :
                                                print(f"\nVous avez tirer une torpille en plein sur VOTRE sous-marin !!! 💥\nVous prennez 2 points de dégats !!!\nVous entendez votre équipage crier : 'LE CAPITAINE EST DEVENU FOU ?!'\n")
                                                self.vie -= 2
                                                print(f"========== Sous-marin '{nom_self}' ==========\n- Vie restante : {self.vie}❤️\n")

                                                if self.vie <= 0 :
                                                    #fin de game
                                                    fin = True
                                                
                                            #le sous marin tir sur un emplacement à côté de lui
                                            elif ((x == self.pos[0]+1 or x == self.pos[0]-1) and (y == self.pos[1]+1 or y == self.pos[1]-1)) or ((x == self.pos[0]+1 or x == self.pos[0]-1) and (y == self.pos[1])) or ((y == self.pos[1]+1 or y == self.pos[1]-1) and (x == self.pos[0])) :
                                                print(f"\nVous avez tirer une torpille à côté de votre propre sous-marin ! 💥\nVous prennez 1 point de dégats !\n\n")
                                                self.vie -= 1
                                                print(f"========== Sous-marin '{nom_self}' ==========\n- Vie restante : {self.vie}❤️\n")
                                                    
                                                if self.vie <= 0 :
                                                    #fin de game
                                                    fin = True

                                            #si l'emplacement du tir est égale à la position du sous marin ennemi.
                                            if emplacement_tir == sous_marin_ennemi.pos :
                                                print(f"\n\nLe capitaine adverse '{sous_marin_ennemi.capitaine}' annonce : \n🚨 IMPACT DIRECT !🚨")
                                                print(f"\nVous avez tirer une torpille en plein sur le sous-marin ennemi '{nom_ennemi}' ! 💥\nIl prend 2 points de dégats !!!\n")
                                                sous_marin_ennemi.vie -= 2
                                                print(f"========== Sous-marin '{nom_ennemi}' ==========\n- Vie restante : {sous_marin_ennemi.vie}❤️\n")
                                                    
                                                if sous_marin_ennemi.vie <= 0 :
                                                    #fin de game
                                                    fin = True

                                                input("SUIVANT")
                                                return fin

                                            #La première condition and (les deux premières parenthèses) vérifie si l'emplacement du tir est dans la diagonale du sous marin ennemi. Le deux suivante check si le tir se situe à côté horizontalement du sm ennemi. Et les deux dernières check si le tir a été fait à côté verticalement du sm ennemi. Un peu indigeste, mais ca marche
                                            elif ((x == sous_marin_ennemi.pos[0]+1 or x == sous_marin_ennemi.pos[0]-1) and (y == sous_marin_ennemi.pos[1]+1 or y == sous_marin_ennemi.pos[1]-1)) or ((x == sous_marin_ennemi.pos[0]+1 or x == sous_marin_ennemi.pos[0]-1) and (y == sous_marin_ennemi.pos[1])) or ((y == sous_marin_ennemi.pos[1]+1 or y == sous_marin_ennemi.pos[1]-1) and (x == sous_marin_ennemi.pos[0])):
                                                print(f"\n\nLe capitaine adverse '{sous_marin_ennemi.capitaine}' annonce : \n🚨 IMPACT INDIRECT !🚨")
                                                print(f"\nVous avez tirer une torpille juste à côté du sous-marin ennemi '{nom_ennemi}' ! 💥\nIl prend tout de même 1 point de dégats !\n")
                                                sous_marin_ennemi.vie -= 1
                                                print(f"========== Sous-marin '{nom_ennemi}' ==========\n- Vie restante : {sous_marin_ennemi.vie}❤️\n")
                                                    
                                                if sous_marin_ennemi.vie <= 0 :
                                                    #fin de game
                                                    fin = True
                                                    
                                                input("SUIVANT")
                                                return fin

                                            #l'emplacement du tir est ni sur le sous-marin ennemi ni à ses alentours.
                                            else :
                                                print(f"\n\nLe capitaine adverse '{sous_marin_ennemi.capitaine}' annonce : \n🚨 RAS !🚨") 
                                                print(f"\nVous avez tirer une torpille pour rien !\n")
                                                print(f"========== Sous-marin '{nom_ennemi}' ==========\n- Vie restante : {sous_marin_ennemi.vie}❤️\n")
                                                input("\nSUIVANT")
                                                return fin

                                        else :
                                            if self.nom == "Tigre" :
                                                print("\n\n❌ Votre sous-marin ne peut larguer une torpille qu'à une distance maximal de 4 cases sans diagonale !")

                                            if self.nom == "Ecureille" :
                                                print("\n\n❌ Votre sous-marin ne peut larguer une torpille qu'à une distance maximal de 5 cases sans diagonale !")
                                    else : 
                                        print("\n\n❌ Veuillez larguer votre torpille dans les limites de la map !")

                                else :
                                    print("\n\n❌ Vous ne pouvez pas traverser les îles avec votre torpille !")

                            else :
                                print("\n\n❌ Entrée une ligne correcte.")

                        else :
                            print("\n\n❌ Entrée une colonne correcte.")

                    else :
                        print("\n\n❌ Entrée des coordonnées correcte, par exemple 'A3'")
                
                except ValueError :
                    print("\n\n❌ Veuillez choisir des valeurs valides.")


    def larguer_mine(self, carte):
        print("\nSelectionner un emplacement sur la map :")
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
                                if ((x == self.pos[0]+1 or x == self.pos[0]-1) and (y == self.pos[1]+1 or y == self.pos[1]-1)) or ((x == self.pos[0]+1 or x == self.pos[0]-1) and (y == self.pos[1])) or ((y == self.pos[1]+1 or y == self.pos[1]-1) and (x == self.pos[0])) :
                                    if carte.carte[x][y] != "■" :
                                        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

                                        self.emplacement_mines.append((x, y))
                                        
                                        for i in range(6):
                                                self.arme2[i] = "0"
                                        
                                        #Si le sm a déjà naviguer là ou la mine est posé, alors le signalement de la mine sera en majuscule est le sm ne pourra pas naviguer dessus;
                                        if carte.carte[x][y] == '←':
                                            self.mine_cap.append("OUEST")
                                            carte.carte[x][y] = "M"

                                        elif carte.carte[x][y] == '→':
                                            self.mine_cap.append("EST")
                                            carte.carte[x][y] = "M"

                                        elif carte.carte[x][y] == '↑':
                                            self.mine_cap.append("NORD")
                                            carte.carte[x][y] = "M"

                                        elif carte.carte[x][y] == '↓':
                                            self.mine_cap.append("SUD")
                                            carte.carte[x][y] = "M"
                                        
                                        else :
                                            carte.carte[x][y] = "m"
                                            self.mine_cap.append("Rien")

                                        self.a2_charge = False
                                        print("\nVotre mine a été placé en : ", position[0], x+1, "\n")
                                        carte.Afficher_carte()
                                        input("SUIVANT")

                                        return
                                    
                                    else :
                                        print("\n\n❌ Vous ne pouvez pas poser une mine sur une île !")
                                
                                else :
                                    print("\n\n❌ Veuillez choisir des valeurs autour de votre sous-marin sur des cases de mer qui ne sont déjà pas occupé par l'une de vos mines.")

                            else :
                                print("\n\n❌ Veuillez choisir des valeurs dans la limite de la map.")

                        else :
                            print("\n\n❌ Entrée une ligne correcte.")

                    else :
                        print("\n\n❌ Entrée une colonne correcte.")

                else :
                    print("\n\n❌ Entrée des coordonnées correcte.")

            except ValueError : 
                print("\n\n❌ Veuillez choisir des valeurs valides.")


    def exploser_mine(self, sous_marin_ennemi, nom_ennemi, nom_self, carte, fin) :
        nb_mines = len(self.emplacement_mines)
        condition_boucle_explo = False
        
        print("\n")
        carte.Afficher_carte()

        #afficher l'emplacement des mines à exploser et le lier à un numéro de mine
        for i in range(nb_mines) :
            x, y = self.emplacement_mines[i]
            y_l = chiffre_to_lettre(y)
            print(f"{i + 1} - Faire exploser la mine placée en {y_l}{x + 1}")

        while True :
            try :
                choix = int(input(f"\nChoisissez la mine que vous voulez faire exploser (1 - {nb_mines}). Annuler l'explosion (0) : "))

                if 0 < choix <= nb_mines :

                    emplacement_mine_choisis = self.emplacement_mines[choix - 1]
                    x, y = emplacement_mine_choisis
                    mine_cap_choisis = self.mine_cap[choix - 1]

                    #si le cap associé à la mine posée égale une valeur de cap alors on remet sur la carte la fléche du cap pour prévenir que le sm est déjà passer par la
                    if mine_cap_choisis == "OUEST" :
                        carte.carte[x][y] = '←'

                    elif mine_cap_choisis == "EST" :
                        carte.carte[x][y] = '→'

                    elif mine_cap_choisis == "NORD" :
                        carte.carte[x][y] = '↑'

                    elif mine_cap_choisis == "SUD" :
                        carte.carte[x][y] = '↓'

                    else :
                        carte.carte[x][y] = '.'

                    # i, j = self.pos
                    # carte.carte[i][j] = self.nom[0]

                    #on retire la mine qui a explosée dans le tableau des emplacement_mines ainsi que son cap associé.
                    self.emplacement_mines.remove(emplacement_mine_choisis)
                    self.mine_cap.remove(mine_cap_choisis)

                    #le sous-marin explose une mine sur sois
                    if emplacement_mine_choisis == self.pos :
                        print(f"\nVous avez fait exploser une mine en plein sur VOTRE SOUS-MARIN !!! 💥\nVous prennez 2 points de dégats !!!\nVous entendez votre équipage crier : 'MUTINERIE, CHANGEONS DE CAPITAINE !!!'\n")
                        self.vie -= 2
                        print(f"========== Sous-marin '{nom_self}' ==========\n- Vie restante : {self.vie}❤️\n")

                        if self.vie <= 0 :
                            #fin de game
                            fin = True
                            
                    #le sous marin explose la mine sur un emplacement à côté de lui
                    elif ((x == self.pos[0]+1 or x == self.pos[0]-1) and (y == self.pos[1]+1 or y == self.pos[1]-1)) or ((x == self.pos[0]+1 or x == self.pos[0]-1) and (y == self.pos[1])) or ((y == self.pos[1]+1 or y == self.pos[1]-1) and (x == self.pos[0])) :
                        print(f"\nVous avez fait exploser une mine à côté de votre propre sous-marin ! 💥\nVous prennez 1 point de dégats !\n\n")
                        self.vie -= 1
                        print(f"========== Sous-marin '{nom_self}' ==========\n- Vie restante : {self.vie}❤️\n")

                        if self.vie <= 0 :
                            #fin de game
                            fin = True

                    if emplacement_mine_choisis == sous_marin_ennemi.pos :
                        print(f"\n\nLe capitaine adverse '{sous_marin_ennemi.capitaine}' annonce : \n🚨 IMPACT DIRECT !🚨")
                        print(f"\nVotre mine a explosé en plein sur le sous-marin ennemi '{nom_ennemi}' ! 💥\nIl prend 2 points de dégats !!!\n")
                        sous_marin_ennemi.vie -= 2
                        print(f"========== Sous-marin '{nom_ennemi}' ==========\n- Vie restante : {sous_marin_ennemi.vie}❤️\n")
                                
                        if sous_marin_ennemi.vie <= 0 :
                            #fin de game
                            fin = True

                        input("SUIVANT")
                        return fin, condition_boucle_explo

                    #La première condition and (les deux premières parenthèses) vérifie si l'emplacement du tir est dans la diagonale du sous marin ennemi. Le deux suivante check si le tir se situe à côté horizontalement du sm ennemi. Et les deux dernières check si le tir a été fait à côté verticalement du sm ennemi. Un peu indigeste, mais ca marche
                    elif ((x == sous_marin_ennemi.pos[0]+1 or x == sous_marin_ennemi.pos[0]-1) and (y == sous_marin_ennemi.pos[1]+1 or y == sous_marin_ennemi.pos[1]-1)) or ((x == sous_marin_ennemi.pos[0]+1 or x == sous_marin_ennemi.pos[0]-1) and (y == sous_marin_ennemi.pos[1])) or ((y == sous_marin_ennemi.pos[1]+1 or y == sous_marin_ennemi.pos[1]-1) and (x == sous_marin_ennemi.pos[0])):
                        print(f"\n\nLe capitaine adverse '{sous_marin_ennemi.capitaine}' annonce : \n🚨 IMPACT INDIRECT !🚨")
                        print(f"\nVotre mine a explosé juste à côté du sous-marin ennemi '{nom_ennemi}' ! 💥\nIl prend tout de même 1 point de dégats !\n")
                        sous_marin_ennemi.vie -= 1
                        print(f"========== Sous-marin '{nom_ennemi}' ==========\n- Vie restante : {sous_marin_ennemi.vie}❤️\n")
                                
                        if sous_marin_ennemi.vie <= 0 :
                            #fin de game
                            fin = True
                                
                        input("SUIVANT")
                        return fin, condition_boucle_explo

                    #l'emplacement du tir est ni sur le sous-marin ennemi ni à ses alentours.
                    else :
                        print(f"\n\nLe capitaine adverse '{sous_marin_ennemi.capitaine}' annonce : \n🚨 RAS !🚨") 
                        print(f"\nVous avez fait exploser une mine pour rien !\n")
                        print(f"========== Sous-marin '{nom_ennemi}' ==========\n- Vie restante : {sous_marin_ennemi.vie}❤️\n")
                        input("\nSUIVANT")
                        return fin, condition_boucle_explo

                if choix == 0 :
                    condition_boucle_explo = True
                    return fin, condition_boucle_explo
            
            except ValueError :
                print("\n\n❌ choisissez une valeur valide.")


    def explosion_auto(self, sous_marin_ennemi, nom_self, carte, fin, carte_ennemi):

        if sous_marin_ennemi.nom == "Ecureille" :
            if sous_marin.ennemi.emplacement_mines :
                for i in range(len(sous_marin_ennemi.emplacement_mines)) :
                    x, y = sous_marin_ennemi.emplacement_mines[i - 1]
                    
                    if self.pos == sous_marin_ennemi.emplacement_mines[i - 1] :
                        
                        if sous_marin_ennemi.mine_cap[i - 1] == "OUEST" :
                            carte_ennemi.carte[x][y] = '←'

                        elif sous_marin_ennemi.mine_cap[i - 1] == "EST" :
                            carte_ennemi.carte[x][y] = '→'

                        elif sous_marin_ennemi.mine_cap[i - 1] == "NORD" :
                            carte_ennemi.carte[x][y] = '↑'

                        elif sous_marin_ennemi.mine_cap[i - 1] == "SUD" :
                            carte_ennemi.carte[x][y] = '↓'

                        emplacement_mine_explose = sous_marin_ennemi.emplacement_mines[i - 1]
                        mine_cap_explose = sous_marin_ennemi.mine_cap[i - 1]
                        sous_marin_ennemi.emplacement_mines.remove(emplacement_mine_explose)
                        sous_marin_ennemi.mine_cap.remove(mine_cap_explose)

                        self.vie -= 1

                        print(f"\nUne mine ennemi à déjà été larguée sur votre nouvelle position et celle-ci a explosé au contact de votre sous-marin ! 💥 \nVous prenez 1 point de dégats !\n")
                        print(f"========== Sous-marin '{nom_self}' ==========\n- Vie restante : {self.vie}❤️\n")

                        if self.vie <= 0 :
                            #fin de game
                            fin = True
                                
                        return fin

        if self.nom == "Ecureille" :
            if self.emplacement_mines :
                for i in range(len(self.emplacement_mines)) :
                    x, y = self.emplacement_mines[i - 1]

                    if self.pos == self.emplacement_mines[i - 1] :

                        if self.mine_cap[i - 1] == "OUEST" :
                            carte.carte[x][y] = '←'

                        elif self.mine_cap[i - 1] == "EST" :
                            carte.carte[x][y] = '→'

                        elif self.mine_cap[i - 1] == "NORD" :
                            carte.carte[x][y] = '↑'

                        elif self.mine_cap[i - 1] == "SUD" :
                            carte.carte[x][y] = '↓'

                        emplacement_mine_explose = self.emplacement_mines[i - 1]
                        mine_cap_explose = self.mine_cap[i - 1]
                        self.emplacement_mines.remove(emplacement_mine_explose)
                        self.mine_cap.remove(mine_cap_explose)

                        self.vie -= 1

                        print(f"\nVous aviez déjà posé une mine sur cette position et celle-ci à exploser au contact de votre sous-marin ! 💥 \nVous prenez 1 point de dégats !\n")
                        print(f"========== Sous-marin '{nom_self}' ==========\n- Vie restante : {self.vie}❤️\n")
            
                        if self.vie <= 0 :
                            fin = True
                                
                        return fin
        
        return fin
    

    def larguer_drone(self, carte, sous_marin_ennemi) :
        #si le sm est l'ecureille, alors on check si le sm ennemie se trouve autour d'une ile, si oui on renvoie un msg, si non on renvoie un msg
        milieu_largeur = carte.largeur // 2
        milieu_hauteur = carte.hauteur // 2
        x, y = sous_marin_ennemi.pos
        condition_boucle_det1 = False

        if self.nom == "Ecureille" :
            #si une case "■" se trouve autour du sous-marin
            if sous_marin_ennemi.pos[0] + 1 == "■" or sous_marin_ennemi.pos[0] - 1 == "■" or sous_marin_ennemi.pos[1] + 1 == "■" or sous_marin_ennemi.pos[1] - 1 == "■" or ((sous_marin_ennemi.pos[0] + 1 or sous_marin_ennemi.pos[0] - 1) and (sous_marin_ennemi.pos[1] + 1 or sous_marin_ennemi.pos[0] - 1)) :
                ile = "et le sous-marin ennemi se trouve autour d'une île ! 🏝️ "

            else :
                ile = "et les flots de la mer entourent le sous-marin ennemi. 🌊 "
        
        while True :
            try : 
                choix = int(input("Vous larguez votre drone secteur (1 - 4) ou changé de compétence (0): "))
                if 1 <= choix <= 4 :
                    self.d1_charge = False
                    #on reset graphiquement le chargement du drone
                    for i in range(6):
                        self.dete1[i] = "0"
                    
                    #le joueur a selectionner le secteur 1 et la position du sm ennemi est dans le secteur 1
                    if choix == 1 and x < milieu_hauteur and y < milieu_largeur :
                        rep = "\nVotre drone vous retourne : '✅ OUI ✅' "
                        
                        if self.nom == "Ecureille" :
                            print(rep + ile)
                        
                        else :
                            print(rep)
                            
                        return condition_boucle_det1
                    
                    #le joueur a selectionner le secteur 2 et la position du sm ennemi est dans le secteur 2
                    elif choix == 2 and x < milieu_hauteur and y >= milieu_largeur:
                        rep = "\nVotre drone vous retourne : '✅ OUI ✅' "
                        
                        if self.nom == "Ecureille" :
                            print(rep + ile)
                        
                        else :
                            print(rep)
                            
                        return condition_boucle_det1

                    elif choix == 3 and x >= milieu_hauteur and y < milieu_largeur :
                        rep = "\nVotre drone vous retourne : '✅ OUI ✅' "
                        
                        if self.nom == "Ecureille" :
                            print(rep + ile)
                        
                        else :
                            print(rep)
                            
                        return condition_boucle_det1

                    elif choix == 4 and x >= milieu_hauteur and y >= milieu_largeur :
                        rep = "\nVotre drone vous retourne : '✅ OUI ✅' "

                        if self.nom == "Ecureille" :
                            print(rep + ile)
                        
                        else :
                            print(rep)

                        return condition_boucle_det1

                    else :
                        print("\nVotre drone vous retourne : '🚫 NON 🚫' ")
                        return 

                elif choix == 0 :
                    condition_boucle_det1 = True
                    return condition_boucle_det1
                
                else :
                    print("\n\n❌ choisissez un secteur existant.")

            except ValueError :
                print("\n\n❌ choisissez une valeur valide.")

    def lancer_sonar(self, carte, sous_marin_ennemi, nom_ennemi, nom_self, carte_ennemi) :
        print(changement)
        print(f"\n⚠⚠⚠ Attention ⚠⚠⚠ : \nC'est au Capitaine : '{sous_marin_ennemi.capitaine}', de l'équipe '{nom_ennemi}' de jouer.")
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
                faux = int(input("\n\n\nVoici le type de coordonnées trompeuse que vous pouvez choisir : \n1 - Colonne\n2 - Ligne\n3 - Secteur\n\nVeuillez maintenant sélectionné celle que le sonar ennemi captera  (1 - 3) : "))

                if faux != condition_vrai :
                    print("\n\n")
                    carte_ennemi.Afficher_carte()
                    print("\n")

                    if faux == 1 :
                        while faux == 1 :
                            try :
                                y_lettre = input(f"Choisissez une colonne sur laquelle votre sous-marin n'est pas (A - {carte.derniere_colonne}) ou revenir en arrière (0) : ")
                                
                                if y_lettre == "0" :
                                    break
                                
                                y_given = lettre_to_chiffre(y_lettre)
                                
                                #si je met False a la place d'alpha, alors A ne marche pas car 0 (A=0) est égale a False.
                                if y_given != "alpha" :
                                    if y_lettre != y_self :
                                        if 0 <= y_given <= ord(carte.derniere_colonne) - ord('A') : 
                                            faux = "Le sous-marin ennemi se trouve colonne : " + y_lettre
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
                                x_given = int(input(f"Choisissez une ligne sur laquelle votre sous-marin n'est pas (1 - {carte.derniere_ligne}) ou revenir en arrière (0) : "))
                                
                                if x_given == 0 :
                                    break

                                elif x_given != x + 1 :
                                    if 0 <= x_given <= int(carte.derniere_ligne) - 1 : 
                                        faux = "Le sous-marin ennemi se trouve ligne : " + str(x_given)
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
            self.dete2[i] = "0"

        self.d2_charge = False

        #On renvoie la réponse de l'ennemi aléatoirement.
        print(changement)
        print(f"\n⚠⚠⚠ Attention ⚠⚠⚠ : \nC'est au Capitaine : '{self.capitaine}', de l'équipe '{nom_self}' de jouer.")
        input("\nSUIVANT")

        print("\n\n==================== Résultat du drone ====================")

        #alea_1 est égale à vrai ou à faux choisis aléatoirement
        alea_1 = random.choice([vrai, faux])
        #si alea_1 est égale à vrai alors alea_2 est égale à faux et vise versa
        alea_2 = faux if alea_1 == vrai else vrai

        print("\n" + alea_1 + "\nOU\n" + alea_2) 
        print("\nVous ne savez pas laquelle est vrai ou fausse...")
        input("\n\nSUIVANT")

        return
    
    def lancer_silence(self, carte) :
        x, y = self.pos
        print("\n\n")
        carte.Afficher_carte()
        
        while True :
            try :
                cap_silence = input(f"\n{self.capitaine}, annoncez discretement un cap à votre équipe (OUEST, NORD, EST, SUD) ou retourner à la sélection des compétences (0): ")
                cap_silence = cap_silence.upper()

                if cap_silence == "O" :
                    cap_silence = "OUEST"

                elif cap_silence == "N" :
                    cap_silence = "NORD"

                elif cap_silence == "E" :
                    cap_silence = "EST"

                elif cap_silence == "S" :
                    cap_silence = "SUD"

                if cap_silence == "OUEST" or cap_silence == "EST" or cap_silence == "NORD" or cap_silence == "SUD" :
                    while True :
                        try :
                            distance = int(input(f"\n{self.capitaine}, choisissez une distance à parcourir (0 - 4) ou choisir un autre cap (9): "))
                            if 0 <= distance <= 4 :
                                condition_boucle_spe = False 
                                condition_impossible = False
                                premiere_lettre = self.nom[0]

                                if cap_silence == "OUEST" :
                                    #on vérifie si le sm ne sort pas de la map
                                    if 0 <= y - distance :
                                        y_ouest = y
                                            
                                        #le sous-marin ne peut se déplacer que sur des cases valides non exploré
                                        for _ in range(distance) :
                                            y_ouest -= 1
                                            if carte.carte[x][y_ouest] not in [".", "m"] :
                                                #variable empéchant le déplacement
                                                condition_impossible = True

                                        #le sm ne se déplace pas SUR une case explorable
                                        if carte.carte[x][y - distance] not in [".", "m", premiere_lettre] :
                                            condition_impossible = True
                                            
                                        if condition_impossible == True :
                                            print("\n\n❌ Vous ne pouvez pas traverser les îles NI traverser une zone déjà exploré !")

                                        else :
                                            y_ouest = y
                                            for _ in range(distance) :
                                                carte.carte[x][y_ouest] = "←"
                                                y_ouest -= 1

                                            y -= distance
                                            carte.carte[x][y] = self.nom[0]
                                            self.pos = x, y

                                            for i in range(6) :
                                                self.spe1[i] = "0"

                                            self.spe_charge = False

                                            return condition_boucle_spe
                                        
                                    else :
                                        print("\n\n❌ Vous ne pouvez pas sortir de la map !")
                                        
                                if cap_silence == "EST" :
                                    if y + distance <= ord(carte.derniere_colonne) - ord('A') :
                                        y_est = y
                                            
                                        for _ in range(distance) :
                                            y_est += 1
                                            if carte.carte[x][y_est] not in [".", "m"] :
                                                #variable empéchant le déplacement
                                                condition_impossible = True

                                        if carte.carte[x][y + distance] not in [".", "m", premiere_lettre] :
                                            condition_impossible = True
                                            
                                        if condition_impossible == True :
                                            print("\n\n❌ Vous ne pouvez pas traverser les îles NI traverser une zone déjà exploré !")

                                        else :
                                            y_est = y
                                            for _ in range(distance) :
                                                carte.carte[x][y_est] = '→'
                                                y_est += 1

                                            y += distance
                                            carte.carte[x][y] = self.nom[0]
                                            self.pos = x, y

                                            for i in range(6) :
                                                self.spe1[i] = "0"

                                            self.spe_charge = False

                                            return condition_boucle_spe
                                        
                                    else :
                                        print("\n\n❌ Vous ne pouvez pas sortir de la map !")

                                if cap_silence == "NORD" :
                                    if 0 <= x - distance :
                                        x_nord = x
                                            
                                        for _ in range(distance) :
                                            x_nord -= 1
                                            if carte.carte[x_nord][y] not in [".", "m"] :
                                                #variable empéchant le déplacement
                                                condition_impossible = True

                                        if carte.carte[x - distance][y] not in [".", "m", premiere_lettre] :
                                            condition_impossible = True
                                            
                                        if condition_impossible == True :
                                            print("\n\n❌ Vous ne pouvez pas traverser les îles NI traverser une zone déjà exploré !")

                                        else :
                                            x_nord = x
                                            for _ in range(distance) :
                                                carte.carte[x_nord][y] = '↑'
                                                x_nord -= 1

                                            x -= distance
                                            carte.carte[x][y] = self.nom[0]
                                            self.pos = x, y

                                            for i in range(6) :
                                                self.spe1[i] = "0"

                                            self.spe_charge = False

                                            return condition_boucle_spe
                                        
                                    else :
                                        print("\n\n❌ Vous ne pouvez pas sortir de la map !")
                                        
                                if cap_silence == "SUD" :
                                    if x + distance <= int(carte.derniere_ligne) - 1 :
                                        x_sud = x
                                            
                                        for _ in range(distance) :
                                            x_sud += 1
                                            if carte.carte[x_sud][y] not in [".", "m"] :
                                                #variable empéchant le déplacement
                                                condition_impossible = True
                                        
                                        if carte.carte[x + distance][y] not in [".", "m", premiere_lettre] :
                                            condition_impossible = True
                                            
                                        if condition_impossible == True :
                                            print("\n\n❌ Vous ne pouvez pas traverser les îles NI traverser une zone déjà exploré !")

                                        else :
                                            x_sud = x
                                            for _ in range(distance) :
                                                carte.carte[x_sud][y] = '↓'
                                                x_sud += 1

                                            x += distance
                                            carte.carte[x][y] = self.nom[0]
                                            self.pos = x, y

                                            for i in range(6) :
                                                self.spe1[i] = "0"

                                            self.spe_charge = False

                                            return condition_boucle_spe
                                    
                                    else :
                                        print("\n\n❌ Vous ne pouvez pas sortir de la map !")
                                        
                            elif distance == 9 :
                                print("\n\n")
                                carte.Afficher_carte()
                                break
                            
                            else :
                                print("\n\n❌ Veuillez entrer une distance comprise entre 0 et 4 !")

                        except ValueError :
                            print("\n\n❌ Veuillez entrer une distance valide !")

                elif cap_silence == "0" :
                    self.position = x, y
                    condition_boucle_spe = True
                    return condition_boucle_spe
                
                else :
                    print("\n\n❌ Veuillez choisir un cap compris dans les options ! ")

            except ValueError :
                print("\n\n❌ Veuillez entrer un cap valide !")


    def lancer_leurre(self, leurre) :
        leurre.vivant = True


#creation d'un objet leurre (pour pouvoir utiliser la fonction déplacement_sm de l'objet map)
class Leurre(SousMarin):
    def __init__(self) :
        self.nom = "leurre"
        self.pos = None
        self.vie = 1
        self.vivant = True

leurre = Leurre()

def lettre_to_chiffre(lettre):
    if len(lettre) == 1 and lettre.isalpha() :
        return ord(lettre.upper()) - ord('A')
    
    else :
        return "alpha" 

def chiffre_to_lettre(chiffre):
    return chr(chiffre + ord('A'))


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