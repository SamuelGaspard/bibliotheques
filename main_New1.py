from livre import ajouterLivre, validerAuteure, validerGenre, validerTitre, afficherTousLesLivres, rechercherLivres, archiverLivre,retournererLivre, supprimerLivre,listerUtilisateurs,supprimerUtilisateur,sauvegarderUtilisateurs

# ajouter livre
# rechercher livre
# afficher livres

def menu_principal():
    print("1. Ajouter un livre")
    print("2. Rechercher un livre")
    print("3. Supprimer un livre")
    print("4. Afficher tous les livres")
    print("5. Emprunter un livre")
    print("6. Retourner un livre")
    print("7. Ajouter un utilisateur")
    print("8. Afficher les utilisateurs")
    print("9. Supprimer un utilisateur")
    print("10. Quitter le progamme")
    choix = int(input("Sélectionner une option : "))
    return choix

def main():
    while True:
        choix = menu_principal()
        if choix == 1:
            print("Option 1 : Ajouter un livre")
            # Appeler la fonction ajouterLivre ici
            ajouterLivre()
        elif choix == 2:
            print("Option 2 : Rechercher un livre")
            # Appeler la fonction de recherche de livre ici
            rechercherLivres()
            pass
        elif choix == 3:
            print("Option 3 : Supprimer un livre")
            # Appeler la fonction de suppression de livre ici
            idLivre = int(input("Entrez l'ID du livre à supprimer : "))
            supprimerLivre(idLivre)
            
        elif choix == 4:
            print("Option 4 : Afficher tous les livres")
            # Appeler la fonction pour afficher tous les livres ici
            afficherTousLesLivres()
            pass
        elif choix == 5:
            print("Option 5 : Emprunter un livre")
            idLivre = int(input("Entrez l'ID du livre à archiver : "))
            archiverLivre(idLivre)
            
            # Appeler la fonction pour emprunter un livre ici
        elif choix == 6:
            print("Option 6 : Retourner un livre")
            # Appeler la fonction pour retourner un livre ici
            idLivre = int(input("Entrez l'ID du livre à retourner : "))
            retournererLivre(idLivre)
        elif choix == 7:
            print("option 7: Ajouter un utilisateur")
            sauvegarderUtilisateurs()
        elif choix == 8:
            print("option 7: Afficher tous les  utilisateurs")
            listerUtilisateurs()
        elif choix == 9:
            print("option 9: Supprimer un utilisateur")
            supprimerUtilisateur()
            
        elif choix == 10:
            print("Option 10 : Quitter le programme")
            break  # Quitter la boucle while et donc le programme

if __name__ == "__main__":
    main()
