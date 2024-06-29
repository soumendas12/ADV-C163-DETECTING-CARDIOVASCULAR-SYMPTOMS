from tkinter import *
root = Tk()
from tkinter import messagebox
root.title("Heart_Diagnose_Report")
root.geometry("600x630")
root.configure(background="#fa8071")

question1_radioButton=StringVar(value="0")
question2_radioButton=StringVar(value="0")
question3_radioButton=StringVar(value="0")
question4_radioButton=StringVar(value="0")
question5_radioButton=StringVar(value="0")

Question1=Label(root, text ="Do you experience shortness of breath during activities?")
Question1.pack()
question1_r1=Radiobutton(root, text = "yes", variable=question1_radioButton, value="yes")
question1_r1.pack()
question1_r2=Radiobutton(root, text = "no", variable=question1_radioButton, value="no")
question1_r2.pack()

Question2=Label(root, text ="Do you have a swelling in the feet/ankles/legs (shoes feel tighter) or abdomen?")
Question2.pack()
question2_r1=Radiobutton(root, text = "yes", variable=question2_radioButton, value="yes")
question2_r1.pack()
question2_r2=Radiobutton(root, text = "no", variable=question2_radioButton, value="no")
question2_r2.pack()

Question3=Label(root, text ="Do you feel any of the symptoms - confusion, disorientatione or loss of memory ?")
Question3.pack()
question3_r1=Radiobutton(root, text = "yes", variable=question3_radioButton, value="yes")
question3_r1.pack()
question3_r2=Radiobutton(root, text = "no", variable=question3_radioButton, value="no")
question3_r2.pack()

Question4=Label(root, text ="Do you experience shortness of breath while at rest/lying down?")
Question4.pack()
question4_r1=Radiobutton(root, text = "yes", variable=question4_radioButton, value="yes")
question4_r1.pack()
question4_r2=Radiobutton(root, text = "no", variable=question4_radioButton, value="no")
question4_r2.pack()

Question5=Label(root, text ="Do you experience persistent weezing/coughing that produces white or pink blood tinged muscles?")
Question5.pack()
question5_r1=Radiobutton(root, text = "yes", variable=question5_radioButton, value="yes")
question5_r1.pack()
question5_r2=Radiobutton(root, text = "no", variable=question5_radioButton, value="no")
question5_r2.pack()

def heart_score():
    score = 0
    if question1_radioButton.get()=="yes":
        score = score+10
        print(score)
    if question2_radioButton.get()=="yes":
        score = score+10
        print(score)
    if question3_radioButton.get()=="yes":
        score = score+10
        print(score)
    if question4_radioButton.get()=="yes":
        score = score+10
        print(score)
    if question5_radioButton.get()=="yes":
        score = score+10
        print(score)
        
    if score <= 10:
        messagebox.showinfo("Report","You don't need to visit a doctor.")
    elif score > 10 and score <= 30:
         messagebox.showinfo("Report","You might perhaps have to visit a doctor.")
    else:
         messagebox.showinfo("Report","I strongly advise you to visit a doctor.")
btn = Button(root, text= "Click me", command= heart_score)        
btn.pack()
root.mainloop()