import tkinter as tk
from tkinter import simpledialog, messagebox
import random

bombe_art = """
             . . .                         
              \|/                          
            `--+--'                        
              /|\                          
             ' | '                         
               |                           
               |                           
           ,--'#`--.                       
           |#######|                       
        _.-'#######`-._                    
     ,-'###############`-.                 
   ,'#####################`,               
  /#########################\              
 |###########################|             
|#############################|            
|#############################|            
|#############################|            
|#############################|            
 |###########################|             
  \#########################/              
   `.#####################,'               
     `._###############_,'                 
        `--..#####..--'
"""

code_secret = "8_5(9ç"
fenetres_actives = 0
wave_counter = 0

def clignoter(fen, label, état=[True]):
    couleur = "red" if état[0] else "black"
    fen.configure(bg=couleur)
    label.configure(bg=couleur, fg="white" if état[0] else "red")
    état[0] = not état[0]
    fen.after(300, lambda: clignoter(fen, label, état))

def creer_bombe():
    global fenetres_actives
    for _ in range(10):
        fen = tk.Toplevel(root)
        fen.title("💣 Bombe")
        fen.geometry("300x200+{}+{}".format(random.randint(0, 800), random.randint(0, 400)))
        label = tk.Label(fen, text=bombe_art, font=("Courier", 10), justify="center")
        label.pack(pady=10)
        clignoter(fen, label)

        def on_close():
            code = simpledialog.askstring("Code", "Entre le code pour désactiver :")
            if code == code_secret:
                fen.destroy()
                root.quit()
            else:
                fen.destroy()
                creer_bombe()

        fen.protocol("WM_DELETE_WINDOW", on_close)
        fenetres_actives += 1

def vague_bombes():
    global wave_counter
    wave_counter += 1
    creer_bombe()
    label_status.config(text=f"⚠️ Vague #{wave_counter} - {fenetres_actives} fenêtres ouvertes")
    root.after(60000, vague_bombes)  # 1 min

root = tk.Tk()
root.title("💥 TROLL EXPLOSIF 💥")
root.geometry("400x200")

label_start = tk.Label(root, text="Appuie pour DÉCLENCHER LA BOMBE", font=("Arial", 12), fg="red")
label_start.pack(pady=20)

btn = tk.Button(root, text="ACTIVER", command=vague_bombes, bg="black", fg="white")
btn.pack(pady=10)

label_status = tk.Label(root, text="Aucune vague lancée", fg="red")
label_status.pack(pady=10)

root.mainloop()

