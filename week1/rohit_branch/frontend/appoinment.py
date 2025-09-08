from tkinter import *
from tkcalendar import DateEntry
from tkinter import ttk
from PIL import Image, ImageTk

# Sample list of doctors
doctor_list = ["Dr. Amrit Chand Thakuri", "Dr. Rohit Thakur", "Dr. Jharana Adhakari", "Dr. Aman Rauniyar", "Dr. Sitasma Kc", 
                "Dr. Pratiksha Thapa", "Dr. Suman Thapa", "Dr. Anupama Thapa", "Dr. Ayush Raut"]

final_window = Tk()
final_window.title("Appointment")
final_window.geometry("500x470")
final_window.resizable(False, False)
final_window.configure(bg="light blue")

# ------------------ Image ------------------
img = Image.open("download.webp")
img = img.resize((500,470))
photo = ImageTk.PhotoImage(img)
img_label = Label(final_window, image=photo)
img_label.place(x=0, y=0)

# ------------------ Select Doctor ------------------
select_label = Label(final_window, text="Select Doctor:", font=("Segoe UI", 18,"bold"), bg="light blue", fg="black")
select_label.place(x=50, y=50)

select_doctor = ttk.Combobox(final_window, values=doctor_list, font=("Segoe UI", 16), state="readonly", width=15)
select_doctor.place(x=250, y=50)
select_doctor.set("Choose Doctor")

# ------------------ Date ------------------
date_label = Label(final_window, text="Date (YYYY-MM-DD):", font=("Segoe UI", 15, "bold"),fg= "black" ,bg="light blue")
date_label.place(x=25, y=120)

date_entry=Entry(final_window,width= 15, text= "", font=("Segoe UI", 17), bg="gray", fg= "white")
date_entry.place(x=250, y=120)

def r_btn():

    var1=StringVar()
    r1=Radiobutton(final_window,text="10:00 am",variable=var1,value=1, bg= "light blue", fg= "black",font=("Arial",14))
    r1.place(x=250,y=190)

    r2=Radiobutton(final_window,text="11:00 am",variable=var1,value=2 , bg= "light blue", fg= "black",font=("Arial",14))
    r2.place(x=250,y=210)

    r3=Radiobutton(final_window,text="1:00  pm",variable=var1,value=3, bg= "light blue", fg= "black",font=("Arial",14))
    r3.place(x=250,y=230)

    r4=Radiobutton(final_window,text="2:00  pm",variable=var1,value=4, bg= "light blue", fg= "black",font=("Arial",14))
    r4.place(x=250,y=250)

    r5=Radiobutton(final_window,text="4:00  pm",variable=var1,value=5, bg= "light blue", fg= "black",font=("Arial",14))
    r5.place(x=250,y=270)


# ------------------ Time ------------------
time_btn = Button(final_window, text="Select Time", fg="blue", font=("Segoe UI", 14), command= r_btn)
time_btn.place(x=90, y=220)


# ------------------ Buttons ------------------
save_btn = Button(final_window, text="Save", font=("Segoe UI", 16), bg="lightgreen", width=10)
save_btn.place(x=50, y=330)

cancel_btn = Button(final_window, text="Cancel", font=("Segoe UI", 16), bg="lightcoral", width=10, command=final_window.destroy)
cancel_btn.place(x=230, y=330)

final_window.mainloop()
