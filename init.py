from tkinter import *
from random import *

NbRow = 24  # 25
NbColumn = 39  # 40

root = Tk()
root.title("La Dynamique des Patterns")
# root.geometry("850x550") # 

#  800 + 25*2
#  500 + 25*2

canvas1 = Canvas(root, width=800, height=500, bg="light yellow", highlightthickness=2, highlightbackground="black", bd=0)
canvas1.grid(column=0,row=0, padx=25, pady=25)

canvas2 = Canvas(root, width=800, height=170, bg="light yellow", highlightthickness=2, highlightbackground="black", bd=0)
canvas2.grid(column=0,row=2, padx=25, pady=25)


### création des differents patterns

# pattern11 = [0,0,0, 1,1,1, 0,0,0]
# pattern12 = [0,1,0, 0,1,0, 0,1,0]

# pattern21 = [0,0,0, 0,1,1, 0,1,0]
# pattern22 = [0,1,0, 0,1,1, 0,0,0]
# pattern23 = [0,1,0, 1,1,0, 0,0,0]
# pattern24 = [0,0,0, 1,1,0, 0,1,0]

# pattern31 = [0,0,0, 1,1,1, 0,1,0]
# pattern32 = [0,1,0, 0,1,1, 0,1,0]
# pattern33 = [0,1,0, 1,1,1, 0,0,0]
# pattern34 = [0,1,0, 1,1,0, 0,1,0]

# pattern4 = [0,1,0, 1,1,1, 0,1,0]

# pattern5 = [1,1,1, 1,1,1, 1,1,1] # pattern vide

# # listePattern = [pattern11,pattern12, pattern21,pattern22,pattern23,pattern24, pattern31,pattern32,pattern33,pattern34, pattern4, pattern5]
# ###                 0           1       2           3       4           5           6       7           8       9           10      11



compatibilites = [
    [0,0,1,1], # 0
    [1,1,0,0], # 1
    [0,1,0,1], # 2
    [1,0,0,1], # 3
    [1,0,1,0], # 4
    [0,1,1,0], # 5
    [0,1,1,1], # 6
    [1,1,0,1], # 7
    [1,0,1,1], # 8
    [1,1,1,0], # 9
    [1,1,1,1], # 10
    [1,1,1,1], # 11 / pattern vide
]


### tentative de création des patterns avec le tableau de Compatibilité

listePattern = []
model = [0,0,0, 2,1,3, 0,1,0]
#model = [0,"N",0, "W",1,"E", 0,"S",0]

compa = compatibilites[:-1] # liste des compatibilité moins le dernier

for c in compa:
    pattern = []
    indexI = 0
    for i in model:
        
        if indexI%2 == 0: # paire
            pattern.append(i)
        else:
            # val = c[indexI]
            val = c[i]
            pattern.append(val)
        indexI += 1
    listePattern.append(pattern)

listePattern.append([1,1,1, 1,1,1, 1,1,1])