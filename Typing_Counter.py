
import tkinter as tk

root = tk.Tk()
root.geometry("400x400")
root.title("Typing Counter")
root.config(bg="lightyellow")

label1 = tk.Label(root,text="Enter Something",font=("Arial",16), bg="lightyellow")
label1.pack(pady=30)


textbox1 = tk.Text(root,height=10,width=30, wrap="word")
textbox1.pack(pady=5)

def word_count():
    user_text = textbox1.get("1.0","end-1c").strip() 
    if not user_text:
        return 0
    return len(user_text.split())

def count(event=None):
    w_count = word_count()
    ch_count = len(textbox1.get("1.0","end-1c"))
    words_label.config(text=f"Words: {w_count}")
    counter_label.config(text=f"Characters: {ch_count}")

textbox1.bind("<KeyRelease>", count)

bottom_frame = tk.Frame(root, bg="lightyellow")
bottom_frame.pack(side="bottom",fill="x")

words_label = tk.Label(bottom_frame,text="Words: 0", font=("Arial", 14), bg="lightyellow")
words_label.pack(side="top",pady=5)

counter_label = tk.Label(bottom_frame,text="Characters: 0", font=("Arial", 14), bg="lightyellow")
counter_label.pack(side="top",pady=5)

def exit_function():
    root.destroy()

exit_button = tk.Button(bottom_frame, text="Exit", command=exit_function, bg="green", fg="white", width=10,font=("Arial", 10))
exit_button.pack(side="bottom",pady=20)

root.mainloop()

