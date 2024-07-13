from livre import ajouterLivre, rechercherLivres,  afficherTousLesLivres
def menu_principal():
    print("1. AJOUTER UN LIVRE")
    print("2. RECHERCHER UN LIVRE")
    print("3. SUPPRIMER UN LIVRE")
    print("4. AFFICHER UN LIVRE")
    print("5. EMPRUNTER UN LIVRE")
    print("6. RETOURNER UN LIVRE")
    print("7. QUITTER")
    choix = int(input("Sélectionner une option: "))
    return choix
def main():
    while True:
        choix = menu_principal()
        if choix == 1:
            ajouterLivre()
        elif choix == 2:
            rechercherLivres()
        elif choix == 3:
            afficherTousLesLivres()
        elif choix == 4:
            print('')
        elif choix == 5:
            print('')
        elif choix == 6:
            print('')
        elif choix == 7:
            break
if __name__ == 'main':
    main()
        
            
        
    