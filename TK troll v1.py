from tkinter import *
import random


top = Tk()
SongList = []
MyRolls = []


def Print():
    print(SongList)

def ExportList():
    with open('Playlist.txt', 'w') as f:
        for song in SongList:
                f.write("%s\n" % song)

def ClearWindow():
    for LoveAndHappiness in top.winfo_children():
        LoveAndHappiness.destroy()

def MainMenu():
    ClearWindow()
    
    LMain = Label(top, text = "b5 GUIs")
    LMain.grid(column = 0, row = 1)
    
    B1Main = Button(text = "week 1", bg = "#b00b69", bd = "40", command = week1)
    B1Main.grid(column = 0, row = 2)
    
    B2Main = Button(text = "Week 2",bd = "40", command = week2)
    B2Main.grid(column = 0, row = 3)
    
    B3Main = Button(text = "week 3" ,bd = "40",)
    B3Main.grid(column = 0, row = 4)

    Bruh = Button(text = "hell",bd = "40", command = HELL)
    Bruh.grid(column = 2, row = 6)

    temp = Button(text = "temp", command = no)
    temp.grid(column = 2, row = 5)
    
def week1():
    def AddSong():
        SongList.append(E1.get())
        E1.delete(0, END)
        
    ClearWindow()
    L1 = Label(top, bg = "#8c919c", text="PlayList generator")
    L1.grid(column= 0, row= 1)

    E1 = Entry(top, bg = "#948723")
    E1.grid(column = 0, row = 2)

    B1 = Button(text="+" ,bg = "cyan", command = no)
    B1.grid(column = 1,row = 2)

    B1 = Button(text="print list",bg = "#8a7e42", command = no)
    B1.grid(column = 0, row = 3)

    B3 = Button(text="This button will export the list. amazing", bg = "#f54284",  command = no)
    B3.grid(column = 1, row = 3)

    BC = Button(text="Main menu",bg = "#8a7e42", command = MainMenu)
    BC.grid(column = 0, row = 4)

    
    
def week2():
    def RollDice():
        RollTimes = E1W2.get()
        DieType =E2W2.get()

        ClearWindow()

        for x in range(0, int(RollTimes)):
            MyRolls.append(random.randint(1, int(DieType)))

        L3W2 = Label(top, text="here ya rolls, nerd")
        L3W2.grid(column = 0, row = 1)
        
        L4W2 = Label(top, text = MyRolls)
        L4W2.grid(column = 0, row = 2)
        
        B2W2 = Button(text="Back to menu",bg = "pink", command = MainMenu)
        B2W2.grid(column = 0, row = 3)
        
    ClearWindow()
    
    L1W2 = Label(top, text="Dice roller engine")
    L1W2.grid(column=1,row = 1)
    
    L2W2 = Label(text = "# of sides")
    L2W2.grid(column = 0, row = 3)
    
    L3W2 = Label(text = "#of rolls")
    L3W2.grid(column = 2, row = 3)
    
    E1W2 = Entry()
    E1W2.grid(column = 2, row = 2)
    
    E2W2 = Entry()
    E2W2.grid(column = 0, row = 2)

    B1W2 = Button(text="roll", bg = "blue", command = RollDice)
    B1W2.grid(column = 1, row = 4)


def HELL():
    ClearWindow()
    Tr = Button(wraplength=100, justify=LEFT,text = ":trollface::trollface: :trollface::trollface::trollface: :trollface::trollface::trollface:::trollface::trollface:::trollface::trollface:: :trollface:  :trollface: :trollface::trollface::trollface::trollface:::trollface::trollface:: :trollface::trollface::trollface:: :trollface::trollface::trollface:::trollface::trollface:::trollface::trollface:: :trollface: :trollface: :trollface:  :trollface:  :trollface:  :trollface:  :trollface: :trollface: :trollface: :trollface:  :trollface: :trollface:  :trollface:", bg = "#abb06b", )
    Tr.grid(column = 0, row = 1)

    T2 = Button(text = "leave, forever",bd = "40", command = Trolled)
    T2.grid(column = 1, row = 1)


def Trolled():
    ClearWindow()
    
    LaMain = Label(top, text = "No Escape")
    LaMain.grid(column = 0, row = 1)
    
    Ba1Main = Button(text = "week 1", bg = "#b00b69", command = HELL2)
    Ba1Main.grid(column = 0, row = 2)
    
    Ba2Main = Button(text = "Week 2", command = HELL2)
    Ba2Main.grid(column = 0, row = 3)
    
    Ba3Main = Button(text = "week 3", command = HELL2)
    Ba3Main.grid(column = 0, row = 4)

    Bruh = Button(text = "Return", command = HELL2)
    Bruh.grid(column = 2, row = 6)

def HELL2():
    ClearWindow()
    Tr = Button(wraplength=100, justify=LEFT, text = ":trollface::trollface: :trollface::trollface::trollface: :trollface::trollface::trollface:::trollface::trollface:::trollface::trollface:: :trollface:  :trollface: :trollface::trollface::trollface::trollface:::trollface::trollface:: :trollface::trollface::trollface:: :trollface::trollface::trollface:::trollface::trollface:::trollface::trollface:: :trollface: :trollface: :trollface:  :trollface:  :trollface:  :trollface:  :trollface: :trollface: :trollface: :trollface:  :trollface: :trollface:  :trollface:" ,bd = "50", bg = "#abb06b")
    Tr.grid(column = 0, row = 1,)

    T2 = Button(text = "leave, for real this time",  command = TROLL2)
    T2.grid(column = 1, row = 1)

def TROLL2():
    ClearWindow()
    
    LaMain = Label(top, text = "There is no return")
    LaMain.grid(column = 0, row = 1)
    
    Ba1Main = Button(text = "Give up", bg = 'red', command = TROLL2)
    Ba1Main.grid(column = 0, row = 2)
    
    Ba2Main = Button(text = "Give up", bg = 'red', command = TROLL2)
    Ba2Main.grid(column = 0, row = 3)
    
    Ba3Main = Button(text = "Give up", bg = 'red', command = TROLL2)
    Ba3Main.grid(column = 0, row = 4)


def no():
    ClearWindow()
    
    Ba3Main = Button(text = "U shoukd have never come here", bg = 'red')
    Ba3Main.grid(column = 0, row = 1)

    Ba3Main = Button(text = "there is no returning", bg = 'red')
    Ba3Main.grid(column = 0, row = 2)

    Ba3Main = Button(text = "you will be destroyed", bg = 'red')
    Ba3Main.grid(column = 0, row = 3)

    Ba3Main = Button(text = "to escape you must answer this riddle", bg = 'red')
    Ba3Main.grid(column = 0, row = 4)

    Ba3Main = Button(text = "RIDDLE", bg = 'red')
    Ba3Main.grid(column = 0, row = 5)

    Ba3Main = Button(text = "a mistake could be the last one you male", bg = 'red', command = crash)
    Ba3Main.grid(column = 0, row = 6)




def crash():
    ferd = random.randint(0,5)
    if ferd == 1:
        print("you should have never come")
    if ferd == 2:
        print("why didnt you leave")
    if ferd == 3:
        print("YOU HAVE LOST")
    if ferd == 4:
        print("you should have lsitened better")
    if ferd == 5:
        print("perhaps next time you wont be a fool")
    crash()
    



    
if __name__ == "__main__":
    MainMenu()
    top.mainloop()
