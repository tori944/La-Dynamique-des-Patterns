from init import *
from random import *

class Cellule :
    global NbColumn, NbRow, listePattern

    listeCellulesCanv1 = []
    listeCellulesCanv2 = []

    listeIdCentreGroupe = [] # les IDs

    pat = 0

    listeSuivantes = []


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

        # self.canv.create_text(self.coA+10, self.coB+10, text=self.row, fill="white")

        # canvas.tag_bind(self.rec, "<Button-1>", self.clicG) 
        # canvas.tag_bind(self.rec, "<Button-3>", self.clicD)
        self.canv.focus_set()                                  # pour le clavier
        self.canv.bind("<Key>", self.clavier)                  # idem
        #canvas.bind("<KeyPress>", self.clavier)                  # idem
        self.canv.tag_bind(self.rec, "<Button-1>", self.clicG)  # pour le clic gauche
        self.canv.tag_bind(self.rec, "<Button-3>", self.clicD)  # pour le clic gauche
        

    ###### Les Voisines Id ######

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
        
        # idVoisines = [NbColumn-1, NbColumn, NbColumn+1, -1, 1, (-NbColumn)-1, (-NbColumn), (-NbColumn)+1]   # en réalité ce id voisine  = ces_valeurs + self.id

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

        # for i in (idVoisines):          # ne prendre que celle qui figure dans la liste (ne dépasse ni en haut ni en bas)
        #     if 0 <= myId + i < len(Cellule.listeCellulesCanv1): # refaire cette fonction en fonctin des differents canvas
        #         listeVoisinesID.append(myId+i)

        for i in (idVoisines):
            if myId+i >= 0 and myId+i < len(Cellule.listeCellulesCanv1):
                listeVoisinesID.append(myId+i)


        return listeVoisinesID


    #### création des groupes de cellules (carré 3x3) ####


    def voisinesIDGroupe (self):    # renvoi la liste des voisines directes des groupe de 3x3 # et on part du principe pour le moment qu'on fait partie de la liste des groupe ID, on est un centre quoi
        global NbColumn

        idVoisinesGroupe = []  
        myCol = self.get_column()
        groupe = Cellule.listeIdCentreGroupe    # liste d'ID
        myIdName = self.get_id()                # ID dans la liste de toute les cellules
        myIdGroupe = groupe.index(myIdName)     # ID dans la liste du groupe

        presId = [(-NbColumn)//3, NbColumn//3, -1, 1]       # haut , bas,  gauche, droite

        if myCol+2 == NbColumn:
            del presId[-1]
            #print("trop à droite")

        if myCol-1 == 0:
            del presId[2]
            #print("trop à gauche")

        for i in presId: 
            if myIdGroupe+i >= 0 and myIdGroupe+i < len(self.listeIdCentreGroupe): # c'est incompressible incompressible incompressible
                idVoisinesGroupe.append(groupe[myIdGroupe+i])

        # for i in presId:
        #     if 0 <= myIdGroupe+i < len(Cellule.listeIdCentreGroupe): ## nan mais serieux je ne comprend pas cette ligne je n'en veux plus !!
        #         idVoisinesGroupe.append(groupe[myIdGroupe+i])

        # for i in (idVoisines):
        #     if 0 <= myId + i < len(Cellule.listeCellules):
        #         listeVoisinesID.append(myId+i)

        # for i in presId:
            # varId = myIdGroupe+i            # new ID de la liste de groupe
            # varVal = groupe[varId]          # on prend la valeur de la liqte de groupe
            # idVoisinesGroupe.append(varVal) # on l'ajoute à la liste 


        return idVoisinesGroupe
    

    def DessinerPattern(self, idPat):
        global listePattern
        listeVoisines = self.voisinesID()  # juste des ids des voisines
        pattern = listePattern[idPat]

        for i in listeVoisines:
            if pattern[listeVoisines.index(i)] == 1:
                cel = Cellule.listeCellulesCanv1[i]
                cel.set_etat()



    def DessinerTout(self):
        global listePattern
        listeVoisines = self.voisinesID()  # juste des ids des voisines

        self.etatPat = 1

        pattern = listePattern[randrange(0,10)]

        for i in listeVoisines:
            if pattern[listeVoisines.index(i)] == 1:
                cel = Cellule.listeCellulesCanv1[i]
                cel.set_etat()

        listeProchain = self.voisinesIDGroupe()

        for j in listeProchain: # le probmème c'est que c'est exponentielle ?
            cel = Cellule.listeCellulesCanv1[j]
            if cel.etatPat == 0:
                # Cellule.listeSuivantes.append(cel)
                cel.DessinerTout()
        


    def clicG (self, event):

        if self.get_id() in Cellule.listeIdCentreGroupe:
            self.DessinerTout()

            # self.DessinerPattern(Cellule.pat)
        # listeVoisineID = self.voisinesID()
        # for i in listeVoisineID:
        #     cel = Cellule.listeCellulesCanv1[i]
            
        #     # canvas1.itemconfig(cel.rec, fill="blue")
        # print(listeVoisineID)

        # self.set_etat()

        # if self.get_id() in Cellule.listeIdCentreGroupe:
        #     # self.DessinerPattern()
        #     for i in self.voisinesIDGroupe():
        #         cel = Cellule.listeCellulesCanv1[i]
        #         canvas1.itemconfig(cel.rec, fill="orange")
        # else:
        #     print("n'est pas un centre de groupe")

        
    def clicD (self, event):
        print("il y a eu un clic droit")   
        
    def clavier (self, event):
        touche = event.keysym
        print("il y a eu une touche pressé : ", touche)

        