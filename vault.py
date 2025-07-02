import tkinter as tk

def open_vault():
    vault_window = tk.Toplevel()
    vault_window.title("PDF Vault")
    vault_window.geometry("400x300")
    vault_window.configure(bg="black")

    tk.Label(vault_window, text="Welcome to your Vault!", font=("Arial", 16), fg="white", bg="black").pack(pady=20)
    tk.Button(vault_window, text="Close Vault", command=vault_window.destroy).pack(pady=10)
