# MALAVAL Hugo, MONNERET Martin le 15/11/2024

# Création du fichier SpaceInvader

import random
from tkinter import Tk, Label, Button, Canvas, Menu, StringVar, Toplevel, messagebox
from classes.Aliens import Alien
from classes.Joueur import Joueur
from classes.Missiles import Missile
from classes.Murs import Murs

class SpaceInvader:
    def __init__(self):
        # Dimensions du jeu
        self.largeur = 1200
        self.hauteur = 700

        # Données du jeu
        self.aliens_blancs = []
        self.aliens_rouges = []
        self.alien_bonus = []
        self.missiles_aliens = []
        self.missiles_joueur = []
        self.liste_murs = []
        self.joueur = None

        # Interface utilisateur
        self.fenetre_principale = Tk()
        self.fenetre_principale.title("Space Invaders")
        self.fenetre_principale.minsize(self.largeur + 150, self.hauteur + 50)
        self.canvas = Canvas(self.fenetre_principale, width=self.largeur, height=self.hauteur, bg="black")
        self.canvas.pack()

        # Variables globales
        self.str_score = StringVar()
        self.str_vies = StringVar()
        self.canvas_reduit = False
        self.dernier_score_reduit = 0

        # Ligne initiale et espacement
        self.ligne_initiale_y = 50
        self.espacement_y = 50

        # Dessiner le logo Space Invaders
        self.dessiner_logo_texte(150, 300, taille_pixel=15, couleurs=None)

        # Initialisation de l'interface
        self._setup_ui()

    def dessiner_logo_texte(self, x=150, y=300, taille_pixel=15, couleurs=None):
        """
        Dessine un texte "SPACE INVADERS" sous forme de matrice pixelisée, centré horizontalement si x est None, avec des couleurs variées.

        :param x: Position X du coin supérieur gauche du texte. Si None, le texte est centré.
        :param y: Position Y du coin supérieur gauche du texte.
        :param taille_pixel: Taille d'un pixel dans la matrice.
        :param couleurs: Liste ou dictionnaire de couleurs pour chaque lettre.
        
        Ecrit les lettres dans des matrices, choisi les couleurs pour chaque lettre,
        défini la taille du logo, centre le logo
        
        Renvoie le logo SPACE INVADERS centré sur la page d'accueil
        """
        # Matrice représentant chaque lettre (1 = pixel rempli, 0 = vide)
        lettres = {
            'S': [
                [1, 1, 1, 1],
                [1, 0, 0, 0],
                [1, 1, 1, 1],
                [0, 0, 0, 1],
                [1, 1, 1, 1]
            ],
            'P': [
                [1, 1, 1],
                [1, 0, 1],
                [1, 1, 1],
                [1, 0, 0],
                [1, 0, 0]
            ],
            'A': [
                [0, 1, 1, 0],
                [1, 0, 0, 1],
                [1, 1, 1, 1],
                [1, 0, 0, 1],
                [1, 0, 0, 1]
            ],
            'C': [
                [0, 1, 1, 1],
                [1, 0, 0, 0],
                [1, 0, 0, 0],
                [1, 0, 0, 0],
                [0, 1, 1, 1]
            ],
            'E': [
                [1, 1, 1, 1],
                [1, 0, 0, 0],
                [1, 1, 1, 1],
                [1, 0, 0, 0],
                [1, 1, 1, 1]
            ],
            ' ': [
                [0, 0],
                [0, 0],
                [0, 0],
                [0, 0],
                [0, 0]
            ],
            'I': [
                [1],
                [1],
                [1],
                [1],
                [1]
            ],
            'N': [
                [1, 0, 0, 1],
                [1, 1, 0, 1],
                [1, 0, 1, 1],
                [1, 0, 0, 1],
                [1, 0, 0, 1]
            ],
            'V': [
                [1, 0, 0, 1],
                [1, 0, 0, 1],
                [1, 0, 0, 1],
                [0, 1, 1, 0],
                [0, 1, 1, 0]
            ],
            'D': [
                [1, 1, 1],
                [1, 0, 1],
                [1, 0, 1],
                [1, 0, 1],
                [1, 1, 1]
            ],
            'R': [
                [1, 1, 1],
                [1, 0, 1],
                [1, 1, 1],
                [1, 1, 0],
                [1, 0, 1]
            ]
        }

        # Texte à dessiner
        texte = "SPACE INVADERS"

        # Définir les couleurs si elles ne sont pas fournies
        if couleurs is None:
            # Couleurs par défaut : arc-en-ciel (red, orange, yellow, green, cyan, blue, purple)
            couleurs = ["red", "orange", "yellow", "green", "cyan", "blue", "purple"]

        # Si c'est une liste, boucle en répétant les couleurs
        if isinstance(couleurs, list):
            couleur_par_lettre = {lettre: couleurs[i % len(couleurs)] for i, lettre in enumerate(texte)}
        else:
            # Sinon, utiliser le dictionnaire directement
            couleur_par_lettre = couleurs

        # Calculer la largeur totale en pixels du texte
        largeur_totale = 0
        for lettre in texte:
            if lettre in lettres:
                largeur_totale += len(lettres[lettre][0]) * taille_pixel
            largeur_totale += taille_pixel  # Ajouter un espace entre les lettres

        # Si x n'est pas fourni, centrer le texte horizontalement
        if x is None:
            x = (self.largeur - largeur_totale) // 2

        # Dessiner chaque lettre
        x_courant = x
        y_courant = y

        for lettre in texte:
            if lettre in lettres:
                couleur = couleur_par_lettre.get(lettre, "white")  # Couleur par défaut : blanc
                # Dessiner chaque pixel de la lettre
                for i, ligne in enumerate(lettres[lettre]):
                    for j, pixel in enumerate(ligne):
                        if pixel == 1:
                            x1 = x_courant + j * taille_pixel
                            y1 = y_courant + i * taille_pixel
                            x2 = x1 + taille_pixel
                            y2 = y1 + taille_pixel
                            self.canvas.create_rectangle(x1, y1, x2, y2, fill=couleur, outline="")
                # Ajouter un espacement horizontal après chaque lettre
                x_courant += (len(lettres[lettre][0]) + 1) * taille_pixel


    def _setup_ui(self):
        """Configure la page d'accueil:
        Le score, nombre de vies, boutons du haut, règles du jeu"""
        # Score
        self.str_score.set("SCORE : 0")
        score_label = Label(self.fenetre_principale, textvariable=self.str_score, fg="darkblue", font=("Arial", 14))
        score_label.place(x=0, y=0)

        # Vies restantes
        self.str_vies.set("Vie restante : 3")
        vies_label = Label(self.fenetre_principale, textvariable=self.str_vies, fg="darkblue", font=("Arial", 14))
        vies_label.place(x=0, y=27)

        # Boutons
        bouton_go = Button(self.fenetre_principale, text="Nouvelle Partie", command=self.nouvelle_partie)
        bouton_go.pack(side="bottom", fill="both", padx=5, pady=5)
        bouton_quitter = Button(self.fenetre_principale, text="Quitter", command=self.fenetre_principale.destroy)
        bouton_quitter.pack(side="bottom", fill="both", padx=5, pady=5)

        # Menu
        menubar = Menu(self.fenetre_principale)
        menu_fichier = Menu(menubar, tearoff=0)
        menu_fichier.add_command(label="Nouvelle Partie", command=self.nouvelle_partie)
        menu_fichier.add_command(label="Quitter", command=self.fenetre_principale.destroy)
        menubar.add_cascade(label="Menu", menu=menu_fichier)

        menu_aide = Menu(menubar, tearoff=0)
        menu_aide.add_command(label="Règles du jeu", command=self.afficher_regles)
        menu_aide.add_command(label="À propos", command=self.afficher_a_propos)
        menubar.add_cascade(label="Aide", menu=menu_aide)

        self.fenetre_principale.config(menu=menubar)

    def nouvelle_partie(self):
        """Démarre une nouvelle partie.
        Réinitialise le score, nb de vies à 3
        Créé le joueur, les murs, les aliens... pour que la partie puisse commencer"""
        self.canvas.bind_all('<KeyPress>', self.Clavier)
        self.canvas.delete("all")
        self.aliens_blancs = []
        self.aliens_rouges = []
        self.missiles_aliens = []
        self.missiles_joueur = []
        self.liste_murs = []

        self.str_score.set("SCORE : 0")
        self.str_vies.set("Vie restante : 3")
        
        self.joueur = Joueur(self.canvas, x=650, y=650, size=30, score=0, vie=3,
                             update_vie_callback=self.mettre_a_jour_vies_interface,
                             update_score_callback=self.mettre_a_jour_score_interface)
        
        self.creer_murs(4)
        self.creer_aliens_blancs_en_ligne(0)
        self.creer_alien_rouge(5)
        self.creer_alien_bonus(1)
        
        self.mouvement_aliens_blancs()
        self.mouvement_aliens_rouges()
        self.mouvement_alien_bonus()

        self.tirs_aliens_rouges()
        self.tirs_aliens_bonus()
        
        self.mettre_a_jour_cibles_rouges()
        self.verifier_aliens_rouges()
        
        self.envoyer_nouvelle_ligne()

        self.verifier_collisions()


    def Clavier(self, event):
        """Gère les interactions clavier pour déplacer le joueur ou tirer.
        Met à jour automatiquement la position du joueur"""
        touche = event.keysym
        if touche == 'a':  # Déplacer à gauche
            self.joueur.deplacer(-10)
        elif touche == 'z':  # Déplacer à droite
            self.joueur.deplacer(10)
        elif touche == 'space':  # Tirer
            self.tirs_joueurs()

        # Met à jour la position visuelle du joueur sur le canevas
        self.canvas.coords(self.joueur.id, self.joueur.x - 10, 600, self.joueur.x + 10, 630)



    def creer_murs(self, nombre):
        """Crée des murs protecteurs.
        Prends en entrée le nombre de murs"""
        x_position = 50
        for _ in range(nombre):
            y_position = 500
            mur = Murs(self.canvas, x=x_position, y=y_position, size=30, color="white")
            self.liste_murs.append(mur)
            x_position += 330

    def creer_aliens_blancs_en_ligne(self, nombre, y_position=500, espacement_x=70):
        """Crée une ligne d'aliens blancs.
        Prends en entrée le nombre d'aliens, leur position de départ et l'espacement entre eux"""
        x_position = 50
        for _ in range(nombre):
            alien = Alien(self.canvas, x=x_position, y=y_position, size=30, speed=5, color="white")
            self.aliens_blancs.append(alien)
            x_position += espacement_x

    
    def creer_alien_rouge(self, nombre):
        """Crée des aliens rouges à des positions aléatoires.
        Prends en entrée le nombre d'aliens"""
        for _ in range(nombre):
            x_position = random.randint(50, self.largeur - 50)
            alien = Alien(self.canvas, x=x_position, y=self.ligne_initiale_y, size=30, speed=7, color="red")
            self.aliens_rouges.append(alien)

    def creer_alien_bonus(self, nombre):
        """Crée des aliens bonus à des positions aléatoires."""
        for _ in range(nombre):
            x_position = random.randint(50, self.largeur - 50)
            alien = Alien(self.canvas, x=x_position, y=self.ligne_initiale_y, size=90, speed=15, color="purple")
            self.alien_bonus.append(alien)



    def mouvement_aliens_blancs(self):
        """Gère le déplacement des aliens blancs."""
        for alien in self.aliens_blancs:
            alien.move()
        self.fenetre_principale.after(42, self.mouvement_aliens_blancs)

    def mouvement_aliens_rouges(self):
        """Gère le déplacement des aliens rouges."""
        for alien in self.aliens_rouges:
            alien.move_towards_target()
        self.fenetre_principale.after(42, self.mouvement_aliens_rouges)

    def mouvement_alien_bonus(self):
        """Gère le déplacement des aliens bonus."""
        for alien in self.alien_bonus:
            alien.move()
        self.fenetre_principale.after(42, self.mouvement_alien_bonus)

    def envoyer_nouvelle_ligne(self):
        """Envoie une nouvelle ligne d'aliens blancs toutes les 10 secondes."""
        y_position = self.ligne_initiale_y
        self.creer_aliens_blancs_en_ligne(10, y_position=y_position)
        self.fenetre_principale.after(10000, self.envoyer_nouvelle_ligne)  # Ajoute une ligne toutes les 10 secondes

    def verifier_aliens_rouges(self):
        """Vérifie le nombre d'aliens rouges et en ajoute si nécessaire."""
        if len(self.aliens_rouges) <= 2:  # Seuil minimum d'aliens rouges
            self.creer_alien_rouge(5)
        self.fenetre_principale.after(1000, self.verifier_aliens_rouges)

    def mettre_a_jour_cibles_rouges(self):
        """Met à jour les cibles des aliens rouges pour qu'ils aient de nouveaux objectifs."""
        for alien in self.aliens_rouges:
            if alien.alien_id:  # Vérifie que l'alien est actif
                alien.set_new_target()
        self.fenetre_principale.after(5000, self.mettre_a_jour_cibles_rouges)  # Mise à jour toutes les 5 secondes

    def mettre_a_jour_cibles_bonus(self):
        """Met à jour les cibles de l'alien bonus pour qu'il ait de nouveaux objectifs."""
        for alien in self.alien_bonus:
            if alien.alien_id:  # Vérifie que l'alien est actif
                alien.set_new_target()
        self.fenetre_principale.after(5000, self.mettre_a_jour_cibles_bonus)  # Mise à jour toutes les 5 secondes


    def tirs_aliens_rouges(self):
        """Gère les tirs des aliens rouges."""
        for alien in self.aliens_rouges:
            if random.random() < 0.5:
                x, y = alien.get_position()
                missile = Missile(self.canvas, x=x, y=y + alien.size, direction="down", color="red")
                self.missiles_aliens.append(missile)
                missile.move()
        self.fenetre_principale.after(500, self.tirs_aliens_rouges)

    def tirs_aliens_bonus(self):
        """Gère les tirs des aliens bonus."""
        for alien in self.alien_bonus:
            if random.random() < 0.9:
                x, y = alien.get_position()
                missile = Missile(self.canvas, x=x, y=y + alien.size, direction="down", color="purple")
                self.missiles_aliens.append(missile)
                missile.move()
        self.fenetre_principale.after(500, self.tirs_aliens_bonus)

    def tirs_joueurs(self):
        """Permet au joueur de tirer un missile."""
        x, y = self.joueur.x, self.joueur.y
        missile = Missile(self.canvas, x=x, y=y - self.joueur.size, direction="up", color="blue")
        self.missiles_joueur.append(missile)
        missile.move()

    def verifier_collisions(self):
        """Gère les collisions entre les objets."""
        # Collisions des missiles du joueur
        for missile in self.missiles_joueur[:]:
            missile_coords = self.canvas.coords(missile.missile_id)
            if len(missile_coords) != 4:
                continue  # Ignorer les missiles sans coordonnées valides
            m_x1, m_y1, m_x2, m_y2 = missile_coords

            # Vérification des collisions avec les aliens blancs
            for alien in self.aliens_blancs[:]:
                alien_coords = self.canvas.coords(alien.alien_id)
                if len(alien_coords) != 4:
                    continue  # Ignorer les aliens sans coordonnées valides
                a_x1, a_y1, a_x2, a_y2 = alien_coords

                # Vérification géométrique
                if m_x2 > a_x1 and m_x1 < a_x2 and m_y2 > a_y1 and m_y1 < a_y2:
                    # Collision détectée
                    points = self.attribuer_points_alien("white")
                    self.joueur.ajouter_score(points)
                    self.mettre_a_jour_score_interface(self.joueur.score)
                    alien.delete()
                    self.aliens_blancs.remove(alien)
                    if missile in self.missiles_joueur:
                        missile.delete()
                        self.missiles_joueur.remove(missile)
                    break
            
            # Vérification des collisions avec les aliens rouges
            for alien in self.aliens_rouges[:]:
                alien_coords = self.canvas.coords(alien.alien_id)
                if len(alien_coords) != 4:
                    continue
                a_x1, a_y1, a_x2, a_y2 = alien_coords

                # Vérification géométrique
                if m_x2 > a_x1 and m_x1 < a_x2 and m_y2 > a_y1 and m_y1 < a_y2:
                    # Collision détectée
                    points = self.attribuer_points_alien("red")
                    self.joueur.ajouter_score(points)
                    self.mettre_a_jour_score_interface(self.joueur.score)
                    alien.delete()
                    self.aliens_rouges.remove(alien)
                    if missile in self.missiles_joueur:
                        missile.delete()
                        self.missiles_joueur.remove(missile)
                    break
                
            # Vérification des collisions avec l'alien bonus
            for alien in self.alien_bonus[:]:
                alien_coords = self.canvas.coords(alien.alien_id)
                if len(alien_coords) != 4:
                    continue
                a_x1, a_y1, a_x2, a_y2 = alien_coords

                # Vérification géométrique
                i = 0
                if m_x2 > a_x1 and m_x1 < a_x2 and m_y2 > a_y1 and m_y1 < a_y2:
                    # Collision détectée
                    i += 1
                    if i == 10: 
                        alien.delete()
                        self.alien_bonus.remove(alien)
                        if missile in self.missiles_joueur:
                            missile.delete()
                            self.missiles_joueur.remove(missile)
                        break

            # Vérification des collisions avec les murs 
            for murs in self.liste_murs[:]:
                if murs.murs_id is None:
                    continue  # Passer les murs supprimés ou non valides
                
                murs_coords = self.canvas.coords(murs.murs_id)
                if len(murs_coords) != 4:
                    continue
                a_x1, a_y1, a_x2, a_y2 = murs_coords
                
                # Vérification géométrique
                if m_x2 > a_x1 and m_x1 < a_x2 and m_y2 > a_y1 and m_y1 < a_y2:
                    # Collision détectée
                    murs.subir_collision()
                    if missile in self.missiles_joueur:
                        missile.delete()
                        self.missiles_joueur.remove(missile)
                    break
                

        # Collisions des missiles aliens
        for missile in self.missiles_aliens[:]:
            missile_coords = self.canvas.coords(missile.missile_id)
            if len(missile_coords) != 4:
                continue
            m_x1, m_y1, m_x2, m_y2 = missile_coords 

            # Collision avec le joueur
            joueur_coords = self.canvas.coords(self.joueur.id)
            if len(joueur_coords) == 4:
                j_x1, j_y1, j_x2, j_y2 = joueur_coords
                if m_x2 > j_x1 and m_x1 < j_x2 and m_y2 > j_y1 and m_y1 < j_y2:
                    print("Collision avec Joueur")
                    self.joueur.perdre_vie()
                    if missile in self.missiles_aliens:
                        missile.delete()
                        self.missiles_aliens.remove(missile)
                    continue

            # Vérification des collisions avec les murs 
            for murs in self.liste_murs[:]:
                if murs.murs_id is None:
                    continue  # Passer les murs supprimés ou non valides

                murs_coords = self.canvas.coords(murs.murs_id)
                if len(murs_coords) != 4:
                    continue
                a_x1, a_y1, a_x2, a_y2 = murs_coords
                
                # Vérification géométrique
                if m_x2 > a_x1 and m_x1 < a_x2 and m_y2 > a_y1 and m_y1 < a_y2:
                    # Collision détectée
                    murs.subir_collision()
                    if missile in self.missiles_aliens:
                        missile.delete()
                        self.missiles_aliens.remove(missile)
                    break

        # Collision entre les aliens blancs et le joueur
        for alien in self.aliens_blancs[:]:
            alien_coords = self.canvas.coords(alien.alien_id)
            if len(alien_coords) != 4:
                continue  # Ignorer les aliens sans coordonnées valides
            a_x1, a_y1, a_x2, a_y2 = alien_coords

            joueur_coords = self.canvas.coords(self.joueur.id)
            if len(joueur_coords) == 4:  # Vérifie que le joueur est actif
                j_x1, j_y1, j_x2, j_y2 = joueur_coords

                # Vérification géométrique de la collision
                if a_x2 > j_x1 and a_x1 < j_x2 and a_y2 > j_y1 and a_y1 < j_y2:
                    # Collision détectée
                    alien.delete()  # Supprimer l'alien du canvas
                    self.aliens_blancs.remove(alien)  # Retirer l'alien de la liste
                    self.joueur.perdre_vie()  # Réduire la vie du joueur
                    self.mettre_a_jour_vies_interface(self.joueur.vie)  # Mettre à jour l'affichage des vies
                    break

        self.fenetre_principale.after(50, self.verifier_collisions)


    def attribuer_points_alien(self, couleur_alien):
        """Attribue des points en fonction de la couleur de l'alien touché.
        Prends en entrée la couleur de l'alien."""
        points_par_couleur = {
            "white": 10,
            "red": 25,
            "purple": 150}
        return points_par_couleur.get(couleur_alien, 0)
    
    def mettre_a_jour_vies_interface(self, vies_restantes):
        """Met à jour l'interface des vies restantes.
        Prends en entrée le nombre de vies restantes"""
        self.str_vies.set(f"Vie restante : {vies_restantes}")
        if vies_restantes <= 0:
            self.game_over()

    def mettre_a_jour_score_interface(self, nouveau_score):
        """Met à jour l'interface du score.
        Prends en entrée le nouveau score"""
        self.str_score.set(f"SCORE : {nouveau_score}")

        
        # Réduction du canevas si le score atteint un palier (100 points)
        if nouveau_score >= 500 and nouveau_score % 100 == 0 and not self.canvas_reduit and (nouveau_score - self.dernier_score_reduit >= 100):
            self.reduire_canvas(self.canvas, largeur_reduction=100, hauteur_reduction=50)
            self.canvas_reduit = True
            self.dernier_score_reduit = nouveau_score
            self.joueur.ajuster_position()

        # Réinitialise la réduction du canevas après le palier
        if nouveau_score % 100 != 0:
            self.canvas_reduit = False

        # Vérifie si le score permet de gagner
        if nouveau_score >= 1000:
            self.gagne()
    
    def reduire_canvas(self, canvas, largeur_reduction, hauteur_reduction):
        """Réduit la taille du canevas en fonction du score.
        Prends en entrée le canvas, la largeur de réduction et la hauteur de réduction"""
        largeur_actuelle = canvas.winfo_width()
        hauteur_actuelle = canvas.winfo_height()

        nouvelle_largeur = max(largeur_actuelle - largeur_reduction, 400)  # Largeur minimale
        nouvelle_hauteur = max(hauteur_actuelle - hauteur_reduction, 300)  # Hauteur minimale

        canvas.config(width=nouvelle_largeur, height=nouvelle_hauteur)

        # Ajuste les objets existants pour qu'ils restent dans les limites
        for obj_id in canvas.find_all():
            x1, y1, x2, y2 = canvas.coords(obj_id)
            if x2 > nouvelle_largeur:
                canvas.move(obj_id, nouvelle_largeur - x2, 0)
            if y2 > nouvelle_hauteur:
                canvas.move(obj_id, 0, nouvelle_hauteur - y2)

        # Ajuste la position du joueur après la réduction
        self.joueur.ajuster_position()

    def gagne(self):
        """Affiche un message de victoire et arrête les animations."""
        messagebox.showinfo("Félicitations", "Vous avez gagné ! Merci d'avoir joué.")
        self.fenetre_principale.destroy()

    def game_over(self):
        """Affiche un message de fin de jeu et arrête les animations."""
        messagebox.showinfo("Game Over", "Vous avez perdu ! Merci d'avoir joué.")
        self.fenetre_principale.destroy()


    def afficher_regles(self):
        """Affiche les règles du jeu."""
        messagebox.showinfo("Règles", "Règles du jeu:\n1. Déplacez votre vaisseau avec les touches.\n2. Tirez sur les aliens.\n3. Ne vous faites pas toucher.")

    def afficher_a_propos(self):
        """Affiche des informations sur le jeu."""
        messagebox.showinfo("À propos", "Space Invaders - Créé par Martin MONNERET et Hugo MALAVAL.")

    def run(self):
        """Lance le jeu."""
        self.fenetre_principale.mainloop()