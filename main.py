from tkinter import *
from change_func import *
#galvenais logs
logs=Tk()
logs.geometry("1000x800")
logs['bg']='orange'
label_font = ("Arial",15) 



#konts ar bilanci
nauda=10000
bilance=Label(logs, 
         text="Bilnace:",
         bg='orange',
         font=label_font,
         )
bilance.place(x=10, 
              y=10)
naudas_text = StringVar(logs, value=nauda)
label = Label(logs, textvariable=naudas_text, font=label_font, bg="orange")
label.place(x=80, y=10)

#priekš testēšanas, simulācija kur tiks nopirkts kaut kas(pats var ievadīt izterēto summu). 
#Kas pēc tamm tiks izmantota, lai veiktu noapaļošanu, un atlikuma ielikšanu krājkontā.
produkts=Label(logs,
               text="Prod.sum:",
               bg='orange',
               font=label_font)
produkts.place(x=10,
               y=50)

prod_sum=Entry(logs)
prod_sum.place(x=110,
               y=55,
               width=50
               )

#Tagad viss priekš produkta summas iegūšanas un tās summas noapaļošanas.
  # Declare kraj_konta_sum as a global variable

def save_and_use_entry():
    
    global prod_sum
    global change
    user_input = prod_sum.get()  # Retrieve value from Entry widget
    if user_input:  # Check if user_input is not empty
        try:
            kraj_konta_sum, change = get_change(user_input)  # Call get_change with user_input
        except ValueError as e:
            print("Error:", e)
    else:
        print("Error: Input is empty")
def output():
    print(change)
        
save_button = Button(logs, 
                     text="Save and Use", 
                     command=save_and_use_entry,
                     activebackground='darkorange',
                     bg='orange' )

save_button.place(x=30, y= 100)

save_button2 = Button(logs, 
                     text="Save and Use2", 
                     command=output,
                     activebackground='darkorange',
                     bg='orange' )

save_button2.place(x=30, y= 300)

krajkonta_bil = StringVar(logs, value=change)
krajkonta_label = Label(logs, textvariable=krajkonta_bil, font=label_font, bg="orange")
krajkonta_label.place(x=200, y=10)


logs.mainloop()