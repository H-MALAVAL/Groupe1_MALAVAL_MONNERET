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
ligne_initiale_y = 50  # Position Y de la première ligne d'aliens
espacement_y = 50      # Espacement vertical entre les lignes d'aliens

# Fonction pour démarrer une nouvelle partie
def nouvelle_partie():
    global aliens_blancs, aliens_rouges
    aliens_blancs, aliens_rouges = [], []  # Réinitialiser les listes d'aliens
    str_score.set("SCORE : 0")

    creer_aliens_blancs_en_ligne(10)  # Créer une ligne d'aliens blancs
    creer_alien_rouge()  # Créer un alien rouge aléatoire

    mouvement_aliens_blancs()  # Démarrer le mouvement en ligne des aliens blancs
    mouvement_aliens_rouges()  # Mouvement aléatoire des aliens rouges
    tirs_aliens_rouges()  # Commencer les tirs des aliens rouges
    
    global joueur
    joueur = Joueur(canvas, x=650, y=600, score=0, vie = 3, size=30)

# Fonction pour créer une ligne d'aliens blancs
def creer_aliens_blancs_en_ligne(nombre_aliens=10, y_position=50, espacement_x=70):
    x_position = 50  # Position de départ en x pour les aliens blancs
    ligne_aliens = []

    for _ in range(nombre_aliens):
        alien_blanc = Alien(canvas, x=x_position, y=y_position, size=30, speed=5, color="white")
        ligne_aliens.append(alien_blanc)
        x_position += espacement_x

    aliens_blancs.extend(ligne_aliens)

# Fonction pour créer plusieurs aliens rouges à des positions aléatoires
def creer_aliens_rouges(nombre_rouges=5):
    for _ in range(nombre_rouges):
        x_position = random.randint(50, largeur - 50)  # Position X aléatoire
        alien_rouge = Alien(canvas, x=x_position, y=ligne_initiale_y, size=30, speed=5, color="red")
        aliens_rouges.append(alien_rouge)

# Fonction pour déplacer les aliens blancs en ligne
def mouvement_aliens_blancs():
    for alien in aliens_blancs:
        alien.move()  # Déplacer l'alien blanc
    fenetre_principale.after(42, mouvement_aliens_blancs)  # Rappel toutes les 42 ms

# Fonction pour déplacer les aliens rouges de manière aléatoire
def mouvement_aliens_rouges():
    for alien_rouge in aliens_rouges:
        dx = random.choice([-10, 10])
        dy = random.choice([-5, 5])
        alien_rouge.move_random(dx, dy)  # Déplacement aléatoire de l'alien rouge
    fenetre_principale.after(500, mouvement_aliens_rouges)  # Rappel toutes les 500 ms

# Fonction pour gérer les tirs aléatoires des aliens rouges
def tirs_aliens_rouges():
    for alien_rouge in aliens_rouges:
        if random.random() < 0.1:  # 10% de chance de tirer à chaque appel
            x, y = alien_rouge.get_position()[0], alien_rouge.get_position()[1] + alien_rouge.size
            missile = Missile(canvas, x=x, y=y, direction="down")  # Créer le missile dirigé vers le bas
            missile.move()
    fenetre_principale.after(500, tirs_aliens_rouges)  # Rappel toutes les 500 ms

"""
# Fonction pour envoyer une nouvelle ligne d'aliens toutes les 10 secondes
def envoyer_nouvelle_ligne():
    # Calculer la position verticale de la nouvelle ligne en fonction du nombre de lignes déjà créées
    y_position = ligne_initiale_y
    creer_aliens_en_ligne(10, y_position)  # Créer une nouvelle ligne d'aliens à cette position
    fenetre_principale.after(10000, envoyer_nouvelle_ligne)  # Appeler cette fonction toutes les 10 secondes

# Création des aliens rouges aléatoirement au-dessus du vaisseau
def creer_alien_aleatoire():
    x_position = random.randint(50, largeur - 50)  # Position X aléatoire entre les bords
    alien = Alien(canvas, x=x_position, y=ligne_initiale_y, size=30, speed=5, color="red")
    aliens.append(alien)

# Fonction pour tirer des missiles depuis les aliens
def tirer_missiles_aliens():
    for alien in aliens:
        if random.random() < 0.7:  # Probabilité de tirer (70% de chance par cycle)
            missile = Missile(canvas, x=alien.get_position()[0], y=alien.get_position()[1] + alien.size)
            missile.move()  # Lance le mouvement du missile
    fenetre_principale.after(300, tirer_missiles_aliens)  # Rappel toutes les 300 ms
"""

# Déplacer le vaisseau avec les touches fléchées
def keyPress(event):
    if event.keysym == 'Up':
        joueur.deplacer(0, -10)
    elif event.keysym == 'Down':
        joueur.deplacer(0, 10)
    elif event.keysym == 'Left':
        joueur.deplacer(-10, 0)
    elif event.keysym == 'Right':
        joueur.deplacer(10, 0)


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
