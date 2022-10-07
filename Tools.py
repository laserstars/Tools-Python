import random
from random import randint
Menu = 1

while Menu == 1:

    print("\n0 -- Quitter")
    print("1 -- Générateur de mot de passe")
    print("2 -- Jeux")
    print("3 -- Calculatrice")
    print("4 -- Transcodage")

    option = int(input(""))

    if (option > 4 or option < 0):
        print("\nOpération impossible, choisissé un bon chiffre.\n")
    elif option == 0:
        Menu = 0
    else:
        fin_calculatrice = 1
        fin_password = 1
        fin_jeu = 1
        fin_transcodage = 1

        print("")

        if option == 3:
            while fin_calculatrice == 1:

                chiffre1 = int(input("Choisis ton premier nombre "))

                print("")

                print("0 -- Multiplier par ... ")
                print("1 -- Diviser par ... ")
                print("2 -- Additionner par ... ")
                print("3 -- Soustraire par ... ")

                print("")

                operation = int(input("Choisir une opération "))

                print("")

                chiffre2 = int(input("Choisis ton deuxième nombre "))

                print("")

                if operation == 0:
                    multiplication = chiffre1 * chiffre2
                    print("Le résultat est ", multiplication)

                elif operation == 1:
                    if chiffre2 == 0:
                        print("Division par zéro impossible !")
                    else:
                        division = chiffre1 / chiffre2
                        print("Le résultat est ", division)

                elif operation == 2:
                    addition = chiffre1 + chiffre2
                    print("Le résultat est ", addition)

                elif operation == 3:
                    soustration = chiffre1 - chiffre2
                    print("Le résultat est ", soustration)

                print("")

                print("0 -- Retour au Menu")
                print("1 -- Nouvelle opération")

                print("")

                print("Que faire ?")

                fin_calculatrice = int(input(""))

                print("")

        elif option == 1:
            while fin_password == 1:
                lower_case = "abcdefghijklmnopqrstuvwxyz"
                upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
                number_password = "0123456789"
                symbols_password = "\/#@%&*$"

                Use_for = lower_case + upper_case + number_password + symbols_password
                lenght_for_pass = int(input("Quelle taille pour le mot de passe ? "))

                print("")

                password = "".join(random.sample(Use_for, lenght_for_pass))
                print("Le nouveau mot de passe est " + password)

                print("")

                print("0 -- Retour au Menu")
                print("1 -- Nouveau mot de passe")

                print("")

                print("Que faire ?")

                fin_password = int(input(""))

                print("")

        elif option == 2:
            while fin_jeu == 1:
                print("0 -- Pierre, Feuille, Ciseaux")
                print("1 -- Trouver le Nombre perdu")
                print("2 -- Retour Menu")

                option_jeu = int(input(""))

                if option_jeu == 2:
                    fin_jeu = 0

                if (option > 2 or option < 0):
                    print("\nOpération impossible, choisissé un bon chiffre.\n")
                else:
                    if option_jeu == 0:
                        fin_jeu_PSF = 1

                        while fin_jeu_PSF == 1:
                            option_jeu = ['pierre', 'feuille', 'ciseaux']
                            chiffre_option_jeu = randint(0, 2)
                            choix_ordi = option_jeu[chiffre_option_jeu]

                            choix_joueur = input("\npierre, feuille, ciseaux. Taper Fin pour quitter.\n")

                            if (
                                    choix_joueur == 'pierre' or choix_joueur == 'Pierre' or choix_joueur == 'PIERRE' or choix_joueur == 'P' or choix_joueur == 'p'):

                                choix_joueur = 'pierre'
                                print('\nVous : ', choix_joueur, ' VS ', choix_ordi, ' : Ordinateur\n')

                            elif (
                                    choix_joueur == 'feuille' or choix_joueur == 'Feuille' or choix_joueur == 'FEUILLE' or choix_joueur == 'F' or choix_joueur == 'f'):

                                choix_joueur = 'feuille'
                                print('\nVous : ', choix_joueur, ' VS ', choix_ordi, ' : Ordinateur\n')

                            elif (
                                    choix_joueur == 'ciseaux' or choix_joueur == 'Ciseaux' or choix_joueur == 'CISEAUX' or choix_joueur == 'C' or choix_joueur == 'c' or choix_joueur == 'ciseau' or choix_joueur == 'Ciseau' or choix_joueur == 'CISEAU'):

                                choix_joueur = 'ciseaux'
                                print('\nVous : ', choix_joueur, ' VS ', choix_ordi, ' : Ordinateur\n')

                            if choix_joueur == choix_ordi:
                                print('Egalité!')

                            elif choix_joueur == 'pierre':
                                if choix_ordi == 'feuille':
                                    print('Perdu! La feuille recouvre la pierre')
                                else:
                                    print('Gagné! La pierre écrase les ciseaux')
                            elif choix_joueur == 'feuille':
                                if choix_ordi == 'pierre':
                                    print('Gagné! La feuille recouvre la pierre.')
                                else:
                                    print('Perdu! Les ciseaux coupent la feuille.')
                            elif choix_joueur == 'ciseaux':
                                if choix_ordi == 'feuille':
                                    print('Gagné! Les ciseaux coupent la feuille.')
                                else:
                                    print('Perdu! Les ciseaux se font écraser par la pierre.')

                            elif (choix_joueur == 'fin' or choix_joueur == 'Fin' or choix_joueur == 'FIN'):
                                fin_jeu_PSF = 0

                            else:
                                print('\nErreur, option invalide.')

                            fin_jeu_PSF = int(input('\n0 -- Choix jeux\n1-- Rejouer\n'))
                            print("")

                    elif option_jeu == 1:
                        fin_jeu_nombre_perdu = 1

                        while fin_jeu_nombre_perdu == 1:
                            nombre_perdu_option = int(input("\nL'intervalle est de 0 à combien.\n"))
                            nombre_perdu = randint(0, nombre_perdu_option)
                            fin_partie_nombre_p = 1

                            nombre_essai_nombre_p = 1
                            nombre_joueur_nombre_p = int(input("\nA ton avis c'est quelle nombre?\n"))

                            while fin_partie_nombre_p == 1:

                                if nombre_perdu < nombre_joueur_nombre_p:

                                    print("\nLe chiffre à trouver est plus petit que ", nombre_joueur_nombre_p, "\n")
                                    nombre_joueur_nombre_p = int(input("A ton avis c'est quelle nombre?\n"))
                                    nombre_essai_nombre_p = nombre_essai_nombre_p + 1

                                elif (nombre_perdu > nombre_joueur_nombre_p and nombre_joueur_nombre_p >= 0):

                                    print("\nLe chiffre à trouver est plus grand que ", nombre_joueur_nombre_p, "\n")
                                    nombre_joueur_nombre_p = int(input("A ton avis c'est quelle nombre?\n"))
                                    nombre_essai_nombre_p = nombre_essai_nombre_p + 1

                                elif nombre_perdu == nombre_joueur_nombre_p:
                                    fin_partie_nombre_p = 0

                                elif nombre_joueur_nombre_p < 0:
                                    print("\nErreur.")
                                    print("\n0 -- Continuer partie")
                                    print("1 -- Menu")

                                    option_erreur_nombre_p = int(input(""))

                                    if option_erreur_nombre_p == 0:
                                        nombre_joueur_nombre_p = int(input("A ton avis c'est quelle nombre?\n"))
                                        print("")
                                    elif option_erreur_nombre_p == 1:
                                        fin_partie_nombre_p = 0
                                    elif option_erreur_nombre_p != 0:
                                        fin_partie_nombre_p = 0

                            if nombre_joueur_nombre_p == nombre_perdu:
                                print("\nBravo, tu as trouvé le nombre en ", nombre_essai_nombre_p, "essais.\n")

                            print("0 -- Retour Menu Jeux")
                            print("1 -- Rejouer")

                            fin_jeu_nombre_perdu = int(input(""))
                            print("")

        elif option == 4:
            while fin_transcodage == 1:
                print("0 -- Transcoder Décimal => Binaire")
                print("1 -- Transcoder Décimal => Héxadécimal")
                print("2 -- Retour Menu")

                option_transcodage = int(input(""))

                if option_transcodage == 2:
                    fin_transcodage = 0

                if (option_transcodage > 2 or option_transcodage < 0):
                    print("\nOpération impossible, choisissé un bon chiffre.\n")
                else:
                    if option_transcodage == 0:
                        fin_transcodage_DB = 1

                        while fin_transcodage_DB == 1:
                            nombre_debut_trans_DB = int(input("\nDonne moi un chiffre à transcoder en Binaire.\n"))
                            nombre_nombre_trans_DB = nombre_debut_trans_DB

                            binaire = []

                            while nombre_nombre_trans_DB != 0:

                                if nombre_nombre_trans_DB % 2 == 0:
                                    binaire.append(0)

                                elif nombre_nombre_trans_DB % 2 == 1:
                                    binaire.append(1)
                                nombre_nombre_trans_DB = nombre_nombre_trans_DB // 2

                            binaire_len = len(binaire)

                            binaire_presque_fini = []
                            choix_nombre_trans_DB = -1

                            for i in range(binaire_len):
                                binaire_presque_fini.append(binaire[choix_nombre_trans_DB])
                                choix_nombre_trans_DB = choix_nombre_trans_DB - 1

                            chiffrebinaire = 1
                            binaire_presque_fini = str(binaire_presque_fini)
                            binaire_fini = ""

                            for i in range(binaire_len):
                                binaire_fini = binaire_fini + binaire_presque_fini[chiffrebinaire]
                                chiffrebinaire = chiffrebinaire + 3

                            print("\nLe nombre", nombre_debut_trans_DB, "s'écrit", binaire_fini, "en binaire.")

                            menu_transcodage_DB = 1
                            erreur_menu_transcodage_DB = int(input("\n0 -- Menu Transcodage \n1 -- Refaire ce transcodage\n"))
                            while menu_transcodage_DB == 1:

                                if erreur_menu_transcodage_DB == 0:
                                    menu_transcodage_DB = 0
                                    fin_transcodage_DB = 0
                                    print("")

                                elif erreur_menu_transcodage_DB == 1:
                                    menu_transcodage_DB = 0

                                elif erreur_menu_transcodage_DB != 0 and erreur_menu_transcodage_DB != 1:
                                    menu_transcodage_DB = 1
                                    print("\nOption impossible\n")
                                    erreur_menu_transcodage_DB = int(input("\n0 -- Menu Transcodage \n1 -- Refaire ce transcodage\n"))

                    elif option_transcodage == 1:
                        fin_transcodage_DH = 1

                        while fin_transcodage_DH == 1:
                            nombre_debut_trans_DH = int(input("\nDonne moi un chiffre à transcoder en Hexadécimal.\n"))
                            nombre_trans_DH = nombre_debut_trans_DH

                            hexadecimal = []

                            while nombre_trans_DH != 0:

                                nombre_reste_trans_DH = nombre_trans_DH % 16
                                nombre_trans_DH = nombre_trans_DH // 16

                                if nombre_reste_trans_DH == 0:
                                    hexadecimal.append("0")
                                elif nombre_reste_trans_DH == 1:
                                    hexadecimal.append("1")
                                elif nombre_reste_trans_DH == 2:
                                    hexadecimal.append("2")
                                elif nombre_reste_trans_DH == 3:
                                    hexadecimal.append("3")
                                elif nombre_reste_trans_DH == 4:
                                    hexadecimal.append("4")
                                elif nombre_reste_trans_DH == 5:
                                    hexadecimal.append("5")
                                elif nombre_reste_trans_DH == 6:
                                    hexadecimal.append("6")
                                elif nombre_reste_trans_DH == 7:
                                    hexadecimal.append("7")
                                elif nombre_reste_trans_DH == 8:
                                    hexadecimal.append("8")
                                elif nombre_reste_trans_DH == 9:
                                    hexadecimal.append("9")
                                elif nombre_reste_trans_DH == 10:
                                    hexadecimal.append("A")
                                elif nombre_reste_trans_DH == 11:
                                    hexadecimal.append("B")
                                elif nombre_reste_trans_DH == 12:
                                    hexadecimal.append("C")
                                elif nombre_reste_trans_DH == 13:
                                    hexadecimal.append("D")
                                elif nombre_reste_trans_DH == 14:
                                    hexadecimal.append("E")
                                elif nombre_reste_trans_DH == 15:
                                    hexadecimal.append("F")

                            hexadecimal_len = len(hexadecimal)

                            hexadecimal_presque_fini = []
                            a = -1

                            for i in range(hexadecimal_len):
                                hexadecimal_presque_fini.append(hexadecimal[a])
                                a = a - 1

                            chiffre_hexadecimal = 2
                            hexadecimal_presque_fini = str(hexadecimal_presque_fini)
                            hexadecimal_fini = ""
                            #print(hexadecimal_presque_fini)

                            for i in range(hexadecimal_len):
                                hexadecimal_fini = hexadecimal_fini + hexadecimal_presque_fini[chiffre_hexadecimal]
                                chiffre_hexadecimal = chiffre_hexadecimal + 5

                            print("\nLe nombre", nombre_debut_trans_DH, "s'écrit", hexadecimal_fini, "en hexadecimal.")

                            menu_transcodage_DH = 1
                            erreur_menu_transcodage_DH = int(
                                input("\n0 -- Menu Transcodage \n1 -- Refaire ce transcodage\n"))
                            while menu_transcodage_DH == 1:

                                if erreur_menu_transcodage_DH == 0:
                                    menu_transcodage_DH = 0
                                    fin_transcodage_DH = 0
                                    print("")

                                elif erreur_menu_transcodage_DH == 1:
                                    menu_transcodage_DH = 0

                                elif erreur_menu_transcodage_DH != 0 and erreur_menu_transcodage_DH != 1:
                                    menu_transcodage_DH = 1
                                    print("\nOption impossible\n")
                                    erreur_menu_transcodage_DH = int(
                                        input("\n0 -- Menu Transcodage \n1 -- Refaire ce transcodage\n"))