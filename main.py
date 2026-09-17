# 1. LES ENTRÉES
solde = 500.0

# 2. LES TRAITEMENTS ET SORTIES
while True:
    print("\n--- MENU DU GUICHET ---")
    print("1. Consulter le solde")
    print("2. Déposer de l'argent")
    print("3. Retirer de l'argent")
    print("4. Quitter")

    choix = input("Entrez votre choix (1-4) : ")

    # Option 1 : Consulter le solde
    if choix == "1":
        print(f"Solde actuel : {solde:.2f} $")

    # Option 2 : Déposer de l'argent
    elif choix == "2":
        montant_depot = float(input("Entrez le montant à déposer : "))
        solde = solde + montant_depot
        print(f"Dépôt effectué ! Nouveau solde : {solde:.2f} $")

    # Option 3 : Retirer de l'argent
    elif choix == "3":
        montant_retrait = float(input("Entrez le montant à retirer : "))
        # Sécurité pour le solde insuffisant
        if montant_retrait <= solde:
            solde = solde - montant_retrait
            print(f"Retrait effectué ! Nouveau solde : {solde:.2f} $")
        else:
            print("Transaction refusée : solde insuffisant !")

    # Option 4 : Quitter
    elif choix == "4":
        print("Au revoir et merci d'avoir utilisé notre guichet !")
        break

    # Sécurité si l'utilisateur se trompe de touche
    else:
        print("Choix invalide. Veuillez entrer un chiffre entre 1 et 4.")