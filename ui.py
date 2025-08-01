# ui.py
# This file contains all the Tkinter code for the user interface.

import tkinter as tk

# This is the corrected file. The incorrect import statement has been removed.

def open_vault_window():
    """Creates and displays the 'Welcome to your Vault!' window."""
    vault_window = tk.Toplevel()
    vault_window.title("PDF Vault")
    vault_window.geometry("400x300")
    vault_window.configure(bg="black")

    tk.Label(
        vault_window,
        text="Welcome to your Vault!",
        font=("Segoe UI", 16, "bold"),
        fg="white",
        bg="black"
    ).pack(pady=40)

    tk.Button(
        vault_window,
        text="Close Vault",
        font=("Segoe UI", 12),
        command=vault_window.destroy,
        bg="gray20",
        fg="white",
        padx=10,
        pady=5
    ).pack(pady=10)


def create_login_window(login_callback):
    """
    Creates the main login window.
    It takes a function 'login_callback' which is executed when the button is pressed.
    """
    root = tk.Tk()
    root.title("Secure PDF Vault")
    root.geometry("300x250") # Increased height for the new label
    root.configure(bg="black")

    tk.Label(
        root,
        text="Login with Face",
        font=("Segoe UI", 14, "bold"),
        fg="white",
        bg="black"
    ).pack(pady=20)

    # --- Status Label ---
    # This label will give feedback to the user during long operations.
    status_label = tk.Label(
        root,
        text="", # Initially empty
        font=("Segoe UI", 10),
        fg="yellow",
        bg="black"
    )
    status_label.pack(pady=10)

    # --- Login Button ---
    # The 'command' for this button is passed in from main.py
    login_button = tk.Button(
        root,
        text="Unlock Vault",
        font=("Segoe UI", 12),
        # Pass both the root window and the status label to the callback
        command=lambda: login_callback(root, status_label),
        bg="gray20",
        fg="white",
        padx=10,
        pady=5
    )
    login_button.pack(pady=10)

    # Start the Tkinter event loop
    root.mainloop()
