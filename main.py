# MALAVAL Hugo, MONNERET Martin le 15/11/2024

# Création du fichier main

import random
from tkinter import Tk, Label, Button, Canvas, Menu, StringVar, Toplevel, messagebox
from classes.Aliens import Alien
from classes.Joueur import Joueur
from classes.Missiles import Missile

# Définition des variables globales
largeur = 1200
hauteur = 700

# Liste pour stocker les objets Alien
aliens_blancs = []
aliens_rouges = []
missiles_aliens = []
missiles_joueur = []

ligne_initiale_y = 50  # Position Y de la première ligne d'aliens
espacement_y = 50      # Espacement vertical entre les lignes d'aliens

# Fonction pour démarrer une nouvelle partie
def nouvelle_partie():
    global aliens_blancs, aliens_rouges, missiles_aliens, missiles_joueur, joueur
    # Réinitialiser les objets
    for alien in aliens_blancs + aliens_rouges:
        alien.delete()
    for missile in missiles_aliens + missiles_joueur:
        missile.delete()
    aliens_blancs, aliens_rouges = [], []
    missiles_aliens, missiles_joueur = [], []

    str_score.set("SCORE : 0")
    creer_aliens_blancs_en_ligne(10)  # Créer une ligne d'aliens blancs
    creer_alien_rouge(5)  # Créer des aliens rouge aléatoire

    mouvement_aliens_blancs()
    mouvement_aliens_rouges()
    tirs_aliens_rouges()
    mettre_a_jour_cibles_rouges()

    envoyer_nouvelle_ligne()
    

    # Réinitialiser le joueur
    joueur = Joueur(canvas, x=650, y=600, score=0, vie=3, size=30)
    
    verifier_collisions()
    

# Fonction pour créer une ligne d'aliens blancs
def creer_aliens_blancs_en_ligne(nombre_aliens=10, y_position=50, espacement_x=70):
    x_position = 50  # Position de départ en x pour les aliens blancs
    ligne_aliens = []
    for _ in range(nombre_aliens):
        alien_blanc = Alien(canvas, x=x_position, y=y_position, size=30, speed=5, color="white")
        ligne_aliens.append(alien_blanc)
        x_position += espacement_x

    aliens_blancs.extend(ligne_aliens)

# Fonction pour créer un alien rouge aléatoire
def creer_alien_rouge(nombre):
    for _ in range(nombre):
        x_position = random.randint(50, largeur - 50)
        alien_rouge = Alien(canvas, x=x_position, y=ligne_initiale_y, size=30, speed=5, color="red")
        aliens_rouges.append(alien_rouge)

# Fonction pour déplacer les aliens blancs en ligne
def mouvement_aliens_blancs():
    for alien in aliens_blancs:
        alien.move()  # Déplacer l'alien blanc
    fenetre_principale.after(42, mouvement_aliens_blancs)  # Rappel toutes les 42 ms

# Fonction pour envoyer une nouvelle ligne d'aliens toutes les 10 secondes
def envoyer_nouvelle_ligne():
    # Calculer la position verticale de la nouvelle ligne en fonction du nombre de lignes déjà créées
    y_position = ligne_initiale_y
    creer_aliens_blancs_en_ligne(10, y_position)  # Créer une nouvelle ligne d'aliens à cette position
    fenetre_principale.after(10000, envoyer_nouvelle_ligne)  # Appeler cette fonction toutes les 10 secondes

# Cibles pour les aliens rouges
def mettre_a_jour_cibles_rouges():
    for alien_rouge in aliens_rouges:
        alien_rouge.set_new_target()
    fenetre_principale.after(5000, mettre_a_jour_cibles_rouges)  # Rappel toutes les 7 secondes

# Fonction pour déplacer les aliens rouges
def mouvement_aliens_rouges():
    for alien_rouge in aliens_rouges:
        alien_rouge.move_towards_target()
    fenetre_principale.after(42, mouvement_aliens_rouges)  # Rappel toutes les 42 ms


# Gestion des tirs des aliens rouges
def tirs_aliens_rouges():
    for alien_rouge in aliens_rouges:
        if random.random() < 0.5:  # 50% de chance de tirer
            x, y = alien_rouge.get_position()
            missile = Missile(canvas, x=x, y=y + alien_rouge.size, direction="down")
            missiles_aliens.append(missile)
            missile.move()
    fenetre_principale.after(500, tirs_aliens_rouges)

