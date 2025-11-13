
import tkinter as tk
from PIL import Image

from PIL import Image, ImageDraw

# 1. Stwórz główne okno
root = tk.Tk()
root.title("Test prostokąta w Tkinter")

# 2. Stwórz płótno (Canvas) o wymiarach 400x500 z białym tłem
# Dajemy mu lekki margines (highlightthickness=0)
canvas = tk.Canvas(root, width=1000, height=500, bg='white', highlightthickness=0)
canvas.pack() # Dopasuj płótno do okna

# -----------------------------------------------------------------
# TUTAJ DOKŁADNA SKŁADNIA
# -----------------------------------------------------------------
# Chcemy narysować prostokąt (np. ramę okna)
# Zaczynając od punktu (50, 50)
# Kończąc w punkcie (350, 450)
# (Szerokość = 350-50 = 300px, Wysokość = 450-50 = 400px)

frame_width = 8

x1 = 50
y1 = 50
x2 = 800
y2 = 450

#podpasodpoa

x1_inside =  x1+ frame_width
y1_inside =  y1+ frame_width
x2_inside =  x2- frame_width
y2_inside =  y2- frame_width

x_middle = x1 + ((x2-x1)/2)
y_middle = y1 + ((y2-y1)/2)

podział = 2

bok_slupka_a = x_middle - (frame_width/2)
bok_slupka_b = x_middle + (frame_width/2)



canvas.create_rectangle(
    x1, y1, x2, y2, 
    outline='black',  # Kolor ramki
    width=2           # Grubość ramki
)

canvas.create_rectangle(
    x1_inside, y1_inside, x2_inside, y2_inside, 
    outline='black',  # Kolor ramki
    width=2           # Grubość ramki
)

for x in range(1,podział):
    
    co_ile_slupek = (x2_inside-x1_inside)/(podział)
    print (co_ile_slupek)
    srodek_slupka= x1_inside + x * co_ile_slupek
    lewy_bok_slupka = srodek_slupka - frame_width/2
    prawy_bok_slupka = srodek_slupka + frame_width/2

    canvas.create_line(
        lewy_bok_slupka ,y1_inside, lewy_bok_slupka, y2_inside,
        fill='black',  # Kolor ramki
        width=2   
    )

    canvas.create_line(
        prawy_bok_slupka ,y1_inside, prawy_bok_slupka, y2_inside,
        fill='black',  # Kolor ramki
        width=2   
    )

"""canvas.create_line(
    bok_slupka_a ,y1_inside, bok_slupka_a, y2_inside,
    fill='black',  # Kolor ramki
    width=2   
)

canvas.create_line(
    bok_slupka_b ,y1_inside, bok_slupka_b, y2_inside,
    fill='black',  # Kolor ramki
    width=2   
)"""
# -----------------------------------------------------------------

# 3. Uruchom pętlę główną okna
root.mainloop()