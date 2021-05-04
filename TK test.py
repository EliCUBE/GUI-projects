from tkinter import *

top = Tk()
SongList = []
def AddSong():
    SongList.append(E1.get())

def Print():
    print(SongList)

L1 = Label(top, text="PlayList generator")
L1.grid(column= 0, row= 1)

E1 = Entry(top, bg = "light blue")
E1.grid(column = 0, row = 2)

B1 = Button(text="add to list" ,bg = "cyan", command = AddSong)
B1.grid(column = 1,row = 2)

B1 = Button(text="print list",bg = "white", command = Print)
B1.grid(column = 1, row = 1)

top.mainloop()
