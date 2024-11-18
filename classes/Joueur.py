# MALAVAL Hugo, MONNERET Martin le 4/11/2024 
from tkinter import Tk, Label, Button, Canvas, Menu, StringVar, Toplevel, messagebox

# Création de la class joueur
class Joueur:
    # Composée de l'apparence du joueur, du score du joueur et de ses points de vie
    def __init__(self, canvas, x, y, score, vie, size = 30):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.size = size
        self.score = score
        self.vie = vie
        self.id = canvas.create_rectangle(
            self.x - self.size // 2,
            self.y - self.size // 2,
            self.x + self.size // 2,
            self.y + self.size // 2,
            fill="blue"
        )
        self.invincible = False  # Indique si le joueur est temporairement invincible
        self.clignotement_actif = False  # Pour gérer le clignotement
        
        """image = Image.open("vaisseau.gif")

        self.image_tk = ImageTk.PhotoImage(image)  # Convertir en format compatible Tkinter"""
                
    def deplacer(self, dx):
        # Modifier la position
        self.x += dx
        # Empêcher le joueur de sortir des limites
        self.x = max(self.size // 2, min(self.canvas.winfo_width() - self.size // 2, self.x))
        # Mettre à jour graphiquement
        self.canvas.coords(
            self.id,
            self.x - self.size // 2,
            self.y - self.size // 2,
            self.x + self.size // 2,
            self.y + self.size // 2
        )

    def perdre_vie(self):
        if not self.invincible:  # Réduire la vie uniquement si le joueur n'est pas invincible
            self.vie -= 1
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
    
    def score(self):
        """Arguments: aucun
        But : calculer le score du joueur quand il tire sur un alien, selon le type d'alier
        (10 points pour alien de base, 25 pour alien qui tire et 150 pour le boss final)
        Renvoi le score actualisé à chaque fois qu'il change et l'affiche sur la fenêtre principale"""
        score = 0
    
    def vie(self):
         vies = 3
    

