##Dnd program
from tkinter import *
from tkinter import messagebox
import random
from operator import attrgetter
top = Tk()
top.geometry("1000x1000")



##Make a class that contains name, stats, attack, initiative 
class NPC:
    def __init__(self,name):
        self.name = name
        self.stats = self.set_stats()
        self.attack = ""
        self.init = 0
        self.HP = 0
        
    def set_stats(self):
        self.stat_list = []
        for i in range(0,6):
            self.roll1 = random.randint(1,6)
            self.roll2 = random.randint(1,6)
            self.roll3 = random.randint(1,6)
            self.stat = self.roll1 + self.roll2 + self.roll3 
            self.stat_list.append(self.stat)
        return self.stat_list
    def print_info(self):
        return(str(self.name + ": " + str(self.stats)) +" " + self.attack + " " +str(self.HP))

class PC:
    def __init__(self, name, init):
        self.name = name
        self.init = init
        self.HP = "NA"
        
mons = []
mon_buttons =[]
encounter_mons=[]

def add_to_mons():
    mon_name = add_mon_entry.get()
    mons.append(NPC(str(mon_name)))
    add_mon_entry.delete(0,END)
    ##Resets text box
    mon_box.delete(1.0, END)
    ##Prints with new line
    for i in mons:
        mon_box.insert(END, i.print_info() + '\n')
    make_mon_buttons()



def read_in_mons():
    file = open("demo_monsters.txt","r")
    lines = file.readlines()
    for i in lines:
        i=str(i)
        i = i.split()
        to_add_to_mons = NPC(i[0])
        to_add_to_mons.stats = i[1:6]
        to_add_to_mons.attack = i[7]
        to_add_to_mons.HP = i[8]
        mons.append(to_add_to_mons)
    mon_box.delete(1.0, END)
    ##Prints with new line
    for i in mons:
        mon_box.insert(END, i.print_info() + '\n')
    make_mon_buttons()




def make_mon_buttons():
    for i in mon_buttons:
        i.destroy()
    starting_pos = 90    
    for i in mons:
        encounter_button = Button(top, text="Add " + str(i.name) + " to Encounters", command=lambda i=i: add_to_encounter(i))
        mon_buttons.append(encounter_button)
        encounter_button.place(x=430, y=starting_pos)
        starting_pos += 30

def clear_mons():
    mons.clear()
    mon_box.delete(1.0,END)
    for i in mon_buttons:
        i.destroy()



##STATS

            
##Monster dictionary

def add_to_encounter(to_add_to_encounter):
    encounter_mons.append(to_add_to_encounter)
    ##Resets text box
    encounter_box.delete(1.0, END)
    ##Prints with new line 
    for i in encounter_mons:
        encounter_box.insert(END, i.print_info() + '\n')

        

##Building an encounter
encounter_box = Text(top, width= 100)
encounter_box.place(x=10, y=600)

def ROLL_IT():
    for i in encounter_mons:
        ROLLED = random.randint(1,20)
        i.init = ROLLED
        init.append(i)
        init_box.delete(1.0, END)
        ##Sorts list using get_order
        init.sort(key=attrgetter("init"), reverse=True)
        ##Prints with new line 
        for i in init:
            init_box.insert(END, i.name + " Init: " +str(i.init)  + " HP: " + str(i.HP)  + '\n')

def clear_encounters():
    encounter_mons.clear()
    encounter_box.delete(1.0,END)
    
##INITIATIVE SHIT

###adding text box
init_box = Text(top, width=30)
init_box.place(x=570,y=60)
##Empty list for storing init
init=[]
def add_to_init():
    ##Retrieve the text from the entry box
    to_add = initiative_tracker_entry.get()
    to_add = to_add.split()
    ##Add to list
    init.append(PC(to_add[0],int(to_add[1])))
    ##Delete text from entry box
    initiative_tracker_entry.delete(0,END)
    ##Resets text box
    init_box.delete(1.0, END)
    ##Sorts list using get_order
    init.sort(key=attrgetter("init"), reverse=True)
    ##Prints with new line 
    for i in init:
        init_box.insert(END, i.name + " Init: " +str(i.init)  + " HP: " + str(i.HP)  + '\n')

##Clears init
    
def clear_the_init():
    init.clear()
    init_box.delete(1.0,END)





##Buttons 

ROLL_IT_BUTTON = Button(text="ROLL FOR INITIATIVE", command=ROLL_IT, height=15)
ROLL_IT_BUTTON.place(x=830, y=600)


clear_encounter_button = Button(top, text="Clear Encounter", command=clear_encounters)
clear_encounter_button.place(x=830, y=900)


initiative_tracker_label = Label(top, text="Add to initiative (Name, initiative): ")
initiative_tracker_label.place(x=570,y=30)

initiative_tracker_entry = Entry(top, bd =5)
initiative_tracker_entry.place(x=760, y=30)

init_track_button = Button(top, text = "Add to initiative", command=add_to_init)
init_track_button.place(x= 900, y=30)


clear_init = Button(top, text = "Clear initiative", command=clear_the_init)
clear_init.place(x=570, y=450)

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


read_in_mons()



top.mainloop()
