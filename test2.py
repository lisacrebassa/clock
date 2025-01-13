import time  

def regler_alarme(heures, minutes, secondes):
    """
    Fonction qui règle l'alarme à partir d'un tuple (heures, minutes, secondes).
    Renvoie le nombre total de secondes correspondant à l'alarme.
    """
    total_alarme = heures * 3600 + minutes * 60 + secondes
    print(f"Alarme réglée à {heures:02}:{minutes:02}:{secondes:02}")
    return total_alarme

# Fonction principale
def afficher_heure():
    # Demander l'heure de départ
    heure_initiale = input("Quelle heure est-il ? (HH:MM:SS) : ")
    heures, minutes, secondes = map(int, heure_initiale.split(":"))#La fonction `map` applique la fonction `int` à chaque élément de la liste . Cela signifie que chaque sous-chaîne (qui est initialement de type `str`) sera convertie en un entier (`int`).
    total_secondes = heures * 3600 + minutes * 60 + secondes 
    """convertie en seconde total"""

    # Demander à l'utilisateur s'il veut programmer une alarme
    alarme = input("Voulez-vous programmer une alarme ? ( HH:MM:SS ou laissez vide) : ")
    if alarme:  
        heures_alarme, minutes_alarme, secondes_alarme = alarme.split(":")
        heures_alarme = int(heures_alarme)
        minutes_alarme = int(minutes_alarme)
        secondes_alarme = int(secondes_alarme)
        # On utilise la nouvelle fonction pour régler l'alarme
        total_secondes_alarme = regler_alarme(heures_alarme, minutes_alarme, secondes_alarme)
    else:  
        total_secondes_alarme = None

    # Boucle infinie pour afficher l'heure
    while True:
        heures = total_secondes // 3600 % 24  # On garde l'heure dans un format 24h
        minutes = (total_secondes % 3600) // 60
        secondes = total_secondes % 60
        
        # Afficher l'heure actuelle
        print(f"{heures:02}:{minutes:02}:{secondes:02}", end="\r")  

        # Vérifier si c'est l'heure de l'alarme
        if total_secondes_alarme is not None and total_secondes == total_secondes_alarme:
            print("\n⏰ Alarme ! Il est temps !")  # Message pour l'alarme
            break  

        # Ajouter et attendre une seconde
        total_secondes += 1
        time.sleep(1)  

afficher_heure()