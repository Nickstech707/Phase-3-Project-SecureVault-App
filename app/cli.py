import getpass
from .auth import Auth
from .credentials import Credentials
from .password_generator import generate_password



class CommandLineInterface:
    def __init__(self):
        self.auth = Auth()
        self.credentials = Credentials()
        self.user_id = None

    def run(self):
        while True:
            if self.user_id is None:
                print("1. Register")
                print("2. Login")
                print("3. Exit")
                choice = input("Select an option: ")
                if choice == "1":
                    self.register()
                elif choice == "2":
                    self.login()
                elif choice == "3":
                    print("Exiting the application.")
                    break
            else:
                print("1. Add Credential")
                print("2. Retrieve Credential")
                print("3. Update Credential")
                print("4. Delete Credential")
                print("5. List All Credentials")
                print("6. Generate Password")
                print("7. Logout")
                choice = input("Select an option: ")
                if choice == "1":
                    self.add_credential()
                elif choice == "2":
                    self.retrieve_credential()
                elif choice == "3":
                    self.update_credential()
                elif choice == "4":
                    self.delete_credential()
                elif choice == "5":
                    self.list_credentials()
                elif choice == "6":
                    self.generate_password()
                elif choice == "7":
                    self.logout()

    def register(self):
        username = input("Enter username: ")
        password = getpass.getpass("Enter password: ")
        if self.auth.register(username, password):
            print("Registration successful 😊.")
        else:
            print("Username already exists. 😕")

    def login(self):
        username = input("Enter username: ")
        password = getpass.getpass("Enter password: ")
        user_id = self.auth.login(username, password)
        if user_id:
            self.user_id = user_id
            print("Login successful. 😊")
        else:
            print("Invalid credentials. 😕")

    def add_credential(self):
        website = input("Enter website: ")
        username = input("Enter username: ")
        password_choice = input("Suggest a strong password? (yes/no): ").strip().lower()
        if password_choice == "yes":
            length = int(input("Enter password length: "))
            password = generate_password(length)
            print(f"Generated password: {password}")
        else:
            password = getpass.getpass("Enter password: ")
        category = input("Enter category (optional): ").strip()
        self.credentials.add_credential(self.user_id, website, username, password, category)
        print("Credential added. 😊")

    def retrieve_credential(self):
        website = input("Enter website: ")
        credential = self.credentials.get_credential(self.user_id, website)
        if credential:
            print(f"Website: {credential['website']}")
            print(f"Username: {credential['username']}")
            print(f"Password: {credential['password']}")
            print(f"Category: {credential['category']}")
        else:
            print("Credential not found. 😕")

    def update_credential(self):
        website = input("Enter website: ")
        username = input("Enter new username: ")
        password_choice = input("Suggest a strong password? (yes/no): ").strip().lower()
        if password_choice == "yes":
            length = int(input("Enter new password length: "))
            password = generate_password(length)
            print(f"Generated password: {password}")
        else:
            password = getpass.getpass("Enter password: ")
        category = input("Enter new category (optional): ").strip()
        self.credentials.update_credential(self.user_id, website, username, password, category)
        print("Credential updated.😊")

    def delete_credential(self):
        website = input("Enter website: ")
        confirm = input(f"Are you sure you want to delete the credential for {website}? (yes/no): ").strip().lower()
        if confirm == "yes":
            self.credentials.delete_credential(self.user_id, website)
            print("Deleted. 🚮")
        else:
            print("Deletion cancelled.")

    def list_credentials(self):
        credentials = self.credentials.list_credentials(self.user_id)
        if credentials:
            for cred in credentials:
                print(f"Website: {cred['website']}")
                print(f"Username: {cred['username']}")
                print(f"Password: {cred['password']}")
                print(f"Category: {cred['category']}")
                print("-" * 20)
        else:
            print("No credentials found. 😢")

    def generate_password(self):
        length = int(input("Enter password length: "))
        password = generate_password(length)
        print(f"Generated password: {password}")

    def logout(self):
        self.user_id = None
        print("Logged out 🔐.")