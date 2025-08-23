import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Registration Form")
root.geometry("400x400")

# Header
header_frame = tk.Frame(root)
header_frame.pack(pady=20)
tk.Label(header_frame, text="Registration From", font=("Arial", 16)).pack(pady=10)

# Form Frame
form_frame = tk.Frame(root)
form_frame.pack(pady=10)

tk.Label(form_frame,text="Enter Name:").grid(row=0,column=0,sticky="w",padx=5,pady=5)
name = tk.StringVar()
tk.Entry(form_frame, textvariable= name,width = 20).grid(row=0,column=1,padx=5,pady=5)

tk.Label(form_frame,text="Enter Email:").grid(row=1,column=0,sticky="w",padx=5,pady=5)
email = tk.StringVar()
tk.Entry(form_frame, textvariable= email,width = 20).grid(row=1,column=1,padx=5,pady=5)

tk.Label(form_frame,text="Enter Address:").grid(row=2,column=0,sticky="w",padx=5,pady=5)
address = tk.StringVar()
tk.Entry(form_frame, textvariable= address,width = 20).grid(row=2,column=1,padx=5,pady=5)

tk.Label(form_frame,text="Enter Password:").grid(row=3,column=0,sticky="w",padx=5,pady=5)
password = tk.StringVar()
tk.Entry(form_frame, textvariable= password,width = 20, show="*").grid(row=3,column=1,padx=5,pady=5)

tk.Label(form_frame, text="Gender:").grid(row=4,column=0,sticky="w",padx=5,pady=5)
gender = tk.StringVar(value = "None")
tk.Radiobutton(form_frame,text="Male", variable=gender,value="Male").grid(row=4,column=1,sticky="w",pady=5)
tk.Radiobutton(form_frame,text="Female", variable=gender,value="Female").grid(row=4,column=1,sticky="e",pady=5)

terms = tk.IntVar()
tk.Checkbutton(form_frame, text="I agree to the Terms & Conditions",variable=terms).grid(row=5,columnspan=2,pady=5)

# Submit Button
submit_frame = tk.Frame(root)
submit_frame.pack(pady=20)

def submit():
    name1 = name.get()
    email1 = email.get()
    address1 = address.get()
    password1 = password.get()
    gender1 = gender.get()
    terms1 = terms.get()

    if not name1 or not email1 or not address1 or not password1 or gender1 == "" or terms1 == 0:
        messagebox.showerror("Error", "Please fill all the fields and accept terms.")
    else:
        messagebox.showinfo("Success",f"Welcome {name1}! Registration complete.")

tk.Button(submit_frame, text="Submit", width=20,bg="green",fg="white", command=submit).pack(pady=5)


root.mainloop()


