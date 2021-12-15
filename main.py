import tkinter
import sqlite3
from PIL import ImageTk, Image
from tkinter import Button, filedialog, Label, Menu, Tk, ttk


root = Tk()
menubar = Menu(root)

root.geometry('1920x1080')
root.title("BIONavEdTool")
root.iconbitmap('icons/puget.ico')
frm = ttk.Frame(root, padding=10)
frm.grid()
root.config(menu=menubar)


# Databasing

conn = sqlite3.connect('templates.db')
# Create cursor
c = conn.cursor()

# Create table


# Commit changes
conn.commit()
# Close connection
conn.close()

def open_image():
    global my_image
    root.filename = filedialog.askopenfilename(initialdir="/images", title="Select a BIOS photo",
                                               filetypes=(("png files", "*.png"), ("all files", "*.*")))
    my_image = ImageTk.PhotoImage(Image.open(root.filename))
    my_image_label = Label(image=my_image).grid(column=0, row=0)


filemenu = Menu(menubar, tearoff=0)
#filemenu.add_command(label="Open Template", command=donothing)
#filemenu.add_command(label="Save Template", command=donothing)
filemenu.add_separator()
#filemenu.add_command(label="Load from Stylesheet", command=donothing)
#filemenu.add_command(label="Export to Stylesheet", command=donothing)
filemenu.add_separator()
#filemenu.add_command(label="Export Current BIOS page", command=donothing)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

imagemenu = Menu(menubar, tearoff=0)

imagemenu.add_command(label="Open BIOS Image", command=open_image)
menubar.add_cascade(label="BIOS Image", menu=imagemenu)

helpmenu = Menu(menubar, tearoff=0)
#helpmenu.add_command(label="Help Index", command=donothing)
#helpmenu.add_command(label="About...", command=donothing)
menubar.add_cascade(label="Help", menu=helpmenu)


#my_btn = Button(root, text="Open BIOS image", command=open).grid(column=0, row=0)



if __name__ == '__main__':
    root.mainloop()
