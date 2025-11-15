import drawsvg as draw

# 1. Stwórz płótno (Drawing)
# szerokość 300px, wysokość 200px
d = draw.Drawing(5000, 5000)

# 2. Narysuj prostokąt
# (x, y, szerokość, wysokość, ...opcje)
START_A = 50
START_B = 50
width = 500
high = 235
frame_width = 8
how_many_glazes = 5

o3 = Window() 

Frame = [START_A, START_B, width, high]
inner_frame = []
d.append(draw.Rectangle(Frame[0],Frame[1],Frame[2],Frame[3],
                        fill="#ffffff",       # Wypełnienie (szary-niebieski)
                        stroke='black',       # Kolor obramowania
                        stroke_width=2))      # Grubość obramowania
#def draw_columns(how_many_glazes):
    
def draw_inner_frame(Frame): #Tutaj widzę, że powinno to być prosciej zrobione. Plus rekurencja jak znalazł
    inner_START_A = 50+frame_width
    inner_START_B = 50+frame_width
    inner_width = 500 - 2* frame_width
    inner_high = 235 - 2* frame_width

    d.append(draw.Rectangle(inner_START_A, inner_START_B, inner_width, inner_high,
                        fill="#ffffff",       # Wypełnienie (szary-niebieski)
                        stroke='black',       # Kolor obramowania
                        stroke_width=2))      # Grubość obramowania



draw_inner_frame(Frame) #W sumie to to samo co draw_frame :/ 


# 5. Zapisz plik
d.save_svg('figury.svg') 

# Opcjonalnie: Wyświetl w Jupyter Notebook
# d