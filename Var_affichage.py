#===========#
'''Menu.py'''
#===========#

bonjour = """\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n
===============================================================================================================================================
===============================================================================================================================================
======                                                                                                                                   ======
===   _________     _____   __________  ___________   _____   .___  _______         _________________    _______      _____   __________    ===
===   \_   ___ \   /  _  \  \______   \ \__    ___/  /  _  \  |   | \      \       /   _____/\_____  \   \      \    /  _  \  \______   \   ===
===   /    \  \/  /  /_\  \  |     ___/   |    |    /  /_\  \ |   | /   |   \      \_____  \  /   |   \  /   |   \  /  /_\  \  |       _/   ===
===   \     \____/    |    \ |    |       |    |   /    |    \|   |/    |    \     /        \/    |    \/    |    \/    |    \ |    |   \   ===
===    \______  /\____|__  / |____|       |____|   \____|__  /|___|\____|__  /    /_______  /\_______  /\____|__  /\____|__  / |____|_  /   ===
===           \/         \/                               \/              \/             \/         \/         \/         \/         \/     ===
======                                                                                                                                   ======
===============================================================================================================================================
===============================================================================================================================================
                                                                                                                        
                                                                                                                        Alessandro GADRAT
                               () |
                             /~~~~~~|
                       `~T~T/ Tigre |   c[ ]----     `.
                        `__/___..---t____.[]--------.._`.
        ______..-----~~~~           ___--'--___  <~)    )###-_                                      ___--'--___           ______
   ~~ ~~-~~----..._________..----~~~           ~~~-__--##      ~~--~~ ~~-~~----..._________..----~~~           ~~~-__--~~~      ~~--__🏊______
                    🐟                                                  
                    

                Veuillez saisir une option :                                                         /                   🫧 
                                                           🐠                                       ( .                 🐠__
                                                                          .                         | I__        ___---~~~| |
                        1 - Commencer la partie                          .                   _i_---~~~~  \_---~~~        _-\|
    🐠                                                      🫧        :;.:                /~      ____--~           __-~
                        2 - Règles du jeu                    🐟        ;         ___---~~~----~~~~             __--~
                                                                     : :  __---~~~  _        🫧            __--~
                        3 - Paramètres                              : _-~~  ___---~~_O        🐟       __--~         🐠
                🫧                                                 .:(_            ~          ___---~~
                🐟                                             *.::; ;;~~~------_____-----~~~~
                                                            ***..;
                                        🐠              .ojO  *                               
         🐠                                          .Ji'`                             🐟
                   🐟                             ;`'`
                                                                🐙        """


