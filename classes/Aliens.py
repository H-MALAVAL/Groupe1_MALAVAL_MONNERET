# MALAVAL Hugo, MONNERET Martin le 4/11/2024

# Création de la class alien

from tkinter import Canvas
import random

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

        # Position cible pour les aliens rouges
        self.target_x = x
        self.target_y = y
        
        # Création de l'alien avec la couleur spécifiée
        self.alien_id = canvas.create_rectangle(x, y, x + size, y + size, fill=self.color)

    def move(self):
        x1, y1, x2, y2 = self.canvas.coords(self.alien_id)
        if x2 >= self.canvas.winfo_width() or x1 <= 0:
            self.direction *= -1
            self.canvas.move(self.alien_id, 0, self.descent_step)
        self.canvas.move(self.alien_id, self.speed * self.direction, 0)

    # Déplacement aléatoires des aliens rouges
    def move_towards_target(self):
        """
        Déplace l'alien vers sa cible en ligne droite.
        """
        x1, y1, x2, y2 = self.canvas.coords(self.alien_id)
        center_x = (x1 + x2) / 2  # Position actuelle (milieu)
        center_y = (y1 + y2) / 2

        # Calculer les vecteurs de déplacement
        dx = self.target_x - center_x
        dy = self.target_y - center_y
        distance = (dx**2 + dy**2)**0.5  # Distance entre la position actuelle et la cible

        # Normaliser le vecteur de déplacement
        if distance > 0:
            dx = dx / distance * self.speed
            dy = dy / distance * self.speed

        # Effectuer le déplacement si l'alien n'est pas encore à la cible
        if distance > self.speed:
            self.canvas.move(self.alien_id, dx, dy)

    def set_new_target(self):
        """
        Définit une nouvelle cible aléatoire pour l'alien rouge.
        """
        largeur_canevas = self.canvas.winfo_width()
        hauteur_canevas = self.canvas.winfo_height()

        self.target_x = random.randint(50, largeur_canevas - 50)
        self.target_y = random.randint(50, hauteur_canevas // 2)  # Limite en haut du canevas

    def delete(self):
        self.canvas.delete(self.alien_id)

    def get_position(self):
        x1, y1, x2, y2 = self.canvas.coords(self.alien_id)
        x_center = (x1 + x2) / 2  # Calculer la position centrale en X
        y_center = (y1 + y2) / 2  # Calculer la position centrale en Y
        return x_center, y_center