import pandas as pd
from tkinter import *

class Question:
    def __init__(self, text, option1, option2, option3, option4, answer):
        self.text = text
        self.options = [option1, option2, option3, option4]
        self.answer = answer

    def is_correct(self, user_answer):
        right_option = self.options.index(self.answer)+1
        return right_option == int(user_answer)

class Quiz(Tk):
    def __init__(self):
        super().__init__()
        self.title("PyQuiz")
        self.geometry("500x400")

        self.btn_start = Button(self, text="Start Quiz", command=self.start_quiz)
        self.btn_start.pack(pady=10)

        self.questions = self.load_questions()  
        self.current_question = 0
        self.score = 0
        self.user_answer = StringVar()  

        self.question_label = Label(self, text="")
        self.question_label.pack(pady=20)
        self.show_score = Label(self, text='')
        self.show_score.pack(pady=20)
        self.options = [] 

        

        # Place buttons at the bottom
        frame = Frame(self)
        frame.pack(side=BOTTOM)

        self.btn_next = Button(frame, text="Next", state=DISABLED, command=self.display_next_question)
        self.btn_next.pack(side=LEFT, padx=10)

        self.btn_finish = Button(frame, text="Finish Quiz", state=DISABLED, command=self.finish_quiz)
        self.btn_finish.pack(side=RIGHT, padx=10)

    def load_questions(self):
        try:
            df = pd.read_csv("question.csv")
            questions = []
            for index, row in df.iterrows():
                questions.append(Question(row["Text"], row["Options1"], row["Options2"],
                                          row["Options3"], row["Options4"], row["Answer"]))
            return questions
        except FileNotFoundError:
            print("Error: 'question.csv' file not found. Please create it.")
            quit()

    def start_quiz(self):
        self.btn_start.config(state=DISABLED) 
        self.btn_next.config(state=NORMAL)  
        self.display_question()

    def display_question(self):
        if self.current_question < len(self.questions):
            question = self.questions[self.current_question]
            self.question_label.config(text=question.text)

            # Destroy previous options if they exist
            for option_button in self.options:  
                option_button.destroy() 
            self.options.clear()

            # Create option buttons only if it's not the last question
            if self.current_question < len(self.questions) - 1:
                for i, option in enumerate(question.options):
                    option_button = Radiobutton(self, text=option, variable=self.user_answer, value=i+1)
                    option_button.pack()
                    self.options.append(option_button)
            else:
                self.finish_quiz()

    def display_next_question(self):
        self.calculate_score(self.questions[self.current_question])
        self.current_question += 1
        self.show_score.config(text=f"Your Score: {self.score}")
        self.display_question()

    def finish_quiz(self):
        self.show_results()
        self.btn_next.config(state=DISABLED)  # Disable next button
        self.btn_finish.config(state=NORMAL)  # Enable finish button

    def calculate_score(self, question):
        # print(self.score)
        # for question in self.questions:
        if question.is_correct(self.user_answer.get()):
            # print(self.user_answer.get())
            self.score += 1

    def show_results(self):
        message = f"Your score is: {self.score}/{len(self.questions)}"
        self.question_label.config(text=message)

        self.update_highest_score()  

    def update_highest_score(self):
        try:
            with open('score.txt', 'r') as f:
                high_score = int(f.read().strip())
        except FileNotFoundError:
            high_score = 0

        if self.score > high_score:
            with open('score.txt', 'w') as f:
                f.write(str(self.score))
            # print(f"New high score: {self.score}")
            self.question_label.config(text=f"New high score: {self.score}")
            self.options = ''
        else:
            #print(f"High score remains: {high_score}")
            self.question_label.config(text=f"High score remains: {high_score}")
            # self.options = ''

if __name__ == "__main__":
    quizApp = Quiz()
    quizApp.mainloop()
