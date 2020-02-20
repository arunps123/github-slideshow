import tkinter
from tkinter import *
import random

python_questions = [
     "Which of these in not a core data type ?",
     "Which of the following functions takes A console Input in Python ?",
     "In order to store values in terms of key and value we use what core data type ?",
     "Which of The Following is must to Execute a Python Code ?",
     "Select the reserved keyword in python  ?",
     "The append Method adds value to the list at the  ?",
     "Which predefined Python function is used to find length of string?",
     "Syntax of constructor in Python ?",
     "Which of the following keyword is used to create a function in Python ?",
     "To Declare a Global variable in python we use the keyword ?",
     "Which statement is correct....? ",
 ]

python_answers_choice = [
     ["list","dictionary","tuples","class",],
     ["get()","input()","gets()","scan()",],
     ["list","dictionary","tuples","class",],
     ["TURBO C","Py Interpreter","Notepad","IDE",],
     ["else","import","raise","all of these",],
     ["custom location","end","center","beginning",],
     ["length()","strlen()","len()","stringlength()",],
     ["def __init__()","def _init_()","_init_()","all of these",],
     ["function","void","fun","def",],
     ["all","var","let","global",],
     ["List is mutable && Tuple is immutable"," List is immutable && Tuple is mutable","Both are Immutable","Both are Mutable",],
 ]

python_answers=[3,1,1,1,3,1,2,0,3,3,0]

java_questions = [
     "Which statement is true regarding an object ?",
     "Why In Java, declaring a class abstract is useful ?",
     "A package is a collection of ?",
     "Given a class named Book, which one of these is a valid constructor declaration for the class ?",
     "Which one of the following class definitions is a valid definition of a class that cannot be extended  ?",
     "How restrictive is the default accessibility compared to public, protected, and private accessibility ?",
     "What is the sequence of major events in the life of an applet?",
     " What is garbage collection in the context of Java ?",
     "Who is known as father of Java Programming Language ?",
     "Which provides runtime environment for java byte code to be executed ?",
     "Java language was initially called as? ",
 ]

java_answers_choice = [
     ["An object is what classes instantiated are from","An object is an instance of a class","An object is a variable","An object is a reference to an attribute",],
     ["When it doesn’t make sense to have objects of that class","To prevent developers from further extending the class","To force developers to extend the class not to use its capabilities","When it makes sense to have objects of that class",],
     ["Classes","Interfaces","Editing tools","Classes and interfaces",],
     ["Book(Book b) { }","Book Book() { }","private final Book() { }","abstract Book() { }",],
     ["abstract class Link { }","native class Link { }","static class Link { }","final class Link { }",],
     ["Less restrictive than public","More restrictive than public, but less restrictive than protected","More restrictive than protected, but less restrictive than private","More restrictive than private",],
     ["init, start, stop, destroy","start, init , stop , destroy","init, start , destroy, stop","init, start, destroy",],
     ["The operating system periodically deletes all of the java files available on the system","Any package imported in a program and not used is automatically deleted"," When all references to an object are gone, the memory used by the object is automatically reclaimed"," The JVM checks the output of any Java program and deletes anything that doesn’t make sense",],
     ["M. P Java","Blais Pascal","Charel Babbage","James Gosling",],
     ["JDK","JVM","JRE","JAVAC",],
     ["Sumatra"," J++","Oak","Pine",],
 ]

java_answers=[1,0,3,0,3,2,0,2,3,1,2]

random_questions = [
     "Which of these is not a core datatype ?",
     "Which of the following functions takes A console Input in Python ?",
     "Java language was initially called as? ",
     "Which of The Following is must to Execute a Python Code ?",
     "Who is known as father of Java Programming Language ?",
     "The append Method adds value to the list at the  ?",
     "Which provides runtime environment for java byte code to be executed ?",
     "Syntax of constructor in Python ?",
     "A package is a collection of ?",
     "To Declare a Global variable in python we use the keyword ?",
     "What is the sequence of major events in the life of an applet?",
 ]

random_answers_choice = [
     ["list","dictionary","tuples","class",],
     ["get()","input()","gets()","scan()",],
     ["Sumatra"," J++","Oak","Pine",],
     ["TURBO C","Py Interpreter","Notepad","IDE",],
     ["M. P Java","Blais Pascal","Charel Babbage","James Gosling",],
     ["custom location","end","center","beginning",],
     ["JDK","JVM","JRE","JAVAC",],
     ["def __init__()","def _init_()","_init_()","all of these",],
     ["Classes","Interfaces","Editing tools","Classes and interfaces",],
     ["all","var","let","global",],
     ["init, start, stop, destroy","start, init , stop , destroy","init, start , destroy, stop","init, start, destroy",]]

random_answers=[3,1,2,1,3,1,1,0,3,3,0]

user_answer=[]