regles = """

                                             _____  __        _           
                                            |  __ \ \_\      | |          
                                            | |__) |___  __ _| | ___  ___ 
                                            |  _  // _ \/ _` | |/ _ \/ __|
                                            | | \ \  __/ (_| | |  __/\__ \ 
                                            |_|  \_\___|\__, |_|\___||___/
                                                         __/ |            
                                                        |___/             



                                Au fond de la mer, personne ne vous entendra hurler !
                2048. Une nouvelle guerre économique a éclaté. La possession de « terres rares »,
                    matériaux indispensables à la construction d'appareils de haute technologie,
                            est devenue un enjeu majeur à l'échelle internationale.
                Des compagnies privées arment des prototypes de sous-marins de dernière génération
                pour partir à l'assaut des grands fonds, et s'emparer de ces « terres rares ». 
                            Sous les flots paisibles, une guerre silencieuse fait rage, 
                    déployant un usage massif de ces nouvelles technologies encore instables.
                    Vous formez l'équipage de l'un de ces bâtiments de dernière génération.
                        Coopérez, échangez, discutez avec les autres membres d'équipage,
                                        pour vous mesurer au navire adverse. 


                                       🎮 ==========BUT DU JEU=========== 🎮

    Vous incarner un sous-marin. Le premier qui fait couler le sous-marin adverse remporte la partie.
        


                                      ⏸️ ==========MISE EN PLACE========== ⏸️

    Séléctionner 'Paramètre' pour changer les réglages de la partie,
    puis 'Commencer la partie' dans le menu du jeu pour lancer le jeu.

    1) Définir le nombres de joueurs.

    2) Sélection de son équipe et définition du nom de son sous-marin.

    3) Répartition des rôles en fonction du nombre de joueur :
        Équipe de 4 : Le chiffre parfait, chaque joueur endosse un rôle différent.
        Équipe de 3 : un joueur cumule le rôle de Capitaine et de Second.
        Équipe de 2 : un joueur cumule le rôle de Capitaine, de Second et de Mécano.
        Équipe de 1 : un joueur cumule tout les rôles.

    4) Sélection du mode de jeu.

    5) Sélection de la map.

    6) Sélection du sous-marin.

    7) Les capitaines choississent leur point de départ sur la map.

    8) La partie commence.
            

                             4️⃣ ==========LES QUATRES DIFFERENTES FONCTIONS==========4️⃣

╰┈➤ Le Capitaine 👨‍✈️ :
            Le Capitaine est l'élément central de tout l'équipage. En plus d'être responsable de la
            trajectoire prise par le sous-marin, il doit être le lien entre tous les postes.
            En début de partie, le Capitaine choisis la case Mer de son choix pour définir sa position de départ. 
            Puis, dès que le départ est donné (les deux capitaines doivent crier « PLONGEZ ! »), 
            chaque Capitaine choisis des ordres de cap, en traçant sa route sur la carte par la suite.
            Le Capitaine peut déplacer son bâtiment d'UNE SEULE CASE À LA FOIS dans l'une des 4 DIRECTIONS 
            (EST, OUEST, NORD ou SUD).
            Vous ne pouvez pas coupez votre propre route, ni revenir sur le tracé de celle-ci.
            Vous ne pouvez pas traverser une île.
            Le Capitaine efface son tracé uniquement quand il est en surface (voir dans FAIRE SURFACE).

        ➟ JEU AU TOUR PAR TOUR :
            Chaque Capitaine choisis un cap à tour de rôle pous décider de la direction du vaisseau.
            Quand c'est a votre tour de jouer, la partie est en pause pour l'adversaire.

        ➟ JEU EN SIMULTANE :
            Chaque Capitaine choisis son cap à la vitesse de son choix.
            La partie ne se met en pause que quand l'adversaire utilise une compétence.

        🚨IMPORTANT🚨:
            Quelque soit le mode de jeu, Le Capitaine doit attendre que Le Second et Le Mécano aient annoncé «OK» 
            après avoir rempli leur tâche pour émettre un nouvel ordre (voir LE SECOND et LE MÉCANO)
          • Il est interdit de couper sa propre route, ni de revenir sur le tracé de sa propre route.
          • Il est interdit de traverser une île.
          • Le Capitaine ne peut effacer son tracé que quand il est en surface (voir FAIRE SURFACE).

        ➟ Blackout :
            Si le Capitaine se retrouve bloqué à cause du manque d'optimisation de son tracé, 
            il est dans une situation de Blackout et doit IMMÉDIATEMENT FAIRE SURFACE (voir FAIRE SURFACE).

        💡 CONSEIL💡 :
            • Le Capitaine doit régulièrement interroger son Détecteur sur son estimation de la position de l'ennemi.
            • Il est déconseillé de vouloir aller trop vite dans l'annonce des caps pour ne pas perdre le reste de son équipage 
              qui doit réagir à la trajectoire prise et à prendre.
            
╰┈➤ Le Second 🧑‍💼 : 
        Le Second est chargé de remplir les jauges des systèmes du sous-marin : 
        les armes, les systèmes de détection et leur spécialité. 
        À chaque ordre de cap donné par le Capitaine de son équipe, le Second choisis une case de la jauge de compétence son choix
        (ou en suivant les consignes du Capitaine, en fonction de ses besoins). 
        Puis il écrit «OK» afin que le Capitaine puisse donner un nouvel ordre.
        Quand une jauge est remplie, le Second le dit. Le Capitaine sait ainsi qu'il dispose de la compétence.
        Le capitaine est le seul a pouvoir activer le système d'armements contrairement aux système de détection 
        qui peuvent eux être activés soit par le capitaine soit par le Second.

        🚨IMPORTANT🚨:
            La jauge d'un système ne pourra être à nouveau remplie qu'après l'utilisation de ce système ou exceptions. 
            (voir ACTIVATION DES SYSTÈMES).

        ➟ DEGATS 💥:
            La vie du sous-marin correspond au nombre de point de dégat qu'un sous-marin peut encaisser.
            À chaque Dégât sur le sous-marin, seul Le Second peut voir le nombre de point de vie restant,
            car tout les autres postes sont trop occupé a réaliser leur rôle.
            Si la vie du sous-marin tombe à 0, le sous-marin est neutralisé et la partie est perdue.

╰┈➤ Le Mécano 👨‍🔧:
        Le Mécano est chargé de répercuter les pannes du sous-marin qui apparaissent suite aux ordres donnés.
        Certaines pannes neutralisent des systèmes du sous-marin, d'autres peuvent provoquer un Dégât.
        
        ➟ PANNE ⚠️ : 
            Pour chaque ordre de cap donné par le Capitaine de son équipe, 
            le Mécano choisis UNE PANNE dans le cadran correspondant au cap donné (Ouest, Nord, Sud, Est).
            Puis il écrit «ok» afin que le Capitaine puisse donner un nouvel ordre. 
            Le Mécano peut cocher un voyant de son choix dans les Circuits Centraux ou dans le Réacteur.
            Si au moins 1 symbole d'un système est coché, il n'est pas possible d'activer ce système.
                            
                IMPORTANT ! Un symbole représente 1 systèmes composé des deux compétences.
                                        ARM = Système d'armement
                                        DET = Système de détection
                                        SPE = Système spéciale
                                        RAD = Système du réacteur
            
            Les pannes Radiations n'ont pas de conséquence tant que TOUS les voyants Radiations ne sont pas cochés,
            ou que ça ne provoque pas une panne Cadran Complet.
            Quand TOUS les voyants D'UN MÊME CADRAN (Nord, Sud, Est, Ouest) sont cochés 
            (qu'ils soient dans les Circuits Centraux ou le Réacteur), le sous-marin subit un Dégât.
            TOUTES les pannes du sous-marin sont ensuite réparer.
            Il faut donc communiquer avec le Capitaine pour éviter d'en arriver là !

            Exemple :
                Le Capitaine a donnée trop d'ordre à l'Ouest,
                et TOUS les voyants du cadran O sont cochés.
                Le navire prend un point de dégat et toute les pannes sont réparés.

                                         /===\       
                                         : O :         
                                         \===/       
                                    /―――――――――――――\   
                                    | ̷J̷A̷U̷N̷E - ̷A̷R̷M |   
                                    | ̷J̷A̷U̷N̷E - ̷S̷P̷E |   
                                    \ ̷J̷A̷U̷N̷E - ̷D̷E̷T /     
                                     |―――――――――――|        
                                    / ̷N̷O̷N̷E  - ̷D̷E̷T \     
                                    | ̷N̷O̷N̷E  - ̷R̷A̷D |  
                                    | ̷N̷O̷N̷E  - ̷R̷A̷D |  
                                    \―――――――――――――/  

       💡 CONSEIL💡 : 
            Pour éviter les catastrophes, le Mécano doit interpeler le Capitaine 
            pour lui demander de ne pas donner d'ordres de cap dangereux pour la machine.

        ➟ REPARATION DES CIRCUITS 🔧 : 
            Les pannes des Circuits Centraux (partie gauche coloré d'un cadran) sont reliées en
            groupes de 4, par un circuit (trait) orange, jaune ou gris.
            SI LES 4 PANNES SITUÉES SUR UN MÊME CIRCUIT SONT COCHÉES, 
            ELLES S'AUTORÉPARENT ET SONT DONC IMMÉDIATEMENT EFFACER.
            Une panne est symboliser par ses caractères barré.
            
            Exemple :

                3 pannes sont déjà cochées sur le circuit jaune (celle du cadran Ouest).
                Le Mécano doit alors interpeller le Capitaine en lui demandant de faire
                si possible route à l'Est pour pouvoir compléter le circuit jaune et bénéficier d'une autoréparation.

                         /===\         ~         /===\         ~         /===\         ~         /===\ 
                         : O :         ~         : N :         ~         : S :         ~         : E :
                         \===/         ~         \===/         ~         \===/         ~         \===/
                    /―――――――――――――\    ~    /―――――――――――――\    ~    /―――――――――――――\    ~    /―――――――――――――\ 
                    | ̷J̷A̷U̷N̷E - ̷A̷R̷M |    ~    | VERT  1 SPE |    ~    | BLEU  1 DET |    ~    | JAUNE 1 DET |
                    | ̷J̷A̷U̷N̷E - ̷S̷P̷E |    ~    | VERT  2 SPE |    ~    | BLEU  2 SPE |    ~    | VERT  2 SPE |
                    \ ̷J̷A̷U̷N̷E - ̷D̷E̷T /    ~    \ VERT  3 ARM /    ~    \ BLEU  3 ARM /    ~    \ BLEU  3 ARM /
                     |―――――――――――|     ~     |―――――――――――|     ~     |―――――――――――|     ~     |―――――――――――|
                    / NONE  4 DET \    ~    / NONE  4 DET \    ~    / NONE  4 ARM \    ~    / NONE  4 DET \ 
                    | NONE  5 RAD |    ~    | NONE  5 ARM |    ~    | NONE  5 SPE |    ~    | NONE  5 RAD |
                    | NONE  6 RAD |    ~    | NONE  6 RAD |    ~    | NONE  6 RAD |    ~    | NONE  6 RAD |
                    \―――――――――――――/    ~    \―――――――――――――/    ~    \―――――――――――――/    ~    \―――――――――――――/
                                       ~                       ~                       ~  
            
            Les pannes des Circuits Centraux peuvent également être réparées en faisant Surface (voir dans FAIRE SURFACE).

        ➟ REPARATION DU REACTEUR 🔧 :
            Lorsque tous les voyants Radiation ont été cochés. 
            Dans ce cas, après avoir subi 1 de Dégât, toutes les pannes RAD du sous-marin se réparent.

            L'autre situation (et de loin la meilleure !) c'est lorsque vous faites Surface (voir dans FAIRE SURFACE ).

                Exemple :

                         /===\         ~         /===\         ~         /===\         ~         /===\ 
                         : O :         ~         : N :         ~         : S :         ~         : E :
                         \===/         ~         \===/         ~         \===/         ~         \===/
                    /―――――――――――――\    ~    /―――――――――――――\    ~    /―――――――――――――\    ~    /―――――――――――――\ 
                    | JAUNE 1 ARM |    ~    | VERT  1 SPE |    ~    | BLEU  1 DET |    ~    | JAUNE 1 DET | 
                    | JAUNE 2 SPE |    ~    | VERT  2 SPE |    ~    | BLEU  2 SPE |    ~    | VERT  2 SPE | 
                    \ JAUNE 3 DET /    ~    \ VERT  3 ARM /    ~    \ BLEU  3 ARM /    ~    \ BLEU  3 ARM /
                     |―――――――――――|     ~     |―――――――――――|     ~     |―――――――――――|     ~     |―――――――――――|
                    / ̷N̷O̷N̷E  - ̷D̷E̷T \    ~    / NONE  4 DET \    ~    / NONE  4 ARM \    ~    / ̷N̷O̷N̷E  - ̷D̷E̷T \ 
                    | ̷N̷O̷N̷E  - ̷R̷A̷D |    ~    | ̷N̷O̷N̷E  - ̷A̷R̷M |    ~    | ̷N̷O̷N̷E  - ̷S̷P̷E |    ~    | NONE  5 RAD | 
                    | ̷N̷O̷N̷E  - ̷R̷A̷D |    ~    | ̷N̷O̷N̷E  - ̷R̷A̷D |    ~    | ̷N̷O̷N̷E  - ̷R̷A̷D |    ~    | ̷N̷O̷N̷E  - ̷R̷A̷D | 
                    \―――――――――――――/    ~    \―――――――――――――/    ~    \―――――――――――――/    ~    \―――――――――――――/
                                       ~                       ~                       ~  

                    Ici, il y a beaucoup de pannes dans le Réacteur (partie sans couleur inférieur).
                    Tous les systèmes sont hors service et il y a 5 voyants Radiations cochés sur 6. 
                    Il devient très urgent de faire surface pour réparer l'intégralité du sous-marin !
                
╰┈➤ Le Détecteur :
        Le Détecteur est chargé d'écouter très précisément ce que dit LE CAPITAINE ADVERSE 
        pour parvenir à localiser le sous-marin ennemi.
        À chaque fois que le Capitaine adverse annonce un cap, le Détecteur le reporte sur son transparent 
        (à partir de la position de départ de son choix, car il ne connaît pas le point de départ de l'ennemi).

        En faisant glisser son transparent sur sa carte, il pourra essayer de déduire où se trouve le sous-marin ennemi 
        (sachant qu'on ne peut ni croiser sa propre route, ni traverser les îles).
        
        Donc plus le Détecteur écoutera le Capitaine adverse, plus il aura d'informations et de tracés, 
        et plus il aura de chances de localiser la position du sous-marin ennemi. 
        Bien entendu, il DOIT communiquer régulièrement avec son Capitaine 
        pour lui faire part de ses progrès sur la localisation de l'ennemi.

        Il pourra aussi affiner la position de l'ennemi grâce aux DRONES et SONAR 
        qui seront activés par le Capitaine ou le Second (voir ACTIVATION DES SYSTÈMES).

        💡 CONSEIL💡 : 
                Pour que le tracé ne sorte pas trop vite de votre transparent, 
                faites attention de commencer en début de partie au milieu de ce transparent.
                Si le tracé sort de votre transparent, ou si vous êtes un peu perdu, effacez tout et reprenez tout à zéro.

                                      🌊 ==========FAIRE SURFACE========== 🌊

    Faire surface permet de réparer efficacement son sous-marin, et de réinitialiser sa route de navigation. 
    Mais cette manœuvre rend vulnérable pendant un certain temps, elle est donc à effectuer avec beaucoup de précaution.
    Pour faire surface, le Capitaine doit lever le poing et entrer "SURFACE !". 
    Puis, il donne immédiatement le numéro du secteur où il fait surface à l'ennemi.

    Les règles de surface varient si vous jouez en mode Tour par Tour ou si vous jouez en mode Simultané :

╰┈➤ TOUR PAR TOUR :
        Au lieu d'annoncer un cap, le capitaine utilise son tour pour annoncer qu'il fait surface. 
        Puis le TOUTES les pannes du sous-marin dont effacer. L'équipage adverse peut ensuite jouer trois coups d'affilée, 
        c'est-à-dire 3 annonces de cap, mais également 3 activations de systèmes. Puis le jeu reprend normalement.

╰┈➤ SIMULTANE :
        Indisponible pour le moment.

        🚨IMPORTANT🚨 :
            L'ENNEMI, LUI, CONTINUE À JOUER PENDANT QUE VOUS ÊTES IMMOBILISÉS EN SURFACE POUR RÉPARATIONS !
            Pendant toute la période où un sous-marin est en surface, l'équipage de ce sous-marin ne peut activer aucun système.

        Pendant ce temps, le Capitaine a réinitialisé sa route. Il efface tout son tracé et ne garde que sa position actuelle.



                                 🛜 ==========ACTIVATION DES SYSTEMES========== 🛜

    Lorsque la jauge d'un des systèmes est remplie, le Second doit l'annoncer au Capitaine. 
    À compter de cet instant, le Capitaine peut déclencher ce système tout moment. Le Capitaine peut déclencher TOUS les systèmes.
    Le Second lui peut déclencher de sa propre initiative uniquements les systèmes de Drones et de Sonar.

╰┈➤ DECLENCHEMENT D'UN SYSTEME 💻 :

        le Capitaine ou le Second doivent :
        1)  Demander au Mécano si aucun voyant du symbole correspondant au système n'est en panne, 
            sinon il faut le réparer pour pouvoir l'activer.
            RAPPEL : Pour activer un système, aucun voyant correspondant au symbole du Système choisi ne doit être coché !
        
        2)  En mode tour par tour le Capitaine peut activer un système après chacun de ses déplacements s'il le souhaite. 
            En mode simultané il doit entrer et crier « STOP ! » en levant le poing 
            (tous les autres joueurs, des 2 équipages, DOIVENT écouter et ne pourrons effectuer aucune action).

        3)  Déclenché un système (par exemple : « JE LARGUE UNE MINE ! »).

        4)  Résoudre l'effet de cette activation (voir ci-dessous).

        5)  Puis le jeu continue.

     
    🚨IMPORTANT🚨 :
        On ne peut pas activer deux systèmes à la suite. 
        Le Capitaine est obligé d'annoncer un nouveau cap entre deux activations de systèmes.

╰┈➤ SYSTEME D'ARMEMENT :
    ➟ LARGAGE D'UNE TORPILLE 🚀 :
        La distance maximal ainsi que les dégats d'une torpille dépend du sous-marin utilisé. 
        Il devra choisir le point d'impact en écrivant la case sur laquelle il l'envoie.
        Les torpilles ne peuvent pas se déplacer en diagonale. 
        Une fois tiré, toute la jauge de torpille est effacer est retombe a 0.
        Si une torpille explose sur la même case qu'une mine, la mine est détruite.
        
        🚨IMPORTANT🚨 :
            Si le point d'impact de votre torpille se trouve à une case de votre sous-marin, 
            vous subirez des dégâts réduit dépendant de la puissance de la torpille !
        
        Les possibilités et les conséquences sont les mêmes que pour l'explosion d'une Mine. Puis la partie reprend normalement.
        Si votre torpille explose par hasard sur la même case qu'une mine (amie ou ennemie), 
        celle-ci explose en même temps que la torpille cumulant les dégats de la zone d'effet. 

    ➟ LARGAGE D'UNE MINE 💣 :
        Le Capitaine largue une M (Mine) sur une case adjacente à son sous-marin. 
        Il annonce ensuite « MINE LARGUÉE ! » et le jeu continue. 
        La jauge de Mine est donc effacer pour le second (puisqu'elle vient d'être utilisée). 
        Les effets de la mine dépendent du type de mine largué.

        EXPLOSION D'UNE MINE 💣 :
            Le Capitaine peut déclencher une mine posée précédemment s'il pense que le sous-marin ennemi est proche.
            Pour celà il met la partie en pause et doit choisir l'option : « STOP, JE FAIS EXPLOSER LA MINE ! » 
            et annonçe la case sur laquelle est disposée la mine (par exemple « STOP, JE FAIS EXPLOSER LA MINE : G7! »
            Certaine mine n'ont pas besoin d'être déclanché car elles exploseront au contact d'un sous-marin.
            Les dégats ainsi que les effets d'une mine dépendent du sous-marin utilisé.

            🚨IMPORTANT🚨 :
                On ne tient pas compte de la jauge MINE lors de l'explosion 
                (peu importe son niveau de remplissage, on ne l'efface pas). 
                En effet la jauge a déjà été remplie et effacée lors du LARGAGE de la mine.
            
            Il y a alors trois possibilités (comme pour le tir d'une torpille) :
                1) La Mine explose à PLUS D'UNE CASE du sous-marin ennemi : 
                    Le Capitaine adverse annonce « RAS ! », et la partie reprend normalement.

                2) La Mine explose sur UNE CASE ADJACENTE du sous-marin ennemi (MÊME EN DIAGONALE) :
                    Le Capitaine adverse annonce « IMPACT INDIRECT ! » Les dégats dépendent du type de mine.
                    La vie du sous-marin baisse en fonction des dégats pris. Puis la partie reprend normalement.

                3) La Mine explose EXACTEMENT SUR LA MÊME CASE où se trouve le sous-marin ennemi :
                    Le Capitaine adverse annonce « IMPACT DIRECT » Les dégats dépendent du type de mine. 
                    La vie du sous-marin baisse en fonction des dégats pris. Ensuite la partie reprend normalement, 
                    mais vous savez maintenant où se trouve l'ennemi !

            🚨IMPORTANT🚨 :
                Si vous faites sauter une de vos mines à une case de distance de votre propre sous-marin, 
                vous subirez des dégâts réduit dépendant de la puissance de la mine !

╰┈➤ SYSTEME DE DETECTION :
        ➟ LARGAGE D'UN DRONE 🤖:
            Les effets du drone varient d'un sous-marin à l'autre, pour le sous-marin TIGRE :
            Un drone permet de demander à l'équipage adverse une information sur le secteur dans lequel il se trouve 
            (la carte est découpée en 9 secteurs en mode simultané et en 4 secteurs en tour par tour).
          • Le Capitaine interroge donc l'adversaire sur un secteur (« ÊTES VOUS EN SECTEUR : 5 ? »).
          • Le Capitaine adverse DOIT répondre sans tricher par OUI ou par NON.
            La jauge de Drone est ensuite totalement réinitialiser (puisqu'elle vient d'être utilisée).
            Puis la partie reprend normalement.

        ➟ ACTIVATION DU SONAR 🔍:
            Les effets du sonar peuvent varier d'un sous-marin à un autre, pour le sous-marin TIGRE :
            Lorsque vous activez votre Sonar, l'équipage adverse doit vous donner DEUX coordonnées sur sa position : 
            Le Capitaine peut choisir par exemple parmi la ligne, la colonne ou le secteur où se situe son sous-marin.
          • UNE SEULE de ces deux coordonnées DOIT être fausse.
          • Les deux coordonnées DOIVENT être différentes (ligne, colonne ou secteur).
            La jauge de Sonar est alors réinitialisée (puisqu'elle vient d'être utilisée).
            Puis la partie reprend normalement.

╰┈➤ SYSTEME SPECIALE 🌟 :
        ➟ ACTIVATION DU SILENCE POUR LE TIGRE :
            Lorsque vous activez le Silence vous pouvez déplacer le sous-marin librement, EN LIGNE DROITE, 
            sans donner l'ordre de cap à l'adversaire.
          • Le déplacement doit être OBLIGATOIREMENT en ligne droite et il peut être de 0 à 4 cases
          • L'odre du cap ne sera pas divulgé à l'adversaire. 
            La jauge de Silence est alors réinitialisée (puisqu'elle vient d'être utilisée).

        ➟ LARGAGE DU LEURRE POUR L'ECUREILLE :
            Lorsque vous larguez le leurre il se déplacera dans la direction opposé à la votre.
            Vous pouvez charger le leurre d'une mine et la faire exploser a votre bon vouloir.
            L'ennemie ne saura pas faire la différence entre votre vrai sous-marin et le leurre largué.
          • Vous ne pouvez larger qu'un leurre à la fois  
          • Le leurre possède 2PV et fonctionne comme un sous-marin.
          • Le leurre se déplace tout seul dans la direction opposée a la votre
            (Si vous choississez le cap NORD, le leurre partira au cap SUD) 
          • L'ennemie recevra deux directions de cap et ne pourra faire la distinction entre le sous-marin et le leurre.
          • Vous pouvez charger une mine dans le leurre, cette mine fonctionne de la même manière que les autres.
          • Si le leurre essaye de traverser une île, il explose sur place. 
          • Si le leurre est chargé d'une mine et qu'il explose par n'importe quel moyen,
            alors l'explosion infligera 1 point de dégat aux sous-marin alentour.
            La jauge du leurre est réinitialisée une fois le leurre détruit.
            (A VOIR SI C PAS TROP FUMER EN LE NERFANT UN PEU)
        
            💡 CONSEIL💡 : 
                Après avoir largué votre leurre, changer de cap pour que le leurre ne revienne pas sur votre position.
                Car le leurre retournera sur vos pas, ce qui n'est pas possible pour votre sous-marin.


                                        🏁 ==========FIN DU JEU========== 🏁

            LORSQU'UN DES DEUX SOUS-MARINS A PERDU TOUTE SES VIE IL EXPLOSE ET C'EST LA FIN DU JEU.
                            C'EST L'ÉQUIPAGE ADVERSE QUI GAGNE LA PARTIE !

   💡 CONSEILS AVISÉS💡:
      • Vous l'aurez compris, la clé du succès réside dans une communication intense entre les différents membres d'équipage. 
        Si personne ne parle, si personne n'écoute… Vous êtes perdus d'avance !
      • Un excellent détecteur est également déterminant. Ce n'est pas pour rien qu'on les appelle, 
                                            LES OREILLES D'OR !
                                                   👂
"""

