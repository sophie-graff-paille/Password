import json
import string

# fonction qui vérifie la validité du mot de passe du user
def vérif_m2p(mot2passe):
    # ascii_letters = concaténation de lettres minuscules et majuscules
    # digits = chaîne contenant les chiffres de 0 à 9
    # punctuation = caractères spéciaux

    # définit l'ensemble des caractères pris en compte dans mon password
    majlettres = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    m = 0
    minletters = "abcdefghijklmnopqrstuvwxyz"
    s = 0
    chiffres = string.digits
    c = 0
    spécialcar = "!@#$%^&*"
    p = 0

    # si la longueur de mon password est supérieure ou égale à 8
    if (len(mot2passe)>=8):
        for i in mot2passe: # pour l'élément dans password
            if (i in majlettres): # s'il y a une lettre majuscule de ma variable majlettres définie avant
                m += 1
            if (i in minletters): # s'il y a une lettre miniscule de ma variable minlettres définie avant
                s += 1
            if (i in chiffres): # s'il y a un chiffre de ma variable chiffre définie avant
                c += 1
            if (i in spécialcar): # s'il y a un caractère spécial de ma variable specialcar définie avant
                p += 1

    # s'il y a 1 majuscule ou +, 1 miniscule ou +, 1 chiffre ou +, 1 caractère spécial ou +
    if (m >= 1 and s >= 1 and c >= 1 and p >= 1):
        return "Votre mot de passe est valide"     
    else:
        return "Votre mot de passe n'est pas valide"

# fonction qui lit, vérifie les doublons et convertit mes objets Python en Json
def convert_data(user, hex_hash):
        # essaye de lire le fichier passdata.json s'il existe, avec la fonction load, r(read)
        try: 
            with open("passdata.json", "r") as mon_fichier:
                dic = json.load(mon_fichier)
        except: # s'il n'existe pas alors le dictionnaire reste vide
            dic = {}
# vérifie en comparant les noms des users et les mots de passe   
        # si le user est déjà dans un dictionnaire
        if user in dic:
            # si le mot de passe hashé n'est pas dans le dictionnaire du user
            if hex_hash not in dic[user]:
                # alors le mot de passe hashé est ajouté au dictionnaire du user
                dic[user] += [hex_hash]
        # et si le user n'est pas dans un dictionnaire
        elif user not in dic:
            # alors un nouveau dictionnaire user est enregistré et associé avec le mot de passe hashé
            dic[user] = [hex_hash]
        # convertit mes objets Python en Json avec la fonction dump, w(write)
        with open("passdata.json", "w") as mon_fichier:
            # fonction à laquelle on ajoute des paramètres d'indentation et de séparations pour une meilleure lecture
            json.dump(dic, mon_fichier, indent=2, separators=(",", ": "))