indexes=[]
def gen():
    global indexes
    while(len(indexes)<10):
        x=random.randint(0,10)
        if x in indexes:
            continue
        else:
            indexes.append(x)

def showresult(score):
    lblQuestion.destroy()
    r1.destroy()
    r2.destroy()
    r3.destroy()
    r4.destroy()
    labelimage = Label(
        root,
        background = "#ffffff",
        border = 0,
    )
    mark="your score is  "+str(score)
    labelimage.pack(pady=(50,30))
    labelresulttext = Label(
        root,
        font = ("Consolas",20),
        background = "#ffffff",
    )
    labelresulttext.pack()
    if score>=20:
        img=PhotoImage(file="great.png")
        labelimage.configure(image=img)
        labelimage.image=img
        labelresulttext.configure(text=mark)
    elif(score>=10 and score<20):
        img=PhotoImage(file="ok.png")
        labelimage.configure(image=img)
        labelimage.image=img
        labelresulttext.configure(text=mark)
    else:
        img=PhotoImage(file="bad.png")
        labelimage.configure(image=img)
        labelimage.image=img
        labelresulttext.configure(text=mark)
        
        

def p_calc():
    global indexes,user_answer,python_answers
    x=0
    score=0
    for i in indexes:
        if user_answer[x]==python_answers[i]:
            score=score+5
        x+=1
    print(score)
    showresult(score)

def j_calc():
    global indexes,user_answer,java_answers
    x=0
    score=0
    for i in indexes:
        if user_answer[x]==java_answers[i]:
            score=score+5
        x+=1
    print(score)
    showresult(score)

def r_calc():
    global indexes,user_answer,random_answers
    x=0
    score=0
    for i in indexes:
        if user_answer[x]==random_answers[i]:
            score=score+5
        x+=1
    print(score)
    showresult(score)
    
            
ques=1
def p_selected():
    global radiovar,user_answer
    global lblQuestion,r1,r2,r3,r4
    global ques
    x=radiovar.get()
    user_answer.append(x)
    radiovar.set(-1)
    if ques<10:
        lblQuestion.config(text=python_questions[indexes[ques]])
        r1['text'] = python_answers_choice[indexes[ques]][0]
        r2['text'] = python_answers_choice[indexes[ques]][1]
        r3['text'] = python_answers_choice[indexes[ques]][2]
        r4['text'] = python_answers_choice[indexes[ques]][3]
        ques += 1
    else:
        print(indexes)
        print(user_answer)
        p_calc()

def j_selected():
    global radiovar,user_answer
    global lblQuestion,r1,r2,r3,r4
    global ques
    x=radiovar.get()
    user_answer.append(x)
    radiovar.set(-1)
    if ques<10:
        lblQuestion.config(text=java_questions[indexes[ques]])
        r1['text'] = java_answers_choice[indexes[ques]][0]
        r2['text'] = java_answers_choice[indexes[ques]][1]
        r3['text'] = java_answers_choice[indexes[ques]][2]
        r4['text'] = java_answers_choice[indexes[ques]][3]
        ques += 1
    else:
        print(indexes)
        print(user_answer)
        j_calc()

def r_selected():
    global radiovar,user_answer
    global lblQuestion,r1,r2,r3,r4
    global ques
    x=radiovar.get()
    user_answer.append(x)
    radiovar.set(-1)
    if ques<10:
        lblQuestion.config(text=random_questions[indexes[ques]])
        r1['text'] = random_answers_choice[indexes[ques]][0]
        r2['text'] = random_answers_choice[indexes[ques]][1]
        r3['text'] = random_answers_choice[indexes[ques]][2]
        r4['text'] = random_answers_choice[indexes[ques]][3]
        ques += 1
    else:
        print(indexes)
        print(user_answer)
        r_calc()

def option():
    global btnStart1,btnStart2,btnStart3
    btnStart1=Button(root,text="python",height=2,width=12,command=option1)
    btnStart1.pack(pady=(100,30))
    btnStart2=Button(root,text="java",height=2,width=12,command=option2)
    btnStart2.pack(pady=(30,30))
    btnStart3=Button(root,text="random",height=2,width=12,command=option3)
    btnStart3.pack(pady=(30,30))

def option1():
    btnStart1.destroy()
    btnStart2.destroy()
    btnStart3.destroy()
    gen()
    p_startquiz()

def option2():
    btnStart1.destroy()
    btnStart2.destroy()
    btnStart3.destroy()
    gen()
    j_startquiz()

def option3():
    btnStart1.destroy()
    btnStart2.destroy()
    btnStart3.destroy()
    gen()
    r_startquiz()
   
            
