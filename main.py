from tkinter import*
import random
from PIL import ImageTk, Image

global questions_answers
names_list = []
asked = []
score=0

questions_answers = {
 1: ["What is 3x7?", '14','27','30','21', '21',4],
 2: ["What is 10x7?", '10','35','90','70', '70',5],
 3: ["What is the formula of a straight line?", 'y=mx+c', 'y=a(x+b)²+c', 'b²-4ac', 'A=πr2', 'y=mx+c',1],
 4: ["Is a parabola a Circle?", 'Yes', 'No', 'Maybe?', 'Not sure', 'Yes',2],
 5: ["Is a vertex V-shaped?", 'Maybe?', 'Yes', 'No', 'Not sure',  'Yes',2],
 6: ["What is the probability of getting a even number on a dice?", '4/6', '6/6', '1/12', '3/6', '3/6',4],
 7: ["What is the shape of a parabola?", 'U-shaped', 'V-shaped', 'O-shaped', 'W-shaped', 'U-shaped',1]

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
    self.heading_label.grid(row=0, padx=5, pady=5)
  
    #Start button
    self.start_button = Button (self.quiz_frame, text = "START", bg="lime", command=self.start)
    self.start_button.grid(row=2, padx=5, pady=5) 
   
   #Exit button
    self.exit_button = Button (self.quiz_frame, text = "EXIT", bg="red", command=self.quiz_frame.destroy)
    self.exit_button.grid(row=4, padx=5, pady=5)

    #Picture resize
    self.picture_image = Image.open("Math equipment.png")
    self.picture_image = self.picture_image.resize((500, 200), Image.ANTIALIAS)
    self.picture_image = ImageTk.PhotoImage(self.picture_image)
    self.image_label= Label(self.quiz_frame, image=self.picture_image)
    self.image_label.grid(row=1, pady=5, padx=5)
    
  
  def start(self):
    self.quiz_frame.destroy()  
    NameEnter(root)


class NameEnter:
  def __init__(self, parent):
    background_color="deep sky blue"

    #Quiz Frame
    self.quiz_frame = Frame(parent, bg = background_color, padx=100, pady=100)
    self.quiz_frame.grid()

    self.heading_label = Label (self.quiz_frame, text = "Enter your name below", font=("Helvetica", "20"), bg=background_color)
    self.heading_label.grid(row=0, padx=5, pady=5)
  
    #Name Enter
    self.entry_box=Entry(self.quiz_frame)
    self.entry_box.grid(row=1, pady=5, padx=5)
 
   #Exit button
    self.continue_button = Button (self.quiz_frame, text = "CONTINUE", bg="lime", command=self.name_collection)
    self.continue_button.grid(row=4, pady=5, padx=5)

  def name_collection(self):
    name = self.entry_box.get()
    names_list.append(name)
    self.quiz_frame.destroy()
    Quiz(root)
    

class Quiz:
  def __init__(self, parent):
    #color selections
    background_color="deep sky blue"
    self.quiz_frame = Frame(parent, bg = background_color, padx=50, pady=50)
    self.quiz_frame.grid()

    #continue Button
    self.quiz_instance = Button(self.quiz_frame, text="CONFIRM", bg="lime", command=self.test_progress)
    self.quiz_instance.grid(row=8, pady=5) 

    #score label to show score
    self.score_label = Label(self.quiz_frame, text="SCORE", font=("Tw Cen MT", "16"), bg=background_color)
    self.score_label.grid(row=9) 

    randomiser()

    #questions
    self.question_label = Label(self.quiz_frame, text=questions_answers[qnum][0], font=("Tw Cen MT","14"),bg=background_color)
    self.question_label.grid(row=0, padx=10, pady=10)

    #holds value of ratio buttons
    self.var1=IntVar()

#radio button 1
    self.rb1 = Radiobutton(self.quiz_frame, text=questions_answers[qnum][1], font=("Helvetica","12"), bg=background_color, value=1, padx=10, pady=10, variable = self.var1, indicator = 1, background = "light grey")
    self.rb1.grid(row=1, pady=5)

#radio button 2
    self.rb2 = Radiobutton(self.quiz_frame, text=questions_answers[qnum][2], font=("Helvetica","12"), bg=background_color, value=2, padx=10, pady=10, variable = self.var1, indicator = 1, background = "light grey")
    self.rb2.grid(row=2, pady=5)

#radio button 3
    self.rb3 = Radiobutton(self.quiz_frame, text=questions_answers[qnum][3], font=("Helvetica","12"), bg=background_color, value=3, padx=10, pady=10, variable = self.var1, indicator = 1, background = "light grey")
    self.rb3.grid(row=3, pady=5)

#radio button 4
    self.rb4 = Radiobutton(self.quiz_frame, text=questions_answers[qnum][4], font=("Helvetica","12"), bg=background_color, value=4, padx=10, pady=10, variable = self.var1, indicator = 1, background = "light grey")
    self.rb4.grid(row=4, pady=5)


  #Set questions setup
  def questions_setup(self):
    randomiser()
    self.var1.set(0)
    self.question_label.config(text=questions_answers[qnum][0])
    self.rb1.config(text=questions_answers[qnum][1])
    self.rb2.config(text=questions_answers[qnum][2])
    self.rb3.config(text=questions_answers[qnum][3])
    self.rb4.config(text=questions_answers[qnum][4])
 

  #confirm button command, could be enchanced  
  def test_progress(self):
      global score
      scr_label = self.score_label
      choice = self.var1.get()
      if len(asked)>6:
        if choice == questions_answers[qnum][4]:  
          score +=1
          scr_label.configure(text=score)
          self.confirm_button.config(text="CONFIRM")
          self.endscreen()
        else:
            score+=0
            scr_label.configure(text="Unfortunately the answer was " + questions_answers[qnum][4]) 
            self.quiz_instance.config(text="CONFIRM")
            self.endscreen()
      else:
         if choice == 0:
             scr_label.configure(text="Why didn't you pick something too hard?")
             choice=self.var1.get()
         else:
           if choice == questions_answers[qnum][4]:
              score +=1
              scr_label.configure(text=score)
              self.quiz_instance.config(text="CONFIRM")
              self.questions_setup()
           else:
               score+=0
               scr_label.configure(text="Unfortunately the answer was " + questions_answers[qnum][4])
               self.quiz_instance.config(text="CONFIRM")
               self.questions_setup()

class End:
  def __init__ (self):
    background="deep sky blue"
    self.end_box = Toplevel(root)# top level widgets work as windows  that are directly managed by the window manager 
    self.end_box.title("End Box")

    self.end_frame = Frame (self.end_box, width=10000, height=10000, bg=background)
    self.end_frame.grid(row=0)

    self.end_heading = Label (self.end_frame, text="Congrats", font=("Helvetica", 22), bg=background, pady=15)
    self.end_heading.grid(row=0)

    self.exit_button = Button (self.end_frame, text="Exit", width=10, bg="deep sky blue", font=("Helvetica", 12), command=self.close_end)
    self.exit_button.grid(row=4, pady=20)

  def close_end(self):
    self.end_box.destroy()
    root.destroy()

  def endscreen(self):
    root.destroy()
    name=names[0]
    file=open("leaderBoard.txt", 'a')
    file.write(str(score))
    file.write(" - ")
    file.write(name+"\n")
    file.close()

    inputFile = open("leaderBoard.txt", 'r')
    lineList = inputFile.readlines()
    lineList.sort()
    top=[]
    top5=(lineList[-5:])
    for line in top5:
      point=line.split(" - ")
      top.append((int(point[0]), point[1]))
    file.close()
    top.sort()
    top.reverse()
    return_string= ""
    for i in range(len(top)):
        return_string +="{} - {}\n" .format(top[i][0], top[i][1])
    print(return_string)

    open_endscrn=End()
    open_endscrn.listLabel.config(text=return_string)

    


    
      

      

#************Starting point program************#

if __name__ == "__main__":
  root = Tk()
  root.title("MATHS")
  quizStarter_object = QuizStarter(root)
  root.mainloop()