from tkinter import * 
from  quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizUi:
    def __init__(self, quiz:QuizBrain):
        self.quiz = quiz

        self.window = Tk()
        self.window.title("Quizztler")
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)
        self.score_text = Label(text="score 0",background=THEME_COLOR)
        self.score_text.grid(row=0,column=1)

        self.canvas = Canvas( bg="white",width=300,height=250)
        self.q_text = self.canvas.create_text(150,125,width=280,text='some text here', fill=THEME_COLOR, font=("Arial", 20,"italic"))
        self.canvas.grid(row=1,column=0,columnspan=2,pady=50)

        right_img = PhotoImage(file="34/images/true.png")
        wrong_img = PhotoImage(file="34/images/false.png")
        self.right_btn = Button(highlightthickness= 0, image=right_img,padx=15,pady=15, command=self.right_answer)
        self.right_btn.grid(row=3, column=0)
        self.wrong_btn = Button(highlightthickness= 0, image=wrong_img,padx=15,pady=15, command=self.wrong_answer)
        self.wrong_btn.grid(row=3, column=1 )

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.score_text.config(text=f"Score: {self.quiz.score}")
            self.canvas.itemconfig(self.q_text,  text=q_text)
        else:
            self.canvas.itemconfig(self.q_text, text="You've reached the end of the quiz.")
            self.right_btn.config(state="disabled")
            self.wrong_btn.config(state="disabled")
    def bg_change(self, ans:bool):
        if ans:
            self.canvas.config(self.canvas, bg='green')
        else:
            self.canvas.config(self.canvas, bg='red')   
        self.window.after(1000,self.get_next_question)

    def right_answer(self):
        ans=self.quiz.check_answer('True')
        self.bg_change(ans)
        
    def wrong_answer(self):
        ans = self.quiz.check_answer('False')
        self.bg_change(ans)