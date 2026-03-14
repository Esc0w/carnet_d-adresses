### carnet_d-adresses_V1.py by Esc0w ###

# import
import json


# Création du fichier de mémoire:



# Chargement des contacts depuis le fichier de mémoire:
def charger_contacts():
    try:
        with open("contacts.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

contacts = charger_contacts()

# Sauvegarde des contacts dans le fichier de mémoire:
def sauvegarder_contacts(contacts):
    with open("contacts.json", "w") as f:
        json.dump(contacts, f)


# Menu:
while True:
    print("\n══════════════════════════════════════════")
    print(" Bienvenue dans votre carnet d'adresses !  ")
    print("══════════════════════════════════════════")
    print("     Vous avez actuellement", len(contacts), "contact(s).")
    print("         Que souhaitez-vous faire ?       ")
    print("         1. Afficher les contacts         ")
    print("         2. Rechercher un contact         ")
    print("         3. Ajouter un contact            ")
    print("         4. Modifier un contact           ")
    print("         5. Supprimer un contact          ")
    print("         Q. Quitter le programme          ")
    print("──────────────────────────────────────────")
    choix = input("         Votre choix : ")
    if choix == "1":
        # Afficher les contacts:
        trouve = False
        for contact in contacts:
            trouve = True
            print(contact["Nom"], contact["Prénom"])
        if not trouve:
            print("Aucun contact trouvé.")
        # Afficher les détails d'un contact:
        else:
            contact_details = input("Quel contact souhaitez-vous afficher ? (Nom Prénom) : ")
            try:
                nom = contact_details.split()[0]
                prenom = contact_details.split()[1]
            except IndexError:
                print ("Format invalide ! Veuillez entrer : Nom Prénom")
                continue
            for contact in contacts:
                if contact["Nom"] == nom and contact["Prénom"] == prenom:
                    print("Nom :", contact["Nom"])
                    print("Prénom :", contact["Prénom"])
                    print("Téléphone perso. :", contact["Téléphone perso."])
                    print("Téléphone pro. :", contact["Téléphone pro."])
                    print("@mail perso. :", contact["@mail perso."])
                    print("@mail pro. :", contact["@mail pro."])
                    print("Adresse :", contact["Adresse"])
                    print("Code postal :", contact["Code postal"])
                    print("Ville :", contact["Ville"])
                    print("Pays :", contact["Pays"])
                    print("Anniversaire :", contact["Anniversaire"])
                    print("Groupe :", contact["Groupe"])
    elif choix == "2":
        # Rechercher un contact:
        print("Rechercher un contact:")
        nom = input("Nom : ")
        prenom = input("Prénom : ")
        trouve = False
        for contact in contacts:
            if contact["Nom"] == nom and contact["Prénom"] == prenom:
                trouve = True
                print("Nom :", contact["Nom"])
                print("Prénom :", contact["Prénom"])
                print("Téléphone perso. :", contact["Téléphone perso."])
                print("Téléphone pro. :", contact["Téléphone pro."])
                print("@mail perso. :", contact["@mail perso."])
                print("@mail pro. :", contact["@mail pro."])
                print("Adresse :", contact["Adresse"])
                print("Code postal :", contact["Code postal"])
                print("Ville :", contact["Ville"])
                print("Pays :", contact["Pays"])
                print("Anniversaire :", contact["Anniversaire"])
                print("Groupe :", contact["Groupe"])
        if not trouve:
            print("Contact non trouvé !")
    elif choix == "3":
        # Ajouter un contact:
        print("Ajouter un contact:")
        nom = input("Nom : ")
        prenom = input("Prénom : ")
        if not nom or not prenom:
            print("Veuillez entrer un nom et/ou un prénom valides pour ajouter le contact.")
            continue
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
        sauvegarder_contacts(contacts)
        print("Contact ajouté !")
    elif choix == "4":
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
                    nouveau_nom = input("Nouveau nom : ")
                    if not nouveau_nom:
                        print("Le nouveau nom ne peut être vide !")
                    else: 
                        contact["Nom"] = nouveau_nom
                        print("Contact modifié !")
                        sauvegarder_contacts(contacts)
                elif choix_modification == "2":
                    nouveau_prenom = input("Nouveau prénom : ")
                    if not nouveau_prenom:
                        print("Le nouveau prénom ne peut être vide !")
                    else:
                        contact["Prénom"] = nouveau_prenom
                        print("Contact modifié !")
                        sauvegarder_contacts(contacts)
                elif choix_modification == "3":
                    contact["Téléphone perso."] = input("Nouveau téléphone perso. : ")
                    print("Contact modifié !")
                    sauvegarder_contacts(contacts)
                elif choix_modification == "4":
                    contact["Téléphone pro."] = input("Nouveau téléphone pro. : ")
                    print("Contact modifié !")
                    sauvegarder_contacts(contacts)
                elif choix_modification == "5":
                    contact["@mail perso."] = input("Nouveau @mail perso. : ")
                    print("Contact modifié !")
                    sauvegarder_contacts(contacts)
                elif choix_modification == "6":
                    contact["@mail pro."] = input("Nouveau @mail pro. : ")
                    print("Contact modifié !")
                    sauvegarder_contacts(contacts)
                elif choix_modification == "7":
                    contact["Adresse"] = input("Nouvelle adresse : ")
                    print("Contact modifié !")
                    sauvegarder_contacts(contacts)
                elif choix_modification == "8":
                    contact["Code postal"] = input("Nouveau code postal : ")
                    print("Contact modifié !")
                    sauvegarder_contacts(contacts)
                elif choix_modification == "9":
                    contact["Ville"] = input("Nouvelle ville : ")
                    print("Contact modifié !")
                    sauvegarder_contacts(contacts)
                elif choix_modification == "10":
                    contact["Pays"] = input("Nouveau pays : ")
                    print("Contact modifié !")
                    sauvegarder_contacts(contacts)
                elif choix_modification == "11":
                    contact["Anniversaire"] = input("Nouvel anniversaire : ")
                    print("Contact modifié !")
                    sauvegarder_contacts(contacts)
                elif choix_modification == "12":
                    contact["Groupe"] = input("Nouveau groupe : ")
                    print("Contact modifié !")
                    sauvegarder_contacts(contacts)
                elif choix_modification == "13":
                    # Modifier tous les champs:
                    nouveau_nom = input("Nouveau nom : ")
                    nouveau_prenom = input("Nouveau prénom : ")
                    if not nouveau_nom or not nouveau_prenom:
                        print("Le nouveau nom et prénom ne peuvent être vide, modification annulée !")
                    else:
                        contact["Nom"] = nouveau_nom
                        contact["Prénom"] = nouveau_prenom
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
                        sauvegarder_contacts(contacts)
                elif choix_modification == "14":
                    print("Modification annulée !")
                else:
                    print("Choix invalide !")
        if not trouve:
            print("Contact non trouvé !")
    elif choix == "5":
        # Supprimer un contact:
        print("Supprimer un contact:")
        nom = input("Nom du contact à supprimer : ")
        prenom = input("Prénom du contact à supprimer : ")
        if not nom or not prenom:
            print("Veuillez entrer un nom et/ou un prénom valides pour supprimer le contact.")
            continue
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
                    sauvegarder_contacts(contacts)
                else:
                    print("Choix invalide, suppression annulée !")
        if not trouve:
            print("Contact non trouvé !")
        # Quitter le programme:
    elif choix.upper() == "Q":
        print("Au revoir !")
        break
    else:
        print("Choix invalide ! Veuillez réessayer.")
### carnet_d-adresses_V1.py by Esc0w ###