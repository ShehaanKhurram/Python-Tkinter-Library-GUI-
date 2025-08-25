
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog

root = tk.Tk()
root.title("Mini Notepad")
root.geometry("700x500")

# __________ File Functions __________
def New(event = None):
    result = messagebox.askyesno("Warning", "Are you sure you want to create new file without saving current file?")
    if result:
        textbox.delete(1.0,tk.END)

def Open(event = None):
    file = filedialog.askopenfilename(
          filetypes = [("Text File", "*.txt")]
    )
    if file:
        with open(file, "r") as f:
            textbox.delete("1.0", "end-1c")
            textbox.insert(tk.END,f.read())

def Save(event = None):
    file = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    if file:
        with open(file, "w") as f:
            f.write(textbox.get(1.0,tk.END))

# __________ Edit Functions __________
def cut_text(event = None):
    textbox.event_generate("<<Cut>>")

def copy_text(event = None):
    textbox.event_generate("<<Copy>>")

def paste_text(event = None):
    textbox.event_generate("<<Paste>>")

def undo_text(event = None):
    try:
        textbox.edit_undo()
    except:
        pass

def redo_text(event = None):
    try:
        textbox.edit_redo()
    except:
        pass

# __________ About Functions __________
def about_app():
    messagebox.showinfo("About Mini Notepad", "Mini Notepad Developer: Shehaan Khurram\nMade with Tkinter in Python")

#-------------------______________________________________________-------------------
menubar = tk.Menu(root, tearoff=0)

# -------------File Menu
file_menu = tk.Menu(menubar, tearoff=0)
file_menu.add_command(label="New", command=New, accelerator="CTRL+N")
file_menu.add_command(label="Open",command=Open,accelerator="CTRL+O")
file_menu.add_command(label="Save",command=Save,accelerator="CTRL+S")
file_menu.add_separator()
file_menu.add_command(label="Exit", command = root.destroy)
menubar.add_cascade(label="File", menu=file_menu)

# -------------Edit Menu
edit_menu = tk.Menu(menubar, tearoff=0)
edit_menu.add_command(label="Cut", command=cut_text,accelerator="CTRL+X")
edit_menu.add_command(label="Copy", command=copy_text,accelerator="CTRL+C")
edit_menu.add_command(label="Paste", command=paste_text,accelerator="CTRL+V")
edit_menu.add_separator()
edit_menu.add_command(label="Undo", command=undo_text,accelerator="CTRL+Z")
edit_menu.add_command(label="Redo", command=redo_text,accelerator="CTRL+Shif+Z")
menubar.add_cascade(label="Edit", menu=edit_menu)

# -------------Help Menu
help_menu = tk.Menu(menubar, tearoff=0)
help_menu.add_command(label="About", command=about_app)
menubar.add_cascade(label="Help", menu=help_menu)

# -------------Bindings

root.bind("<Control-n>", New)
root.bind("<Control-o>", Open)
root.bind("<Control-s>", Save)
root.bind("<Control-z>", undo_text)
root.bind("<Control-Shift-z>", redo_text)
root.bind("<Control-x>", cut_text)
root.bind("<Control-c>", copy_text)
root.bind("<Control-v>", paste_text)

# textbox to type
textbox = tk.Text(root, wrap = "word", undo=True)
textbox.pack(expand=True, fill="both")

root.config(menu=menubar)
root.mainloop()
