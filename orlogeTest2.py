import time

def afficher_heure():
    # Demander l'heure de départ
    heure_initiale = input("Quelle heure est-il ? (HH:MM:SS) : ")
    heures, minutes, secondes = map(int, heure_initiale.split(":"))#La fonction `map` applique la fonction `int` à chaque élément de la liste . Cela signifie que chaque sous-chaîne (qui est initialement de type `str`) sera convertie en un entier (`int`).
    total_secondes = heures * 3600 + minutes * 60 + secondes 
    """convertie en seconde total"""

    # Demander une heure pour l'alarme
    alarme = input("Programmer une alarme ? ( HH:MM:SS ou laisser vide) : ")
    if alarme:
        heures_alarme, minutes_alarme, secondes_alarme = map(int, alarme.split(":"))  
        total_secondes_alarme = heures_alarme * 3600 + minutes_alarme * 60 + secondes_alarme
    else:
        total_secondes_alarme = None

    while True:
        # Afficher l'heure actuelle sur 24h
        heures = total_secondes // 3600 % 24   # (//) = 
        minutes = (total_secondes % 3600) // 60
        secondes = total_secondes % 60
        print(f"{heures:02}:{minutes:02}:{secondes:02}", end="\r")

        # Vérifier si l'heure correspond à l'alarme
        if total_secondes_alarme is not None and total_secondes == total_secondes_alarme:
            print("\n⏰ Alarme ! Il est temps !")
            break  # Terminer la boucle après l'alarme

        total_secondes += 1
        time.sleep(1)

if __name__ == "__main__":
    afficher_heure()