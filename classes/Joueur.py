# MALAVAL Hugo, MONNERET Martin le 4/11/2024 
from tkinter import Tk, Label, Button, Canvas, Menu, StringVar, Toplevel, messagebox

# Création de la class joueur
class Joueur:
    # Composée de l'apparence du joueur, du score du joueur et de ses points de vie
    def __init__(self, canvas, x, score, vie, size = 30):

        self.score = score
        self.vie = vie
        self.canvas = canvas
        self.size = size
        self.x = x
        
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
        self.id = canvas.create_polygon(points, fill="violet", outline="black", width=2)
                
    def deplacer(self,dx):
        
        self.x += dx
        # Met à jour la position sur le canvas
        self.canvas.coords(
            self.id, 
            self.x - self.size // 2,
            self.x + self.size // 2,
        )
    
    def score(self):
        """Arguments: aucun
        But : calculer le score du joueur quand il tire sur un alien, selon le type d'alier
        (10 points pour alien de base, 25 pour alien qui tire et 150 pour le boss final)
        Renvoi le score actualisé à chaque fois qu'il change et l'affiche sur la fenêtre principale"""
        score = 0
    
    def vie(self):
         vies = 3
    

