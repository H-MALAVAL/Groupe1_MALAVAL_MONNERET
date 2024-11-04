# MALAVAL Hugo, MONNERET Martin le 4/11/2024

import tkinter as tk
from PIL import Image,ImageTk 
# Création de la class joueur
class joueur:
    # Composée de l'apparence du joueur, du score du joueur et de ses points de vie
    def __init__(self, canvas, x, y, score, vie):
        self.score = []
        self.vie = []
        
        image = Image.open("vaisseau.png")
        self.image_tk = ImageTk.PhotoImage(image)
        
        # Ajouter l'image au canevas à la position (x, y)
        self.sprite = canvas.create_image(x, y, anchor="center", image=self.image_tk)
        
        self.image_tk = ImageTk.PhotoImage(image)  # Convertir en format compatible Tkinter
        self.image_id = canvas.create_image(self.x, self.y, image=self.image_tk)  # Ajouter l'image au canevas
    
    def score(self):
        """Arguments: aucun
        But : calculer le score du joueur quand il tire sur un alien, selon le type d'alier
        (10 points pour alien de base, 25 pour alien qui tire et 150 pour le boss final)
        Renvoi le score actualisé à chaque fois qu'il change et l'affiche sur la fenêtre principale"""
        score = 0
        
    
    def vie(self):
         vies = 3