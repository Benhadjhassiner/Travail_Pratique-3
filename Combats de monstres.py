#Importation du module random
import random

regle_jeu = f"""\nPour réussir un combat, il faut que la valeur des deux dés lancés soit supérieure à la force de l’adversaire.  
Dans ce cas, le niveau de vie de l’usager est augmenté de la force de l’adversaire.
Une défaite a lieu lorsque la valeur des deux dés lancés par l’usager est inférieure ou égale à la force de l’adversaire.  
Dans ce cas, le niveau de vie de l’usager est diminué de la force de l’adversaire.
\nLa partie se termine lorsque les points de vie de l’usager tombent sous 0.
\nL’usager peut combattre ou éviter chaque adversaire, dans le cas de l’évitement, il y a une pénalité de 1 point de vie.
\nMaintenant, commençons.\n"""
jeu = True

def actions():
    niveau_vie = 20
    global numero_combat
    numero_combat = 0
    nombre_victoires = 0
    nombre_defaites = 0
    nombre_victoires_consecutives = 0
    vie = f"Il vous reste {niveau_vie} points de vie."
    palmares = f"Vous avez maintenant: \n{nombre_victoires} victoire(s), {nombre_victoires_consecutives} victoires consécutives et {nombre_defaites} défaites"
    force_adversaire = random.randint(1, 10)
    force = f"\nVotre adversaire a une force de: {force_adversaire}"
    print(force)
    print("Voici vos options: \nEntrez '1' si vous voulez vous enfuir. \nEntrez '2' si vous voulez le combattre. \nEntrez '3' si vous voulez mettre fin au jeu. \nEntrez '4' si vous voulez voir les règles du jeu. ")
    decision = int(input("Que voulez-vous faire? "))
    if decision == 1:
        niveau_vie -= 1
        print(vie)
        nombre_victoires_consecutives = 0
        print("Rencontre d'un nouvel adversaire...")
    elif decision == 2:
        numero_combat += 1
        print("Lancé des dés...")
        de1 = random.randint(1, 6)
        resultat_de1 = f"\nRésultat du premier dé: {de1}"
        print(resultat_de1)
        de2 = random.randint(1, 6)
        resultat_de2 = f"Résultat du deuxième dé: {de2}"
        print(resultat_de2)
        score = de1 + de2
        resultat_de1_de2 = f"\nRésultat total: {score}"
        print(resultat_de1_de2)
        if score <= force_adversaire:
            print("Défaite!")
            niveau_vie -= force_adversaire
            print(vie)
            nombre_defaites += 1
            nombre_victoires_consecutives = 0
            print(palmares)
        else:
            print("Victoire!")
            niveau_vie += force_adversaire
            print(vie)
            nombre_victoires += 1
            nombre_victoires_consecutives += 1
            print(palmares)
    elif decision == 3:
        print("Au revoir")
        jeu = False
    else:
        print(regle_jeu)
    if niveau_vie < 0:
        print("La partie est terminée, vous avez perdu. Au revoir")
        jeu = False



            


while jeu == True:
    actions()


