from tkinter import Canvas

class Missile:
    def __init__(self, canvas, x, y, size=5, speed=10):
        self.canvas = canvas
        self.size = size
        self.speed = speed
        # Crée le missile sous forme de cercle ou de rectangle
        self.missile_id = canvas.create_rectangle(x, y, x + size, y + size * 2, fill="red")

    def move(self):
        self.canvas.move(self.missile_id, 0, self.speed)
        self.canvas.after(50, self.move)  # Boucle pour continuer le mouvement vers le bas
