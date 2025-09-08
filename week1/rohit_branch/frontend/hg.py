from tkinter import *
from tkcalendar import DateEntry
from tkinter import ttk
from PIL import Image, ImageTk
from datetime import datetime, timedelta
# from open_appointment import open_appointment


# Sample list of doctors
doctor_list = ["Dr. Amrit Chand Thakuri", "Dr. Rohit Thakur", "Dr. Jharana Adhakari", "Dr. Aman Rauniyar", "Dr. Sitasma Kc", 
                "Dr. Pratiksha Thapa", "Dr. Suman Thapa", "Dr. Anupama Thapa", "Dr. Ayush Raut"]

root = Tk()
root.title("Appointment")
root.geometry("700x450")
root.configure(bg="white")
root.resizable(False, False)

# ------------------ Background Frame ------------------
frame1 = Frame(root, bg="light blue")
frame1.place(relx=0.5, rely=0.5, anchor="center", width=700, height=450)

# ------------------ Main Frame ------------------
frame = Frame(frame1, bg="white")
frame.place(relx=0.5, rely=0.5, anchor="center", width=400, height=350)

# ------------------ Image ------------------
img = Image.open("th.jpg")
img = img.resize((400, 400))
photo = ImageTk.PhotoImage(img)
img_label = Label(frame, image=photo)
img_label.place(x=0, y=0)

# ------------------ Title ------------------
title_label = Label(frame, text="Appointment", font=("Segoe UI", 16, "bold"), bg="white")
title_label.place(x=130, y=50)

# ------------------ Select Doctor ------------------
doctor_label = Label(frame, text="Select Doctor:", font=("Segoe UI", 12), bg="white")
doctor_label.place(x=30, y=120)

doctor_combo = ttk.Combobox(frame, values=doctor_list, font=("Segoe UI", 12), state="readonly", width=25)
doctor_combo.place(x=150, y=120)
doctor_combo.set("Choose Doctor")

# ------------------ Date ------------------
date_label = Label(frame, text="Date:", font=("Segoe UI", 12), bg="white")
date_label.place(x=30, y=170)

date_entry = DateEntry(frame, font=("Segoe UI", 12), width=23, background='darkblue',
                       foreground='white', borderwidth=2)
date_entry.place(x=150, y=170)

# ------------------ Time ------------------
time_label = Label(frame, text="Time:", font=("Segoe UI", 12), bg="white")
time_label.place(x=30, y=220)

# Generate time slots
def generate_time_slots(start, end, interval_minutes):
    slots = []
    while start < end:
        slots.append(start.strftime("%I:%M %p"))
        start += timedelta(minutes=interval_minutes)
    return slots

times = generate_time_slots(datetime.strptime("09:00", "%H:%M"),
                            datetime.strptime("18:00", "%H:%M"), 30)

time_combo = ttk.Combobox(frame, values=times, font=("Segoe UI", 12), state="readonly", width=25)
time_combo.place(x=150, y=220)
time_combo.set("Choose Time")

# ------------------ Buttons ------------------
save_btn = Button(frame, text="Save", font=("Segoe UI", 12), bg="lightgreen", width=10)
save_btn.place(x=100, y=300)

cancel_btn = Button(frame, text="Cancel", font=("Segoe UI", 12), bg="lightcoral", width=10, command=root.destroy)
cancel_btn.place(x=220, y=300)

root.mainloop()