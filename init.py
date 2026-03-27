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

pattern11 = [0,0,0, 1,1,1, 0,0,0]
pattern12 = [0,1,0, 0,1,0, 0,1,0]

pattern21 = [0,0,0, 0,1,1, 0,1,0]
pattern22 = [0,1,0, 0,1,1, 0,0,0]
pattern23 = [0,1,0, 1,1,0, 0,0,0]
pattern24 = [0,0,0, 1,1,0, 0,1,0]

pattern31 = [0,0,0, 1,1,1, 0,1,0]
pattern32 = [0,1,0, 0,1,1, 0,1,0]
pattern33 = [0,1,0, 1,1,1, 0,0,0]
pattern34 = [0,1,0, 1,1,0, 0,1,0]

pattern4 = [0,1,0, 1,1,1, 0,1,0]

pattern5 = [1,1,1, 1,1,1, 1,1,1] # pattern vide

listePattern = [pattern11,pattern12, pattern21,pattern22,pattern23,pattern24, pattern31,pattern32,pattern33,pattern34, pattern4, pattern5]
###                 0           1       2           3       4           5           6       7           8       9           10      11


### prediction des patterns en fonction des voisins
### listes de patternes possible

## dictionnaire ou juste en fonction de la place dans la liste

## toujours Haut, Bas, Gauche, Droite

predictionDico = [
    {                                   # pattern 11
        0:[3, 4, 8],                  # 22, 23, 33
        1:[2, 5, 6],                  # 21, 24, 31  
        2:[2, 3, 6, 7, 8, 10, 0],     # 21, 22, 31, 32, 33, 4, 11
        3:[4, 5, 6, 8, 9, 19, 0]      # 23, 24, 31, 33, 34, 4, 11
        
    },
    {                                   # pattern 12
        0:[2, 5, 6, 7, 9, 10, 1],     # 21, 24, 31, 32, 34, 4, 12
        1:[3, 4, 7, 8, 9, 10, 1],     # 22, 23, 32, 33, 34, 4, 12
        2:[4, 5, 9],                  # 23, 24, 34
        3:[2, 3, 7]                   # 21, 22, 32
       
    }
]

predictionListe = [  ## bas / haut /  droite/ gauche /
    [                           #pattern 11
        [2, 5, 6],
        [3, 4, 8],
        [4, 5, 6, 8, 9, 19, 0],
        [2, 3, 6, 7, 8, 10, 0],
        
    ],
    [                           #pattern 12
        [3, 4, 7, 8, 9, 10, 1],
        [2, 5, 6, 7, 9, 10, 1],
        [2, 3, 7],
        [4, 5, 9],
        
    ]
]

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