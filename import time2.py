import time  

# Fonction principale
def afficher_heure():
    heure_initiale = input("Entrez l'heure actuelle (HH:MM:SS) : ")
    # Séparer l'entrée en heures, minutes et secondes
    heures, minutes, secondes = heure_initiale.split(":")  # Diviser le texte en trois parties
    heures = int(heures)  
    minutes = int(minutes)  
    secondes = int(secondes)  
    # Calculer le total en secondes
    total_secondes = heures * 3600 + minutes * 60 + secondes

    # Demander à l'utilisateur s'il veut programmer une alarme
    alarme = input("Voulez-vous programmer une alarme ? ( HH:MM:SS ou laissez vide) : ")
    if alarme:  
        heures_alarme, minutes_alarme, secondes_alarme = alarme.split(":")
        heures_alarme = int(heures_alarme)
        minutes_alarme = int(minutes_alarme)
        secondes_alarme = int(secondes_alarme)
        # Calculer le total en secondes pour l'alarme
        total_secondes_alarme = heures_alarme * 3600 + minutes_alarme * 60 + secondes_alarme
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
