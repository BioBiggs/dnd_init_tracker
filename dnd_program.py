##Dnd program
from  tkinter import*
from tkinter import messagebox
import re
top = Tk()
top.geometry("1000x1000")


###adding text box
text_box = Text(top, width=50)
text_box.place(x=540,y=100)

def get_order(text):
    order = text.split(",")
    return int(order[1])

init=[]
def add_to_init():
    to_add = initiative_tracker_entry.get()
    init.append(to_add)
    initiative_tracker_entry.delete(0,END)
    ##Resets text box
    text_box.delete(1.0, END)
    init.sort(key=get_order)
    for i in init:
        text_box.insert(END, i + '\n')

def clear_the_init():
    init.clear()
    text_box.delete(1.0,END)
    
initiative_tracker_label = Label(top, text="Add to initiative (Name, initiative): ")
initiative_tracker_label.place(x=10,y=100)

initiative_tracker_entry = Entry(top, bd =5)
initiative_tracker_entry.place(x=200, y=100)

init_track_button = Button(top, text = "Add to initiative", command=add_to_init)
init_track_button.place(x= 340, y=100)


clear_init = Button(top, text = "Clear initiative", command=clear_the_init)
clear_init.place(x=540, y=500)




#init_show_button = Button(top, text = "Show initiative", command=show_init)
#init_show_button.place(x=310, y=100)



##Inv management
#stuff_entry = Entry(top, bd=5)
#stuff_entry.place(x=100, y=150)

#stuff_label = Label(top, text="Add to stuff: ")
#stuff_label.place(x=10,y=150)


top.mainloop()
