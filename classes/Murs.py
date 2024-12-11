# MALAVAL Hugo, MONNERET Martin le 4/11/2024

# Création de la class murs

from tkinter import Canvas
import random

class Murs:
    
    def __init__(self, canvas, x, y, size=300, color="white", vie=5):
        """
        Initialise les murs avec leurs paramètres de position et de taille.
        """
        self.canvas = canvas
        self.size = size
        self.direction = 1  # 1 pour aller à droite, -1 pour aller à gauche
        self.color = color
        self.vie_initiale = vie
        self.vie = vie
        
        # Position pour les murs
        self.target_x = x
        self.target_y = y
        
        # Création des murs avec la couleur spécifiée
        self.murs_id = canvas.create_rectangle(x, y, x + 100, y + 50, fill=self.color)

    def subir_collision(self):
        """
        Réduit les points de vie du mur et change sa couleur ou le supprime si nécessaire.
        """
        self.vie -= 1
        if self.vie > 0:
            couleurs = ["#FFCCCC", "#FF9999", "#FF6666", "#FF3333", "#FF0000"]
            self.canvas.itemconfig(self.murs_id, fill=couleurs[max(0, self.vie - 1)])
        else:
            # Supprime le mur du canvas s'il est détruit
            self.canvas.delete(self.murs_id)
            self.murs_id = None 
            self.canvas.after(5000, self.reapparaitre)

    def reapparaitre(self):
        """
        Fait réapparaître le mur avec ses points de vie initiaux.
        """
        self.vie = self.vie_initiale
        self.murs_id = self.canvas.create_rectangle(
            self.target_x, self.target_y,
            self.target_x + 100, self.target_y + 50,
            fill=self.color
        )