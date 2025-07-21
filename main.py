import tkinter as tk
from tkinter import messagebox
import time
import random

# Longer and more realistic typing samples
sample_texts = [
    "The quick brown fox jumps over the lazy dog. This sentence contains every letter in the English alphabet and is often used to test typing or fonts.",
    "Typing is a skill that improves with consistent practice and dedication. Fast and accurate typing helps boost productivity and confidence.",
    "Python is a versatile programming language used in many fields, from web development and automation to artificial intelligence and data science.",
    "The ability to type quickly and correctly is essential in today's digital world, where most communication happens through written text.",
    "Your typing speed is measured in words per minute, and it can significantly improve over time with repeated practice and careful focus."
]

class TypingSpeedApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Test")
        self.root.geometry("850x500")
        self.root.configure(bg="#f0f4f7")
        self.sample_text = random.choice(sample_texts)
        self.start_time = None

        self.create_widgets()

    def create_widgets(self):
        title = tk.Label(self.root, text="💻 Typing Speed Test", font=("Helvetica", 24, "bold"), bg="#f0f4f7", fg="#333")
        title.pack(pady=20)

        self.text_display = tk.Label(self.root, text=self.sample_text, wraplength=800,
                                     font=("Helvetica", 14), bg="#f0f4f7", justify="left", fg="#444")
        self.text_display.pack(padx=20, pady=10)

        self.input_box = tk.Text(self.root, height=7, width=100, font=("Consolas", 13), wrap="word", borderwidth=2, relief="solid")
        self.input_box.pack(pady=10)
        self.input_box.bind("<KeyPress>", self.start_timer)
        self.input_box.bind("<Return>", self.handle_enter)  # handle Enter key

        button_frame = tk.Frame(self.root, bg="#f0f4f7")
        button_frame.pack(pady=10)

        self.check_button = tk.Button(button_frame, text="✅ Done", command=self.calculate_speed, font=("Helvetica", 12), bg="#4CAF50", fg="white")
        self.check_button.grid(row=0, column=0, padx=10)

        self.restart_button = tk.Button(button_frame, text="🔁 Restart", command=self.restart_test, font=("Helvetica", 12), bg="#2196F3", fg="white")
        self.restart_button.grid(row=0, column=1, padx=10)

        self.result_label = tk.Label(self.root, text="", font=("Helvetica", 16), bg="#f0f4f7", fg="#333")
        self.result_label.pack(pady=15)

    def start_timer(self, event):
        if self.start_time is None:
            self.start_time = time.time()

    def handle_enter(self, event):
        # Prevent newline and trigger result calculation
        self.calculate_speed()
        return "break"

    def calculate_speed(self):
        end_time = time.time()
        typed_text = self.input_box.get("1.0", tk.END).strip()

        if not typed_text:
            messagebox.showwarning("Empty", "Please type the sentence before submitting.")
            return

        elapsed_time = end_time - self.start_time
        elapsed_minutes = elapsed_time / 60
        word_count = len(typed_text.split())
        wpm = int(word_count / elapsed_minutes)

        # Accuracy calculation
        correct_chars = sum(1 for i, c in enumerate(typed_text) if i < len(self.sample_text) and c == self.sample_text[i])
        total_chars = len(self.sample_text)
        accuracy = (correct_chars / total_chars) * 100

        result_text = f"🕒 Time: {elapsed_time:.2f} sec | 🔤 WPM: {wpm} | 🎯 Accuracy: {accuracy:.2f}%"
        self.result_label.config(text=result_text)
        self.check_button.config(state='disabled')

    def restart_test(self):
        self.sample_text = random.choice(sample_texts)
        self.text_display.config(text=self.sample_text)
        self.input_box.delete("1.0", tk.END)
        self.result_label.config(text="")
        self.check_button.config(state='normal')
        self.start_time = None

if __name__ == "__main__":
    root = tk.Tk()
    app = TypingSpeedApp(root)
    root.mainloop()
