import aiml
import tkinter as tk
from tkinter import scrolledtext


class NetSwamyGUI:
    def __init__(self):
        self.kernel = aiml.Kernel()

        self.kernel.learn("std-startup.xml")
        self.kernel.respond("load aiml b")

        self.root = tk.Tk()
        self.root.title("SchoolBot")

        # Set background color
        self.root.configure(background='#f2f2f2')


        self.chat_frame = tk.Frame(self.root, bg='#f2f2f2')
        self.chat_frame.pack(padx=10, pady=10, fill="both", expand=True)

        self.input_frame = tk.Frame(self.root, bg='#f2f2f2')
        self.input_frame.pack(padx=10, pady=5, fill="x")

        self.dashboard_frame = tk.Frame(self.root, bg='#f2f2f2')
        self.dashboard_frame.pack(padx=10, pady=5, fill="x")


        self.chat_log = scrolledtext.ScrolledText(self.chat_frame, width=60, height=20, font=("Arial", 14), bg='#e5e5e5', fg='#333')  # Light gray background, dark gray text
        self.chat_log.pack(padx=5, pady=5, fill="both", expand=True)


        self.input_text = tk.StringVar()
        self.entry = tk.Entry(self.input_frame, textvariable=self.input_text, width=50, font=("Arial", 14), bg='#e5e5e5', fg='#333')
        self.entry.pack(side="left", padx=5, pady=5)

        self.send_button = tk.Button(self.input_frame, text="Send", command=self.send_message, font=("Arial", 14), bg='#4CAF50', fg='#fff')  # Green button
        self.send_button.pack(side="left", padx=5, pady=5)


        self.clear_button = tk.Button(self.input_frame, text="Clear", command=self.clear_chat, font=("Arial", 14), bg='#f44336', fg='#fff')  # Red button
        self.clear_button.pack(side="left", padx=5, pady=5)


        self.chat_log.tag_config('green', foreground='#008000')  # Dark green
        self.chat_log.tag_config('blue', foreground='#0000ff')  # Dark blue



    def send_message(self):
        user_message = self.input_text.get()
        response = self.kernel.respond(user_message)
        self.chat_log.insert(tk.END, " User : ", 'blue')
        self.chat_log.insert(tk.END, user_message + "\n\n", 'green')
        self.chat_log.insert(tk.END, " Bot: ", 'blue')
        self.chat_log.insert(tk.END, response + "\n\n", 'green')
        self.chat_log.yview(tk.END)
        self.input_text.set("")


    def clear_chat(self):
        self.chat_log.delete(1.0, tk.END)


    def run(self):
        self.root.geometry("800x600")
        self.root.mainloop()


if __name__ == "__main__":
    chatbot = NetSwamyGUI()
    chatbot.run()