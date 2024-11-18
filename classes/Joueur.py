# MALAVAL Hugo, MONNERET Martin le 4/11/2024 
from tkinter import Tk, Label, Button, Canvas, Menu, StringVar, Toplevel, messagebox

# Création de la class joueur
class Joueur:
    # Composée de l'apparence du joueur, du score du joueur et de ses points de vie
<<<<<<< HEAD
    def __init__(self, canvas, x, y, score, vie, size = 30):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.size = size
=======
    def __init__(self, canvas, x, score, vie, size = 30):

>>>>>>> c53228e2965e001beda9948d6dd120d925546138
        self.score = score
        self.vie = vie
        self.id = canvas.create_rectangle(
            self.x - self.size // 2,
            self.y - self.size // 2,
            self.x + self.size // 2,
            self.y + self.size // 2,
            fill="blue"
        )
        
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

    
    def score(self):
        """Arguments: aucun
        But : calculer le score du joueur quand il tire sur un alien, selon le type d'alier
        (10 points pour alien de base, 25 pour alien qui tire et 150 pour le boss final)
        Renvoi le score actualisé à chaque fois qu'il change et l'affiche sur la fenêtre principale"""
        score = 0
    
    def vie(self):
         vies = 3
    

