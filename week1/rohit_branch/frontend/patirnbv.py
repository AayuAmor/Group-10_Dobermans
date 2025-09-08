from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

# ------- Patient Dashboard ---------
patient_dashboard = Tk()
patient_dashboard.title("Patient Dashboard")
patient_dashboard.geometry("900x600")
patient_dashboard.configure(bg="light blue")

dashboard_frame = Frame(patient_dashboard, bg="white")
dashboard_frame.place(relx=0.5, rely=0.5, anchor="center", width=880, height=560)

# ------------------ All Functions -----------------

# Function to open Appointment window
def open_appointment():
        appointment_window = Toplevel(patient_dashboard)
        appointment_window.title("Appointment")
        appointment_window.geometry("500x300")
        appointment_window.configure(bg="light blue")
        appointment_window.resizable(False, False)

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
            if ph4 and old_password4 and new_password4 and confirm_password4:
                if new_password4 == confirm_password4:
                    messagebox.showinfo("Password Change Successful", "Your password has been changed!")
                    change_password_window.destroy()
                else:
                    messagebox.showwarning("Error", "New passwords do not match!")
            else:
                messagebox.showwarning("Error", "All fields are required!")

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
            name6 = name_patient_entry.get()
            phone6 = phone_patient_entry.get()

            if not name6 or not phone6 :
                messagebox.showwarning("Warning", "All fields are required")
                return  
            else:
                messagebox.showinfo("Success", "Profile updated successfully!")
                update_profile_window.destroy()

        def cancel10():
            messagebox.showinfo("Cancel", "Cancel")
            update_profile_window.destroy()



        # Profile update form (similar to earlier code)
        name_patient=Label(update_profile_window, text="Patient Name:",bg="light blue",fg="black", font=("Arial", 16, "bold"))
        name_patient.place(x=55, y=60)
        name_patient_entry = Entry(update_profile_window, bg="white", fg="black", font=("Arial", 16), width=15)
        name_patient_entry.place(x=220, y=60)

        phone_patient=Label(update_profile_window, text="Phone Number:",bg="light blue",fg="black", font=("Arial", 16, "bold"))
        phone_patient.place(x=50, y=130)
        phone_patient_entry = Entry(update_profile_window, bg="white", fg="black", font=("Arial", 16), width=15)
        phone_patient_entry.place(x=220, y=130)

        btn_update=Button(update_profile_window, text="Update",fg="blue", font=("Arial", 16), width=10, command=info_update)
        btn_update.place(x=95, y=200)
        btn_cancel1=Button(update_profile_window, text="Cancel", fg="blue",font=("Arial", 16), width=10, command=cancel10)
        btn_cancel1.place(x=260, y=200)

    # Function to log out
def log_out():
        result = messagebox.askyesno("Log Out", "Are you sure you want to log out?")
        if result == True:
            patient_dashboard.quit()

img = Image.open("image/admin.jpg")  
img = img.resize((880, 560))
photo = ImageTk.PhotoImage(img)
img_label = Label(dashboard_frame, image=photo)
img_label.place(x=0, y=0)

    #  Buttons on Left
appointment_btn = Button(dashboard_frame, text="Appointment", font=("Arial", 16), width=18, command=open_appointment)
appointment_btn.place(x=55, y=100)

change_password_btn = Button(dashboard_frame, text="Change Password", font=("Arial", 16), width=18, command=open_change_password)
change_password_btn.place(x=55, y=170)

update_profile_btn = Button(dashboard_frame, text="Update Profile", font=("Arial", 16), width=18, command=open_update_profile)
update_profile_btn.place(x=55, y=240)

log_out_btn = Button(dashboard_frame, text="Log Out", font=("Arial", 16), width=18, fg="red", command=log_out)
log_out_btn.place(x=55, y=310)

patient_dashboard.mainloop()