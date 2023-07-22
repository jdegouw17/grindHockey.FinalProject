import tkinter as tk
from tkinter import messagebox

class GrindHockeyDevelopmentGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Grind Hockey Development")
        self.root.geometry("800x600")

        self.pages = {}
        self.current_page = None

        self.create_widgets()
        self.show_signup_page()

    def create_widgets(self):
        self.frame = tk.Frame(self.root, bg="black")
        self.frame.pack(fill=tk.BOTH, expand=True)

        self.pages["Signup"] = self.create_signup_page()
        self.pages["Confirmation"] = self.create_confirmation_page()

    def create_signup_page(self):
        signup_frame = tk.Frame(self.frame, bg="black")

        # Welcome message
        tk.Label(signup_frame, text="Welcome to Grind Hockey Development", fg="blue", font=("Arial", 20)).pack(pady=10)

        # Package selection
        tk.Label(signup_frame, text="Select Package:", fg="yellow", bg="black", font=("Arial", 14)).pack(pady=5)
        package_var = tk.StringVar()
        packages = [("Hat trick package: $1000", "HATTRICK"), ("Bardown package: $800", "BD" ), ("Ovi package: $600", "Ovi")]
        for package, value in packages:
            tk.Radiobutton(signup_frame, text=package, variable=package_var, value=value, bg="black", fg="white",
                           selectcolor="blue", font=("Arial", 12)).pack(pady=5)

        # User information entry fields
        fields = [("Name:", 30), ("Phone Number:", 15), ("Email:", 30), ("Date of Birth:", 15), ("Address:", 30)]
        entry_vars = []
        for field, width in fields:
            label = tk.Label(signup_frame, text=field, fg="yellow", bg="black", font=("Arial", 12))
            label.pack(pady=5)
            entry_var = tk.StringVar()
            entry = tk.Entry(signup_frame, textvariable=entry_var, font=("Arial", 12), width=width)
            entry.pack(pady=5)
            entry_vars.append(entry_var)

        # Submit button
        submit_button = tk.Button(signup_frame, text="Submit", bg="yellow", fg="black", font=("Arial", 12),
                                  command=lambda: self.show_confirmation_page(package_var.get(), entry_vars))
        submit_button.pack(pady=10)


        return signup_frame

    def create_confirmation_page(self):
        confirmation_frame = tk.Frame(self.frame, bg="black")

        # Thank you message
        tk.Label(confirmation_frame, text="Thank you for signing up!", fg="blue", font=("Arial", 20)).pack(pady=10)

        # User information confirmation
        self.confirmation_label = tk.Label(confirmation_frame, fg="white", bg="black", font=("Arial", 12))
        self.confirmation_label.pack(pady=10)



        return confirmation_frame

    def show_signup_page(self):
        if self.current_page:
            self.current_page.pack_forget()
        self.current_page = self.pages["Signup"]
        self.current_page.pack(fill=tk.BOTH, expand=True)

    def show_confirmation_page(self, package, entry_vars):
        name, phone, email, dob, address = [var.get() for var in entry_vars]

        if not name or not phone or not email or not dob or not address:
            messagebox.showerror("Error", "Please fill out all fields.")
            return

        if not package:
            messagebox.showerror("Error", "Please select a package.")
            return

        # Confirmation text
        confirmation_text = (
            f"Name: {name}\n"
            f"Package: {package}\n"
            f"Phone Number: {self.pages['Signup'].children['!entry2'].get()}\n"
            f"Email: {self.pages['Signup'].children['!entry3'].get()}\n"
            f"Date of Birth: {self.pages['Signup'].children['!entry4'].get()}\n"
            f"Address: {self.pages['Signup'].children['!entry5'].get()}"
        )
        self.confirmation_label.config(text=confirmation_text)
        self.show_signup_page()

if __name__ == "__main__":
    root = tk.Tk()
    root.configure(bg="black")
    grind_hockey_app = GrindHockeyDevelopmentGUI(root)
    root.mainloop()
