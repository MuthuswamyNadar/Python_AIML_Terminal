import aiml
import tkinter as tk
import pandas as pd
import matplotlib.pyplot as plt
from tkinter import scrolledtext, messagebox


class ChatBotGUI:
    def __init__(self):
        self.kernel = aiml.Kernel()
        self.kernel.learn("std-startup.xml")
        self.kernel.respond("load aiml b")

        self.root = tk.Tk()
        self.root.title("SchoolBot")

        # Create main frames
        self.chat_frame = tk.Frame(self.root)
        self.chat_frame.pack(padx=10, pady=10, fill="both", expand=True)

        self.input_frame = tk.Frame(self.root)
        self.input_frame.pack(padx=10, pady=5, fill="x")

        # Chat log
        self.chat_log = scrolledtext.ScrolledText(self.chat_frame, width=60, height=20, font=("Arial", 12))
        self.chat_log.pack(padx=5, pady=5, fill="both", expand=True)

        # Input field and send button
        self.input_text = tk.StringVar()
        self.entry = tk.Entry(self.input_frame, textvariable=self.input_text, width=50, font=("Arial", 12))
        self.entry.pack(side="left", padx=5, pady=5)

        self.send_button = tk.Button(self.input_frame, text="Send", command=self.send_message, font=("Arial", 12))
        self.send_button.pack(side="left", padx=5, pady=5)

        # Clear chat button
        self.clear_button = tk.Button(self.input_frame, text="Clear", command=self.clear_chat, font=("Arial", 12))
        self.clear_button.pack(side="left", padx=5, pady=5)

        # Configure chat log colors
        self.chat_log.tag_config('green', foreground='green')
        self.chat_log.tag_config('blue', foreground='blue')





    def send_message(self):
        user_message = self.input_text.get()
        response = self.kernel.respond(user_message)
        self.chat_log.insert(tk.END, ">Human: ", 'blue')
        self.chat_log.insert(tk.END, user_message + "\n", 'green')
        self.chat_log.insert(tk.END, ">Bot: ", 'blue')
        self.chat_log.insert(tk.END, response + "\n", 'green')
        self.chat_log.yview(tk.END)
        self.input_text.set("")



    # Admission form function
    def admission_form(self):
        # Create a new window for admission form
        self.admission_window = tk.Toplevel(self.root)
        self.admission_window.title("Admission Form")

        # Create labels and entry fields
        tk.Label(self.admission_window, text="Student Name:").grid(row=0, column=0)
        self.name_entry = tk.Entry(self.admission_window, width=50)
        self.name_entry.grid(row=0, column=1)

        tk.Label(self.admission_window, text="Age:").grid(row=1, column=0)
        self.age_entry = tk.Entry(self.admission_window, width=50)
        self.age_entry.grid(row=1, column=1)

        tk.Label(self.admission_window, text="Address:").grid(row=2, column=0)
        self.address_entry = tk.Entry(self.admission_window, width=50)
        self.address_entry.grid(row=2, column=1)

        tk.Label(self.admission_window, text="Fees:").grid(row=3, column=0)
        self.fees_entry = tk.Entry(self.admission_window, width=50)
        self.fees_entry.grid(row=3, column=1)

        tk.Label(self.admission_window, text="Standard:").grid(row=4, column=0)
        self.standard_entry = tk.Entry(self.admission_window, width=50)
        self.standard_entry.grid(row=4, column=1)

        # Save button
        self.save_button = tk.Button(self.admission_window, text="Save", command=self.save_admission,
                                     font=("Arial", 12))
        self.save_button.grid(row=5, column=1)

    # Save admission data to Excel
    # Save admission data to Excel
    def save_admission(self):
        # Get values from entry fields
        name = self.name_entry.get()
        age = self.age_entry.get()
        address = self.address_entry.get()
        fees = self.fees_entry.get()
        standard = self.standard_entry.get()

        # Create a dictionary to store admission data
        admission_data = {
            "Name": [name],
            "Age": [age],
            "Address": [address],
            "Standard": [standard]
        }

        # Convert dictionary to DataFrame and save to Excel

        df = pd.DataFrame(admission_data)
        df.to_excel("D:/downloadz/admissions.xlsx", index=False)

        # Show a message box to confirm save
        import tkinter.messagebox
        tkinter.messagebox.showinfo("Success", "Admission data saved successfully!")



    def clear_chat(self):
        self.chat_log.delete(1.0, tk.END)

    def run(self):
        self.root.geometry("600x600")  # Set window size
        self.root.mainloop()

if __name__ == "__main__":
    chatbot = ChatBotGUI()
    chatbot.run()