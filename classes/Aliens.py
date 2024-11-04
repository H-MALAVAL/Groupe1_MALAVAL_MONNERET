# MALAVAL Hugo, MONNERET Martin le 4/11/2024

# Création de la class alien

from tkinter import Canvas

class Alien:
    def __init__(self, canvas, x, y, size=30, speed=5, descent_step=50):
        """
        Initialise l'alien avec ses paramètres de position, de taille et de vitesse.
        """
        self.canvas = canvas
        self.size = size
        self.speed = speed
        self.direction = 1  # 1 pour aller à droite, -1 pour aller à gauche
        self.descent_step = descent_step  # Nombre de pixels que l'alien descend après un aller-retour
        
        # Création de l'alien comme un rectangle (ou un autre objet de votre choix)
        self.alien_id = canvas.create_rectangle(x, y, x + size, y + size, fill="white")

    def move(self):
        """
        Déplace l'alien dans la direction actuelle et vérifie les collisions avec les bords.
        """
        # Obtenir les coordonnées actuelles de l'alien
        x1, y1, x2, y2 = self.canvas.coords(self.alien_id)

        # Si l'alien touche le bord droit ou gauche, inverser la direction
        if x2 >= self.canvas.winfo_width() or x1 <= 0:
            self.direction *= -1  # Changer de direction
            self.canvas.move(self.alien_id, 0, self.descent_step)  # Descendre de `descent_step` pixels

        # Déplacer l'alien dans la direction actuelle
        self.canvas.move(self.alien_id, self.speed * self.direction, 0)

    def get_position(self):
        """
        Renvoie la position actuelle de l'alien.
        """
        return self.canvas.coords(self.alien_id)
