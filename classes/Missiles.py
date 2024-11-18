<<<<<<< HEAD
=======
# MALAVAL Hugo, MONNERET Martin le 15/11/2024

# Création de la class missiles
from tkinter import Canvas
class Missile:
    def __init__(self, canvas, x, y, size=5, speed=10, direction="up"):
        self.canvas = canvas
        self.size = size
        self.speed = speed if direction == "up" else -speed
        self.missile_id = canvas.create_rectangle(x, y, x + size, y + size * 2, fill="red")

    def move(self):
        self.canvas.move(self.missile_id, 0, -self.speed)
        if self.is_out_of_bounds():
            self.delete()
        else:
            self.canvas.after(50, self.move)

    def is_out_of_bounds(self):
        _, y1, _, y2 = self.canvas.coords(self.missile_id)
        return y2 < 0 or y1 > self.canvas.winfo_height()

    def delete(self):
        self.canvas.delete(self.missile_id)
>>>>>>> 63089a2df22482122df7d80703a3ed5f8c122151
