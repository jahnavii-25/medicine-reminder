import tkinter as tk
from tkinter import messagebox
import schedule
import time

reminder_interval = 5  # Interval in minutes for re-reminding

def remind_user(message):
    response = messagebox.askyesno("Reminder", f"{message}\nHave you taken the medicine?", icon='info')
    if response:
        messagebox.showinfo("Confirmation", "Great! Don't forget the next one.", icon='info')
    else:
        messagebox.showinfo("Reminder", "Please take your medicine.", icon='warning')
        # Schedule a re-reminder every 5 minutes if the user selects "No"
        schedule.every(reminder_interval).minutes.do(remind_user, message)

def schedule_reminder():
    reminder_time = time_entry.get()
    reminder_message = message_entry.get()

    try:
        hour, minute = map(int, reminder_time.split(":"))
        schedule.every().day.at(f"{hour:02d}:{minute:02d}").do(remind_user, reminder_message)
        messagebox.showinfo("Success", f"Reminder scheduled for {reminder_time}: {reminder_message}", icon='info')
        time_entry.delete(0, 'end')  # Clear input fields
        message_entry.delete(0, 'end')
    except ValueError:
        messagebox.showerror("Error", "Invalid time format. Please use HH:MM format", icon='error')

# Create the main application window with increased size
root = tk.Tk()
root.title("Medical Reminder App")
root.geometry("400x300")  # Set the window size

# Configure the background colors
root.configure(bg='#E0E0E0')  # Set the background color of the main window

# Create and configure GUI elements with improved design
frame = tk.Frame(root, padx=20, pady=20, bg='#FFFFFF')  # Set the background color of the frame
frame.pack(fill='both', expand=True)

quote_label = tk.Label(frame, text="A healthy outside starts from the inside.", font=('Helvetica', 12), bg='#FFFFFF')
quote_label.pack()

tk.Label(frame, text="Enter reminder time (HH:MM):", font=('Helvetica', 12)).pack()
time_entry = tk.Entry(frame, font=('Helvetica', 12))
time_entry.pack()

tk.Label(frame, text="Enter reminder message:", font=('Helvetica', 12)).pack()
message_entry = tk.Entry(frame, font=('Helvetica', 12))
message_entry.pack()

schedule_button = tk.Button(frame, text="Schedule Reminder", font=('Helvetica', 12), command=schedule_reminder)
schedule_button.pack()

# Check for and trigger reminders
def check_reminders():
    schedule.run_pending()
    root.after(1000, check_reminders)

check_reminders()  # Start checking for reminders

# Start the GUI main loop
root.mainloop()
