from tkinter import Tk, Label, Button, Canvas, Menu, StringVar, Toplevel, messagebox
from classes.Aliens import Alien
from classes.Joueur import Joueur

# Définition des variables globales
largeur = 1200
hauteur = 700

# Fonction pour démarrer une nouvelle partie
def nouvelle_partie():
    str_score.set("SCORE : 0")
    global joueur
    global alien
    creer_aliens_en_ligne(10)  # Créer 10 aliens en ligne
    mouvement_alien()
    
    joueur = Joueur(canvas, x=650, y=600, score=0, vie = 3, size=30)


# Liste pour stocker les aliens
aliens = []

# Fonction pour créer plusieurs aliens en ligne
def creer_aliens_en_ligne(nombre_aliens, y_position=50, espacement=130):
    global aliens
    aliens = []  # Réinitialise la liste des aliens
    x_position = 50  # Position de départ en x
    
    for i in range(nombre_aliens):
        # Créer un nouvel alien et le placer sur la ligne
        alien = Alien(canvas, x=x_position, y=y_position, size=30, speed=5)
        aliens.append(alien)
        
        # Mettre à jour la position x pour le prochain alien en ajoutant l'espacement
        x_position += espacement

# Fonction pour déplacer l'alien en continu
def mouvement_alien():
    for alien in aliens:
        alien.move()  # Déplacer l'alien
    fenetre_principale.after(42, mouvement_alien)  # Appeler cette fonction toutes les 50 ms
    
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
canvas = Canvas(fenetre_principale, width=largeur, height=hauteur, bg="green")
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
