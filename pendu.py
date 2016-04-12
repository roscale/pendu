#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Rosca Alex 4TB
# pendu.py – 12.04.16

from random import choice
from os import system

fichier = open("mots.txt", "r")
lignes = fichier.readlines()
fichier.close()

mot = list(choice(lignes)[:-1])
masque = list("*" * len(mot))
lettres_mauvaises = []
chances = 0

system("clear")
while chances != 5 and chances != 10 and chances != 15:
    chances = int(input("Choisisez un niveau[5-10-15]: "))

while masque != mot and chances > 0:
    system("clear")

    # Chances
    print("Chances: {}".format("|" * chances))

    # Masque
    for lettre in masque:
        if lettre != "*":
            print('\033[92m' + '\033[1m' + lettre + '\033[0m', end="")
        else:
            print(lettre, end="")
    print('\n')

    # Mauvaises lettres
    print('\033[31m' + '\033[1m' + "({}".format(" – ".join(lettres_mauvaises) + ')\033[0m'))

    # Proposition
    proposition = input("Proposition: ")

    # Vérifications
    trouve = False
    for lettre_pos in range(len(mot)):
        if mot[lettre_pos] == proposition:
            masque[lettre_pos] = proposition
            trouve = True

    if trouve == False and proposition not in lettres_mauvaises and proposition != "":
        lettres_mauvaises.append(proposition)
        chances -= 1

# Fin
if masque == mot:
    print('\nVous avez devinez le mot {}.'.format('\033[92m' + '\033[1m' + "".join(mot) + '\033[0m'))
else:
    print('\nLe mot était {}.'.format('\033[92m' + '\033[1m' + "".join(mot) + '\033[0m'))
