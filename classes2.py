#classes2.py
#Creates a window with a label and math questions
#Jason 27 Feb 2020

from tkinter import * #imports all modules of tool kit interface, * is called wildcard

class MathQuiz: #OOP will have classes and functions will be part of the classes
    #Keeps your widgetsin instantiate (__init__) method, each instance (object) must have self. as prefix
    def __init__(self, parent):

        """Widgets for frame 1"""
        self.frame1 = Frame(parent)
        self.frame1.grid(row=0, column=0)

        self.TitleLabel = Label(self.frame1, bg = "black", fg = "white", width = 20, padx=30, pady=10,
                                text="Welcome to Math Quiz", font=("Times", "14", "bold italic"))
        self.TitleLabel.grid(columnspan = 2)
        self.button1 = Button(self.frame1, text="Proceed", anchor = W, command = self.show_frame2)
        self.button1.grid(row=1, column=1)

        """Widgets for frame 2"""
        self.frame2 = Frame(parent) #Notice how .grid is missing here
        self.questions = Label(self.frame2, bg = "black", fg = "white", width = 20, padx=30, pady=10,
                                text="Quiz Questions", font=("Times", "14", "bold italic"))
        self.questions.grid(columnspan = 2)
        self.QuestionLabel = Label(self.frame2, text="", width =15, height=3) #Empty lable to print questions
        self.QuestionLabel.grid(row=1, column=0, sticky = W)
        self.home = Button(self.frame2, text="Home", anchor = W, command = self.show_frame1)
        self.home.grid(row=2, column=0)

        self.next_btn = Button(self.frame2, text = "Next", width = 5, command = self.next_problem, relief = RIDGE)
        self.next_btn.grid(row=2, column=1)


    def show_frame2(self):
        self.frame1.grid_remove() #Removes frame 1
        self.frame2.grid(row=0, column=0)
        self.next_problem()

    def show_frame1(self):
        self.frame2.grid_remove() #Removes frame 2
        self.frame1.grid()

    def next_problem(self):
        """Creates a problem, stores the correct answer"""
        import random
        x = (random.randrange(10))
        y = (random.randrange(10))
        self.answer = x + y

        problem_text = str(x) + " + " + str(y) + "  = "
        self.QuestionLabel.configure(text = problem_text)



#Code in main routine
if __name__ == "__main__": #Checks to see class name is the main module
    root = Tk() #root is variable that calls module to create GUI
    frames = MathQuiz(root)
    root.title("OOP") #Window title appears on top left
    root.geometry("600x300+850+0")
