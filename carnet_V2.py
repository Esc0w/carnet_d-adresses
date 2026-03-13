# import
import json

# Nom du fichier où les contacts seront sauvegardés
FICHIER = "contacts.json"

# Chargement des contacts depuis le fichier
def charger_contacts():
    """Lit le fichier JSON et retourne la liste des contacts."""
    try:
        with open(FICHIER, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []


# Sauvegarde des contacts dans le fichier
def sauvegarder_contacts(contacts):
    """Écrit la liste des contacts dans le fichier JSON."""
    with open(FICHIER, "w") as f:
        json.dump(contacts, f)

# Affichage des contacts
def afficher_contacts(contacts):
    """Affiche la liste des contacts et leurs détails."""

# Recherche d'un contact
def rechercher_contact(contacts):
    """Permet à l'utilisateur de rechercher un contact par nom et prénom."""

# Ajout d'un contact
def ajouter_contact(contacts):
    """Permet à l'utilisateur d'ajouter un nouveau contact."""

# Modification d'un contact
def modifier_contact(contacts):
    """Permet à l'utilisateur de modifier les informations d'un contact existant."""

# Suppression d'un contact
def supprimer_contact(contacts):
    """Permet à l'utilisateur de supprimer un contact."""

# Affichage du menu et gestion des choix de l'utilisateur
def menu():
    """Affiche le menu et traite les choix de l'utilisateur."""

###