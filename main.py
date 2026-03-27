from Cellule import *

for i in range (NbRow):             # row
    for j in range (NbColumn):      # column
        Cellule(j*20+10, i*20+10, j, i, canvas1)

marge = 10
for k in range (5):

    for i in range (3):
        for j in range (3):
            Cellule(j*20+marge, i*20+10, j,i, canvas2)
    marge += 80


marge = 10
for k in range (6):

    for i in range (3):
        for j in range (3):
            Cellule(j*20+marge, i*20+80, j,i, canvas2)
    marge += 80




#### passer en revu les carrés pour illustrer les paternes ####
var = 0
for j in range (11):

    for i in range (9):
        cel = Cellule.listeCellulesCanv2[i+var]

        if listePattern[j][i] == 1:
            cel.set_etat()
    var += 9


def Clear ():
    for cel in Cellule.listeCellulesCanv1:
        if cel.get_etat() == 1:
            cel.set_etat()
        
        if cel.get_id() in Cellule.listeIdCentreGroupe:
            canvas1.itemconfig(cel.rec, fill="dark blue")
            cel.etatPat = 0
            cel.pat = None


#### frame du haut ####

frame2 = Frame(root) # , bg="light blue"
frame2.grid(sticky=NS, padx=10, pady=10, column=1, row=0) # , rowspan=2

frame2.rowconfigure([0,1,2,3], weight=1)

btn5 = Button(frame2, text="5",font=("",15), ) 
btn5.grid(column=0, row=0, padx=10)

btn6 = Button(frame2, text="Clear", font=("",15), command=Clear)
btn6.grid(column=0, row=1, padx=10)

btn7 = Button(frame2, text="7", font=("",15))
btn7.grid(column=0, row=2, padx=10)

btn8 = Button(frame2, text="OK", font=("",15), )
btn8.grid(column=0, row=3, padx=10)

scaleVitesse = Scale(frame2, from_=0, to=10, orient=HORIZONTAL, resolution=1)
scaleVitesse.grid(column=0, row=4, padx=10)



root.mainloop()
