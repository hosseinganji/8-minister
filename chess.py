from tkinter import *
from PIL import Image , ImageTk

def createfullarray(createlittlearray, i):
    if (len(createlittlearray) == o):
        feasible.append(createlittlearray)
        print(createlittlearray)
    if (i not in [_[0] for _ in createlittlearray]):
        for j in range(1, u+1):
            if (j not in [_[1] for _ in createlittlearray]):
                if len([0 for p in createlittlearray if abs(p[0]-i) == abs(p[1]-j)]) == 0:
                    createfullarray(createlittlearray+[[i, j]], i+1)

def start(n, k):
    global feasible, u, o
    u = n
    o = k
    feasible = []
    createfullarray([], 1)
    return feasible

start(8, 8)

def next_button():
    global z
    canvas_chessFlat.delete("all") 
    z += 1
    layout_chess(z)

def previos_button():
    global z
    canvas_chessFlat.delete("all") 
    z -= 1
    layout_chess(z)

def reset_button():
    global z
    canvas_chessFlat.delete("all") 
    z = 0
    layout_chess(z)

chessFlat = Tk()
chessFlat.geometry("600x670")
chessFlat.maxsize(600,670)
chessFlat.title("Chess")
canvas_chessFlat = Canvas(chessFlat, width=560, height=560)
image_chess_flat = ImageTk.PhotoImage(Image.open("chessflat.png"))
image_queen = ImageTk.PhotoImage(Image.open("queen.png"))

def layout_chess(z):
    canvas_chessFlat.create_image(280,280,image=image_chess_flat)
    for y in range(8):
        for x in range(8):
            if (feasible[z][y][1] == x+1):
                canvas_chessFlat.create_image( 35+(x*70) , 35+((y)*70) ,image=image_queen)
    Label(chessFlat, font=('arial', 13, 'bold'), text="level: " + str(z+1), fg="black").place(relx=0.03, rely=0.85, height=30, width=70)
    Button(chessFlat, padx=10, pady=16, font=('arial', 11), fg='black', bg='#04AA6D', text='Next >', command=next_button).place(relx=0.83, rely=0.9, height=50, width=80)
    Button(chessFlat, padx=10, pady=16, font=('arial', 11), fg='black', bg='#3d30ff', text='< previos', command=previos_button).place(relx=0.03, rely=0.9, height=50, width=80)
    Button(chessFlat, padx=10, pady=16, font=('arial', 11), fg='black', bg='#ff4c4c', text='Reset', command=reset_button).place(relx=0.43, rely=0.9, height=50, width=80)

z = 0
layout_chess(z)
canvas_chessFlat.pack()
chessFlat.mainloop()