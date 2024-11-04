# MALAVAL Hugo, MONNERET Martin le 4/11/2024 
from tkinter import Canvas
# Création de la class joueur
class Joueur:
    # Composée de l'apparence du joueur, du score du joueur et de ses points de vie
    def __init__(self, canvas, x, y, score, vie, size = 30):

        self.score = score
        self.vie = vie
        self.canvas = canvas
        
        """image = Image.open("vaisseau.gif")

        self.image_tk = ImageTk.PhotoImage(image)  # Convertir en format compatible Tkinter"""
        
        self.vaisseau_id = canvas.create_rectangle(x, y, x + size, y + size, fill="white")
        
        
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