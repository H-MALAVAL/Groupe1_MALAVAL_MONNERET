# MALAVAL Hugo, MONNERET Martin le 4/11/2024 
from tkinter import Canvas
from PIL import Image, ImageTk

# Création de la class joueur
class Joueur:
    # Composée de l'apparence du joueur, du score du joueur et de ses points de vie
    def __init__(self, canvas, x, y, score, vie, size = 30):

        self.score = score
        self.vie = vie
        self.canvas = canvas
        
        """image = Image.open("vaisseau.gif")

        self.image_tk = ImageTk.PhotoImage(image)  # Convertir en format compatible Tkinter"""
        # Coordonnées du trapèze centré sur (650, 600)
        x_center, y_center = 650, 600
        width_top = 100  # Largeur du haut du trapèze
        width_bottom = 200  # Largeur du bas du trapèze
        height = 100  # Hauteur du trapèze

        # Calcul des points du trapèze
        points = [
            x_center - width_top // 2, y_center - height // 2,    # Point en haut à gauche
            x_center + width_top // 2, y_center - height // 2,    # Point en haut à droite
            x_center + width_bottom // 2, y_center + height // 2, # Point en bas à droite
            x_center - width_bottom // 2, y_center + height // 2  # Point en bas à gauche
        ]
        self.vaisseau_id = canvas.create_polygon(points, fill="violet", outline="black", width=2)
                
        
    def move(self):
        
        self.x += dx
        self.y += dy
        canvas.move(self.image_id, dx, dy)
    
    def score(self):
        """Arguments: aucun
        But : calculer le score du joueur quand il tire sur un alien, selon le type d'alier
        (10 points pour alien de base, 25 pour alien qui tire et 150 pour le boss final)
        Renvoi le score actualisé à chaque fois qu'il change et l'affiche sur la fenêtre principale"""
        score = 0
        
    
    def vie(self):
         vies = 3