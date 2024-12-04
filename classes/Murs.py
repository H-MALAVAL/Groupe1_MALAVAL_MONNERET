# MALAVAL Hugo, MONNERET Martin le 4/11/2024

# Création de la class murs

from tkinter import Canvas
import random

class Murs:
    
    def __init__(self, canvas, x, y, size=300, color="white"):
        """
        Initialise les murs avec leurs paramètres de position et de taille.
        """
        self.canvas = canvas
        self.size = size
        self.direction = 1  # 1 pour aller à droite, -1 pour aller à gauche
        self.color = color
        
        # Position pour les murs
        self.target_x = x
        self.target_y = y
        
        # Création des murs avec la couleur spécifiée
        self.murs_id = canvas.create_rectangle(x, y, x + 100, y + 50, fill=self.color)

    def deplacer(self):
        """
        Déplace les murs horizontalement entre deux limites (rebond).
        """
        # Déplacement en fonction de la direction
        dx = 5 * self.direction  # Vitesse du déplacement
        self.canvas.move(self.murs_id, dx, 0)

        # Mise à jour de la position actuelle
        x1, y1, x2, y2 = self.canvas.coords(self.murs_id)
        
        # Détection des limites (rebond)
        if x2 >= self.canvas.winfo_width() or x1 <= 0:
            self.direction *= -1  # Inverser la direction

    def animer(self):
        """
        Anime les murs en appelant la méthode de déplacement périodiquement.
        """
        self.deplacer()  # Déplace les murs
        self.canvas.after(50, self.animer)  # Rappel toutes les 50 ms
