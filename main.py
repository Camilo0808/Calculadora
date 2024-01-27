from tkinter import *


app = Tk()

app.geometry("344x460")
app.title("Calculadora")
app.config(background='Dark gray')
app.iconbitmap("./img/calc.ico")

textin = StringVar()
operador = ""

def clickbut(number):
     global operador
     operador=operador+str(number)
     textin.set(operador)

def equlbut():
     global operador
     add=str(eval(operador))
     textin.set(add)
     operador=''
def equlbut():
     global operador
     sub=str(eval(operador))
     textin.set(sub)
     operador=''     
def equlbut():
     global operador
     mul=str(eval(operador))
     textin.set(mul)
     operador=''
def equlbut():
     global operador
     div=str(eval(operador))
     textin.set(div)
     operador=''    

def clrbut():
     textin.set('')


apptext = Entry(app, font=("Arial",12,'bold'), textvar=textin, width=31, bd=5, bg='light blue')
apptext.place(x=10, y=20)

button1 = Button(app, padx=14, pady=14, bd=4, bg='white', command=lambda:clickbut(1), text="1", font=("Courier New",16,'bold'))
button1.place(x=10, y=100)

button2 = Button(app, padx=14, pady=14, bd=4, bg='white', command=lambda:clickbut(2), text="2", font=("Courier New",16,'bold'))
button2.place(x=10, y=170)

button3 = Button(app, padx=14, pady=14, bd=4, bg='white', command=lambda:clickbut(3), text="3", font=("Courier New",16,'bold'))
button3.place(x=10, y=240)

button4 = Button(app, padx=14, pady=14, bd=4, bg='white', command=lambda:clickbut(4),text="4", font=("Courier New",16,'bold'))
button4.place(x=75, y=100)

button5 = Button(app, padx=14, pady=14, bd=4, bg='white', command=lambda:clickbut(5), text="5", font=("Courier New",16,'bold'))
button5.place(x=75, y=170)

button6 = Button(app, padx=14, pady=14, bd=4, bg='white', command=lambda:clickbut(6), text="6", font=("Courier New",16,'bold'))
button6.place(x=75, y=240)

button7 = Button(app, padx=14, pady=14, bd=4, bg='white', command=lambda:clickbut(7), text="7", font=("Courier New",16,'bold'))
button7.place(x=140, y=100)

button8 = Button(app, padx=14, pady=14, bd=4, bg='white', command=lambda:clickbut(8), text="8", font=("Courier New",16,'bold'))
button8.place(x=140, y=170)

button9 = Button(app, padx=14, pady=14, bd=4, bg='white', command=lambda:clickbut(9), text="9", font=("Courier New",16,'bold'))
button9.place(x=140, y=240)

button0 = Button(app, padx=14, pady=14, bd=4, bg='white', command=lambda:clickbut(0), text="0", font=("Courier New",16,'bold'))
button0.place(x=10, y=310)

buttondot = Button(app, padx=47, pady=14, bd=4, bg='white', command=lambda:clickbut("."), text=".", font=("Courier New",16,'bold'))
buttondot.place(x=75, y=310)

buttonpl = Button(app, padx=14, pady=14, bd=4, bg='white', text="+", command=lambda:clickbut("+"), font=("Courier New",16,'bold'))
buttonpl.place(x=205, y=100)

buttonsub = Button(app, padx=14, pady=14, bd=4, bg='white', text="-", command=lambda:clickbut("-"), font=("Courier New",16,'bold'))
buttonsub.place(x=205, y=170)

buttonml = Button(app, padx=14, pady=14, bd=4, bg='white', text="*", command=lambda:clickbut("*"), font=("Courier New",16,'bold'))
buttonml.place(x=205, y=240)

buttondiv = Button(app, padx=14, pady=14, bd=4, bg='white', text="/", command=lambda:clickbut("/"), font=("Courier New",16,'bold'))
buttondiv.place(x=205, y=310)

buttonclear = Button(app, padx=14, pady=119, bd=4, bg='white', text="C", command=clrbut, font=("Courier New",16,'bold'))
buttonclear.place(x=270, y=100)

buttonequal = Button(app, padx=144, pady=14, bd=4, bg='white', command=equlbut, text="=", font=("Courier New",16,'bold'))
buttonequal.place(x=10, y=380)

app.mainloop()