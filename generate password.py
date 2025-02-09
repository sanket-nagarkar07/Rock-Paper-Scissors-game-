from tkinter import *
from random import randint     #to take random numbers 

root=Tk()
root.title('Strong Password Generator')   # shows Title 
root.geometry("500x300")          


def new_rand():
    #clear our entry box
    pw_entry.delete(0,END)

    #get pw length and convert to integer
    pw_length = int(my_entry.get())

    #create variable to hold our password
    my_password =''

    #Loop through passwod length 
    for x in range(pw_length):
        my_password += chr(randint(33,126))

    #output password to the screen
    pw_entry.insert(0, my_password)

def clipper():
    #clear the clipboard
    root.clipboard_clear()
    #copy to clipboard 
    root.clipboard_append(pw_entry.get())

#label frame

lf=LabelFrame(root, text='how many charecters?')
lf.pack(pady=20)

#create entry box to designate number of characters

my_entry =Entry(lf,font='Helvetica 24 bold')
my_entry.pack(pady=20,padx=20)

#create entry box for our returned password 
pw_entry = Entry(root,text='',font='Helvetica 24 bold')
pw_entry.pack(pady=20)

# create frame for our buttons
my_frame = Frame(root)
my_frame.pack(pady=20)

#create our buttons 
my_buttons=Button(my_frame,text='Generate Strong Password ' , command=new_rand)
my_buttons.grid(row=0,column=0 ,padx=10)

clip_buttons=Button(my_frame,text='copy to clipborad ' , command=clipper)
clip_buttons.grid(row=0,column=1 ,padx=20)
root.mainloop()