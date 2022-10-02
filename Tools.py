import random
from random import randint
Menu = 1

while Menu == 1:

    print("0 -- Calculatrice")
    print("1 -- Générateur de mot de passe")
    print("2 -- Jeux")
    option = int(input(""))

    if (option > 2 or option < 0):
        print("\nOpération impossible, choisissé un bon chiffre.\n")
    else:
        fin_calculatrice = 1
        fin_password = 1
        fin_jeu = 1

        print("")

        if option == 0:
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


                option_jeu = int(input(""))

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

                        fin_jeu_PSF1 = int(input('\n0 -- Choix jeux\n1-- Rejouer\n'))
