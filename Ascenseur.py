#Bibliotheque python qui permet la manipulation du temps, et qui nous permet d'integrer des pauses de temps entre l'execution des instructions.
import time

#Fonction qui gere la montée de l'ascenceur, en incrementant le chiffre correspondant aux niveaux
def montee(niveauActuel,niveauRecherche):
    while(int(niveauActuel) <= int(niveauRecherche)):
        print("niveau : ",niveauActuel)
        niveauActuel=int(niveauActuel)+1
        #Introduction d'une pause de 1 seconde entre passage des niveaux ou incrementation du chiffre correspondant aux niveaux
        time.sleep(1)
pass

#Fonction qui gere la descente de l'ascenceur, en decrementant le chiffre correspondant aux niveaux'
def descente(niveauActuel,niveauRecherche):
    while(int(niveauActuel) >= int(niveauRecherche)):
        print("niveau : ",niveauActuel)
        niveauActuel=int(niveauActuel)-1
        time.sleep(1)
pass
#Initialisation du niveau actuel par defaut egale à 0.
#Ca veut dire au debut du code l'assenceur est au rez de chaussé'
niveauActuel=0
#Initialisation du niveau recherché ou niveau ciblé à 0, juste pour permettre à la condition qui gere le cas où l'utilisateur entre un nombre hors plage d'etre fausse au lancement du programme et ne pas aussi creer un bug.
niveauRecherche=0

#Boucle infinie qui gere le fonctionnement de l'ascenceur'
while True:
    print("="*30)
    niveauRecherche=input("Vous etes à quel niveau ? : ")
    #Fonction qui gere l'entree d'un nombre hors plage par l'utilisateur'
    if((int(niveauActuel) > 12 or int(niveauRecherche) > 12 or int(niveauActuel) < -4 or int(niveauRecherche) < -4)):
        break
    else:
    #Gestion de l'appel de l'ascenseur pour qu'il vienne d'ane d'abord à vous avant d'indiquer votre niveau de destination 
         if(int(niveauActuel) > int(niveauRecherche)):
            descente(niveauActuel,niveauRecherche)
            print("On est au niveau",niveauRecherche)
         else:
            montee(niveauActuel,niveauRecherche)
            print("On est au niveau",niveauRecherche)
          
         niveauActuel=niveauRecherche  
         niveauRecherche=input("A quelle niveau voulez-vous allez ? : ")
     #Gestion de la montée ou la descente de l'ascenseur en fonction de votre destination 
        if((int(niveauActuel) > 12 or int(niveauRecherche) > 12 or int(niveauActuel) < -4 or int(niveauRecherche) < -4)):
            break
         if(int(niveauActuel) < int(niveauRecherche)):
            montee(niveauActuel,niveauRecherche)
            print("Vous etes arrivé au niveau",niveauRecherche)
         else:
            descente(niveauActuel,niveauRecherche)
            print("Vous etes arrivé au niveau",niveauRecherche)
            print("_"*30)
         niveauActuel=niveauRecherche
print("="*30)
print("Vous avez entrez un chiffre hors plage, Merci d'avoir utilisé nos service")
