import json

FICHIER_UTILISATEURS = 'utilisateurs.json'

def chargerUtilisateurs():
    try:
        with open(FICHIER_UTILISATEURS, 'r', encoding='utf-8') as fichier:
            utilisateurs = json.load(fichier)
        return utilisateurs
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []

def sauvegarderUtilisateurs(utilisateurs):
    with open(FICHIER_UTILISATEURS, 'w', encoding='utf-8') as fichier:
        json.dump(utilisateurs, fichier, ensure_ascii=False, indent=4)

def ajouterUtilisateur():
    utilisateurs = chargerUtilisateurs()

    nom = input("Entrez le nom de l'utilisateur : ").strip()
    email = input("Entrez l'email de l'utilisateur : ").strip()
    tel = input("Entrez le numéro de téléphone de l'utilisateur : ").strip()

    utilisateur = {"nom": nom, "email": email, "tel": tel}
    utilisateurs.append(utilisateur)
    sauvegarderUtilisateurs(utilisateurs)
    print("Utilisateur ajouté avec succès")

def supprimerUtilisateur():
    utilisateurs = chargerUtilisateurs()

    if not utilisateurs:
        print("Aucun utilisateur n'est enregistré")
        return

    email = input("Entrez l'email de l'utilisateur à supprimer : ").strip()

    utilisateur_a_supprimer = None
    for utilisateur in utilisateurs:
        if utilisateur['email'] == email:
            utilisateur_a_supprimer = utilisateur
            break

    if utilisateur_a_supprimer:
        utilisateurs.remove(utilisateur_a_supprimer)
        sauvegarderUtilisateurs(utilisateurs)
        print(f"L'utilisateur avec l'email {email} a été supprimé avec succès")
    else:
        print(f"Aucun utilisateur trouvé avec l'email {email}")

def listerUtilisateurs():
    utilisateurs = chargerUtilisateurs()

    if utilisateurs:
        print("Liste des utilisateurs :")
        for utilisateur in utilisateurs:
            print(f"Nom: {utilisateur['nom']}, Email: {utilisateur['email']}, Téléphone: {utilisateur['tel']}")
    else:
        print("Aucun utilisateur n'est enregistré")

