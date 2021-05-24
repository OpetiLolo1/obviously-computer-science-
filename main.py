from tkinter import*
from PIL import ImageTk, Image

names_list = []
global questions_answers
asked = []

questions_answers = {
    1: ["What is 3x7?",
        '14',
        '27',
        '30',
        '21',
        '12'
      ,4],
    2: ["What is 10x7?",
        '10',
        '60',
        '35',
        '90',
        '70'
      ,5],
    3: ["What is the equation of a straight line?",
        'y=mx+c',
        'y=a(x+b)²+c',
        'b²-4ac',
        'y=(x+a)(x+b)(x+c)',
        'Apples'
      ,1],
    4: ["Is a parabola a Circle ?",
        'Yes',
        'No',
        'Maybe?'
      ,2],
    5: ["Is a vertex V-shaped",
        'Maybe?',
        'Yes',
        'No'
      ,2],
    6: ["If a dice is rolled what is the probability of getting a even number",
        '4/6',
        '6/6',
        '1/12',
        '3/6',
        '4/4'
      ,4],
    7: ["What is the shape of a parabola?",
        'U-shaped',
        'V-shaped',
        'O-shaped'
      ,1]
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
    self.entry_box.grid(row=3, pady=10)
 
   #Exit button
    self.exit_button = Button (self.quiz_frame, text = "CONTINUE", bg="lime", command=self.name_collection)
    self.exit_button.grid(row=4)

  def name_collection(self):
    name = self.entry_box.get()
    names_list.append(name)
    print(names_list)
    self.quiz_frame.destroy()










#************Starting point program************#\
randomiser()
if __name__ == "__main__":
  root = Tk()
  root.title("MATHS")
  quizStarter_object = QuizStarter(root)
  root.mainloop()