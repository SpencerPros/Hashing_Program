##
# Name: Spencer Prosniewski
##


import hashlib
import tkinter as tk
from tkinter import messagebox

def hash_password(password):
    # Use a secure hash function to store passwords securely
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    return hashed_password

def login():
    entered_username = username_entry.get()
    entered_password = password_entry.get()

    # In a real-world scenario, these values would be stored securely in a database
    stored_user = "Admin"
    stored_password_hash = hash_password("Admin_password")

    # Check if the entered password matches the stored hashed password
    entered_password_hash = hash_password(entered_password)
    if entered_password_hash == stored_password_hash:
        messagebox.showinfo("Login Successful", f"Welcome, {entered_username}!")
    else:
        messagebox.showerror("Login Failed", "Incorrect username or password")

# Create the main window
window = tk.Tk()
window.title("Login System")

# Set the window size
window.geometry("1920x1080")  # Width x Height

# Username Label and Entry
username_label = tk.Label(window, text="Username:")
username_label.pack(pady=5)
username_entry = tk.Entry(window)
username_entry.pack(pady=5)

# Password Label and Entry
password_label = tk.Label(window, text="Password:")
password_label.pack(pady=5)
password_entry = tk.Entry(window, show="*")
password_entry.pack(pady=5)

# Login Button
login_button = tk.Button(window, text="Login", command=login)
login_button.pack(pady=10)

# Run the main loop
window.mainloop()

