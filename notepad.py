from tkinter import *
from tkinter import filedialog
from tkinter import font

# I thought I had to resort to importing all from tkinter to make MENU work but all I had to do was use
# tk.Menu
# from tkinter import *

# Global var to hold the open status of a file
global Open_Status_Name
Open_Status_Name = FALSE


# creating a gui class so methods do not get confused
class MyGUI:

    def ourcommand(self):
        pass

    # Function called when user chooses new file from file menu
    def newfile(self):
        # Clear current text box contents
        self.textbox.delete("1.0", END)
        # Set title to "New File"
        self.root.title("New File")

        global Open_Status_Name
        Open_Status_Name = FALSE
        self.status_bar.config(text='New File      ')

    def openfile(self):
        # Clear current text box contents
        self.textbox.delete("1.0", END)

        # Open file dialog , conditional statement for if the user presses cancel
        chosen_file = filedialog.askopenfilename(initialdir="C:/users", title="Open File",
                                                 filetypes=(("Text files", ".txt"), ("All files", ".*")))
        if chosen_file and chosen_file != "":
            # Open the chosen file and read all contents into memory
            self.textfile = open(chosen_file, 'r')
            contents = self.textfile.read()
            self.textfile.close()

            # Apply contents to editor
            self.textbox.delete("1.0", END)
            self.textbox.insert(END, contents)

            # Update open status of the file now open
            global Open_Status_Name
            Open_Status_Name = chosen_file
            self.status_bar.config(text=chosen_file + '      ')

    def saveasfileas(self):
        self.textfile = filedialog.asksaveasfilename(defaultextension=".*", title="Save File",
                                                     filetypes=(("Text files", "*.txt"), ("All files", "*.*")))
        if self.textfile:
            self.textfile = open(self.textfile, 'w')
            self.textfile.write(self.textbox.get("1.0", END))
            self.textfile.close()
            self.status_bar.config(text='File Saved      ')

    def savefile(self):
        global Open_Status_Name
        if Open_Status_Name:
            self.textfile = open(Open_Status_Name, 'w')
            self.textfile.write(self.textbox.get("1.0", END))
            self.textfile.close()
        else:
            self.saveasfileas()

    def __init__(self):

        # Creating the main window panel
        self.root = Tk()

        # Setting root window height and width
        # Setting root background color
        self.root.geometry("675x675")
        self.root.config(bg='#B6D8F2')

        # Setting root window title
        self.root.title("TK Notepad")

        # Creating main frame
        self.myframe = Frame(self.root)
        self.myframe.pack()

        # Creating Menus
        self.mymenu = Menu(self.root)
        self.root.config(menu=self.mymenu)
        # Creating file menu entry and adding to root
        self.filemenu = Menu(self.mymenu, tearoff=False)
        self.mymenu.add_cascade(label="File", menu=self.filemenu)
        self.filemenu.add_command(label="New", command=self.newfile)
        self.filemenu.add_command(label="Open", command=self.openfile)
        self.filemenu.add_command(label="Save", command=self.savefile)
        self.filemenu.add_command(label="Save As", command=self.saveasfileas)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Exit", command=self.root.quit)

        # Creating file menu entry and adding to root
        self.editmenu = Menu(self.mymenu, tearoff=False)
        self.mymenu.add_cascade(label="Edit", menu=self.editmenu)
        self.editmenu.add_command(label="Cut", command=self.ourcommand)
        self.editmenu.add_command(label="Copy", command=self.ourcommand)
        self.editmenu.add_command(label="Paste", command=self.ourcommand)
        self.editmenu.add_command(label="Undo", command=self.ourcommand)
        self.editmenu.add_command(label="Redo", command=self.ourcommand)

        # Add Status Bar to bottom of app
        self.status_bar = Label(self.root, text='Ready      ', anchor=E)
        self.status_bar.pack(fill=X, side=BOTTOM, ipady=5)


        # Scrollbar for textbox
        self.textscroll = Scrollbar(self.myframe)
        self.textscroll.pack(side=RIGHT, fill=Y)

        # Creating text area, Pastel colors for the font and background, setup wordwrap
        self.textbox = Text(self.myframe, bg="#F4CFDF", font=('Arial', '18'), fg="#5784BA", wrap=WORD, undo=True)
        self.textbox.config(yscrollcommand=self.textscroll.set)
        self.textbox.pack()

        # Configure scrollbar
        self.textscroll.config(command=self.textbox.yview)

        self.root.mainloop()


MyGUI()
