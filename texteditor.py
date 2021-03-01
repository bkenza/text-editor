import sys
from tkinter import *
from tkinter import filedialog

####################
# FUNCTIONS #
####################


def saveas():
    global text
    t = text.get("1.0", "end-1c")
    savelocation = filedialog.asksaveasfilename()
    file1 = open(savelocation, "w+")
    file1.write(t)
    file1.close()


def darktheme():
    global text
    text.config(background='black', foreground='white',
                insertbackground='white')


def lighttheme():
    global text
    text.config(background='white', foreground='black',
                insertbackground='black')


def FontHelvetica():
    global text
    text.config(font="Helvetica")


def FontCourier():
    global text
    text.config(font="Courier")


def FontArial():
    global text
    text.config(font="Arial")


def FontTimes():
    global text
    text.config(font='Times')

#########################
    # TEXT EDITOR
#########################


# Create text editor
text_editor = Tk("Kenza's text editor")

# Add text widget
text = Text(text_editor)
text.grid()

# Add save button
button = Button(text_editor, text="Save", command=saveas)
button.grid(row=1, column=1)


# Dark mode
theme = Button(text_editor, text="Dark", command=darktheme)
theme.grid(row=1, column=2)

# Light mode
theme = Button(text_editor, text="Light", command=lighttheme)
theme.grid(row=1, column=3)


# Add font menu
font = Menubutton(text_editor, text="Font")
font.grid(row=1, column=4)
font.menu = Menu(font, tearoff=0)
font["menu"] = font.menu
Helvetica = IntVar()
Arial = IntVar()
Times = IntVar()
Courier = IntVar()

font.menu.add_checkbutton(label="Courier", variable=Courier,
                          command=FontCourier)
font.menu.add_checkbutton(label="Helvetica", variable=Helvetica,
                          command=FontHelvetica)
font.menu.add_checkbutton(label="Arial", variable=Arial,
                          command=FontArial)
font.menu.add_checkbutton(label="Times", variable=Times,
                          command=FontTimes)


text_editor.mainloop()
