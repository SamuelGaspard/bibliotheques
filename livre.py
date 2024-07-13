import json

livres = []

def lireLivresDepuisFichier():
    try:
        with open('livres.json', 'r') as f:
            livres = json.load(f)
            return livres
    except FileNotFoundError:
        print("Le fichier livres.json n'existe pas ou n'a pas encore été créé.")
        return []
def afficherTousLesLivres():
    livres = lireLivresDepuisFichier()
    if not livres:
        print("Aucun livre n'a été enregistré.")
    else:
        print("Liste de tous les livres enregistrés :")
        for livre in livres:
            print(f"ID: {livre['id']}, Titre: {livre['titre']}, Auteur: {livre['auteur']}, Genre: {livre['Genre']}, Disponible: {livre['Disponible']}")

def validerTitre(titre):
    premier_caractere = titre[0]
    if premier_caractere.isdigit() or not premier_caractere.isalpha() :#and len(titre) < 5:
        print("Le titre ne peut pas commencer par un chiffre ou un caractère spécial")
        return False
    else:
        return True

def validerAuteure(auteur):
    premier = auteur[0]
    if premier.isdigit() or not premier.isalpha():
        print("Entrer un nom valide de l'auteur qui commence par une lettre")
        return False
    return True

def validerGenre(genre):
    genre_livre = ["historique", "roman", "revues", "livres scientifiques", "bible", "bandes dessinées", "TFC et these"]
    if genre not in genre_livre:
        print("Le genre est inconnu")
        return False
    return True


def sauvegarderLivres(livres):
    with open('livres.json', 'a') as f:
        json.dump(livres, f, indent=4)

def genererProchainID():
    livres = lireLivresDepuisFichier()
    if livres:
        dernier_id = max(livre['id'] for livre in livres)
        return dernier_id + 1
    else:
        return 1  # Si aucun livre n'est enregistré, commence à partir de l'ID 1

def ajouterLivre(titreLivre, auteurLivre, genreLivre):
    disponible = True
    idLivre = genererProchainID()
    livres = lireLivresDepuisFichier()
    
    
    
   
        # ... (boucles de validation pour titreLivre, auteurLivre et genreLivre restent identiques)
    while True:
        titreLivre = input("Saisir le titre du livre : ")
        if len(titreLivre) < 5 or not titreLivre[0].isalpha():
            print("Le titre ne peut pas commencer par un chiffre ou un caractère spécial et doit faire au moins 5 caractères.")
            continue
        break
    
    while True:
        auteurLivre = input("Saisir le auteur du livre : ")
        if not auteurLivre[0].isalpha():
            print("Entrer un nom valide de l'auteur qui commence par une lettre")
            continue
        break
    
    while True:
        genreLivre = input("Saisir le genre du livre,\n veuillez choisir parmi ceci :historique, roman, revues, livres scientifiques, bible, bandes dessinées, TFC et these: ")
        genre_livre = ["historique", "roman", "revues", "livres scientifiques", "bible", "bandes dessinées", "TFC et these"]
        if genreLivre not in genre_livre:
            print("Le genre est inconnu")
            continue
        break
    for livre_existant in livres:
        if (livre_existant["titre"] == titreLivre and
            livre_existant["auteur"] == auteurLivre and
            livre_existant["Genre"] == genreLivre):
            print(f"Un livre avec le même titre '{titreLivre}', le même auteur '{auteurLivre}' et le même genre '{genreLivre}' existe déjà.")
            return  # Annuler l'ajout
    livre = {"id": idLivre, "titre": titreLivre, "auteur": auteurLivre, "Genre": genreLivre, "Disponible": disponible}
    livre = {"id": idLivre, "titre": titreLivre, "auteur": auteurLivre, "Genre": genreLivre, "Disponible": disponible}
    livres.append(livre)
    sauvegarderLivres(livres)
    print( livre ,"\n Ajouté avec succès.")
    #Fonction de recherche de livre
