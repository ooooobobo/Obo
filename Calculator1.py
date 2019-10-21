from tkinter import*
def btnClick(numbers):
    global operator
    operator=operator + str(numbers)
    text_Input.set(operator)
    
def btnClearDisplay():
    global operator
    operator=""
    text_Input.set("")

def btnEqualsInput():
    global operator
    sumup=str(eval(operator))
    text_Input.set(sumup)
    operator=""

cal = Tk()
cal.title("Obo\'s Calculator")
operator=""
text_Input= StringVar()
txtDisplay =Entry(cal,font=('bold italic ', 22,'bold'),textvariable=text_Input, bd=32, insertwidth=5, bg="red", justify='right') .grid(columnspan=5)

btn7=Button(cal,padx=16,bd=9, fg="purple" ,font=('bold italic ', 22,'bold'),
            text="7",bg="black",command=lambda:btnClick(7)).grid(row=1,column=0)
btn6=Button(cal,padx=16,bd=9, fg="purple",font=('bold italic ', 22,'bold'),
            text="6",bg="black",command=lambda:btnClick(6)).grid(row=2,column=2)
btn5=Button(cal,padx=16,bd=9, fg="purple",font=('bold italic ', 22,'bold'),
            text="5",bg="black",command=lambda:btnClick(5)).grid(row=2,column=1)
btn4=Button(cal,padx=16,bd=9, fg="purple",font=('bold italic ', 22,'bold'),
            text="4",bg="black",command=lambda:btnClick(4)).grid(row=2,column=0)
btn3=Button(cal,padx=16,bd=9, fg="purple",font=('bold italic ', 22,'bold'),
            text="3",bg="black",command=lambda:btnClick(3)).grid(row=3,column=2)
btn2=Button(cal,padx=16,bd=9, fg="purple",font=('bold italic ', 22,'bold'),
            text="2",bg="black",command=lambda:btnClick(2)).grid(row=3,column=1)
btn1=Button(cal,padx=16,bd=9, fg="purple",font=('bold italic ', 22,'bold'),
            text="1",bg="black",command=lambda:btnClick(1)).grid(row=3,column=0)
btn0=Button(cal,padx=16,bd=9, fg="purple",font=('bold italic ', 22,'bold'),
            text="0",bg="black",command=lambda:btnClick(0)).grid(row=4,column=0)
btn9=Button(cal,padx=16,bd=9, fg="purple",font=('bold italic ', 22,'bold'),
            text="9",bg="black",command=lambda:btnClick(9)).grid(row=1,column=2)
btn8=Button(cal,padx=16,bd=9, fg="purple",font=('bold italic ', 22,'bold'),
            text="8",bg="black",command=lambda:btnClick(8)).grid(row=1,column=1)
Addition=Button(cal,padx=16,bd=9, fg="purple",font=('bold italic ', 22,'bold'),
            text="+",bg="black",command=lambda:btnClick('+')).grid(row=1,column=3)
Subtraction=Button(cal,padx=16,bd=9, fg="purple",font=('bold italic ', 22,'bold'),
        text="-",bg="black",command=lambda:btnClick('-')).grid(row=2,column=3)
Multiplication=Button(cal,padx=16,bd=9, fg="purple",font=('bold italic ', 22,'bold'),
        text="*",bg="black",command=lambda:btnClick('*')).grid(row=3,column=3)
Divition=Button(cal,padx=16,bd=9, fg="purple",font=('bold italic ', 22,'bold'),
        text="/",bg="black",command=lambda:btnClick('/')).grid(row=4,column=2)
Equal=Button(cal,padx=16,bd=9, fg="purple",font=('bold italic ', 22,'bold'),
            text="=",bg="black",command=btnEqualsInput).grid(row=4,column=3)
C=Button(cal,padx=16,bd=9, fg="purple",font=('bold italic ', 22,'bold'),
            text="C",bg="black",command=btnClearDisplay).grid(row=4,column=1)















cal.mainloop()


                               
