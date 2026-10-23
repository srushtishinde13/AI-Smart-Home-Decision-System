
import tkinter as tk
from tkinter import messagebox


def make_decision():
    is_dark = dark_var.get()
    motion_detected = motion_var.get()
    security_mode = security_var.get()

    # Read temperature
    try:
        temperature = float(temp_entry.get().strip())
    except ValueError:
        messagebox.showerror(
            "Invalid Input",
            "Please enter a valid temperature, such as 25 or 30."
        )
        return

    if is_dark:
        light = "ON"
    else:
        light = "OFF"

    if temperature >= 28:
        fan = "ON"
    else:
        fan = "OFF"

    if motion_detected and security_mode:
        alarm = "ON"
    else:
        alarm = "OFF"

    # Display the result
    result_text = (
        f"Light: {light}\n"
        f"Fan: {fan}\n"
        f"Security Alarm: {alarm}"
    )

    result_label.config(text=result_text)


root = tk.Tk()
root.title("AI Smart Home Decision System By Srushti Shinde")
root.geometry("450x520")
root.configure(bg="#EDE7F6")



title_label = tk.Label(
    root,
    text="AI Smart Home System",
    font=("Arial", 18, "bold"),
    bg="#EDE7F6",
    fg="#A02757"
)
title_label.pack(pady=20)


dark_var = tk.BooleanVar(value=False)

dark_check = tk.Checkbutton(
    root,
    text="Is the room dark?",
    variable=dark_var,
    font=("Arial", 12),
    bg="#EDE7F6",
    activebackground="#EDE7F6"
)
dark_check.pack(pady=8)


temp_label = tk.Label(
    root,
    text="Enter Temperature (°C):",
    font=("Arial", 12),
    bg="#EDE7F6"
)
temp_label.pack(pady=5)

temp_entry = tk.Entry(
    root,
    font=("Arial", 12),
    justify="center"
)
temp_entry.insert(0, "25")
temp_entry.pack(pady=5)


motion_var = tk.BooleanVar(value=False)

motion_check = tk.Checkbutton(
    root,
    text="Is motion detected?",
    variable=motion_var,
    font=("Arial", 12),
    bg="#EDE7F6",
    activebackground="#EDE7F6"
)
motion_check.pack(pady=8)


security_var = tk.BooleanVar(value=False)

security_check = tk.Checkbutton(
    root,
    text="Is security mode ON?",
    variable=security_var,
    font=("Arial", 12),
    bg="#EDE7F6",
    activebackground="#EDE7F6"
)
security_check.pack(pady=8)


decision_button = tk.Button(
    root,
    text="Make Decision",
    command=make_decision,
    font=("Arial", 12, "bold"),
    bg="#7E57C2",
    fg="white",
    activebackground="#A02757",
    activeforeground="white",
    padx=15,
    pady=8
)
decision_button.pack(pady=18)


output_heading = tk.Label(
    root,
    text="System Decisions",
    font=("Arial", 14, "bold"),
    bg="#EDE7F6",
    fg="#A02757"
)
output_heading.pack(pady=5)


result_label = tk.Label(
    root,
    text="Enter inputs and click Make Decision",
    font=("Arial", 12),
    bg="white",
    fg="#333333",
    width=32,
    height=5,
    relief="groove",
    justify="left",
    anchor="w",
    padx=10
)
result_label.pack(pady=10)


# Run application
root.mainloop()