# Fonction pour vérifier les collisions
def verifier_collisions():
    # Collisions des missiles du joueur
    for missile in missiles_joueur[:]:
        missile_coords = canvas.coords(missile.missile_id)
        items = canvas.find_overlapping(*missile_coords)

        for item in items:
            if item == missile.missile_id:
                continue

            # Collision avec un alien blanc
            for alien in aliens_blancs[:]:
                if alien.alien_id == item:
                    alien.delete()
                    aliens_blancs.remove(alien)
                    missile.delete()
                    missiles_joueur.remove(missile)
                    break

            # Collision avec un alien rouge
            for alien in aliens_rouges[:]:
                if alien.alien_id == item:
                    alien.delete()
                    aliens_rouges.remove(alien)
                    missile.delete()
                    missiles_joueur.remove(missile)
                    break

    # Collisions des missiles aliens
    for missile in missiles_aliens[:]:
        missile_coords = canvas.coords(missile.missile_id)
        items = canvas.find_overlapping(*missile_coords)

        for item in items:
            if item == missile.missile_id:
                continue

            # Collision avec le joueur
            if joueur.id == item:
                joueur.perdre_vie()
                missile.delete()
                missiles_aliens.remove(missile)
                break

            # Collision avec un autre alien blanc
            for alien in aliens_blancs[:]:
                if alien.alien_id == item:
                    alien.delete()
                    aliens_blancs.remove(alien)
                    missile.delete()
                    missiles_aliens.remove(missile)
                    break

            # Collision avec un autre alien rouge
            for alien in aliens_rouges[:]:
                if alien.alien_id == item:
                    alien.delete()
                    aliens_rouges.remove(alien)
                    missile.delete()
                    missiles_aliens.remove(missile)
                    break

    # Répéter la vérification périodiquement
    fenetre_principale.after(50, verifier_collisions)

# Fonction pour afficher les règles du jeu
def afficher_regles():
    messagebox.showinfo("Règles du jeu", "Les règles du jeu Space Invaders sont simples :\n"
                                         "1. Déplacez votre vaisseau avec les touches.\n"
                                         "2. Tirez sur les aliens pour les éliminer.\n"
                                         "3. Évitez que les aliens atteignent votre vaisseau.")

# Fonction pour afficher des informations "À propos"
def afficher_a_propos():
    messagebox.showinfo("À propos", "Space Invaders - Créé par Martin MONNERET et Hugo MALAVAL.\n"
                                    "Un jeu rétro qui vous rappelera votre enfance.")

# Fonction pour sélectionner la difficulté
def changer_difficulte():
    difficulte_fenetre = Toplevel(fenetre_principale)
    difficulte_fenetre.title("Choisir la difficulté")
    Label(difficulte_fenetre, text="Sélectionnez un niveau de difficulté :").pack(pady=10)
    Button(difficulte_fenetre, text="Facile", command=lambda: definir_difficulte("Facile")).pack(fill="x")
    Button(difficulte_fenetre, text="Moyen", command=lambda: definir_difficulte("Moyen")).pack(fill="x")
    Button(difficulte_fenetre, text="Difficile", command=lambda: definir_difficulte("Difficile")).pack(fill="x")

def definir_difficulte(niveau):
    print(f"Difficulté sélectionnée : {niveau}")  # Ou toute autre action pour paramétrer la difficulté
    messagebox.showinfo("Difficulté", f"Niveau de difficulté réglé sur : {niveau}")

# Création de la fenêtre principale
fenetre_principale = Tk()
fenetre_principale.minsize(largeur + 150, hauteur + 50)
fenetre_principale.title("Space Invaders")

# Création d'un canevas pour dessiner les éléments du jeu
canvas = Canvas(fenetre_principale, width=largeur, height=hauteur, bg="black")
canvas.pack(pady=20)

# Création d'une zone de texte pour afficher le score actuel
str_score = StringVar()
str_score.set("SCORE : 0")
score_label = Label(fenetre_principale, textvariable=str_score, fg="darkblue", font=("Arial", 14))
score_label.pack(side='left', padx=10)

# Création d'un widget Button pour démarrer une nouvelle partie
bouton_go = Button(fenetre_principale, text="New Game", fg='white', bg="purple", command=nouvelle_partie)
bouton_go.pack(side='bottom', fill="both", padx=5, pady=5)

# Création d'un widget Button pour quitter l'application
bouton_quitter = Button(fenetre_principale, text="Quit", bg='black', fg="white", command=fenetre_principale.destroy)
bouton_quitter.pack(side='bottom', fill="both", padx=5, pady=5)

# Création d'un menu principal avec options
menubar = Menu(fenetre_principale)

# Menu Fichier
menu_fichier = Menu(menubar, tearoff=0, bg='pink')
menu_fichier.add_command(label="Nouvelle Partie", command=nouvelle_partie)
menu_fichier.add_command(label="Quitter", command=fenetre_principale.destroy)
menubar.add_cascade(label="Menu", menu=menu_fichier)

# Menu pour l'aide
menu_aide = Menu(menubar, tearoff=0)
menu_aide.add_command(label="Règles du jeu", command=afficher_regles)
menu_aide.add_command(label="À propos", command=afficher_a_propos)
menubar.add_cascade(label="Aide", menu=menu_aide)

# Menu pour la difficulté
menu_difficulte = Menu(menubar, tearoff=0)
menu_difficulte.add_command(label="Changer la difficulté", command=changer_difficulte)
menubar.add_cascade(label="Difficulté", menu=menu_difficulte)

# Affichage du menu
fenetre_principale.config(menu=menubar)
# Lancement de la boucle principale de l'interface
fenetre_principale.mainloop()