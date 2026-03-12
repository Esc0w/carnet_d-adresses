# Carnet d'adresses
contacts = []
#groupes = ["Famille", "Ami", "Travail"]

# Création du fichier de mémoire:


# Menu:
while True:
    print("Bienvenue dans votre carnet d'adresses !")
    print("1. Afficher les contacts")
    print("2. Ajouter un contact")
    print("3. Supprimer un contact")
    print("4. Quitter le programme")
    choix = input("Votre choix : ")
    if choix == "1":
        # Afficher les contacts
        for contact in contacts:
            print(contact["Nom"], contact["Prénom"])
    elif choix == "2":
        # Ajouter un contact:
        nom = input("Nom : ")
        prenom = input("Prénom : ")
        telephone_perso = input("Téléphone perso. : ")
        telephone_pro = input("Téléphone pro. : ")
        mail_perso = input("@mail perso. : ")
        mail_pro = input("@mail pro. : ")
        adresse = input("Adresse : ")
        code_postal = input("Code postal : ")
        ville = input("Ville : ")
        pays = input("Pays : ")
        anniversaire = input("Anniversaire : ")
        groupe = input("Groupe : ")
        contact_infos = {
            "id": len(contacts) + 1, 
            "Nom": nom, 
            "Prénom": prenom, 
            "Téléphone perso.": telephone_perso, 
            "Téléphone pro.": telephone_pro,
            "@mail perso.": mail_perso, 
            "@mail pro.": mail_pro, 
            "Adresse": adresse, 
            "Code postal": code_postal, 
            "Ville": ville, 
            "Pays": pays, 
            "Anniversaire": anniversaire, 
            "Groupe": groupe,
        }
        contacts.append(contact_infos)
    elif choix == "3":
        # Supprimer un contact:
        pass
        # Quitter le programme:
    elif choix == "4":
        print("Au revoir !")
        break