def p_startquiz():
    global lblQuestion,r1,r2,r3,r4
    lblQuestion=Label(root,text=python_questions[indexes[0]],
                      font=("consolas",16),width=500,
                      justify="center",wraplength=400,
                      background="#ffffff",)
    lblQuestion.pack(pady=(100,30))

    global radiovar

    radiovar=IntVar()
    radiovar.set(-1)

    r1=Radiobutton(root,text=python_answers_choice[indexes[0]][0],
                   font=("Times",12),value=0,
                   variable=radiovar,command = p_selected,
                   background="#ffffff",)
    r1.pack(pady=7)

    r2=Radiobutton(root,text=python_answers_choice[indexes[0]][1],
                   font=("Times",12),value=1,
                   variable=radiovar,command = p_selected,
                   background="#ffffff",)
    r2.pack(pady=7)

    r3=Radiobutton(root,text=python_answers_choice[indexes[0]][2],
                   font=("Times",12),value=2,
                   variable=radiovar,command = p_selected,
                   background="#ffffff",)
    r3.pack(pady=7)

    r4=Radiobutton(root,text=python_answers_choice[indexes[0]][3],
                   font=("Times",12),value=3,
                   variable=radiovar,command = p_selected,
                   background="#ffffff",)
    r4.pack(pady=7)

def j_startquiz():
    global lblQuestion,r1,r2,r3,r4
    lblQuestion=Label(root,text=java_questions[indexes[0]],
                      font=("consolas",16),width=500,
                      justify="center",wraplength=400,
                      background="#ffffff",)
    lblQuestion.pack(pady=(100,30))

    global radiovar

    radiovar=IntVar()
    radiovar.set(-1)

    r1=Radiobutton(root,text=java_answers_choice[indexes[0]][0],
                   font=("Times",12),value=0,
                   variable=radiovar,command = j_selected,
                   background="#ffffff",)
    r1.pack(pady=7)

    r2=Radiobutton(root,text=java_answers_choice[indexes[0]][1],
                   font=("Times",12),value=1,
                   variable=radiovar,command = j_selected,
                   background="#ffffff",)
    r2.pack(pady=7)

    r3=Radiobutton(root,text=java_answers_choice[indexes[0]][2],
                   font=("Times",12),value=2,
                   variable=radiovar,command = j_selected,
                   background="#ffffff",)
    r3.pack(pady=7)

    r4=Radiobutton(root,text=java_answers_choice[indexes[0]][3],
                   font=("Times",12),value=3,
                   variable=radiovar,command = j_selected,
                   background="#ffffff",)
    r4.pack(pady=7)

def r_startquiz():
    global lblQuestion,r1,r2,r3,r4
    lblQuestion=Label(root,text=random_questions[indexes[0]],
                      font=("consolas",16),width=500,
                      justify="center",wraplength=400,
                      background="#ffffff",)
    lblQuestion.pack(pady=(100,30))

    global radiovar

    radiovar=IntVar()
    radiovar.set(-1)

    r1=Radiobutton(root,text=random_answers_choice[indexes[0]][0],
                   font=("Times",12),value=0,
                   variable=radiovar,command = r_selected,
                   background="#ffffff",)
    r1.pack(pady=7)

    r2=Radiobutton(root,text=random_answers_choice[indexes[0]][1],
                   font=("Times",12),value=1,
                   variable=radiovar,command = r_selected,
                   background="#ffffff",)
    r2.pack(pady=7)

    r3=Radiobutton(root,text=random_answers_choice[indexes[0]][2],
                   font=("Times",12),value=2,
                   variable=radiovar,command = r_selected,
                   background="#ffffff",)
    r3.pack(pady=7)

    r4=Radiobutton(root,text=random_answers_choice[indexes[0]][3],
                   font=("Times",12),value=3,
                   variable=radiovar,command = r_selected,
                   background="#ffffff",)
    r4.pack(pady=7)


                      
def startIspressed():
    labelimage.destroy()
    labeltext.destroy()
    lblInstruction.destroy()
    btnStart.destroy()
    lblRules.destroy()
    option()
    

root=tkinter.Tk()
root.title("QUIZ MASTER")
root.geometry("700x600")
root.config(background="#ffffff")

img1=PhotoImage(file="logo.png")

labelimage=Label(root,image=img1,background="#ffffff")
labelimage.pack()

labeltext=Label(root,text="QUIZ MASTER",font=("calibri",24,"bold"))
labeltext.pack(pady=(0,50))


btnStart=Button(root,text="START",height=2,width=12,command=startIspressed)
btnStart.pack()

lblInstruction = Label(
    root,
    text = "Read The Rules And\nClick Start Once You Are ready",
    background = "#ffffff",
    font = ("Consolas",14),
    justify = "center",
)
lblInstruction.pack(pady=(10,100))

lblRules = Label(
    root,
    text = "This quiz contains 10 questions\n each correct answer is awarded with 5 points \n Once you select a radio button that will be a final choice\nhence think before you select",
    width = 100,
    font = ("Times",14),
    background = "gray",
    foreground = "#FACA2F",
)
lblRules.pack()


 

root.mainloop()
