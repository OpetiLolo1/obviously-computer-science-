from tkinter import*
from PIL import ImageTk, Image

names_list = []

class QuizStarter:
  def __init__(self, parent):
    background_color="deep sky blue"

    #frame set up
    self.quiz_frame = Frame(parent, bg = background_color, padx=10, pady=10)
    self.quiz_frame.grid()

    #Label widget for heading
    self.heading_label = Label (self.quiz_frame, text = "MATHS", font=("Helvetica", "30", "bold"), bg=background_color)
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

  

#************Starting point program************#
if __name__ == "__main__":
  root = Tk()
  root.title("MATHS")
  quizStarter_object = QuizStarter(root)
  root.mainloop()