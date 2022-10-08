import random
from random import randint
Menu = 1

while Menu == 1:

    print("\n0 -- Quitter")
    print("1 -- Générateur de mot de passe")
    print("2 -- Jeux")
    print("3 -- Calculatrice")
    print("4 -- Transcodage")

    option = input("")

    option_digit = option.isdigit()

    while option_digit == False:
        print("\nOpération impossible, choisissé un bon chiffre.\n")
        print("\n0 -- Quitter")
        print("1 -- Générateur de mot de passe")
        print("2 -- Jeux")
        print("3 -- Calculatrice")
        print("4 -- Transcodage")

        option = input("")
        option_digit = option.isdigit()

    if option_digit == True:
        option = int(option)

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

                    choix_chiffre1_calculatrice = input("Choisis ton premier nombre ")

                    choix_chiffre1_calculatrice_digit = choix_chiffre1_calculatrice.isdigit()

                    while choix_chiffre1_calculatrice_digit == False:
                        print("\nOpération impossible\n")
                        choix_chiffre1_calculatrice = input("\nChoisis ton premier nombre.\n")
                        choix_chiffre1_calculatrice_digit = choix_chiffre1_calculatrice.isdigit()

                    if choix_chiffre1_calculatrice_digit == True:
                        choix_chiffre1_calculatrice = int(choix_chiffre1_calculatrice)

                        print("")

                        print("0 -- Multiplier par ... ")
                        print("1 -- Diviser par ... ")
                        print("2 -- Additionner par ... ")
                        print("3 -- Soustraire par ... ")

                        print("")

                        operation_calculatrice = input("Choisir une opération ")

                        operation_calculatrice_digit = operation_calculatrice.isdigit()

                        if operation_calculatrice_digit == True:
                            operation_calculatrice = int(operation_calculatrice)

                        while operation_calculatrice_digit == False or operation_calculatrice < 0 or operation_calculatrice >3:

                            print("\nOpération impossible\n")
                            print("0 -- Multiplier par ... ")
                            print("1 -- Diviser par ... ")
                            print("2 -- Additionner par ... ")
                            print("3 -- Soustraire par ... ")
                            operation_calculatrice = input("\nChoisir une opération\n")
                            operation_calculatrice_digit = operation_calculatrice.isdigit()

                            if operation_calculatrice_digit == True:
                                operation_calculatrice = int(operation_calculatrice)



                        if operation_calculatrice_digit == True:
                            operation_calculatrice = int(operation_calculatrice)

                            print("")

                            choix_chiffre2_calculatrice = input("Choisis ton deuxième nombre ")

                            choix_chiffre2_calculatrice_digit = choix_chiffre2_calculatrice.isdigit()

                            while choix_chiffre2_calculatrice_digit == False:
                                print("\nOpération impossible\n")
                                choix_chiffre2_calculatrice = input("Choisis ton deuxième nombre.\n")
                                choix_chiffre2_calculatrice_digit = choix_chiffre2_calculatrice.isdigit()

                            if choix_chiffre2_calculatrice_digit == True:
                                choix_chiffre2_calculatrice = int(choix_chiffre2_calculatrice)

                            print("")

                            if operation_calculatrice == 0:
                                multiplication_calculatrice = choix_chiffre1_calculatrice * choix_chiffre2_calculatrice
                                print("Le résultat est ", multiplication_calculatrice)

                            elif operation_calculatrice == 1:
                                if choix_chiffre2_calculatrice == 0:
                                    print("Division par zéro impossible !")
                                else:
                                    division_calculatrice = choix_chiffre1_calculatrice / choix_chiffre2_calculatrice
                                    print("Le résultat est ", division_calculatrice)

                            elif operation_calculatrice == 2:
                                addition_calculatrice = choix_chiffre1_calculatrice + choix_chiffre2_calculatrice
                                print("Le résultat est ", addition_calculatrice)

                            elif operation_calculatrice == 3:
                                soustration_calculatrice = choix_chiffre1_calculatrice - choix_chiffre2_calculatrice
                                print("Le résultat est ", soustration_calculatrice)

                            print("")

                            print("0 -- Retour au Menu")
                            print("1 -- Nouvelle opération")

                            print("")

                            print("Que faire ?")

                            menu_fin_calculatrice = input("")

                            menu_fin_calculatrice_digit = menu_fin_calculatrice.isdigit()

                            if menu_fin_calculatrice_digit == True:
                                menu_fin_calculatrice = int(menu_fin_calculatrice)

                            while menu_fin_calculatrice_digit == False or menu_fin_calculatrice < 0 or menu_fin_calculatrice > 1:

                                print("\nOpération impossible\n")

                                print("0 -- Retour au Menu")
                                print("1 -- Nouvelle opération\n")

                                menu_fin_calculatrice = input("Que faire ?\n")
                                menu_fin_calculatrice_digit = menu_fin_calculatrice.isdigit()

                                if menu_fin_calculatrice_digit == True:
                                    menu_fin_calculatrice = int(menu_fin_calculatrice)

                            if menu_fin_calculatrice_digit == True:
                                menu_fin_calculatrice = int(menu_fin_calculatrice)

                            if menu_fin_calculatrice == 0:
                                fin_calculatrice = 0
                            elif menu_fin_calculatrice == 1:
                                fin_calculatrice = 1

                            print("")





            elif option == 1:
                while fin_password == 1:
                    lower_case = "abcdefghijklmnopqrstuvwxyz"
                    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
                    number_password = "0123456789"
                    symbols_password = "\/#@%&*$"

                    Use_for = lower_case + upper_case + number_password + symbols_password
                    lenght_for_pass = input("Quelle taille pour le mot de passe ? ")

                    lenght_for_pass_digit = lenght_for_pass.isdigit()

                    if lenght_for_pass_digit == True:
                        lenght_for_pass = int(lenght_for_pass)

                    while lenght_for_pass_digit == False or lenght_for_pass < 1:

                        print("\nOpération impossible\n")

                        lenght_for_pass = input("\nQuelle taille pour le mot de passe ?\n")
                        lenght_for_pass_digit = lenght_for_pass.isdigit()

                        if lenght_for_pass_digit == True:
                            lenght_for_pass = int(lenght_for_pass)

                    if lenght_for_pass_digit == True:
                        lenght_for_pass = int(lenght_for_pass)

                    print("")

                    password = "".join(random.sample(Use_for, lenght_for_pass))
                    print("Le nouveau mot de passe est " + password)

                    print("")

                    print("0 -- Retour au Menu")
                    print("1 -- Nouveau mot de passe")

                    print("")

                    print("Que faire ?")

                    menu_fin_password = input("")

                    menu_fin_password_digit = menu_fin_password.isdigit()

                    if menu_fin_password_digit == True:
                        menu_fin_password = int(menu_fin_password)

                    while menu_fin_password_digit == False or menu_fin_password < 0 or menu_fin_password > 1:

                        print("\nOpération impossible\n")

                        print("0 -- Retour au Menu")
                        print("1 -- Nouveau mot de passe\n")

                        menu_fin_password = input("Que faire ?\n")
                        menu_fin_password_digit = menu_fin_password.isdigit()

                        if menu_fin_password_digit == True:
                            menu_fin_password = int(menu_fin_password)

                    if menu_fin_password_digit == True:
                        menu_fin_password = int(menu_fin_password)

                    if menu_fin_password == 0:
                        fin_password = 0
                    elif menu_fin_password == 1:
                        fin_password = 1

                    print("")

            elif option == 2:
                while fin_jeu == 1:
                    print("0 -- Pierre, Feuille, Ciseaux")
                    print("1 -- Trouver le Nombre perdu")
                    print("2 -- Retour Menu\n")

                    option_jeu = input("Que faire ?\n")

                    option_jeu_digit = option_jeu.isdigit()

                    if option_jeu_digit == True:
                        option_jeu = int(option_jeu)

                    while option_jeu_digit == False or option_jeu < 0 or option_jeu > 2:

                        print("\nOpération impossible\n")
                        print("0 -- Pierre, Feuille, Ciseaux")
                        print("1 -- Trouver le Nombre perdu")
                        print("2 -- Retour Menu")
                        option_jeu = input("\nQue faire ?\n")

                        option_jeu_digit = option_jeu.isdigit()

                        if option_jeu_digit == True:
                            option_jeu = int(option_jeu)

                    if option_jeu_digit == True:
                        option_jeu = int(option_jeu)

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
                                    print('\nOpération impossible.')

                                menu_fin_jeu_PSF = input('\n0 -- Choix jeux\n1-- Rejouer\n')

                                menu_fin_jeu_PSF_digit = menu_fin_jeu_PSF.isdigit()

                                if menu_fin_jeu_PSF_digit == True:
                                    menu_fin_jeu_PSF = int(menu_fin_jeu_PSF)

                                while menu_fin_jeu_PSF_digit == False or menu_fin_jeu_PSF < 0 or menu_fin_jeu_PSF > 1:

                                    print("\nOpération impossible\n")

                                    print("0 -- Choix jeux")
                                    print("1-- Rejouer\n")

                                    menu_fin_jeu_PSF = input("Que faire ?\n")
                                    menu_fin_jeu_PSF_digit = menu_fin_jeu_PSF.isdigit()

                                    if menu_fin_jeu_PSF_digit == True:
                                        menu_fin_jeu_PSF = int(menu_fin_jeu_PSF)

                                if menu_fin_jeu_PSF_digit == True:
                                    menu_fin_jeu_PSF = int(menu_fin_jeu_PSF)

                                if menu_fin_jeu_PSF == 0:
                                    fin_jeu_PSF = 0
                                elif menu_fin_jeu_PSF == 1:
                                    fin_jeu_PSF = 1

                                print("")

                        elif option_jeu == 1:
                            fin_jeu_nombre_perdu = 1

                            while fin_jeu_nombre_perdu == 1:
                                nombre_perdu_option = input("\nL'intervalle est de 0 à combien ?\n")

                                nombre_perdu_option_digit = nombre_perdu_option.isdigit()

                                if nombre_perdu_option_digit == True:
                                    nombre_perdu_option = int(nombre_perdu_option)

                                while nombre_perdu_option_digit == False or nombre_perdu_option < 1:

                                    print("\nOpération impossible\n")

                                    nombre_perdu_option = input("\nL'intervalle est de 0 à combien ?\n")
                                    nombre_perdu_option_digit = nombre_perdu_option.isdigit()

                                    if nombre_perdu_option_digit == True:
                                        nombre_perdu_option = int(nombre_perdu_option)

                                if nombre_perdu_option_digit == True:
                                    nombre_perdu_option = int(nombre_perdu_option)

                                nombre_perdu = randint(0, nombre_perdu_option)
                                fin_partie_nombre_p = 1

                                nombre_essai_nombre_p = 1
                                nombre_joueur_nombre_p = input("\nA ton avis c'est quelle nombre ?\n")

                                nombre_joueur_nombre_p_digit = nombre_joueur_nombre_p.isdigit()

                                if nombre_joueur_nombre_p_digit == True:
                                    nombre_joueur_nombre_p = int(nombre_joueur_nombre_p)

                                while nombre_joueur_nombre_p_digit == False or nombre_joueur_nombre_p < 0:

                                    print("\nOpération impossible\n")

                                    nombre_joueur_nombre_p = input("\nA ton avis c'est quelle nombre ?\n")
                                    nombre_joueur_nombre_p_digit = nombre_joueur_nombre_p.isdigit()

                                    if nombre_joueur_nombre_p_digit == True:
                                        nombre_joueur_nombre_p = int(nombre_joueur_nombre_p)

                                if nombre_joueur_nombre_p_digit == True:
                                    nombre_joueur_nombre_p = int(nombre_joueur_nombre_p)

                                while fin_partie_nombre_p == 1:

                                    if nombre_perdu < nombre_joueur_nombre_p:

                                        print("\nLe chiffre à trouver est plus petit que ", nombre_joueur_nombre_p,
                                              "\n")
                                        nombre_joueur_nombre_p = input("A ton avis c'est quelle nombre ?\n")

                                        nombre_joueur_nombre_p_digit = nombre_joueur_nombre_p.isdigit()

                                        if nombre_joueur_nombre_p_digit == True:
                                            nombre_joueur_nombre_p = int(nombre_joueur_nombre_p)

                                        while nombre_joueur_nombre_p_digit == False or nombre_joueur_nombre_p < 0:

                                            print("\nOpération impossible\n")

                                            nombre_joueur_nombre_p = input("\nA ton avis c'est quelle nombre ?\n")
                                            nombre_joueur_nombre_p_digit = nombre_joueur_nombre_p.isdigit()

                                            if nombre_joueur_nombre_p_digit == True:
                                                nombre_joueur_nombre_p = int(nombre_joueur_nombre_p)

                                        if nombre_joueur_nombre_p_digit == True:
                                            nombre_joueur_nombre_p = int(nombre_joueur_nombre_p)

                                        nombre_essai_nombre_p = nombre_essai_nombre_p + 1

                                    elif (nombre_perdu > nombre_joueur_nombre_p and nombre_joueur_nombre_p >= 0):

                                        print("\nLe chiffre à trouver est plus grand que ", nombre_joueur_nombre_p,
                                              "\n")
                                        nombre_joueur_nombre_p = input("A ton avis c'est quelle nombre ?\n")

                                        nombre_joueur_nombre_p_digit = nombre_joueur_nombre_p.isdigit()

                                        if nombre_joueur_nombre_p_digit == True:
                                            nombre_joueur_nombre_p = int(nombre_joueur_nombre_p)

                                        while nombre_joueur_nombre_p_digit == False or nombre_joueur_nombre_p < 0:

                                            print("\nOpération impossible\n")

                                            nombre_joueur_nombre_p = input("\nA ton avis c'est quelle nombre ?\n")
                                            nombre_joueur_nombre_p_digit = nombre_joueur_nombre_p.isdigit()

                                            if nombre_joueur_nombre_p_digit == True:
                                                nombre_joueur_nombre_p = int(nombre_joueur_nombre_p)

                                        if nombre_joueur_nombre_p_digit == True:
                                            nombre_joueur_nombre_p = int(nombre_joueur_nombre_p)

                                        nombre_essai_nombre_p = nombre_essai_nombre_p + 1

                                    elif nombre_perdu == nombre_joueur_nombre_p:
                                        fin_partie_nombre_p = 0



                                if nombre_joueur_nombre_p == nombre_perdu:
                                    print("\nBravo, tu as trouvé le nombre en ", nombre_essai_nombre_p, "essais.\n")

                                print("0 -- Retour Menu Jeux")
                                print("1 -- Rejouer")

                                menu_fin_jeu_nombre_perdu = input("")

                                menu_fin_jeu_nombre_perdu_digit = menu_fin_jeu_nombre_perdu.isdigit()

                                if menu_fin_jeu_nombre_perdu_digit == True:
                                    menu_fin_jeu_nombre_perdu = int(menu_fin_jeu_nombre_perdu)

                                while menu_fin_jeu_nombre_perdu_digit == False or menu_fin_jeu_nombre_perdu < 0 or menu_fin_jeu_nombre_perdu > 1:

                                    print("\nOpération impossible\n")

                                    print("0 -- Retour Menu Jeux")
                                    print("1-- Rejouer\n")

                                    menu_fin_jeu_nombre_perdu = input("Que faire ?\n")
                                    menu_fin_jeu_nombre_perdu_digit = menu_fin_jeu_nombre_perdu.isdigit()

                                    if menu_fin_jeu_nombre_perdu_digit == True:
                                        menu_fin_jeu_nombre_perdu = int(menu_fin_jeu_nombre_perdu)

                                if menu_fin_jeu_nombre_perdu_digit == True:
                                    menu_fin_jeu_nombre_perdu = int(menu_fin_jeu_nombre_perdu)

                                if menu_fin_jeu_nombre_perdu == 0:
                                    fin_jeu_nombre_perdu = 0
                                elif menu_fin_jeu_nombre_perdu == 1:
                                    fin_jeu_nombre_perdu = 1

                                print("")

            elif option == 4:
                while fin_transcodage == 1:
                    print("0 -- Transcoder Décimal => Binaire")
                    print("1 -- Transcoder Décimal => Héxadécimal")
                    print("2 -- Retour Menu")

                    option_transcodage = input("\nQue faire ?\n")

                    option_transcodage_digit = option_transcodage.isdigit()

                    while option_transcodage_digit == False:
                        print("\nOpération impossible, choisissé un bon chiffre.\n")
                        print("0 -- Transcoder Décimal => Binaire")
                        print("1 -- Transcoder Décimal => Héxadécimal")
                        print("2 -- Retour Menu")

                        option_transcodage = input("\nQue faire ?\n")
                        option_transcodage_digit = option_transcodage.isdigit()

                    if option_transcodage_digit == True:
                        option_transcodage = int(option_transcodage)

                    if option_transcodage == 2:
                        fin_transcodage = 0

                    if (option_transcodage > 2 or option_transcodage < 0):
                        print("\nOpération impossible, choisissé un bon chiffre.\n")
                    else:
                        if option_transcodage == 0:
                            fin_transcodage_DB = 1

                            while fin_transcodage_DB == 1:
                                nombre_debut_trans_DB = input("\nDonne moi un chiffre à transcoder en Binaire.\n")

                                nombre_debut_trans_DB_digit = nombre_debut_trans_DB.isdigit()

                                if nombre_debut_trans_DB_digit == True:
                                    nombre_debut_trans_DB = int(nombre_debut_trans_DB)

                                while nombre_debut_trans_DB_digit == False or nombre_debut_trans_DB < 0:

                                    print("\nOpération impossible\n")

                                    nombre_debut_trans_DB = input("\nDonne moi un chiffre à transcoder en Binaire.\n")
                                    nombre_debut_trans_DB_digit = nombre_debut_trans_DB.isdigit()

                                    if nombre_debut_trans_DB_digit == True:
                                        nombre_debut_trans_DB = int(nombre_debut_trans_DB)

                                if nombre_debut_trans_DB_digit == True:
                                    nombre_debut_trans_DB = int(nombre_debut_trans_DB)

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
                                range1_nombre_trans_DB = -1

                                for i in range(binaire_len):
                                    binaire_presque_fini.append(binaire[range1_nombre_trans_DB])
                                    range1_nombre_trans_DB = range1_nombre_trans_DB - 1

                                chiffrebinaire = 1
                                binaire_presque_fini = str(binaire_presque_fini)
                                binaire_fini = ""

                                for i in range(binaire_len):
                                    binaire_fini = binaire_fini + binaire_presque_fini[chiffrebinaire]
                                    chiffrebinaire = chiffrebinaire + 3

                                print("\nLe nombre", nombre_debut_trans_DB, "s'écrit", binaire_fini, "en binaire.")

                                menu_transcodage_DB = 1
                                erreur_menu_transcodage_DB = input("\n0 -- Menu Transcodage \n1 -- Refaire ce transcodage\n")

                                erreur_menu_transcodage_DB_digit = erreur_menu_transcodage_DB.isdigit()

                                if erreur_menu_transcodage_DB_digit == True:
                                    erreur_menu_transcodage_DB = int(erreur_menu_transcodage_DB)

                                while erreur_menu_transcodage_DB_digit == False or erreur_menu_transcodage_DB < 0 or erreur_menu_transcodage_DB > 1:

                                    print("\nOpération impossible\n")

                                    print("0 -- Menu Transcodage")
                                    print("1 -- Refaire ce transcodage\n")

                                    erreur_menu_transcodage_DB = input("Que faire ?\n")
                                    erreur_menu_transcodage_DB_digit = erreur_menu_transcodage_DB.isdigit()

                                    if erreur_menu_transcodage_DB_digit == True:
                                        erreur_menu_transcodage_DB = int(erreur_menu_transcodage_DB)

                                if erreur_menu_transcodage_DB_digit == True:
                                    erreur_menu_transcodage_DB = int(erreur_menu_transcodage_DB)


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
                                        erreur_menu_transcodage_DB = input("\n0 -- Menu Transcodage \n1 -- Refaire ce transcodage\n")

                                        erreur_menu_transcodage_DB_digit = erreur_menu_transcodage_DB.isdigit()

                                        if erreur_menu_transcodage_DB_digit == True:
                                            erreur_menu_transcodage_DB = int(erreur_menu_transcodage_DB)

                                        while erreur_menu_transcodage_DB_digit == False or erreur_menu_transcodage_DB < 0 or erreur_menu_transcodage_DB > 1:

                                            print("\nOpération impossible\n")

                                            print("0 -- Menu Transcodage")
                                            print("1 -- Refaire ce transcodage\n")

                                            erreur_menu_transcodage_DB = input("Que faire ?\n")
                                            erreur_menu_transcodage_DB_digit = erreur_menu_transcodage_DB.isdigit()

                                            if erreur_menu_transcodage_DB_digit == True:
                                                erreur_menu_transcodage_DB = int(erreur_menu_transcodage_DB)

                                        if erreur_menu_transcodage_DB_digit == True:
                                            erreur_menu_transcodage_DB = int(erreur_menu_transcodage_DB)


                        elif option_transcodage == 1:
                            fin_transcodage_DH = 1

                            while fin_transcodage_DH == 1:
                                transcodage_hexa_table = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4',
                                                          5: '5', 6: '6', 7: '7',
                                                          8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C',
                                                          13: 'D', 14: 'E', 15: 'F'}

                                choix_nombre_debut_trans_DH = input("Donne moi un chiffre à transcoder en Hexadécimal.\n")

                                choix_nombre_debut_trans_DH_digit = choix_nombre_debut_trans_DH.isdigit()

                                if choix_nombre_debut_trans_DH_digit == True:
                                    choix_nombre_debut_trans_DH = int(choix_nombre_debut_trans_DH)

                                while choix_nombre_debut_trans_DH_digit == False or choix_nombre_debut_trans_DH < 0:

                                    print("\nOpération impossible\n")

                                    choix_nombre_debut_trans_DH = input("\nDonne moi un chiffre à transcoder en Hexadécimal.\n")
                                    choix_nombre_debut_trans_DH_digit = choix_nombre_debut_trans_DH.isdigit()

                                    if choix_nombre_debut_trans_DH_digit == True:
                                        choix_nombre_debut_trans_DH = int(choix_nombre_debut_trans_DH)

                                if choix_nombre_debut_trans_DH_digit == True:
                                    choix_nombre_debut_trans_DH = int(choix_nombre_debut_trans_DH)

                                nombre_debut_trans_DH = choix_nombre_debut_trans_DH

                                hexadecimal_fini = ''
                                while nombre_debut_trans_DH != 0:
                                    nombre_reste_trans_DH = nombre_debut_trans_DH % 16
                                    hexadecimal_fini = transcodage_hexa_table[nombre_reste_trans_DH] + hexadecimal_fini
                                    nombre_debut_trans_DH = nombre_debut_trans_DH // 16
                                print("\nLe nombre", choix_nombre_debut_trans_DH, "s'écrit", hexadecimal_fini,
                                      "en hexadecimal.")

                                menu_transcodage_DH = 1
                                erreur_menu_transcodage_DH = input("\n0 -- Menu Transcodage \n1 -- Refaire ce transcodage\n")

                                erreur_menu_transcodage_DH_digit = erreur_menu_transcodage_DH.isdigit()

                                if erreur_menu_transcodage_DH_digit == True:
                                    erreur_menu_transcodage_DH = int(erreur_menu_transcodage_DH)

                                while erreur_menu_transcodage_DH_digit == False or erreur_menu_transcodage_DH < 0 or erreur_menu_transcodage_DH > 1:

                                    print("\nOpération impossible\n")

                                    print("0 -- Menu Transcodage")
                                    print("1 -- Refaire ce transcodage\n")

                                    erreur_menu_transcodage_DH = input("Que faire ?\n")
                                    erreur_menu_transcodage_DH_digit = erreur_menu_transcodage_DH.isdigit()

                                    if erreur_menu_transcodage_DH_digit == True:
                                        erreur_menu_transcodage_DH = int(erreur_menu_transcodage_DH)

                                if erreur_menu_transcodage_DH_digit == True:
                                    erreur_menu_transcodage_DH = int(erreur_menu_transcodage_DH)

                                if erreur_menu_transcodage_DH == 0:
                                    menu_transcodage_DH = 0
                                    fin_transcodage_DH = 0
                                    print("")

                                elif erreur_menu_transcodage_DH == 1:
                                    menu_transcodage_DH = 0

