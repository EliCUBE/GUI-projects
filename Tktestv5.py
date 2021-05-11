from tkinter import *

top = Tk()
SongList = []


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
    
    B1Main = Button(text = "week 1", bg = "#b00b69", command = week1)
    B1Main.grid(column = 0, row = 2)
    
    B2Main = Button(text = "Week 2", command = week2)
    B2Main.grid(column = 0, row = 3)
    
    B3Main = Button(text = "week 3")
    B3Main.grid(column = 0, row = 4)

def week1():
    def AddSong():
        SongList.append(E1.get())
        E1.delete(0, END)
        
    ClearWindow()
    L1 = Label(top, bg = "#8c919c", text="PlayList generator")
    L1.grid(column= 0, row= 1)

    E1 = Entry(top, bg = "#948723")
    E1.grid(column = 0, row = 2)

    B1 = Button(text="+" ,bg = "cyan", command = AddSong)
    B1.grid(column = 1,row = 2)

    B1 = Button(text="print list",bg = "#8a7e42", command = Print)
    B1.grid(column = 0, row = 3)

    B3 = Button(text="This button will export the list. amazing", bg = "#f54284",  command = ExportList)
    B3.grid(column = 1, row = 3)

    BC = Button(text="Main menu",bg = "#8a7e42", command = MainMenu)
    BC.grid(column = 0, row = 4)

def week2():
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

    B1W2 = Button(text="roll")
    B1W2.grid(column = 1, row = 4)

if __name__ == "__main__":
    MainMenu()
    top.mainloop()
