def login():
    p = phone_entry.get()
    pas = password_entry.get()

    if p == "9745702074" and pas == "amrit@221":
        login_interface = Toplevel()
        login_interface.title("Clinic Management System")
        login_interface.geometry("600x400")
        login_interface.configure(bg="blue")
        after_login_text=Label(login_interface, text="WELCOME TO MY WEB APPLICATION", fg="red", bg="blue", font=("Arial", 18))
        after_login_text.place(x=30, y=30)
    elif not p or not pas:
        messagebox.showerror("Login Failed", "Enter both phone number and password")
    else:
        messagebox.showerror("Login Failed", "Invalid phone number or password")

# ------------------ Register Function ------------------
def register():
    window = Toplevel()
    window.title("Register")
    window.geometry("600x400")
    window.configure(bg="light blue")
    window.resizable(False, False)

    # Create frame
    frame2 = Frame(window, bg="purple")
    frame2 = Frame(window, bg="light blue")
    frame2.place(relx=0.5, rely=0.5, anchor="center", width=600, height=400)

    # Full Name
    full_name = Label(frame2, text="Full Name:", bg="purple", fg="white", font=("Arial", 16))
    full_name = Label(frame2, text="Full Name:", bg="white", fg="black", font=("Arial", 16))
    full_name.place(x=60, y=30)
    name_entry = Entry(frame2, font=("Arial", 16), bg="yellow", fg="black",width=25)
    name_entry.place(x=210, y=30)
    name_entry = Entry(frame2, font=("Arial", 16), bg="white", fg="black",width=25)
    name_entry.place(x=245, y=30)

    # Phone
    phone = Label(frame2, text="Phone:", bg="purple", fg="white", font=("Arial", 16))
    phone = Label(frame2, text="Phone:", bg="white", fg="black", font=("Arial", 16))
    phone.place(x=60, y=80)
    phone_entry = Entry(frame2, font=("Arial", 16),bg="yellow", fg="black", width=25)
    phone_entry.place(x=210, y=80)
    phone_entry = Entry(frame2, font=("Arial", 16),bg="white", fg="black", width=25)
    phone_entry.place(x=245, y=80)

    # Email
    email = Label(frame2, text="Email:", bg="purple", fg="white", font=("Arial", 16))
    email.place(x=60, y=130)
    email_entry = Entry(frame2, font=("Arial", 16), bg="yellow", fg="black", width=25)
    email_entry.place(x=210, y=130)
    # Date of Birth
    birth = Label(frame2, text="Date of Birth:", bg="white", fg="black", font=("Arial", 16))
    birth.place(x=60, y=130)
    birth_entry = Entry(frame2, font=("Arial", 16), bg="white", fg="black", width=25)
    birth_entry.place(x=245, y=130)

    #Gender
    gender = Label(frame2, text="Gender:", bg="purple", fg="white", font=("Arial", 16))
    gender.place(x=60, y=180)
    gender_entry = Entry(frame2, font=("Arial", 16), bg="yellow", fg="black", width=25)
    gender_entry.place(x=210, y=180)

    gender_label = Label(frame2, text="Gender:", bg="white", fg="black", font=("Arial", 16))
    gender_label.place(x=60, y=180)

    gender_var = StringVar()
    gender_var.set("Male")

    male_rb = Radiobutton(frame2, text="Male", variable=gender_var, value="Male", font=("Arial", 12), bg="white", fg="black", selectcolor="white")
    male_rb.place(x=245, y=180)

    female_rb = Radiobutton(frame2, text="Female", variable=gender_var, value="Female", font=("Arial", 12), bg="white", fg="black", selectcolor="white")
    female_rb.place(x=320, y=180)

    other_rb = Radiobutton(frame2, text="Other", variable=gender_var, value="Other", font=("Arial", 12), bg="white", fg="black", selectcolor="white")
    other_rb.place(x=410, y=180)


    # Password
    password1 = Label(frame2, text="Password:", bg="purple", fg="white", font=("Arial", 16))
    password1 = Label(frame2, text="Password:", bg="white", fg="black", font=("Arial", 16))
    password1.place(x=60, y=230)
    password1_entry = Entry(frame2, font=("Arial", 16), show="*", bg="yellow", fg="black", width=25)
    password1_entry.place(x=210, y=230)
    password1_entry = Entry(frame2, font=("Arial", 16), show="*", bg="white", fg="black", width=25)
    password1_entry.place(x=245, y=230)

    # Confirm Password
    confirm_pass = Label(frame2, text="Confirm Password:", bg="purple", fg="white", font=("Arial", 16))
    confirm_pass = Label(frame2, text="Confirm Password:", bg="white", fg="black", font=("Arial", 16))
    confirm_pass.place(x=60, y=280)
    password2_entry = Entry(frame2, font=("Arial", 16), show="*", bg="yellow", fg="black", width=25)
    password2_entry.place(x=210, y=280)
    password2_entry = Entry(frame2, font=("Arial", 16), show="*", bg="white", fg="black", width=25)
    password2_entry.place(x=245, y=280)


    def popup():
        n = name_entry.get()
        g= gender_var.get()
        ph = phone_entry.get()
        e = email_entry.get()
        g = gender_entry.get()
        d = birth_entry.get()

        pass1 = password1_entry.get()
        pass2 = password2_entry.get()

        if not n or not ph or not e or not g or not pass1 or not pass2:
        if not n or not ph or not d or not g or not pass1 or not pass2:
            messagebox.showerror("Error", "Fill all the information 😥")
            return

@@ -92,15 +105,15 @@
        messagebox.showinfo("Congratulations 🎉", "Registered Successfully!")
        name_entry.delete(0, END)
        phone_entry.delete(0, END)
        email_entry.delete(0, END)
        gender_entry.delete(0, END)
        birth_entry.delete(0, END)
        gender_var.delete(0, END)
        password1_entry.delete(0, END)
        password2_entry.delete(0, END)

    btn_register2=Button(frame2, text="REGISTER", font=("Arial", 16), fg="blue", command=popup)
    btn_register2.place(x=225, y=330)

# ------------------ Login Frame ------------------
# ------------------ Login Frame -----------
frame1 = Frame(root, bg="white")
frame1.place(relx=0.5, rely=0.5, anchor="center", width=700, height=450)

@@ -142,4 +155,4 @@
btn_register1=Button(frame1, text="Register", font=("Arial", 14), fg="green",command= register)
btn_register1.place(x=386, y=360)

root.mainloop()
root.mainloop()