from tkinter import*
import random
from PIL import ImageTk, Image

global questions_answers
names_list = []
asked = []
score=0

questions_answers = {
    1: ["What is 3x7?",
        '14','27','30','21','12', 4],
    2: ["What is 10x7?",
        '10','60','35','90','70', 5],
    3: ["What is the formula of a straight line?",
        'y=mx+c', 'y=a(x+b)²+c', 'b²-4ac', 'y=(x+a)(x+b)(x+c)', 'Apples', 1],
    4: ["Is a parabola a Circle?", 
        'Yes', 'No', 'Maybe?', 2],
    5: ["Is a vertex V-shaped?",
        'Maybe?', 'Yes', 'No', 2],
    6: ["What is the probability of getting a even number on a dice?",
        '4/6', '6/6', '1/12', '3/6', '4/4', 4],
    7: ["What is the shape of a parabola?",
        'U-shaped', 'V-shaped', 'O-shaped', 1]
}

def randomiser():
  global qnum
  qnum = random.randint(1,7)
  if qnum not in asked:
    asked.append(qnum)
  elif qnum in asked:
    randomiser()


class QuizStarter:
  def __init__(self, parent):
    background_color="deep sky blue"

    #frame set up
    self.quiz_frame = Frame(parent, bg = background_color, padx=10, pady=10)
    self.quiz_frame.grid()

    #Label widget for heading
    self.heading_label = Label (self.quiz_frame, text = "MATHS", font=("Helvetica", "30"), bg=background_color)
    self.heading_label.grid(row=0)
  
    #Start button
    self.start_button = Button (self.quiz_frame, text = "START", bg="lime", command=self.start)
    self.start_button.grid(row=2) 
   
   #Exit button
    self.exit_button = Button (self.quiz_frame, text = "EXIT", bg="red", command=self.quiz_frame.destroy)
    self.exit_button.grid(row=4)

    #Picture resize
    self.picture_image = Image.open("Math equipment.png")
    self.picture_image = self.picture_image.resize((500, 200), Image.ANTIALIAS)
    self.picture_image = ImageTk.PhotoImage(self.picture_image)
    self.image_label= Label(self.quiz_frame, image=self.picture_image)
    self.image_label.grid(row=1)
    
  
  def start(self):
    self.quiz_frame.destroy()  
    NameEnter(root)


class NameEnter:
  def __init__(self, parent):
    background_color="deep sky blue"

    self.quiz_frame = Frame(parent, bg = background_color, padx=100, pady=100)
    self.quiz_frame.grid()

    self.heading_label = Label (self.quiz_frame, text = "Enter your name below", font=("Helvetica", "20"), bg=background_color)
    self.heading_label.grid(row=0)
  
    #Name Enter
    self.entry_box=Entry(self.quiz_frame)
    self.entry_box.grid(row=1, pady=10)
 
   #Exit button
    self.continue_button = Button (self.quiz_frame, text = "CONTINUE", bg="lime", command=self.name_collection)
    self.continue_button.grid(row=4)

  def name_collection(self):
    name = self.entry_box.get()
    names_list.append(name)
    self.quiz_frame.destroy()
    Quiz(root)
    

class Quiz:
  def __init__(self, parent):
    #color selections
    background_color="deep sky blue"
    self.quiz_frame = Frame(parent, bg = background_color, padx=125, pady=125)
    self.quiz_frame.grid()

    #continue Button
    self.confirm_button = Button(self.quiz_frame, text="Confirm", bg="lime")
    self.confirm_button.grid(row=8) 


    randomiser()

    #questions
    self.question_label = Label(self.quiz_frame, text=questions_answers[qnum][0], font=("Tw Cen MT","16"),bg=background_color)
    self.question_label.grid(row=0, padx=10, pady=10)

    #holds value of ratio buttons
    self.var1=IntVar()

#radio button 1
    self.rb1 = Radiobutton(self.quiz_frame, text=questions_answers[qnum][1], font=("Helvetica","12"), bg=background_color, value=1, padx=10, pady=10, variable = self.var1, indicator = 1, background = "light blue")
    self.rb1.grid(row=1)

#radio button 2
    self.rb2 = Radiobutton(self.quiz_frame, text=questions_answers[qnum][2], font=("Helvetica","12"), bg=background_color, value=2, padx=10, pady=10, variable = self.var1, indicator = 1, background = "light blue")
    self.rb2.grid(row=2)

#radio button 3
    self.rb3 = Radiobutton(self.quiz_frame, text=questions_answers[qnum][3], font=("Helvetica","12"), bg=background_color, value=3, padx=10, pady=10, variable = self.var1, indicator = 1, background = "light blue")
    self.rb3.grid(row=3)

#radio button 4
    self.rb4 = Radiobutton(self.quiz_frame, text=questions_answers[qnum][4], font=("Helvetica","12"), bg=background_color, value=4, padx=10, pady=10, variable = self.var1, indicator = 1, background = "light blue")
    self.rb4.grid(row=4)

#radio button 5
    self.rb5 = Radiobutton(self.quiz_frame, text=questions_answers[qnum][5], font=("Helvetica","12"), bg=background_color, value=5, padx=10, pady=10, variable = self.var1, indicator = 1, background = "light blue")
    self.rb5.grid(row=5)

#radio button 6
    self.rb6 = Radiobutton(self.quiz_frame, text=questions_answers[qnum][6], font=("Helvetica","12"), bg=background_color, value=6, padx=10, pady=10, variable = self.var1, indicator = 1, background = "light blue")
    self.rb6.grid(row=6)

#radio button 7
    self.rb7 = Radiobutton(self.quiz_frame, text=questions_answers[qnum][7], font=("Helvetica","12"), bg=background_color, value=7, padx=10, pady=10, variable=self.var1, indicator = 1, background = "light blue")
    self.rb7.grid(row=7)



#************Starting point program************#

if __name__ == "__main__":
  root = Tk()
  root.title("MATHS")
  quizStarter_object = QuizStarter(root)
  root.mainloop()