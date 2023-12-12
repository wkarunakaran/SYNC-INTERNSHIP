import datetime
import tkinter as tk
from tkinter import messagebox

def set_alarm():
    try:
        # Get the alarm time from the user input
        alarm_time = entry.get()
        alarm_time = datetime.datetime.strptime(alarm_time, '%H:%M').time()

        # Get the current time
        current_time = datetime.datetime.now().time()

        # Combine the current date with the alarm time
        alarm_datetime = datetime.datetime.combine(datetime.date.today(), alarm_time)

        # Combine the current date with the current time
        current_datetime = datetime.datetime.combine(datetime.date.today(), current_time)

        # Calculate the time difference
        time_difference = alarm_datetime - current_datetime

        # Display a message box with the time remaining until the alarm
        messagebox.showinfo("Alarm Set", f"Alarm set for {alarm_time.strftime('%H:%M')}. Time remaining: {time_difference}")

        # Schedule the alarm using the `after` method
        root.after(time_difference.seconds * 1000, show_alarm_message)

    except ValueError:
        messagebox.showerror("Error", "Invalid time format. Please enter time in 24-hour format (HH:MM).")

def show_alarm_message():
    # Display a message when the alarm goes off
    messagebox.showinfo("Alarm", "Time's up! Your alarm is ringing.")

# Create the main window
root = tk.Tk()
root.title("Alarm Clock")

# Create and place widgets
label = tk.Label(root, text="Enter alarm time (24-hour format):")
label.pack(pady=10)

entry = tk.Entry(root)
entry.pack(pady=10)

set_button = tk.Button(root, text="Set Alarm", command=set_alarm)
set_button.pack(pady=10)

# Run the main loop
root.mainloop()

