##Dnd program
from tkinter import *
from tkinter import messagebox
import random 
top = Tk()
top.geometry("1000x1000")






##INITIATIVE SHIT

###adding text box
init_box = Text(top, width=30)
init_box.place(x=570,y=60)
##Sorting function, sort by the number after the comma
def get_order(text):
    order = text.split(",")
    return int(order[1])

##Empty list for storing init
init=[]
def add_to_init():
    ##Retrieve the text from the entry box
    to_add = initiative_tracker_entry.get()
    ##Add to list
    init.append(to_add)
    ##Delete text from entry box
    initiative_tracker_entry.delete(0,END)
    ##Resets text box
    init_box.delete(1.0, END)
    ##Sorts list using get_order
    init.sort(key=get_order, reverse=True)
    ##Prints with new line 
    for i in init:
        init_box.insert(END, i + '\n')
##Clears init
def clear_the_init():
    init.clear()
    init_box.delete(1.0,END)


##Buttons 
initiative_tracker_label = Label(top, text="Add to initiative (Name, initiative): ")
initiative_tracker_label.place(x=570,y=30)

initiative_tracker_entry = Entry(top, bd =5)
initiative_tracker_entry.place(x=760, y=30)

init_track_button = Button(top, text = "Add to initiative", command=add_to_init)
init_track_button.place(x= 900, y=30)


clear_init = Button(top, text = "Clear initiative", command=clear_the_init)
clear_init.place(x=570, y=450)



##STATS
##Defining a class, which has a name and 6 numbers which correspond to stats
def set_stats():
        stat_list = []
        for i in range(0,6):
            roll1 = random.randint(1,6)
            roll2 = random.randint(1,6)
            roll3 = random.randint(1,6)
            stat = roll1 + roll2 + roll3 
            stat_list.append(stat)
        return stat_list
            
##Monster dictionary
mons = {}
mon_buttons =[]
encounter_mons=[]
def add_to_encounter(to_add_to_encounter):
    encounter_mons.append(to_add_to_encounter)
    ##Resets text box
    encounter_box.delete(1.0, END)
    ##Prints with new line 
    for i in encounter_mons:
        encounter_box.insert(END, i + " " + str(mons[i]) + '\n')

        
def make_mon_buttons():
    for i in mon_buttons:
        i.destroy()
    starting_pos = 90    
    for i in mons:
        encounter_button = Button(top, text="Add " + i + " to Encounters", command=lambda: add_to_encounter(i))
        mon_buttons.append(encounter_button)
        encounter_button.place(x=430, y=starting_pos)
        starting_pos += 30

def add_to_mons():
    mon_name = add_mon_entry.get()
    mons[mon_name] = set_stats()
    add_mon_entry.delete(0,END)
    ##Resets text box
    mon_box.delete(1.0, END)
    ##Prints with new line 
    for x,y in mons.items():
        mon_box.insert(END, x + " " + str(y) + '\n')
    make_mon_buttons()

def clear_mons():
    mons.clear()
    mon_box.delete(1.0,END)
    for i in mon_buttons:
        i.destroy()





#manually add a monster
add_mon_label = Label(top, text="Add a Monster: ")
add_mon_label.place(x=10, y=30)

add_mon_entry = Entry(top, bd=5)
add_mon_entry.place(x=150,y=30)

add_mon_button = Button(top, text="Add Monster", command = add_to_mons)
add_mon_button.place(x=290, y=30)


stats_label = Label(top, text="Str, Dex, Con, Int, Wis, Char")
stats_label.place(x=45, y=60)

mon_box = Text(top, width=50)
mon_box.place(x=10,y=90)

clear_mon_button = Button(top, text="Clear Monsters", command=clear_mons)
clear_mon_button.place(x=10, y=480)




##Building an encounter
encounter_box = Text(top, width= 100)
encounter_box.place(x=10, y=600)


def ROLL_IT():
    for i in encounter_mons:
        ROLLED = random.randint(1,20)
        i = str(i + ", " + str(ROLLED))
        init.append(i)
        init_box.delete(1.0, END)
        ##Sorts list using get_order
        init.sort(key=get_order, reverse=True)
        ##Prints with new line 
        for i in init:
            init_box.insert(END, i + '\n')

def clear_encounters():
    encounter_mons.clear()
    encounter_box.delete(1.0,END)
    

ROLL_IT_BUTTON = Button(text="ROLL FOR INITIATIVE", command=ROLL_IT, height=15)
ROLL_IT_BUTTON.place(x=830, y=600)


clear_encounter_button = Button(top, text="Clear Encounter", command=clear_encounters)
clear_encounter_button.place(x=830, y=900)


top.mainloop()
