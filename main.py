from tkinter import *
import random
from PIL import ImageTk, Image

global questions_answers
names_list = []
asked = []
score = 0

questions_answers = {
    1: [
        'What is 3x7?',
        '14',
        '27',
        '30',
        '21',
        '21',
        4,
        ],
    2: [
        'What is 10x7?',
        '10',
        '35',
        '90',
        '70',
        '70',
        4,
        ],
    3: [
        'What is the formula of a straight line?',
        'A=r2',
        'y=a(x+b)+c',
        'b-4ac',
        'y=mx+c',
        'y=mx+c',
        4,
        ],
    4: [
        'Is a parabola a Circle?',
        'Not sure',
        'Yes',
        'Maybe?',
        'No',
        'No',
        4,
        ],
    5: [
        'Expand (x+3)(x+4)',
        'x²+4x+8',
        'x+6x+12',
        '2x²+4x+3x+7',
        'x²+7x+12',
        'x²+7x+12',
        4,
        ],
    6: [
        'What is the probability of getting a even number on a dice?',
        '4/6',
        '6/6',
        '1/12',
        '3/6',
        '3/6',
        4,
        ],
    7: [
        'Simplify 3x+4+5x²+7x',
        '5x²+10x+42x+3x',
        '5x²+21x+4',
        '3x²+4x+10',
        '5x²+10x+4',
        '5x²+10x+4',
        4,
        ],
    }


# function for randomising the order of the questions so they are not predictable

def randomiser():
    global qnum
    qnum = random.randint(1, 7)
    if qnum not in asked:
        asked.append(qnum)
    elif qnum in asked:
        randomiser()


class QuizStarter:

    def __init__(self, parent):
        background_color = 'deep sky blue'

    # frame set up

        self.quiz_frame = Frame(parent, bg=background_color, padx=10,
                                pady=10)
        self.quiz_frame.grid()

    # Label widget for heading

        self.heading_label = Label(self.quiz_frame, text='MATHS',
                                   fg='white', font=('Helvetica', '30',
                                   'bold'), bg=background_color)
        self.heading_label.grid(row=0, padx=5, pady=5)

    # Start button to begin the code

        self.start_button = Button(
            self.quiz_frame,
            text='START',
            fg='white',
            bg='lime',
            font=('Helvetica', '10', 'bold'),
            command=self.start,
            )
        self.start_button.grid(row=2, padx=5, pady=5)

   # Exit button to leave the quiz

        self.exit_button = Button(
            self.quiz_frame,
            text='EXIT',
            fg='white',
            bg='red',
            font=('Helvetica', '10', 'bold'),
            command=self.quiz_frame.destroy,
            )
        self.exit_button.grid(row=4, padx=5, pady=5)

        self.picture_image = Image.open('Math equipment.png')  # choose image from files
        self.picture_image = self.picture_image.resize((500, 200),
                Image.ANTIALIAS)  # resize the image
        self.picture_image = ImageTk.PhotoImage(self.picture_image)
        self.image_label = Label(self.quiz_frame,
                                 image=self.picture_image)
        self.image_label.grid(row=1, pady=5, padx=5)

  # function for continuong to the NameEnter window

    def start(self):
        self.quiz_frame.destroy()
        NameEnter(root)


class NameEnter:

    def __init__(self, parent):
        background_color = 'deep sky blue'

    # Quiz Frame

        self.quiz_frame = Frame(parent, bg=background_color, padx=100,
                                pady=100)
        self.quiz_frame.grid()

    # text to let the user know to enter there name

        self.heading_label = Label(self.quiz_frame,
                                   text='Enter your name below',
                                   fg='white', font=('Helvetica', '20',
                                   'bold'), bg=background_color)
        self.heading_label.grid(row=0, padx=5, pady=5)

    # Entry box so users can inout there names

        self.entry_box = Entry(self.quiz_frame)
        self.entry_box.grid(row=1, pady=5, padx=5)

   # continue button to let the user start the quiz

        self.continue_button = Button(
            self.quiz_frame,
            text='CONTINUE',
            bg='lime',
            fg='white',
            font=('Helvetica', '10', 'bold'),
            command=self.name_collection,
            )
        self.continue_button.grid(row=4, pady=5, padx=5)

    def name_collection(self):
        name = self.entry_box.get()
        if name.strip() != '' and len(name) <= 15:
            names_list.append(name)
            self.quiz_frame.destroy()
            Quiz(root)
        elif len(name) > 15:

                       # if user enters name over 15 characters

            self.heading_label.config(text='Enter something under 15 characters you stupid person'
                    , fg='red')  # text will appear to let user know thatthey must enter less characters
        elif len(name) == 0:

                       # if user doesn't enter anything at all

            self.heading_label.config(text='At least enter something you stupid person'
                    , fg='red')  # text will appear that to let user know that they need to enter at least 1 character


