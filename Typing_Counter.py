
import tkinter as tk

root = tk.Tk()
root.geometry("400x400")
root.title("Typing Counter")
root.config(bg="lightyellow")

label1 = tk.Label(root,text="Enter Something",font=("Arial",16), bg="lightyellow")
label1.pack(pady=30)


textbox1 = tk.Text(root,height=10,width=25)
textbox1.pack(pady=5)

def count(event=None):
    count = len(textbox1.get("1.0","end-1c"))
    counter_label.config(text=f"Characters: {count}")

textbox1.bind("<KeyRelease>", count)

bottom_frame = tk.Frame(root, bg="lightyellow")
bottom_frame.pack(side="bottom",fill="x")

counter_label = tk.Label(bottom_frame,text="Characters: 0", font=("Arial", 14), bg="lightyellow")
counter_label.pack(side="top",pady=5)

# Exit Button
def exit_function():
    root.destroy()

exit_button = tk.Button(bottom_frame, text="Exit", command=exit_function, bg="green", width=10,font=("Arial", 10))
exit_button.pack(side="bottom",pady=20)

root.mainloop()