#================#
'''Debut_jeu.py'''
#================#

equipe = '''\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n
    ___________            .__               
    \_   _____/ ________ __|__|_____   ____  
     |    __)_ / ____/  |  \  \____ \_/ __ \ 
     |        < <_|  |  |  /  |  |_> >  ___/ 
    /_______  /\__   |____/|__|   __/ \___  >
            \/    |__|        |__|        \/
        '''

affichage_mode = '''\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n
       _____             .___           .___            __              
      /     \   ____   __| _/____     __| _/____       |__| ____  __ __ 
     /  \ /  \ /  _ \ / __ |/ __ \   / __ |/ __ \      |  |/ __ \|  |  \ 
    /    Y    (  <_> ) /_/ \  ___/  / /_/ \  ___/      |  \  ___/|  |  /
    \____|__  /\____/\____ |\___  > \____ |\___  > /\__|  |\___  >____/ 
            \/            \/    \/       \/    \/  \______|    \/       
                
    
    1 - Mode tour par tour
    2 - Mode simultané (INDISPONIBLE)\n
                '''

aff_map = '''\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n

       _____                 
      /     \  _____  ______  
     /  \ /  \ \__  \ \____ \ 
    /    Y    \ / __ \|  |_> >
    \____|___  (____  /   __/ 
             \/     \/|__|   


    1 - Mer Noir :              2 - Mer Rouge :
        longueur = 15               longueur = 15
        largeur = 15                largeur = 15
        difficulté = 1/10           difficulté = 1/10
        terrain = vide              terrain = île

    '''

