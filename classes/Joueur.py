# MALAVAL Hugo, MONNERET Martin le 4/11/2024 
from tkinter import Tk, Label, Button, Canvas, Menu, StringVar, Toplevel, messagebox, PhotoImage

# Création de la class joueur
class Joueur:
    # Composée de l'apparence du joueur, du score du joueur et de ses points de vie
    def __init__(self, canvas, x, y, size, score, vie, update_vie_callback, update_score_callback):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.size = size
        self.score = score
        self.vie = vie
        self.update_vie_callback = update_vie_callback
        self.update_score_callback = update_score_callback
        self.id = canvas.create_rectangle(
            self.x - self.size // 2, self.y - self.size // 2,
            self.x + self.size // 2, self.y + self.size // 2,
            fill="blue"
        )
        
        self.invincible = False  # Indique si le joueur est temporairement invincible
        self.clignotement_actif = False  # Pour gérer le clignotement

        # Appeler le callback pour synchroniser l'interface au démarrage
        if self.update_vie_callback:
            self.update_vie_callback(self.vie)
        if self.update_score_callback:
            self.update_score_callback(self.score)
                
    def deplacer(self, dx):
        largeur = 1200
        self.x += dx
        if self.x - self.size // 2 < 0:  # Limite gauche
            self.x = self.size // 2
        if self.x + self.size // 2 > largeur:  # Limite droite
            self.x = largeur - self.size // 2

        # Met à jour la position graphique
        self.canvas.coords(
            self.id,
            self.x - self.size // 2, self.y - self.size // 2,
            self.x + self.size // 2, self.y + self.size // 2
        )
        self.ajuster_position()
    
    def ajuster_position(self):
        """
        Ajuste la position du joueur pour qu'il reste dans les nouvelles limites du Canvas.
        """
        largeur_canvas = self.canvas.winfo_width()
        hauteur_canvas = self.canvas.winfo_height()

        # Vérifie et ajuste les coordonnées
        if self.x - self.size // 2 < 0:
            self.x = self.size // 2
        elif self.x + self.size // 2 > largeur_canvas:
            self.x = largeur_canvas - self.size // 2

        if self.y - self.size // 2 < 0:
            self.y = self.size // 2
        elif self.y + self.size // 2 > hauteur_canvas:
            self.y = hauteur_canvas - self.size // 2

        # Applique les nouvelles coordonnées
        self.canvas.coords(
            self.id,
            self.x - self.size // 2, self.y - self.size // 2,
            self.x + self.size // 2, self.y + self.size // 2
        )
        
    def perdre_vie(self):
        if not self.invincible:  # Réduire la vie uniquement si le joueur n'est pas invincible
            self.vie -= 1
            if self.update_vie_callback:
                self.update_vie_callback(self.vie)
            print(f"Vie restante : {self.vie}")
            if self.vie <= 0:
                self.mourir()
            else:
                self.devenir_invincible()

    def mourir(self):
        print("Game Over!")
        self.canvas.delete(self.id)  # Supprimer le joueur du canvas

    def devenir_invincible(self, duree=2000):  # Période d'invincibilité en ms
        self.invincible = True
        self.clignotement_actif = True
        self.clignoter()
        self.canvas.after(duree, self.fin_invincibilite)

    def fin_invincibilite(self):
        self.invincible = False
        self.clignotement_actif = False
        self.canvas.itemconfig(self.id, state="normal")  # Rendre visible

    def clignoter(self):
        if self.clignotement_actif:
            # Alterner entre visible/invisible
            etat_actuel = self.canvas.itemcget(self.id, "state")
            nouvel_etat = "hidden" if etat_actuel == "normal" else "normal"
            self.canvas.itemconfig(self.id, state=nouvel_etat)
            # Répéter toutes les 200 ms
            self.canvas.after(200, self.clignoter)
    
    def ajouter_score(self, points):
        """
        Ajoute des points au score et met à jour l'interface via le callback.
        """
        self.score += points
        print(f"Score actuel : {self.score}")
        if self.update_score_callback:
            self.update_score_callback(self.score)
    
    def vie(self):
         vies = 3
    

