# Demander la taille du tableau
taille = int(input("Entrez la taille du tableau : "))

# Initialiser le tableau pour stocker les informations des personnes
personnes = []

# Saisir les informations pour chaque personne
for i in range(taille):
    print(f"\nSaisie des informations pour la personne {i + 1}")
    prenom = input("Prénom : ")
    nom = input("Nom : ")
    note = float(input("Note : "))
    moyenne = float(input("Moyenne : "))
    classe = input("Classe : ")

    # Ajouter les informations de la personne au tableau
    personnes.append({
        "prenom": prenom,
        "nom": nom,
        "note": note,
        "moyenne": moyenne,
        "classe": classe
    })

# Afficher le résultat de la saisie
print("\nRésultat de la saisie :")
for i, personne in enumerate(personnes, 1):
    print(f"\nPersonne {i}:")
    print(f"Prénom : {personne['prenom']}")
    print(f"Nom : {personne['nom']}")
    print(f"Note : {personne['note']}")
    print(f"Moyenne : {personne['moyenne']}")
    print(f"Classe : {personne['classe']}")