class Quiz:

    def __init__(self, parent):

    # color selections

        background_color = 'deep sky blue'
        self.quiz_frame = Frame(parent, bg=background_color, padx=50,
                                pady=50)
        self.quiz_frame.grid()

    # continue Button

        self.quiz_instance = Button(self.quiz_frame, text='CONFIRM',
                                    bg='lime', 
                                    fg='white',
                                    font=('Helvetica', '10', 'bold'),
                                    command=self.test_progress)
        self.quiz_instance.grid(row=8, pady=5)  # show position of the continue button

    # score label to show score

        self.score_label = Label(self.quiz_frame, font=('Tw Cen MT',
                                 '16'), bg=background_color)
        self.score_label.grid(row=9)  # position of score

        randomiser()

    # questions

        self.question_label = Label(self.quiz_frame,
                                    text=questions_answers[qnum][0],
                                    font=('Tw Cen MT', '14', 'bold'),
                                    bg=background_color, fg='white')
        self.question_label.grid(row=0, padx=10, pady=10)

    # holds value of ratio buttons

        self.var1 = IntVar()

# radio button 1

        self.rb1 = Radiobutton(
            self.quiz_frame,
            text=questions_answers[qnum][1],
            font=('Helvetica', '12'),
            bg=background_color,
            value=1,
            padx=10,
            pady=10,
            variable=self.var1,
            indicator=1,
            background='light grey',
            )
        self.rb1.grid(row=1, pady=5)

# radio button 2

        self.rb2 = Radiobutton(
            self.quiz_frame,
            text=questions_answers[qnum][2],
            font=('Helvetica', '12'),
            bg=background_color,
            value=2,
            padx=10,
            pady=10,
            variable=self.var1,
            indicator=1,
            background='light grey',
            )
        self.rb2.grid(row=2, pady=5)

# radio button 3

        self.rb3 = Radiobutton(
            self.quiz_frame,
            text=questions_answers[qnum][3],
            font=('Helvetica', '12'),
            bg=background_color,
            value=3,
            padx=10,
            pady=10,
            variable=self.var1,
            indicator=1,
            background='light grey',
            )
        self.rb3.grid(row=3, pady=5)

# radio button 4

        self.rb4 = Radiobutton(
            self.quiz_frame,
            text=questions_answers[qnum][4],
            font=('Helvetica', '12'),
            bg=background_color,
            value=4,
            padx=10,
            pady=10,
            variable=self.var1,
            indicator=1,
            background='light grey',
            )
        self.rb4.grid(row=4, pady=5)

  # Set questions setup

    def questions_setup(self):
        randomiser()
        self.var1.set(0)
        self.question_label.config(text=questions_answers[qnum][0])
        self.rb1.config(text=questions_answers[qnum][1])
        self.rb2.config(text=questions_answers[qnum][2])
        self.rb3.config(text=questions_answers[qnum][3])
        self.rb4.config(text=questions_answers[qnum][4])

  # confirm button command, could be enchanced

    def test_progress(self):
        global score  # score needs to be accesiable to all
        scr_label = self.score_label
        choice = self.var1.get()
        if len(asked) > 6:
            if choice == questions_answers[qnum][6]:  # give the right answer to user instead of score

                scr_label.configure(text='Correct', fg='white')  # will show if the user picks correct answer
                self.quiz_instance.config(text='CONFIRM', fg='white')
                self.endscreen()  # open the endscreen after the quiz
            else:
                scr_label.configure(text='Unfortunately the answer was '
                                     + questions_answers[qnum][4], fg='red')  # this will give the user the right answer
                self.quiz_instance.config(text='CONFIRM', fg='white')  # button text
                self.endscreen()  # this will open the end screen when the user finished the quiz
        else:
            if choice == 0:  # if user doesn't pick a option
                scr_label.configure(text="Why didn't you pick something too hard?"
                                    , fg='red')  # text will pop up that lets the user know that they haven't chosen anything
                choice = self.var1.get()  # still will get the user the even if correct
            else:
                if choice == questions_answers[qnum][6]:  # If user picks right answer

                    scr_label.configure(text='Correct', fg='white')
                    self.quiz_instance.config(text='CONFIRM', fg='white')
                    self.questions_setup()  # will move on to the next question
                else:

                    scr_label.configure(text='Unfortunately the answer was '
                             + questions_answers[qnum][4], fg='red')
                    self.quiz_instance.config(text='CONFIRM', fg='white')
                    self.questions_setup()  # will move on to the next question

  # function for closing quiz window and opening end screen

    def endscreen(self):
        root.withdraw()
        open_endscrn = End()


class End:

    def __init__(self):
        background = 'deep sky blue'
        self.end_box = Toplevel(root)  # top level widgets work as windows that are directly managed by the window manager
        self.end_box.title('End Box')

    # frame for endscreen

        self.end_frame = Frame(self.end_box, width=250, height=300,
                               bg=background)
        self.end_frame.grid(row=0)

    # heading for endscreen

        self.end_heading = Label(
            self.end_frame,
            text='Congrats on finishing the quiz now leave and never come back'
                ,
            font=('Helvetica', 18, 'bold'),
            bg=background,
            pady=50,
            padx=10, 
            fg='white'
            )
        self.end_heading.grid(row=0)

    # exit button for endscreen

        self.exit_button = Button(
            self.end_frame,
            text='Exit',
            width=10,
            bg='red',
            font=('Helvetica', 12),
            command=self.close_end,
            )
        self.exit_button.grid(row=4, pady=20)

  # function for exit button to close the program

    def close_end(self):
        self.end_box.destroy()
        root.withdraw()


# ************Starting point program************#

if __name__ == '__main__':
    root = Tk()
    root.title('MATHS')
    quizStarter_object = QuizStarter(root)
    root.mainloop()