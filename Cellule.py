from init import *
from random import *

class Cellule :
    global NbColumn, NbRow, listePattern

    listeCellulesCanv1 = []
    listeCellulesCanv2 = []

    listeIdCentreGroupe = [] # les IDs

    #### zone de test ####
    pat = 0
    listeSuivantes = []
    #### fin de zone ####

    def __init__(self, coA, coB, column,row, canvName):
        
        self.etat = 0

        self.canv = canvName

        if self.canv == canvas1 :
            Cellule.listeCellulesCanv1.append(self)
            self.id = Cellule.listeCellulesCanv1.index(self)
        else:
            Cellule.listeCellulesCanv2.append(self)
            self.id = Cellule.listeCellulesCanv2.index(self)    


        self.column = column
        self.row = row

        self.coA = coA
        self.coB = coB

        self.etatPat = 0

        self.rec = self.canv.create_rectangle(coA, coB, coA+20, coB+20, fill='black', outline="grey")
        # self.canv.create_text(self.coA+10, self.coB+10, text=self.id, fill="white")

        if self.canv == canvas1:

            if (self.column-1) % 3 == 0 and self.column < NbColumn:
                if (self.row-1) % 3 == 0 and self.row >= 0:
                    Cellule.listeIdCentreGroupe.append(self.id)
                    
                    canvas1.itemconfig(self.rec, fill="dark blue")

        self.canv.tag_bind(self.rec, "<Button-1>", self.clicG)  # pour le clic gauche
        self.canv.tag_bind(self.rec, "<Button-3>", self.clicD)  # pour le clic gauche
        

   

    def get_id (self):
        return self.id 
    
    def get_etat (self):
        return self.etat
    
    def get_column (self):
        return self.column
    
    def get_row (self):
        return self.row

    def set_etat (self):  
        if self.get_etat() == 0:
            self.etat = 1
            self.canv.itemconfig(self.rec, fill="light green") 

        elif self.get_etat() == 1:
            self.etat = 0
            self.canv.itemconfig(self.rec, fill="black") 


    def voisinesID (self): # liste des id des voisines avec moi

        myId = self.get_id()
        myColumn = self.get_column()
        
        idVoisines = [(-NbColumn)-1, (-NbColumn), (-NbColumn)+1, -1, 0, 1, NbColumn-1, NbColumn, NbColumn+1 ]   # en réalité ce id voisine  = ces_valeurs + self.id


        if myColumn == NbColumn-1 :     # si les cellules sont hors du tableau coté droit
            del idVoisines[8]
            del idVoisines[5]
            del idVoisines[2]
        
        if myColumn == 0 :              # si les cellules sont hors du tableau coté gauche
            del idVoisines[6]
            del idVoisines[3]
            del idVoisines[0]

        listeVoisinesID = []

        for i in (idVoisines):  # ne dépasse ni en haut ni en bas 
            if myId+i >= 0 and myId+i < len(Cellule.listeCellulesCanv1):
                listeVoisinesID.append(myId+i)

        return listeVoisinesID


    def voisinesIDGroupe (self):    # renvoie la liste des voisines directes des groupes de 3x3 # et on part du principe pour le moment qu'on fait partie de la liste des groupe ID, on est un centre quoi
        global NbColumn

        idVoisinesGroupe = []  # liste que l'on va renvoyer

        myCol = self.get_column()
        groupe = Cellule.listeIdCentreGroupe    # liste d'ID
        myIdName = self.get_id()                # ID dans la liste de toute les cellules
        myIdGroupe = groupe.index(myIdName)     # ID dans la liste du groupe

        presId = [(-NbColumn)//3, NbColumn//3, -1, 1]       # haut , bas, gauche, droite

        if myCol+2 == NbColumn: # si trop à droite
            del presId[-1]

        if myCol-1 == 0:        # si trop à gauche
            del presId[2]

        for i in presId: 
            if myIdGroupe+i >= 0 and myIdGroupe+i < len(self.listeIdCentreGroupe): # si dépasse de la liste
                idVoisinesGroupe.append(groupe[myIdGroupe+i])  

        return idVoisinesGroupe


    def DessinerPattern(self):
        global listePattern
        self.etatPat = 1

        # pattern = listePattern[3]
        pattern = listePattern[randrange(0,10)]

        listeVoisines = self.voisinesID() # la liste des voisines

        for idV in listeVoisines:
            indexID = listeVoisines.index(idV)
            if pattern[indexID] == 1:
                cel = Cellule.listeCellulesCanv1[idV]
                cel.set_etat()


    def DessinerTout(self):

        self.DessinerPattern()

        voisinesG = self.voisinesIDGroupe()

        Suivantes = []

        for id in voisinesG:
            cel = Cellule.listeCellulesCanv1[id]

            if cel.etatPat == 0 and cel not in Cellule.listeSuivantes:
                Suivantes.append(cel)

        for cel in Suivantes:
            if cel.etatPat == 0:
                cel.etatPat = 1
                root.after(500, cel.DessinerTout)
                # cel.DessinerTout()

        # Suivantes.clear()
        
    def PredirPattern (self):

        VoisineGroupe = self.voisinesIDGroupe()





    def clicG (self, event):
        
        if self.get_id() in Cellule.listeIdCentreGroupe:  # si la cellule est un centre de groupe
            self.DessinerTout()

    def clicD (self, event):
        self.DessinerPattern() 