aff_s = '''\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n

  _________                                _____                 .__        
 /   _____/ ____  __ __  ______           /     \  _____  _______|__| ____  
 \_____  \ /  _ \|  |  \/  ___/  ______  /  \ /  \ \__  \ \_ ___ \  |/    \ 
 /        (  <_> )  |  /\___ \  /_____/ /    Y    \ / __ \ |  | \/  |   |  \ 
/_______  /\____/|____//____  >         \____|___  (____  /|__|  |__|___|  /
        \/                  \/                   \/     \/               \/ 


    1 - Tigre :        
        vie = 4           
        difficulté = 1               
        armement 1 = Mine a déclanchement       
        armement 2 = Torpille électrique à guidage acoustique actif  
        détection 1 = Sonar passif  
        détection 2 = Drone par magnétométrie     
        spéciale = Silence

    2 - Ecureille :        
        vie = 3
        difficulté = 1               
        armement 1 = Mine a déclanchement       
        armement 2 = Torpille thermique à guidage acoustique passif  
        détection 1 = Sonar actif  
        détection 2 = Drone électomagnétique    
        spéciale = Leurre
    '''

start = '''\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n
    =========================================== QUE LA PARTIE COMMENCE ! =================================================
   
   
    __________.__                                       ._.
    \______   \  |   ____   ____    ____   ___________  | |
     |     ___/  |  /  _ \ /    \  / ___\_/ __ \_  __ \ | |
     |    |   |  |_(  <_> )   |  \/ /_/  >  ___/|  | \/  \|
     |____|   |____/\____/|___|  /\___  / \___  >__|     __
                               \//_____/      \/         \/
                           '''

changement = '''
\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n
    _________ .__                                                         __   
    \_   ___ \|  |__  _____    ____    ____   ____   _____   ____   _____/  |_ 
    /    \  \/|  |  \ \__  \  /    \  / ___\_/ __ \ /     \_/ __ \ /    \   __\ 
    \     \___|   Y  \ / __ \|   |  \/ /_/  >  ___/|  Y Y  \  ___/|   |  \  |  
     \______  /___|  _(____  /___|  /\___  / \___  >__|_|  /\___  >___|  /__|  
            \/     \/      \/     \//_____/      \/      \/     \/     \/      
             '''