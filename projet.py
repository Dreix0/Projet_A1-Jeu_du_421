### Fonctions ####
def tirer_des(liste, choix1, choix2, choix3):
    if choix1 == True:
        de1 = random.randint(1,6)
    else:
        de1 = liste[0]
    
    if choix2 == True:
        de2 = random.randint(1,6)
    else:
        de2 = liste[1]
        
    if choix3 == True:
        de3 = random.randint(1,6)
    else:
        de3 = liste[2]
    return de1,de2,de3


def calcul_pt(de1, de2, de3):
    # Ranger du plus grand au plus petit
    if de1>=de2 and de1>=de3:
        val1 = de1
        if de2>=de3:
            val2 = de2
            val3 = de3
        else:
            val2 = de3
            val3 = de2
    elif de2>=de1 and de2>=de3:
        val1 = de2
        if de1>=de3:
            val2 = de1
            val3 = de3
        else:
            val2 = de3
            val3 = de1
    else:
        val1 = de3
        if de1>=de2:
            val2 = de1
            val3 = de2
        else:
            val2 = de2
            val3 = de1
    # Calcul des points        
    if val1==4 and val2==2 and val3==1:
        score=10
    elif val1==val2==val3==1:
        score=7
    elif val1==6 and val2==val3==1 or val1==val2==val3==6:
        score=6
    elif val1==5 and val2==val3==1 or val1==val2==val3==5:
        score=5
    elif val1==4 and val2==val3==1 or val1==val2==val3==4:
        score=4
    elif val1==3 and val2==val3==1 or val1==val2==val3==3:
        score=3
    elif val1==2 and val2==val3==1 or val1==val2==val3==2:
        score=2
    elif val1==val2+1 and val1==val3+2:
        score=2
    else:
        score=1
    return score

def choix_des(de1, de2, de3):
    choix1 = int(input("Voulez vous relancez le dé 1 ("+ str(de1) +") ? Entrez 1 pour oui et 0 pour non : "))
    choix2 = int(input("Voulez vous relancez le dé 2 ("+ str(de2) +") ? Entrez 1 pour oui et 0 pour non : "))
    choix3 = int(input("Voulez vous relancez le dé 3 ("+ str(de3) +") ? Entrez 1 pour oui et 0 pour non : "))
    return choix1,choix2,choix3

def verif_score(liste):
    verif = False
    for i in range(nbr_joueur):
        if verif==True:
            break
        elif score_joueur[i] >= score_max:
            verif = True
        else:
            verif = False
    return verif

def gagnant(liste):
    max=0
    gagnant = 0
    for i in range(nbr_joueur):
        if liste[i]>max:
            max=liste[i]
            gagnant = i+1
    return print("Le gagnant est le joueur "+str(gagnant)+" avec "+str(max)+" points !")
            

### Initaialisation  des variables et importation des bibliothèques###

import random    

nbr_joueur = 0
score_max = 0
manche = 0
i=0
score_joueur = []

### Programme principale ###
nbr_joueur = int(input("Entrez le nombre de joueur : "))
for i in range(nbr_joueur):
    score_joueur.append(0)
score_max = int(input("Entrez le score maximal(final) : "))
while verif_score(score_joueur)==False:
    i = 0
    manche += 1
    print("### Manche " + str(manche) + " ###")
    while i<nbr_joueur:
        i+=1
        de1=random.randint(1,6)
        de2=random.randint(1,6)
        de3=random.randint(1,6)
        print("Joueur "+str(i)+", lancé 1 : "+str(de1)+" , "+str(de2)+" , "+str(de3))
        choix1, choix2, choix3 = choix_des(de1,de2,de3)
        de1, de2, de3= tirer_des([de1,de2,de3],choix1,choix2,choix3)
        print("Joueur "+str(i)+", lancé 2 : "+str(de1)+" , "+str(de2)+" , "+str(de3))
        choix1, choix2, choix3 = choix_des(de1,de2,de3)
        de1, de2, de3= tirer_des([de1,de2,de3],choix1,choix2,choix3)
        print("Joueur "+str(i)+", lancé 3 : "+str(de1)+" , "+str(de2)+" , "+str(de3))
        score_joueur[i-1]+=calcul_pt(de1,de2,de3)
        print("Score du joueur "+str(i)+" : "+str(score_joueur[i-1]))
gagnant(score_joueur)