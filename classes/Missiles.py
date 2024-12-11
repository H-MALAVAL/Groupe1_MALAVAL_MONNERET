# MALAVAL Hugo, MONNERET Martin le 15/11/2024

# Création de la class missiles
from tkinter import Canvas
class Missile:
    def __init__(self, canvas, x, y, size=5, speed=10, delay = 0.1, direction="up", color="white"):
        self.canvas = canvas
        self.size = size
        self.color = color
        self.delay = delay
        self.speed = speed if direction == "up" else -speed
        self.missile_id = canvas.create_rectangle(x, y, x + size, y + size * 2, fill=self.color)

    def move(self):
        """Permet aux missiles de se déplacer"""
        if self.canvas.coords(self.missile_id):  # Vérifiez que le missile existe encore
            self.canvas.move(self.missile_id, 0, -self.speed)
            if self.is_out_of_bounds():
                self.delete()
            else:
                self.canvas.after(50, self.move)

    def is_out_of_bounds(self):
        """Si le missile est en dehors des murs, le signal"""
        coords = self.canvas.coords(self.missile_id)
        if len(coords) != 4:  # Si les coordonnées ne sont pas valides
            return True
        _, y1, _, y2 = coords
        return y2 < 0 or y1 > self.canvas.winfo_height()

    def delete(self):
        """Efface le missile"""
        self.canvas.delete(self.missile_id)
