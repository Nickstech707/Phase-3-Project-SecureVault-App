import tkinter as tk
from tkinter import messagebox, simpledialog
from .auth import Auth
from .credentials import Credentials
from .password_generator import generate_password

class GUI:
    def __init__(self, root):
        self.root = root
        self.auth = Auth()
        self.credentials = Credentials()
        self.user_id = None
        self.create_widgets()

    def create_widgets(self):
        self.root.title("Password Manager")

        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(pady=20)

        self.login_frame = tk.Frame(self.main_frame)
        self.menu_frame = tk.Frame(self.main_frame)

        self.show_login()

    def show_login(self):
        self.clear_frames()
        self.login_frame.pack()

        tk.Label(self.login_frame, text="1. Register").grid(row=0, column=0, padx=10, pady=10)
        tk.Label(self.login_frame, text="2. Login").grid(row=1, column=0, padx=10, pady=10)
        tk.Label(self.login_frame, text="3. Exit").grid(row=2, column=0, padx=10, pady=10)

        tk.Button(self.login_frame, text="Register", command=self.register).grid(row=0, column=1, padx=10, pady=10)
        tk.Button(self.login_frame, text="Login", command=self.login).grid(row=1, column=1, padx=10, pady=10)
        tk.Button(self.login_frame, text="Exit", command=self.root.quit).grid(row=2, column=1, padx=10, pady=10)

    def show_menu(self):
        self.clear_frames()
        self.menu_frame.pack()

        tk.Label(self.menu_frame, text="1. Add Credential").grid(row=0, column=0, padx=10, pady=10)
        tk.Label(self.menu_frame, text="2. Retrieve Credential").grid(row=1, column=0, padx=10, pady=10)
        tk.Label(self.menu_frame, text="3. Update Credential").grid(row=2, column=0, padx=10, pady=10)
        tk.Label(self.menu_frame, text="4. Delete Credential").grid(row=3, column=0, padx=10, pady=10)
        tk.Label(self.menu_frame, text="5. List All Credentials").grid(row=4, column=0, padx=10, pady=10)
        tk.Label(self.menu_frame, text="6. Generate Password").grid(row=5, column=0, padx=10, pady=10)
        tk.Label(self.menu_frame, text="7. Logout").grid(row=6, column=0, padx=10, pady=10)

        tk.Button(self.menu_frame, text="Add Credential", command=self.add_credential).grid(row=0, column=1, padx=10, pady=10)
        tk.Button(self.menu_frame, text="Retrieve Credential", command=self.retrieve_credential).grid(row=1, column=1, padx=10, pady=10)
        tk.Button(self.menu_frame, text="Update Credential", command=self.update_credential).grid(row=2, column=1, padx=10, pady=10)
        tk.Button(self.menu_frame, text="Delete Credential", command=self.delete_credential).grid(row=3, column=1, padx=10, pady=10)
        tk.Button(self.menu_frame, text="List All Credentials", command=self.list_credentials).grid(row=4, column=1, padx=10, pady=10)
        tk.Button(self.menu_frame, text="Generate Password", command=self.generate_password).grid(row=5, column=1, padx=10, pady=10)
        tk.Button(self.menu_frame, text="Logout", command=self.logout).grid(row=6, column=1, padx=10, pady=10)

    def clear_frames(self):
        for widget in self.main_frame.winfo_children():
            widget.pack_forget()

    def register(self):
        username = simpledialog.askstring("Register", "Enter username:")
        password = simpledialog.askstring("Register", "Enter password:", show='*')
        if username and password:
            if self.auth.register(username, password):
                messagebox.showinfo("Success", "Registration successful.")
            else:
                messagebox.showerror("Error", "Username already exists.")

    def login(self):
        username = simpledialog.askstring("Login", "Enter username:")
        password = simpledialog.askstring("Login", "Enter password:", show='*')
        if username and password:
            user_id = self.auth.login(username, password)
            if user_id:
                self.user_id = user_id
                messagebox.showinfo("Success", "Login successful.")
                self.show_menu()
            else:
                messagebox.showerror("Error", "Invalid credentials.")

    def add_credential(self):
        website = simpledialog.askstring("Add Credential", "Enter website:")
        username = simpledialog.askstring("Add Credential", "Enter username:")
        password_choice = messagebox.askyesno("Add Credential", "Generate a strong password?")
        if password_choice:
            length = simpledialog.askinteger("Password Length", "Enter password length:")
            password = generate_password(length)
            messagebox.showinfo("Generated Password", f"Generated password: {password}")
        else:
            password = simpledialog.askstring("Add Credential", "Enter password:", show='*')
        category = simpledialog.askstring("Add Credential", "Enter category (optional):")
        if website and username and password:
            self.credentials.add_credential(self.user_id, website, username, password, category)
            messagebox.showinfo("Success", "Credential added.")

    def retrieve_credential(self):
        website = simpledialog.askstring("Retrieve Credential", "Enter website:")
        credential = self.credentials.get_credential(self.user_id, website)
        if credential:
            messagebox.showinfo("Credential", f"Website: {credential['website']}\nUsername: {credential['username']}\nPassword: {credential['password']}\nCategory: {credential['category']}")
        else:
            messagebox.showerror("Error", "Credential not found.")

    def update_credential(self):
        website = simpledialog.askstring("Update Credential", "Enter website:")
        username = simpledialog.askstring("Update Credential", "Enter new username:")
        password = simpledialog.askstring("Update Credential", "Enter new password:", show='*')
        category = simpledialog.askstring("Update Credential", "Enter new category (optional):")
        if website and username and password:
            self.credentials.update_credential(self.user_id, website, username, password, category)
            messagebox.showinfo("Success", "Credential updated.")

    def delete_credential(self):
        website = simpledialog.askstring("Delete Credential", "Enter website:")
        if website:
            self.credentials.delete_credential(self.user_id, website)
            messagebox.showinfo("Success", "Credential deleted.")

    def list_credentials(self):
        credentials = self.credentials.list_credentials(self.user_id)
        if credentials:
            cred_str = ""
            for cred in credentials:
                cred_str += f"Website: {cred['website']}\nUsername: {cred['username']}\nPassword: {cred['password']}\nCategory: {cred['category']}\n{'-'*20}\n"
            messagebox.showinfo("All Credentials", cred_str)
        else:
            messagebox.showinfo("No Credentials", "No credentials found.")

    def generate_password(self):
        length = simpledialog.askinteger("Generate Password", "Enter password length:")
        if length:
            password = generate_password(length)
            messagebox.showinfo("Generated Password", f"Generated password: {password}")

    def logout(self):
        self.user_id = None
        self.show_login()
        messagebox.showinfo("Logout", "Logged out.")