from tkinter import *
from tkinter import messagebox
from tkinter import ttk 
from PIL import Image, ImageTk
from change_pass import change_password
import sqlite3

def admin_dashboard():
    # ------- Admin Dashboard ---------
    
    admin = Toplevel()
    admin.title("Admin Dashboard")
    admin.geometry("1400x1100")
    admin.configure(bg="light blue")

    admin_frame = Frame(admin, bg="white")
    admin_frame.place(relx=0.5, rely=0.5, anchor="center", width=880, height=560)




    # ------------------ All Functions ------------------
    def view_appointment():
        appointment1 = Toplevel() 
        appointment1.title("View appointment")
        appointment1.geometry("600x300")
        appointment1.resizable(False, False)
        appointment1.config(bg="light blue")

        style = ttk.Style(appointment1)
        style.theme_use('clam')
        style.configure ("Treeview", background= "white" , foreground = "black", fieldbackground="gray")
        
        # Create a table using Treeview
        table = ttk.Treeview(appointment1)
        table["columns"] = ("Doctor", "Date", "Time", "Phone")

        table.column("#0", width=0, stretch=NO)  # Hide default column
        table.column("Doctor", width=170)
        table.column("Date", width=100)
        table.column("Time", width=70)
        table.column("Phone", width=150)

        table.heading("#0", text="")
        table.heading("Doctor", text="Doctor")
        table.heading("Date", text="Date")
        table.heading("Time", text="Time")
        table.heading("Phone", text="Phone")

        # Place the table using place()
        table.place(x=40, y=50, width=500, height=200)

        conn = sqlite3.connect("clinic_management_system.db")
        c = conn.cursor()

        c.execute("SELECT doctor, date, time, phone FROM appointment")
        result5 = c.fetchall()
        conn.close()

            # Insert records into the table
        for i in result5:
            doctor, date, time, phone = i
            table.insert("", "end", values=(doctor, date, time, phone))
        
    def logout():
        admin.destroy()
        
    def manage_doctors():
        doctor = Toplevel(admin)
        doctor.title("Manage Doctors")
        doctor.geometry("580x750")
        doctor.configure(bg="light blue")
        doctor.resizable(False, False)

        add_frame = Frame(doctor, bg="white") 
        add_frame.place(relx=0.15, rely=0.1, width=390, height=280) 

        def add_doc():
            name_doc= add_name_entry.get()
            spec_doc = add_spec_entry.get()
            phone_doc = number_spec_entry.get()
            if not name_doc or not spec_doc or not phone_doc:
                messagebox.showwarning("Warning", "All fields are required")
                return

            conn = sqlite3.connect("clinic_management_system.db")
            cursor = conn.cursor()
            cursor.execute('''
                 INSERT INTO doctor (name, phone, specialization)
                VALUES (?, ?, ?)
                ''', (name_doc, phone_doc, spec_doc))
            conn.commit()
            conn.close()    

            messagebox.showinfo("Success", "Doctor added successfully")
            add_name_entry.delete(0, END)
            add_spec_entry.delete(0, END)
            number_spec_entry.delete(0, END)
            doctor.destroy()

        def delete_doc():
            phone_num2 = phone_num1_entry.get()
            if not phone_num2:
                messagebox.showwarning("Warning", "Phone number is required")
                return

            conn = sqlite3.connect("clinic_management_system.db")
            c= conn.cursor()

            c.execute("SELECT * FROM doctor WHERE phone = ?", (phone_num2,))
            result1=c.fetchone()
            conn.commit()
            conn.close()
            if result1!=None:
                conn= sqlite3.connect("clinic_management_system.db")
                c = conn.cursor()
                c.execute('''
                          DELETE FROM doctor WHERE phone = ?
                          ''', (phone_num2,))
                conn.commit()
                conn.close()
                messagebox.showinfo("Success", "Doctor removed successfully")
                phone_num1_entry.delete(0, END)
                doctor.destroy()

            else:
                messagebox.showerror("Warning", "Number not found")



        # ---------- Add Doctor Section ----------
        add_label = Label(add_frame, text="Add Doctor",bg= "white", fg="black" ,font=("Arial", 18, "bold"))
        add_label.place(x=117,y=10)

        name_label = Label(add_frame, text="Name:", fg="black",bg="white", font=("Arial", 13))
        name_label.place(x=20, y=58)
        add_name_entry = Entry(add_frame, width=20,bg="white", fg="black")
        add_name_entry.place(x=145, y=60)

        spec_label = Label(add_frame, text="Specialization:", fg="black",bg="white",font=("Arial", 13))
        spec_label.place(x=20, y=105)
        add_spec_entry = Entry(add_frame, width=20,bg="white", fg="black")
        add_spec_entry.place(x=145, y=108)

        number_label = Label(add_frame, text="Phone Number:", fg="black", bg="white", font=("Arial", 13))
        number_label.place(x=20, y=155)
        number_spec_entry = Entry(add_frame, width=20,bg="white", fg="black")
        number_spec_entry.place(x=145, y=153)

    
        btn_save = Button(add_frame, text="Save", fg="Green", width=8, font=("Arial", 16), command=add_doc)
        btn_save.place(x=60, y=215)

        cancel_btn2 = Button(add_frame, text="Cancel", font=("Segoe UI", 14),fg="red", width=7, command=doctor.destroy)
        cancel_btn2.place(x=225, y=215)
    
        #doctor frame 
        remove_frame = Frame(doctor, bg="white") 
        remove_frame.place(relx=0.15, rely=0.5, width=390, height=280) 

        # ---------- Remove doctor ----------
        remove_label = Label(remove_frame, text="Remove Doctor",bg= "white", fg="black", font=("Arial", 18, "bold"))
        remove_label.place(x=96,y=20)

        phone_num_label = Label(remove_frame, text="Phone number:", fg="black",bg="white", font=("Arial", 12))
        phone_num_label.place(x=32, y=94)
        phone_num1_entry = Entry(remove_frame, width=20,bg="white",fg="black")
        phone_num1_entry.place(x=160, y=96)

    

        btn_del = Button(remove_frame, text="Delete", fg="blue", width=8, font=("Arial", 16),command= delete_doc)
        btn_del.place(x=60, y=160)

        cancel_btn3 = Button(remove_frame, text="Cancel", font=("Segoe UI", 14), fg="red", width=7, command=doctor.destroy)
        cancel_btn3.place(x=230, y=162)

        # ------------------ Image ------------------
    img = Image.open("image/admin.jpg")
    img = img.resize((880, 560))
    photo1 = ImageTk.PhotoImage(img)
    img_label1 = Label(admin_frame, image=photo1)
    img_label1.image = photo1
    img_label1.place(x=0, y=0)

    

    #  Buttons on Left
    
    view_btn = Button(admin_frame, text="View Appointment", font=("Arial", 14), width=18, command=view_appointment)
    view_btn.place(x=30, y=80)
    
    manage_doctors_btn = Button(admin_frame, text="Manage Doctor", font=("Arial", 14), width=18, command=manage_doctors)
    manage_doctors_btn.place(x=30, y=150)

    admin_pass_change = Button(admin_frame, text="Change Password", font=("Arial", 14), width=18,command=change_password)
    admin_pass_change.place(x=30, y=220)

    admin_logout_btn = Button(admin_frame, text="Log Out", font=("Arial", 14), width=18, fg="red",command=logout)
    admin_logout_btn.place(x=30, y=290)

