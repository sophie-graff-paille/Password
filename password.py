import hashlib
from fonctions import *

# on demande en premier le nom du user
user = input("Quel est votre nom ? ")

# boucle qui vérifie si le mot de passe est valide, et si elle est false envoie un message d'erreur et la fonction vérif_m2p s'applique
while True:
    mot2passe = input("Saisir votre mot de passe ")
    verif = vérif_m2p(mot2passe)
   
    if verif != "Votre mot de passe est valide" :
        print("Erreur de saisie ! Veuillez rentrer un nouveau mot de passe...")
        print(verif)
# si la boucle est true, alors elle récupère le mot de passe et l'affiche crypté.
# la fonction convert_data s'applique et la boucle se ferme
    else: 
        # je définis la chaîne de caractères à hasher
        string_to_hash = str(mot2passe)
        # si les 2 premières conditions sont remplies alors il affiche un message de confirmation et le mot de passe hashé
        print("Mot de passe validé", mot2passe)
        # cryptage avec hashlib.sha256 qui s'actualise avant de hasher le mot de passe
        hash = hashlib.sha256(string_to_hash.encode())
        # renvoie le mot de passe hashé en hexadécimale et l'affiche
        hex_hash = hash.hexdigest()
        print(hex_hash)
        convert_data(user, hex_hash)
        break