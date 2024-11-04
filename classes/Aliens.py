# MALAVAL Hugo, MONNERET Martin le 4/11/2024

# Création de la class alien

from tkinter import Canvas

class Alien:
    def __init__(self, canvas, x, y, size=30, speed=5, descent_step=50, color="white"):
        """
        Initialise l'alien avec ses paramètres de position, de taille et de vitesse.
        """
        self.canvas = canvas
        self.size = size
        self.speed = speed
        self.direction = 1  # 1 pour aller à droite, -1 pour aller à gauche
        self.descent_step = descent_step if color == "white" else 0  # Les rouges ne descendent pas
        self.color = color
        
        # Création de l'alien avec la couleur spécifiée
        self.alien_id = canvas.create_rectangle(x, y, x + size, y + size, fill=self.color)

    def move(self):
        if self.color == "white":
            self.move_downward()
        else:
            self.move_randomly()

    def move_downward(self):
        x1, y1, x2, y2 = self.canvas.coords(self.alien_id)
        if x2 >= self.canvas.winfo_width() or x1 <= 0:
            self.direction *= -1
            self.canvas.move(self.alien_id, 0, self.descent_step)
        self.canvas.move(self.alien_id, self.speed * self.direction, 0)

    def move_randomly(self):
        x1, y1, x2, y2 = self.canvas.coords(self.alien_id)
        random_direction = random.choice([-1, 1])
        random_distance = random.randint(5, 15)
        self.canvas.move(self.alien_id, random_direction * random_distance, 0)

    def get_position(self):
        """
        Renvoie la position actuelle de l'alien.
        """
        return self.canvas.coords(self.alien_id)
    

