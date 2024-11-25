# MALAVAL Hugo, MONNERET Martin le 4/11/2024 
from tkinter import Tk, Label, Button, Canvas, Menu, StringVar, Toplevel, messagebox

# Création de la class joueur
class Joueur:
    # Composée de l'apparence du joueur, du score du joueur et de ses points de vie
    def __init__(self, canvas, x, y, image_path, score, vie, size = 30, update_vie_callback=None, update_score_callback=None):
        self.canvas = canvas
        self.x = x
        self.y = y
        
        # Chargement de l'image du vaisseau
        self.image = Tk.PhotoImage(file=image_path)
        
        self.size = size
        self.score = score
        self.vie = vie
        self.update_vie_callback = update_vie_callback
        self.update_score_callback = update_score_callback
        self.id = canvas.create_rectangle(
            self.x - self.size // 2,
            self.y - self.size // 2,
            self.x + self.size // 2,
            self.y + self.size // 2,
            fill="blue"
        )
        self.invincible = False  # Indique si le joueur est temporairement invincible
        self.clignotement_actif = False  # Pour gérer le clignotement

        # Appeler le callback pour synchroniser l'interface au démarrage
        if self.update_vie_callback:
            self.update_vie_callback(self.vie)
        if self.update_score_callback:
            self.update_score_callback(self.score)
        
        # Ajout de l'image au Canvas
        self.image_id = self.canvas.create_image(self.x, self.y, image=self.image, anchor=Tk.CENTER)
        
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
        self.canvas.move(self.image_id, dx)

    def perdre_vie(self):
        if not self.invincible:  # Réduire la vie uniquement si le joueur n'est pas invincible
            self.vie -= 1
            if self.update_vie_callback:
                self.update_vie_callback(self.vie)
            print(f"Vie restante : {self.vie}")
            if self.vie <= 0:
                self.mourir()
            else:
                self.devenir_invincible()

    def mourir(self):
        print("Game Over!")
        self.canvas.delete(self.id)  # Supprimer le joueur du canvas

    def devenir_invincible(self, duree=2000):  # Période d'invincibilité en ms
        self.invincible = True
        self.clignotement_actif = True
        self.clignoter()
        self.canvas.after(duree, self.fin_invincibilite)

    def fin_invincibilite(self):
        self.invincible = False
        self.clignotement_actif = False
        self.canvas.itemconfig(self.id, state="normal")  # Rendre visible

    def clignoter(self):
        if self.clignotement_actif:
            # Alterner entre visible/invisible
            etat_actuel = self.canvas.itemcget(self.id, "state")
            nouvel_etat = "hidden" if etat_actuel == "normal" else "normal"
            self.canvas.itemconfig(self.id, state=nouvel_etat)
            # Répéter toutes les 200 ms
            self.canvas.after(200, self.clignoter)
    
    def ajouter_score(self, points):
        """
        Ajoute des points au score et met à jour l'interface via le callback.
        """
        self.score += points
        print(f"Score actuel : {self.score}")
        if self.update_score_callback:
            self.update_score_callback(self.score)
    
    def vie(self):
         vies = 3
    

