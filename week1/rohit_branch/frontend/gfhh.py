from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import sqlite3
from appointment import appointment_dashboard


# Function to open Appointment window
def user_dashboard():
    patient_dashboard = Toplevel()
    patient_dashboard.title("Patient Dashboard")
    patient_dashboard.geometry("1400x1100")
    patient_dashboard.configure(bg="light blue")

    dashboard_frame = Frame(patient_dashboard, bg="white")
    dashboard_frame.place(relx=0.5, rely=0.5, anchor="center", width=880, height=560)
    
    def open_appointment():
        appointment_dashboard()

   
    def view_my_appointments():
        view_window = Toplevel(patient_dashboard)
        view_window.title("My Appointments")
        view_window.geometry("600x300")
        view_window.configure(bg="light blue")
        view_window.resizable(False, False)

        phone_label2 = Label(view_window, text="Enter your phone number:", bg="light blue", fg="black", font=("Arial", 14, "bold"))
        phone_label2.place(x=20, y=20)

        phone_entry2 = Entry(view_window, font=("Arial", 14), width=15, bg="white", fg="black")
        phone_entry2.place(x=290, y=20)


        def show_appointments():
            phone3 = phone_entry2.get()
            if not phone3:
                messagebox.showwarning("Warning", "Please enter your phone number")
                return
            
            # Connect to database and fetch appointments
            conn = sqlite3.connect("clinic_management_system.db")
            c = conn.cursor()
            c.execute("SELECT doctor, date, time FROM appointment WHERE phone = ?", (phone3,))
            status = c.fetchall()
            conn.close()
            
            if not status:
                messagebox.showinfo("Info", "No appointments found for this phone number")

            else:
                messagebox.showinfo("Appointments", "Appointments found for this phone number")

        search_btn = Button(view_window, text="Search", font=("Arial", 10), bg="lightgreen", command=show_appointments)
        search_btn.place(x=470, y=20)


    # Function to open Change Password window
    def open_change_password():
        change_password_window = Toplevel(patient_dashboard)
        change_password_window.title("Change Password")
        change_password_window.geometry("470x400")
        change_password_window.configure(bg="light blue")
        change_password_window.resizable(False, False)

        # Function to handle password update
        def change_password7():
            ph4=ph3_entry.get()
            old_password4 = old_pass3_entry.get()
            new_password4 = new_pass3_entry.get()
            confirm_password4 = confirm_pass3_entry.get()

            # Validate if all fields are filled
            if not ph4 or not old_password4 or not new_password4 or not confirm_password4:
                messagebox.showwarning("Warning", "All fields are required")
                return
            
            if new_password4 != confirm_password4:
                messagebox.showerror("Error", "New passwords do not match")
                return
            
            conn = sqlite3.connect("clinic_management_system.db")
            c = conn.cursor()

            c.execute("SELECT password FROM clinic_record WHERE phone = ?", (ph4,))
            result10 = c.fetchone()
       
            if result10 == None:
                messagebox.showerror("Error", "Phone number not found")
                return
            
            if result10[0] != old_password4:
                messagebox.showerror("Error", "Old password is incorrect")
                return
            
            # update the password
            c.execute("UPDATE clinic_record SET password = ? WHERE phone = ?", (new_password4, ph4))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Password changed successfully!")
            change_password_window.destroy()

        # Function to handle cancellation
        def cancel2():
            messagebox.showinfo("Cancel", "Cancel")
            change_password_window.destroy()
        
        # Labels and Entry fields for Change Password
        ph3_label=Label(change_password_window, text="Phone Number:", bg="light blue",fg="black", font=("Arial", 16))
        ph3_label.place(x=50, y=10)
        ph3_entry = Entry(change_password_window, font=("Arial", 15), width=15, bg="white",fg="black", show="*")
        ph3_entry.place(x=230, y=10)



        old_pass3=Label(change_password_window, text="Old Password:", bg="light blue",fg="black", font=("Arial", 16))
        old_pass3.place(x=50, y=60)
        old_pass3_entry = Entry(change_password_window, font=("Arial", 15), width=15, bg="white",fg="black", show="*")
        old_pass3_entry.place(x=230, y=60)

        new_pass3=Label(change_password_window, text="New Password:", bg="light blue",fg="black", font=("Arial", 16))
        new_pass3.place(x=50, y=115)
        new_pass3_entry = Entry(change_password_window, font=("Arial", 15), width=15, bg="white",fg="black", show="*")
        new_pass3_entry.place(x=230, y=115)

        confirm_pass3=Label(change_password_window, text="Confirm Password:", bg="light blue",fg="black", font=("Arial", 16))
        confirm_pass3.place(x=45, y=167)
        confirm_pass3_entry = Entry(change_password_window, font=("Arial", 15), width=15, bg="white",fg="black", show="*")
        confirm_pass3_entry.place(x=230, y=165)

        # Buttons for Change Password
        change_btn = Button(change_password_window, text="Save",fg="green", font=("Arial", 18), width=10, command=change_password7)
        change_btn.place(x=80, y=230)

        cancel_btn = Button(change_password_window, text="Cancel",fg="green", font=("Arial", 18), width=10, command=cancel2)
        cancel_btn.place(x=250, y=230)
        

    # Function to open Update Profile window
    def open_update_profile():
        update_profile_window = Toplevel()
        update_profile_window.title("Update Profile")
        update_profile_window.geometry("500x400")
        update_profile_window.configure(bg="light blue")
        update_profile_window.resizable(False, False)

        def info_update():
            phone6 = phone_number9_entry.get()
            password_patient = pass_patient_entry.get()
            name6 = name_patient_entry.get()
            phone_new = new_number9_entry.get()

            if not phone6 or not password_patient or not name6 or not phone_new :
                messagebox.showwarning("Warning", "All fields are required")
                return  
            
            conn = sqlite3.connect("clinic_management_system.db")
            c = conn.cursor()

            c.execute("SELECT password FROM clinic_record WHERE phone = ?", (phone6,))
            result11 = c.fetchone()
       
            if result11 == None:
                messagebox.showerror("Error", "User not found")
                return
            
            if result11[0]== password_patient :
                c.execute("UPDATE clinic_record SET phone = ?, full_name = ? WHERE phone = ? AND password = ? ",
                          (phone_new, name6, phone6, password_patient))
                conn.commit()
                conn.close()
                messagebox.showinfo("Success", "Profile updated successfully!")
                update_profile_window.destroy()
            
            else:
                messagebox.showerror("Error", "Password not match 😭")

        def cancel10():
            messagebox.showinfo("Cancel", "Cancel")
            update_profile_window.destroy()



        # Profile update form (similar to earlier code)

        phone_number9=Label(update_profile_window, text="Phone Number:",bg="light blue",fg="black", font=("Arial", 16, "bold"))
        phone_number9.place(x=45, y=40)
        phone_number9_entry = Entry(update_profile_window, bg="white", fg="black", font=("Arial", 16), width=15)
        phone_number9_entry.place(x=265, y=40)

        pass_patient=Label(update_profile_window, text="Password:",bg="light blue",fg="black", font=("Arial", 16, "bold"))
        pass_patient.place(x=45, y=110)
        pass_patient_entry = Entry(update_profile_window, bg="white", fg="black", font=("Arial", 16), width=15)
        pass_patient_entry.place(x=265, y=110)

        name_patient=Label(update_profile_window, text=" New Name:",bg="light blue",fg="black", font=("Arial", 16, "bold"))
        name_patient.place(x=45, y=180)
        name_patient_entry = Entry(update_profile_window, bg="white", fg="black", font=("Arial", 16), width=15)
        name_patient_entry.place(x=265, y=178)

        new_number9=Label(update_profile_window, text=" New Phone Number:",bg="light blue",fg="black", font=("Arial", 16, "bold"))
        new_number9.place(x=45, y=250)
        new_number9_entry = Entry(update_profile_window, bg="white", fg="black", font=("Arial", 16), width=15)
        new_number9_entry.place(x=265, y=247)



        btn_update=Button(update_profile_window, text="Update",fg="blue", font=("Arial", 16), width=10, command=info_update)
        btn_update.place(x=95, y=320)
        btn_cancel1=Button(update_profile_window, text="Cancel", fg="blue",font=("Arial", 16), width=10, command=cancel10)
        btn_cancel1.place(x=260, y=320)

    # Function to log out
    def log_out():
            patient_dashboard.destroy()

    img = Image.open("image/admin.jpg")  
    img = img.resize((880, 560))
    photo = ImageTk.PhotoImage(img)
    img_label = Label(dashboard_frame, image=photo)
    img_label.image = photo
    img_label.place(x=0, y=0)

    #  Buttons on Left

    view_appointments_btn = Button(dashboard_frame, text="View My Appointments", font=("Arial", 16), width=18, command=view_my_appointments)
    view_appointments_btn.place(x=55, y=80)

    appointment_btn = Button(dashboard_frame, text="Appointment", font=("Arial", 16), width=18, command=open_appointment)
    appointment_btn.place(x=55, y=150)

    change_password_btn = Button(dashboard_frame, text="Change Password", font=("Arial", 16), width=18, command=open_change_password)
    change_password_btn.place(x=55, y=220)

    update_profile_btn = Button(dashboard_frame, text="Update Profile", font=("Arial", 16), width=18, command=open_update_profile)
    update_profile_btn.place(x=55, y=290)

    log_out_btn = Button(dashboard_frame, text="Log Out", font=("Arial", 16), width=18, fg="red", command=log_out)
    log_out_btn.place(x=55,y=360)
