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
