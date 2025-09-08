from tkinter import *
from tkcalendar import DateEntry
from tkinter import ttk
from PIL import Image, ImageTk
from datetime import datetime, timedelta

# Sample list of doctors
doctor_list = ["Dr. Amrit Chand Thakuri", "Dr. Rohit Thakur", "Dr. Jharana Adhakari", "Dr. Aman Rauniyar", "Dr. Sitasma Kc", 
                "Dr. Pratiksha Thapa", "Dr. Suman Thapa", "Dr. Anupama Thapa", "Dr. Ayush Raut"]

final_window = Tk()
final_window.title("Appointment")
final_window.geometry("500x470")
final_window.resizable(False, False)
final_window.configure(bg="light blue")

# ------------------ Select Doctor ------------------
select_label = Label(final_window, text="Select Doctor:", font=("Segoe UI", 18,"bold"), bg="light blue", fg="black")
select_label.place(x=55, y=50)

select_doctor = ttk.Combobox(final_window, values=doctor_list, font=("Segoe UI", 16), state="readonly", width=15,)
select_doctor.place(x=250, y=50)
select_doctor.set("Choose Doctor")

# ------------------ Date ------------------
date_label = Label(final_window, text="Date (YYYY-MM-DD):", font=("Segoe UI", 15, "bold"),fg= "black" ,bg="light blue")
date_label.place(x=25, y=120)

date_entry=Entry(final_window,width= 15, text= "", font=("Segoe UI", 17), bg="white", fg= "black")
date_entry.place(x=250, y=120)

# date_entry = Entry(final_window, font=("Segoe UI", 16))
# date_entry.pack()
# date_entry = DateEntry(final_window, font=("Segoe UI", 16), width=15, background='darkblue',
#                        fg='blue', borderwidth=2)
# date_entry.place(x=225, y=120)

# ------------------ Time ------------------
time_label = Label(final_window, text="Select Time:", fg="black", font=("Segoe UI", 18, "bold"), bg="light blue")
time_label.place(x=55, y=190)

# Generate time slots
def generate_time_slots(start, end, interval_minutes):
    slots = []
    while start < end:
        slots.append(start.strftime("%I:%M %p"))
        start += timedelta(minutes=interval_minutes)
    return slots

times = generate_time_slots(datetime.strptime("09:00", "%H:%M"),
                            datetime.strptime("18:00", "%H:%M"), 30)

time_combo = ttk.Combobox(final_window, values=times, font=("Segoe UI", 16), state="readonly", width=15)
time_combo.place(x=250, y=190)
time_combo.set("Choose Time")

# ------------------ Buttons ------------------
save_btn = Button(final_window, text="Save", font=("Segoe UI", 16), bg="lightgreen", width=10)
save_btn.place(x=50, y=300)

cancel_btn = Button(final_window, text="Cancel", font=("Segoe UI", 16), bg="lightcoral", width=10, command=final_window.destroy)
cancel_btn.place(x=230, y=300)

final_window.mainloop()