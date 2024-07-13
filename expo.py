
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

