from tkinter import *
from change_func import *
#galvenais logs
logs=Tk()
logs.geometry("1000x800")
logs['bg']='orange'
label_font = ("Arial",15) 



#konts ar bilanci
bilance=Label(logs, 
         text="Bilnace:",
         bg='orange',
         font=label_font,
         )
bilance.place(x=10, 
              y=10)
nauda=10000
nauda_v2="{:.2f}".format(nauda)
naudas_text = StringVar(logs, value=nauda_v2)
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

#Tagad viss priekš produkta summas iegūšanas un tās summas noņēmšanu no bilances
#pluss errori.
def update_bilance():
    global nauda
    user_input = prod_sum.get()
    if user_input:
        try:
            amount=float(user_input)
            if amount > nauda:
                print("Error: Nav tik daudz naudas")
            else:
                nauda-= amount
                naudas_text.set("{:.2f}".format(nauda))
        except ValueError as e:
            print("Error:", e)
    else:
        print("Error: Input is empty")
        
#Viss priekš krājkonta un bilances aprēķināšanu, 

        
krajkonts=0
krajkonts_v2="{:.2f}".format(krajkonts)
krajkonta_text = StringVar(logs, value=krajkonts_v2)
krajkonta_label = Label(logs, textvariable=krajkonta_text, font=label_font, bg="orange")
krajkonta_label.place(x=200, y=10)

def krajkonta_bilance():
    global change
    global krajkonts
    global nauda
    user_input=prod_sum.get()
    if user_input:
        try:
            change = get_change(user_input)
            changes=float(change)
            krajkonts +=changes
            nauda -=changes
            naudas_text.set("{:.2f}".format(nauda))
            krajkonta_text.set("{:.2f}".format(krajkonts))
           
        except ValueError as e:
            print("Error:", e)
    else:
        print("Error: Input is empty")

#uzpsiežot save and use pogu, viss uz ekrana mainīsies tāka tas notiktu, kad kaut ko 
#nopērk un aktivizējas krājrīks.      
def galvenais_cikls():
    update_bilance()
    krajkonta_bilance()
            
save_button = Button(logs, 
                     text="Save and Use", 
                     command=galvenais_cikls,
                     activebackground='darkorange',
                     bg='orange' )

save_button.place(x=30, y= 100)

logs.mainloop()