# Carnet d'adresses
#groupes = ["Famille", "Ami", "Travail"]

# Création du fichier de mémoire:

# Liste de contacts:
contacts = []
# Menu:
while True:
    print("Bienvenue dans votre carnet d'adresses !")
    print("1. Afficher les contacts")
    print("2. Ajouter un contact")
    print("3. Modifier un contact")
    print("4. Supprimer un contact")
    print("5. Quitter le programme")
    choix = input("Votre choix : ")
    if choix == "1":
        # Afficher les contacts
        for contact in contacts:
            print(contact["Nom"], contact["Prénom"])
    elif choix == "2":
        # Ajouter un contact:
        print("Ajouter un contact:")
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
        # Modifier un contact:
        print("Modifier un contact:")
        nom = input("Nom du contact à modifier : ")
        prenom = input("Prénom du contact à modifier : ")
        trouve = False
        for contact in contacts:
            if contact["Nom"] == nom and contact["Prénom"] == prenom:
                trouve = True
                print("Que souhaitez-vous modifier ?")
                print("1. Nom")
                print("2. Prénom")
                print("3. Téléphone perso.")
                print("4. Téléphone pro.")
                print("5. @mail perso.")
                print("6. @mail pro.")
                print("7. Adresse")
                print("8. Code postal")
                print("9. Ville")
                print("10. Pays")
                print("11. Anniversaire")
                print("12. Groupe")
                print("13. Tout modifier")
                print("14. Annuler")
                choix_modification = input("Votre choix : ")
                if choix_modification == "1":
                    contact["Nom"] = input("Nouveau nom : ")
                    print("Contact modifié !")
                elif choix_modification == "2":
                    contact["Prénom"] = input("Nouveau prénom : ")
                    print("Contact modifié !")
                elif choix_modification == "3":
                    contact["Téléphone perso."] = input("Nouveau téléphone perso. : ")
                    print("Contact modifié !")
                elif choix_modification == "4":
                    contact["Téléphone pro."] = input("Nouveau téléphone pro. : ")
                    print("Contact modifié !")
                elif choix_modification == "5":
                    contact["@mail perso."] = input("Nouveau @mail perso. : ")
                    print("Contact modifié !")
                elif choix_modification == "6":
                    contact["@mail pro."] = input("Nouveau @mail pro. : ")
                    print("Contact modifié !")
                elif choix_modification == "7":
                    contact["Adresse"] = input("Nouvelle adresse : ")
                    print("Contact modifié !")
                elif choix_modification == "8":
                    contact["Code postal"] = input("Nouveau code postal : ")
                    print("Contact modifié !")
                elif choix_modification == "9":
                    contact["Ville"] = input("Nouvelle ville : ")
                    print("Contact modifié !")
                elif choix_modification == "10":
                    contact["Pays"] = input("Nouveau pays : ")
                    print("Contact modifié !")
                elif choix_modification == "11":
                    contact["Anniversaire"] = input("Nouvel anniversaire : ")
                    print("Contact modifié !")
                elif choix_modification == "12":
                    contact["Groupe"] = input("Nouveau groupe : ")
                    print("Contact modifié !")
                elif choix_modification == "13":
                    # Modifier tous les champs:
                    contact["Nom"] = input("Nouveau nom : ")
                    contact["Prénom"] = input("Nouveau prénom : ")
                    contact["Téléphone perso."] = input("Nouveau téléphone perso. : ")
                    contact["Téléphone pro."] = input("Nouveau téléphone pro. : ")
                    contact["@mail perso."] = input("Nouveau @mail perso. : ")
                    contact["@mail pro."] = input("Nouveau @mail pro. : ")
                    contact["Adresse"] = input("Nouvelle adresse : ")
                    contact["Code postal"] = input("Nouveau code postal : ")
                    contact["Ville"] = input("Nouvelle ville : ")
                    contact["Pays"] = input("Nouveau pays : ")
                    contact["Anniversaire"] = input("Nouvel anniversaire : ")
                    contact["Groupe"] = input("Nouveau groupe : ")
                    print("Contact modifié !")
                elif choix_modification == "14":
                    print("Modification annulée !")
        if not trouve:
            print("Contact non trouvé !")
    elif choix == "4":
        # Supprimer un contact:
        print("Supprimer un contact:")
        nom = input("Nom du contact à supprimer : ")
        prenom = input("Prénom du contact à supprimer : ")
        trouve = False
        for contact in contacts:
            if contact["Nom"] == nom and contact["Prénom"] == prenom:
                trouve = True
                validation = input("Êtes-vous sûr de vouloir supprimer ce contact ? (O/N) : ")
                if validation.upper() == "N":
                    print("Suppression annulée !")
                elif validation.upper() == "O":
                    contacts.remove(contact)
                    print("Contact supprimé !")
        if not trouve:
            print("Contact non trouvé !")
        # Quitter le programme:
    elif choix == "5":
        print("Au revoir !")
        break