def rechercherLivres():
    critereTitre = input("Saisir le titre à rechercher (ou vide pour ne pas filtrer par titre) : ")
    critereAuteur = input("Saisir l'auteur à rechercher (ou vide pour ne pas filtrer par auteur) : ")
    critereGenre = input("Saisir le genre à rechercher (ou vide pour ne pas filtrer par genre) : ")
    critereDisponibilite = input("Rechercher uniquement les livres disponibles ? (oui/non) : ")

    livres = lireLivresDepuisFichier()
    livres_trouves = []

    for livre in livres:
        if (critereTitre in livre["titre"].lower() or critereTitre == "") and \
           (critereAuteur in livre["auteur"].lower() or critereAuteur == "") and \
           (critereGenre in livre["Genre"].lower() or critereGenre == "") and \
           (critereDisponibilite.lower() == "oui" and livre["Disponible"] or critereDisponibilite.lower() == "non" or critereDisponibilite == ""):
            livres_trouves.append(livre)

    if livres_trouves:
        print("Livres trouvés :")
        for livre in livres_trouves:
            print(f"ID: {livre['id']}, Titre: {livre['titre']}, Auteur: {livre['auteur']}, Genre: {livre['Genre']}, Disponible: {livre['Disponible']}")
    else:
        print("Aucun livre ne correspond aux critères de recherche.") 
def archiverLivre(idLivre):
    livres = lireLivresDepuisFichier()
    livre_trouve = False
    for livre in livres:
        if livre["id"] == idLivre:
            livre["Archivé"] = True
            livre["Disponible"] = False  # Assurez-vous que le livre est marqué comme non dispon
            livre_trouve = True
            break

    if not livre_trouve:
        print(f"Livre avec l'ID {idLivre} non trouvé.")
    else:
        sauvegarderLivres(livres)
        print(f"Livre avec l'ID {idLivre} a été archivé avec succès.")
def retournererLivre(idLivre):
    livres = lireLivresDepuisFichier()
    livre_trouve = True
    for livre in livres:
        if livre["id"] == idLivre:
            livre["Archivé"] = False
            livre["Disponible"] = True  # Assurez-vous que le livre est marqué comme non disponi
            livre_trouve = False
            break

    if not livre_trouve:
        sauvegarderLivres(livres)
        print(f"Livre avec l'ID {idLivre} a été retourné avec succès.")
    else:
        
        print(f"Livre avec l'ID {idLivre} non trouvé.")   
def supprimerLivre(idLivre):
  livres = lireLivresDepuisFichier()
  livre_trouve = False
  for livre in livres:
    if livre["id"] == idLivre:
      if livre["Archivé"]:
        print("Impossible de supprimer ce livre car il est archivé.")
      else:
        livres.remove(livre)
        livre_trouve = True
        break

  if not livre_trouve:
    print(f"Livre avec l'ID {idLivre} non trouvé.")
  else:
    sauvegarderLivres(livres)
    print(f"Livre avec l'ID {idLivre} a été supprimé avec succès.")
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

#class Lecteur:
def __init__(self, nom, profession, expérience, besoins, attentes):
        self.nom = nom
        self.profession = profession
        self.expérience = expérience
        self.besoins = besoins
        self.attentes = attentes

def __str__(self):
        return f"Nom : {self.nom}, Profession : {self.profession}, Expérience : {self.expérience}, Besoins : {self.besoins}, Attentes : {self.attentes}"


class Bibliothécaire:
    def __init__(self):
        self.lecteurs = []

    def ajouter_lecteur(self, nom, profession, expérience, besoins, attentes):
        for lecteur in self.lecteurs:
            if lecteur.nom == nom:
                print("Ce lecteur est déjà enregistré.")
                return
        nouvel_lecteur = Lecteur(nom, profession, expérience, besoins, attentes)
        self.lecteurs.append(nouvel_lecteur)
        print("Lecteur enregistré avec succès.")

    def afficher_lecteurs(self):
        for lecteur in self.lecteurs:
            print(lecteur)
#fonction pour authentifier 
