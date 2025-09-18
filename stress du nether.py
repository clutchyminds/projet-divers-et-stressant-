import pygame
import random
import sys
import tkinter as tk
import threading

pygame.init()

# Fenêtre principale
WIDTH, HEIGHT = 800, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bienvenue en enfer")

# Couleurs
RED = (255, 0, 0)
BLACK = (0, 0, 0)

font = pygame.font.SysFont("monospace", 45)
messages = ["Il est trop tard...", "Tu ne peux plus fuir...", "Écoute...", "Il t’observe", "Rien n’est réel"]

clock = pygame.time.Clock()
PASSWORD = "8_5(9ç"
exit_button = pygame.Rect(10, 10, 20, 20)

# Tremblements
def get_offset():
    return random.randint(-10, 10), random.randint(-10, 10)

# Fenêtre vivante avec mouvement aléatoire
def spawn_window():
    def move_window():
        w = tk.Tk()
        w.geometry("200x100+{}+{}".format(random.randint(0, 1000), random.randint(0, 600)))
        w.configure(bg="black")
        label = tk.Label(w, text="👁️", fg="red", bg="black", font=("Courier", 40))
        label.pack(expand=True)

        def animate():
            while True:
                x = random.randint(0, 1000)
                y = random.randint(0, 600)
                alpha = random.uniform(0.8, 1.0)
                try:
                    w.geometry(f"+{x}+{y}")
                    w.wm_attributes("-alpha", alpha)
                    w.wm_attributes("-topmost", 1)
                except:
                    break
                w.update()
                w.after(300)

        threading.Thread(target=animate, daemon=True).start()
        w.mainloop()
    threading.Thread(target=move_window).start()

def panic_trigger():
    for _ in range(5):
        spawn_window()

def ask_password():
    def validate():
        code = entry.get()
        if code == PASSWORD:
            pygame.quit()
            sys.exit()
        else:
            panic_trigger()
            popup.destroy()

    popup = tk.Tk()
    popup.title("Code de sortie ?")
    popup.geometry("300x100+200+200")
    popup.configure(bg="black")
    tk.Label(popup, text="Entrez le code : ", bg="black", fg="red", font=("Courier", 14)).pack()
    entry = tk.Entry(popup, font=("Courier", 14))
    entry.pack()
    tk.Button(popup, text="Valider", command=validate).pack()
    popup.mainloop()

# Dessin de la fenêtre principale
def draw_stress():
    dx, dy = get_offset()
    win.fill(random.choice([RED, BLACK]))
    for _ in range(random.randint(15, 30)):
        shape = random.choice(["circle", "rect"])
        x, y = random.randint(0, WIDTH), random.randint(0, HEIGHT)
        size = random.randint(30, 120)
        color = random.choice([RED, BLACK])
        x += dx
        y += dy
        if shape == "circle":
            pygame.draw.circle(win, color, (x, y), size)
        else:
            pygame.draw.rect(win, color, (x, y, size, size))

    if random.random() < 0.5:
        text = font.render(random.choice(messages), True, RED)
        tx = random.randint(0, WIDTH - text.get_width())
        ty = random.randint(0, HEIGHT - text.get_height())
        win.blit(text, (tx + dx, ty + dy))

    pygame.draw.rect(win, RED, exit_button)
    pygame.display.update()

# Boucle principale
def abyss():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                panic_trigger()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if exit_button.collidepoint(event.pos):
                    ask_password()
        draw_stress()
        clock.tick(random.randint(30, 70))

abyss()
