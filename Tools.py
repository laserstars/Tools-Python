import random

print("0 -- Calculatrice")
print("1 -- Générateur de mot de passe")
option = int(input(""))

fin1 = 1
fin2 = 1

print("")

if option == 0:
    while fin1 == 1:

        chiffre1 = int(input("Choisi ton premier nombre "))

        print("")

        print("0 -- Multiplier par ... ")
        print("1 -- Diviser par ... ")
        print("2 -- Additionner par ... ")
        print("3 -- Soustraire par ... ")

        print("")

        symbole = int(input("Choisir une opération "))

        print("")

        chiffre2 = int(input("Choisi ton deuxième nombre "))

        print("")

        multiplication = chiffre1*chiffre2
        division = chiffre1/chiffre2
        addition = chiffre1+chiffre2
        soustration = chiffre1-chiffre2

        if symbole == 0:
            print("Le résultat est ", multiplication)

        elif symbole == 1:
            print("Le résultat est ", division)

        elif symbole == 2:
            print("Le résultat est ", addition)

        elif symbole == 3:
            print("Le résultat est ", soustration)

        print("")

        print("0 -- Quitter")
        print("1 -- Nouvelle opération")

        print("")

        print("Que faire ?")

        fin1 = int(input(""))

        print("")

elif option == 1:
    while fin2 == 1:
        lower_case = "abcdefghijklmnopqrstuvwxyz"
        upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        number = "0123456789"
        symbols = "\/#@%&*$"

        Use_for = lower_case + upper_case + number + symbols
        lenght_for_pass = int(input("Quelle taille pour le mot de passe ? "))

        print("")

        password = "".join(random.sample(Use_for, lenght_for_pass))
        print("Le nouveau mot de passe est " + password)

        print("")

        print("0 -- Quitter")
        print("1 -- Nouveau mot de passe")

        print("")

        print("Que faire ?")

        fin2 = int(input(""))

        print("")