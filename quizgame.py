import tkinter as tk
from tkinter import messagebox
import random

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Quiz Game")

        self.questions = [
            {
                'question': 'What is the capital of INDIA?',
                'options': ['Delhi', 'New Delhi', 'Goa', 'Bihar'],
                'correct_answer': 'Delhi'
            },
            {
                'question': 'What will remain if subtract 20 from 40?',
                'options': ['29', '20', '21', '25'],
                'correct_answer': '20'
            },
            {
                'question': 'What is called the graveyard og RBC"?',
                'options': ['Spleen', 'Stomach', 'hands', 'Kidney'],
                'correct_answer': 'Spleen'
            }
            # Add more questions here
        ]

        self.current_question = 0
        self.score = 0
        self.time_left = 10
        self.timer_running = False

        self.timer_label = tk.Label(root, text="")
        self.timer_label.pack(pady=10)

        self.question_label = tk.Label(root, text="", wraplength=400)
        self.question_label.pack(pady=10)

        self.option_buttons = []
        for _ in range(4):
            button = tk.Button(root, text="", command='lambda btn=button: self.check_answer(btn)')
            self.option_buttons.append(button)
            button.pack(pady=5)

        self.next_button = tk.Button(root, text="Next Question", command=self.next_question)
        self.next_button.pack(pady=10)
        self.next_button.config(state=tk.DISABLED)

        self.load_question()

    def load_question(self):
        if self.current_question < len(self.questions):
            if not self.timer_running:
                self.start_timer()
            question_data = random.choice(self.questions)
            self.questions.remove(question_data)
            self.question_label.config(text=question_data['question'])
            options = question_data['options']
            random.shuffle(options)
            for i, button in enumerate(self.option_buttons):
                button.config(text=options[i])
                button.config(state=tk.NORMAL)
            self.next_button.config(state=tk.DISABLED)
        else:
            self.stop_timer()
            self.show_final_score()

    def check_answer(self, selected_button):
        selected_option = selected_button.cget("text")
        correct_answer = self.questions[self.current_question]['correct_answer']
        if selected_option == correct_answer:
            self.score += 1
        self.stop_timer()
        for button in self.option_buttons:
            button.config(state=tk.DISABLED)
        self.next_button.config(state=tk.NORMAL)

    def next_question(self):
        self.current_question += 1
        self.time_left = 10
        self.load_question()

    def start_timer(self):
        self.timer_running = True
        if self.time_left > 0:
            self.timer_label.config(text=f"Time left: {self.time_left} seconds")
            self.time_left -= 1
            self.root.after(1000, self.start_timer)
        else:
            self.check_answer(None)

    def stop_timer(self):
        self.timer_running = False
        self.timer_label.config(text="Time's up!")

    def show_final_score(self):
        messagebox.showinfo("Quiz Completed", f"Final Score: {self.score}/{len(self.questions)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
