#Importation du module random
import random

#Règles du jeu
regle_jeu = f"""\nPour réussir un combat, il faut que la valeur des deux dés lancés soit supérieure à la force de l’adversaire.  
Dans ce cas, le niveau de vie de l’usager est augmenté de la force de l’adversaire.
Une défaite a lieu lorsque la valeur des deux dés lancés par l’usager est inférieure ou égale à la force de l’adversaire.  
Dans ce cas, le niveau de vie de l’usager est diminué de la force de l’adversaire.
\nLa partie se termine lorsque les points de vie de l’usager tombent sous 0.
\nL’usager peut combattre ou éviter chaque adversaire, dans le cas de l’évitement, il y a une pénalité de 1 point de vie.
\nMaintenant, commençons.\n"""

jeu = True

#Définition des variables qui seront utilisées
nombre_victoires_consecutives = 0
niveau_vie = 20
numero_combat = 0
nombre_victoires = 0
nombre_defaites = 0

#On présente à l'utilisateur son adversaire et ses choix
def actions():
    global force_adversaire
    force_adversaire = random.randint(1, 10)
    force = f"\nVotre adversaire a une force de: {force_adversaire}"
    print(force)
    print("Voici vos options: \nEntrez '1' si vous voulez vous enfuir. \nEntrez '2' si vous voulez le combattre. \nEntrez '3' si vous voulez mettre fin au jeu. \nEntrez '4' si vous voulez voir les règles du jeu. ")
    combat()

#L'utilisateur choisi ce qu'il veut faire et en subi les conséquences
#l'input est la décision prise et l'output est la série de paramètres (niveau_vie, nombre_victoires_consecutives, etc.) qui en résulte
def combat():
    global nombre_victoires_consecutives
    global niveau_vie
    global numero_combat
    global nombre_victoires
    global nombre_defaites
    global jeu
    decision = int(input("Que voulez-vous faire? "))
    #Si l'utilisateur choisi de s'enfuir
    if decision == 1:
        niveau_vie -= 1
        vie = f"Il vous reste {niveau_vie} points de vie."
        print(vie)
        if nombre_victoires_consecutives % 3 == 0 and nombre_victoires_consecutives > 0:
            print("Rencontre d'un nouveau boss...")
        else:
            nombre_victoires_consecutives = 0
            palmares = f"Combat numéro {numero_combat} terminé. Vous avez: \n{nombre_victoires} victoire(s), {nombre_victoires_consecutives} victoires consécutives et {nombre_defaites} défaites"
            print(palmares)
            print("Rencontre d'un nouvel adversaire...")

    #Si l'utilisateur choisi de combattre le monstre
    elif decision == 2:
        numero_combat += 1
        print("\nLancé des dés...")
        de1 = random.randint(1, 6)
        resultat_de1 = f"\nRésultat du premier dé: {de1}"
        print(resultat_de1)
        de2 = random.randint(1, 6)
        resultat_de2 = f"Résultat du deuxième dé: {de2}"
        print(resultat_de2)
        score = de1 + de2
        resultat_de1_de2 = f"\nRésultat total: {score}"
        print(resultat_de1_de2)
        #En cas de défaite
        if score <= force_adversaire:
            nombre_defaites += 1
            nombre_victoires_consecutives = 0
            print("Défaite!")
            niveau_vie -= force_adversaire
            palmares = f"Combat numéro {numero_combat} terminé. Vous avez: \n{nombre_victoires} victoire(s), {nombre_victoires_consecutives} victoires consécutives et {nombre_defaites} défaites"
            print(palmares)
            # Si l'utilisateur tombe à 0 points de vie, il perd la partie
            if niveau_vie <= 0:
                print("La partie est terminée. Vous êtes tombé sous 0 points de vie, vous avez donc perdu. Au revoir")
                jeu = False
            #S'il a toujours plus de 0 points de vie, il continue à jouer
            else:
                vie = f"Il vous reste {niveau_vie} points de vie."
                print(vie)
        #En cas de victoire
        else:
            nombre_victoires += 1
            nombre_victoires_consecutives += 1
            print("Victoire!")
            niveau_vie += force_adversaire
            palmares = f"Combat numéro {numero_combat} terminé. Vous avez: \n{nombre_victoires} victoire(s), {nombre_victoires_consecutives} victoires consécutives et {nombre_defaites} défaites"
            print(palmares)
            vie = f"Il vous reste {niveau_vie} points de vie."
            print(vie)
    #Si l'utilisateur veut revoir les règles
    elif decision == 4:
        regle()
    #Si l'utilisateur décide de quitter la partie
    else:
        print("Au revoir")
        jeu = False

#Fonction présentant à l'utilisateur les règles lors de sa prise de décision face au monstre
def regle():
    print(regle_jeu)
    combat()

#On présente à l'utilisteur un boss qu'il affrontera lorsqu'il atteindra 3 victoires consécutives
def boss():
    global force_adversaire
    force_adversaire = random.randint(10, 12)
    boss = f"\nUn boss est apparu! Il faut prouver que vous êtes assez puissant pour continuer. Force du boss: {force_adversaire}"
    print(boss)
    print("Voici vos options: \nEntrez '1' si vous voulez vous enfuir, ATTENTION! Vous retomberez tout de même sur un boss. \nEntrez '2' si vous voulez le combattre. \nEntrez '3' si vous voulez mettre fin au jeu. \nEntrez '4' si vous voulez voir les règles du jeu.")
    combat()

#Boucle effectuant les actions tant que l'utilisateur a plus de 0 points de vie
while jeu == True:
    if nombre_victoires_consecutives % 3 == 0 and nombre_victoires_consecutives > 0:
        boss()
    else:
        actions()

#QUESTION THÉORIQUE:
#Pour avoir plus d'un monstre derrière chaque porte, il faudrait non pas une variable 'force_adversaire' mais plusieurs d'entre elles (ex: monstre_1, monstre_2, etc.) au début de la fonction 'actions()'.
#On additionnerais ensuite leur force comme on l'a fait avec les dés (monstre_1 + monstre_2) et on placerait cette valeur dans une variable (ex: total)
#Cette variable 'total', qui représente ce que l'utilisateur doit surpasser, prendrait la position de 'force_adversaire' dans ce code.