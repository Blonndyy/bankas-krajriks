from tkinter import *

#galvenais logs
logs=Tk()
logs.geometry("1000x800")
logs['bg']='orange'
label_font = ("Arial",15)
#konts ar bilanci
#melns negeris
#melns baltādainais
print("hallo")
nauda=10000
bilance=Label(logs, 
         text="Bilnace:",
         bg='orange',
         font=label_font
         )
bilance.place(x=10, 
         y=10)



logs.mainloop()
