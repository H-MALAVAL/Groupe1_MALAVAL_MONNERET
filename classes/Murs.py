# MALAVAL Hugo, MONNERET Martin le 4/11/2024

# Création de la class murs

from tkinter import Canvas
import random

class Murs:
    
    def __init__(self, canvas, x, y, size=30, color="red"):
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
        self.murs_id = canvas.create_rectangle(x, y, x + size, y + size, fill=self.color)