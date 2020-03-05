#Learning OOP by trying to use classes
#classes.py
#Jason Poonia

from tkinter import *
import random
import time

class MathQuiz:
    def __init__(self, parent):
        self.correct_answers = []

        self.frame4 = Frame(parent)
        self.frame4.grid(row=0, column=1)
        self.frame4.grid_remove()

        self.TitleLabel = Label(self.frame4, bg = "white", fg = "black", width = 50, padx = 40, pady = 10, text ="PYTHON MATH QUIZ", font = ("Helevtica", "14", "bold"))
        self.TitleLabel.grid(columnspan = 2)

        self.TitleLabel = Label(self.frame4, bg = "white", fg = "black", width = 50, padx = 40, pady = 10, text ="REPORT", font = ("Helevtica", "12", "bold"))
        self.TitleLabel.grid(columnspan = 2)

        self.report = Text(self.frame4, width = 10)
        self.report.grid(columnspan = 2)

        self.back = Button(self.frame4, text = "Go Back", anchor = W, command = self.show_frame1)
        self.back.grid(columnspan = 2)

        self.frame3 = Frame(parent)
        self.frame3.grid(row=0, column=1)

        self.TitleLabel = Label(self.frame3, bg = "white", fg = "black", width = 50, padx = 40, pady = 10, text ="PYTHON MATH QUIZ", font = ("Helevtica", "14", "bold"))
        self.TitleLabel.grid(columnspan = 2)

        self.QuestionLabel = Label(self.frame3, bg = "white", fg = "black", width=30, padx=40, pady=10, text = "NAME:", font = ("Helevtica", "14", "bold"))
        self.QuestionLabel.grid(row = 3, column = 0, stick = W)

        self.NameEntry = Entry(self.frame3, width = 15)
        self.NameEntry.grid(row = 3, column = 1, sticky = W)

        self.QuestionLabel = Label(self.frame3, bg = "white", fg = "black", width=30, padx=40, pady=10, text = "AGE:", font = ("Helevtica", "14", "bold"))
        self.QuestionLabel.grid(row = 4, column = 0, stick = W)

        self.AgeEntry = Entry(self.frame3, width = 15)
        self.AgeEntry.grid(row = 4, column = 1, sticky = W)

        self.text = Button(self.frame3)
        self.text.grid(row = 5, column = 1)

        self.agecheck = Button(self.frame3, text = "Proceed", anchor = W, command = self.age_check)
        self.agecheck.grid(row = 6, column = 1)

        self.frame1 = Frame(parent)
        self.frame1.grid(row=0, column=0)
        self.frame1.grid_remove()
        self.TitleLabel = Label(self.frame1, bg = "white", fg = "black", width = 50, padx = 40, pady = 10, text ="PYTHON MATH QUIZ", font = ("Helevtica", "14", "bold"))
        self.TitleLabel.grid(columnspan = 2)

        self.howto = Text(self.frame1, height = 10)
        self.howto.grid(columnspan = 1)

        self.button1 = Button(self.frame1, text = "Start", anchor = W, command = self.show_frame2)
        self.button1.grid(columnspan = 2)

        self.frame2 = Frame(parent)
        self.frame2.grid(row=0, column=1)
        self.frame2.grid_remove()
        self.TitleLabel = Label(self.frame2, bg = "white", fg = "black", width = 50, padx = 40, pady = 10, text ="PYTHON MATH QUIZ", font = ("Helevtica", "14", "bold"))
        self.TitleLabel.grid(columnspan = 3)

        self.QuestionLabel = Label(self.frame2, bg = "black", fg = "white", width=20, padx=30, pady=10, text = "Answer Quiz Questions", font = ("Helevtica", "14", "bold"))
        self.QuestionLabel.grid(row = 1, column = 0, stick = W)

        self.AnswerEntry = Entry(self.frame2, width = 20)
        self.AnswerEntry.grid(row = 1, column = 2, sticky = W)

        self.home = Button(self.frame2, text = "Home", anchor = W, command = self.show_frame1)
        self.home.grid(row = 3, column = 0)

        self.check = Button(self.frame2, text = "Report", anchor = W, command = self.show_frame4)
        self.check.grid(row = 3, column = 1)

        self.check = Button(self.frame2, text = "Start/Check Answer", anchor = W, command = self.check_problem)
        self.check.grid(row = 3, column = 2)

    def show_frame2(self):
        self.frame1.grid_remove() #Removes frame 1
        self.frame3.grid_remove()
        self.frame4.grid_remove()
        self.frame2.grid(row=0, column=0)
        self.next_problem()

    def show_frame1(self):
        self.frame2.grid_remove() #Removes frame 2
        self.frame1.grid()
        self.frame4.grid_remove()
        self.frame3.grid_remove()

    def next_problem(self):
        """Creates a problem, stores the correct answer"""
        import random
        x = (random.randrange(10))
        y = (random.randrange(10))
        self.answer = x + y
        problem_text = str(x) + " + " + str(y) + "  = "
        self.correct_answers.append(1)
        self.QuestionLabel.configure(text = problem_text)
        self.check.configure(text = "Check Answer", fg = "black")
        self.AnswerEntry.delete(0, END)
        self.AnswerEntry.focus()

    def show_frame4(self):
        self.frame2.grid_remove() #Removes frame 2
        self.frame1.grid_remove()
        self.frame3.grid_remove()
        self.frame4.grid()
        x = len(self.correct_answers)
        reporttext = "Score:{}".format(x)
        self.report.insert(INSERT, reporttext)
        self.report.config(state = DISABLED)

    def check_answer(self):
        self.check.configure(text = "Check Answer", fg = "black")

    def newquestion(self):
        self.check.configure(text = "Next Question", fg = "black")
        self.next_problem()

    def check_problem(self):
        try:
            user_answer = int(self.AnswerEntry.get())
            if user_answer == self.answer:
                self.check.configure(text = "Correct", fg = "green")
                self.check.after(2500, self.newquestion)
            else:
                self.check.configure(text = "Try Again!", fg = "red")
                self.AnswerEntry.delete(0, END)
                self.AnswerEntry.focus()
                self.check.after(2500, self.check_answer)
        except ValueError:
            self.check.configure(text = "That is not a number!", fg = "red")
            self.AnswerEntry.delete(0, END)
            self.AnswerEntry.focus()

    def age_check(self):
        self.frame2.grid_remove() #Removes frame 2
        self.frame1.grid_remove()
        self.frame3.grid()
        self.howto.insert(INSERT, "1. Enter the answer for the question in the empty box \n2. Click on check answer \n3. Click on Report when you want to finish.")
        self.howto.config(state = DISABLED)
        try:
            age = int(self.AgeEntry.get())
            name = str(self.NameEntry.get())
            if age >= 3 and age <= 11 :
                self.show_frame1()
            else:
                self.text.configure(text = "Sorry you're too old")
        except ValueError:
            self.text.configure(text = "That is not a number!")
            self.AgeEntry.delete(0, END)
            self.AgeEntry.focus()

#Code in main routine
if __name__ == "__main__": #Checks to see class name is the main module
    root = Tk() #root is variable that calls module to create GUI
    frames = MathQuiz(root)
    root.title("Python Math Quiz") #Window title appears on top left
    root.geometry("600x300+850+0")
