import aiml
import tkinter as tk
from tkinter import scrolledtext, messagebox
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class ChatBotGUI:
    def __init__(self):
        self.kernel = aiml.Kernel()
        self.kernel.learn("std-startup.xml")
        self.kernel.respond("load aiml b")

        self.root = tk.Tk()
        self.root.title("ChatBot")

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

        # Visualize button
        self.visualize_button = tk.Button(self.input_frame, text="Visualize", command=self.visualize, font=("Arial", 12))
        self.visualize_button.pack(side="left", padx=5, pady=5)

        # Configure chat log colors
        self.chat_log.tag_config('green', foreground='green')
        self.chat_log.tag_config('blue', foreground='blue')

        # Initialize plot
        self.plot_frame = tk.Frame(self.root)
        self.plot_frame.pack(padx=10, pady=10, fill="both", expand=True)
        self.figure = Figure(figsize=(6, 4), dpi=100)
        self.ax = self.figure.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(self.figure, master=self.plot_frame)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    def send_message(self):
        user_message = self.input_text.get()
        response = self.kernel.respond(user_message)
        self.chat_log.insert(tk.END, ">Human: ", 'blue')
        self.chat_log.insert(tk.END, user_message + "\n", 'green')
        self.chat_log.insert(tk.END, ">Bot: ", 'blue')
        self.chat_log.insert(tk.END, response + "\n", 'green')
        self.chat_log.yview(tk.END)
        self.input_text.set("")

    def clear_chat(self):
        self.chat_log.delete(1.0, tk.END)

    def visualize(self):
        try:
            # Simple sentiment analysis
            sentiment = {'positive': 0, 'negative': 0, 'neutral': 0}
            chat_text = self.chat_log.get('1.0', tk.END)
            for line in chat_text.split('\n'):
                if 'happy' in line or 'good' in line:
                    sentiment['positive'] += 1
                elif 'sad' in line or 'bad' in line:
                    sentiment['negative'] += 1
                else:
                    sentiment['neutral'] += 1

            # Plot sentiment analysis
            self.ax.clear()
            self.ax.bar(sentiment.keys(), sentiment.values())
            self.ax.set_title('Sentiment Analysis')
            self.ax.set_xlabel('Sentiment')
            self.ax.set_ylabel('Count')
            self.canvas.draw()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def run(self):
        self.root.geometry("800x600")  # Set window size
        self.root.mainloop()

if __name__ == "__main__":
    chatbot = ChatBotGUI()
    chatbot.run()