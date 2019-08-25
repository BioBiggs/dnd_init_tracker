##Dnd program
from  tkinter import*
from tkinter import messagebox
top = Tk()
top.geometry("1000x1000")


##Functions
##print initiative
init=[]

def add_to_init():
    to_add = initiative_tracker_entry.get()
    init.append(to_add)

def show_init():
    msg = messagebox.showinfo("Initiative order", init)




##Adding stuff to GUI

##Initiative tracker
initiative_tracker_label = Label(top, text="Add to inititiave: ")
initiative_tracker_label.place(x=10,y=100)

initiave_tracker_entry = Entry(top, bd =5)
initiave_tracker_entry.place(x=100, y=100)

init_track_button = Button(top, text = "Add to initiative", command=show_init)
init_track_button.place(x= 210, y=100)

init_show_button = Button(top, text = "Show initiative", command=show_init)
init_show_button.place(x=310, y=100)
##Inv management
stuff_entry = Entry(top, bd=5)
stuff_entry.place(x=100, y=150)

stuff_label = Label(top, text="Add to stuff: ")
stuff_label.place(x=10,y=150)




top.mainloop()
