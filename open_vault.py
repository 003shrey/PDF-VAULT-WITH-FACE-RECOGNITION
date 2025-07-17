import tkinter as tk

def open_vault():
    # nayi window create karte hain jise vault ka access milega
    vault_window = tk.Toplevel()
    vault_window.title("PDF Vault")
    vault_window.geometry("400x300")
    vault_window.configure(bg="black")

    # welcome message vault ke andar
    welcome_label = tk.Label(
        vault_window,
        text="Welcome to your Vault!",
        font=("Segoe UI", 16, "bold"),
        fg="white",
        bg="black"
    )
    welcome_label.pack(pady=40)

    # close button to exit the vault
    close_btn = tk.Button(
        vault_window,
        text="Close Vault",
        font=("Segoe UI", 12),
        command=vault_window.destroy,
        bg="gray20",
        fg="white",
        padx=10,
        pady=5
    )
    close_btn.pack(pady=10)

    # future feature: yahi pe add buttons for upload/view/delete PDFs
