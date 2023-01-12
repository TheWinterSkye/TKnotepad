from tkinter import *
from tkinter import filedialog
from tkinter import font

# Global var to hold the open status of a file
global Open_Status_Name
Open_Status_Name = FALSE


def ourcommand():
    pass


# Function called when user chooses new file from file menu
def newfile():
    # Clear current text box contents
    textbox.delete("1.0", END)
    # Set title to "New File"
    root.title("New File")

    global Open_Status_Name
    Open_Status_Name = FALSE
    status_bar.config(text='New File      ')


def openfile():

    # Open file dialog , conditional statement for if the user presses cancel
    chosen_file = filedialog.askopenfilename(initialdir="C:/users", title="Open File",
                                             filetypes=(("Text files", ".txt"), ("All files", ".*")))
    if chosen_file and chosen_file != "":
        # Open the chosen file and read all contents into memory
        # self.textfile = open(chosen_file, 'r')
        # contents = self.textfile.read()
        # self.textfile.close()
        with open(chosen_file, 'r') as contents:
            textbox.delete("1.0", END)
            size_to_read = 100
            f_contents = contents.read(size_to_read)

            while len(f_contents) > 0:
                textbox.insert(END, f_contents)
                f_contents = contents.read(size_to_read)

        # Apply contents to editor



    # Update open status of the file now open
    global Open_Status_Name
    Open_Status_Name = chosen_file
    status_bar.config(text=chosen_file + '      ')


def saveasfileas():
    textfile = filedialog.asksaveasfilename(defaultextension=".*", title="Save File",
                                            filetypes=(("Text files", "*.txt"), ("All files", "*.*")))
    if textfile:
        with open(textfile, 'w') as textfile:
            textfile.write(textbox.get("1.0", END))
        # textfile = open(textfile, 'w')
        # textfile.write(textbox.get("1.0", END))
        # textfile.close()
        status_bar.config(text='File Saved      ')


def savefile():
    global Open_Status_Name
    if Open_Status_Name:
        with open(Open_Status_Name, 'w') as textfile:
            textfile.write(textbox.get("1.0", END))

        # textfile = open(Open_Status_Name, 'w')
        # textfile.write(textbox.get("1.0", END))
        # textfile.close()
    else:
        saveasfileas()


# Creating the main window panel
root = Tk()

# Setting root window height and width
# Setting root background color
root.geometry("675x675")
root.config(bg='#B6D8F2')

# Setting root window title
root.title("TK Notepad")

# Creating main frame
myframe = Frame(root)
myframe.pack()

# Creating Menus
mymenu = Menu(root)
root.config(menu=mymenu)
# Creating file menu entry and adding to root
filemenu = Menu(mymenu, tearoff=False)
mymenu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New", command=newfile)
filemenu.add_command(label="Open", command=openfile)
filemenu.add_command(label="Save", command=savefile)
filemenu.add_command(label="Save As", command=saveasfileas)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)

# Creating file menu entry and adding to root
editmenu = Menu(mymenu, tearoff=False)
mymenu.add_cascade(label="Edit", menu=editmenu)
editmenu.add_command(label="Cut", command=ourcommand)
editmenu.add_command(label="Copy", command=ourcommand)
editmenu.add_command(label="Paste", command=ourcommand)
editmenu.add_command(label="Undo", command=ourcommand)
editmenu.add_command(label="Redo", command=ourcommand)

# Add Status Bar to bottom of app
status_bar = Label(root, text='Ready      ', anchor=E)
status_bar.pack(fill=X, side=BOTTOM, ipady=5)

# Scrollbar for textbox
textscroll = Scrollbar(myframe)
textscroll.pack(side=RIGHT, fill=Y)

# Creating text area, Pastel colors for the font and background, setup wordwrap
textbox = Text(myframe, bg="#F4CFDF", font=('Arial', '18'), fg="#5784BA", wrap=WORD, undo=True)
textbox.config(yscrollcommand=textscroll.set)
textbox.pack()

# Configure scrollbar
textscroll.config(command=textbox.yview)

root.mainloop()
