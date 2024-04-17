from tkinter import *
from change_func import *
import tkinter as tk

def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x_coordinate = (screen_width - width) // 2
    y_coordinate = (screen_height - height) // 2

    window.geometry(f"{width}x{height}+{x_coordinate}+{y_coordinate}")

def close_krajriks_widgets():
    krajriks_frame.place_forget()
   

def show_krajriks_widgets():
    open_popup()

def no():
    popup.destroy()

def yes():
    popup.destroy()
    show_krajriks_frame()

def open_popup():
    global popup
    popup = Toplevel(logs)
    popup.title("Popup Window")
    popup.grab_set()

    # Calculate the position of the popup relative to the main window (logs)
    logs.update_idletasks()
    x = logs.winfo_x() + logs.winfo_width() // 2 - 100
    y = logs.winfo_y() + logs.winfo_height() // 2 - 50
    popup.geometry("200x100+{}+{}".format(x, y))

    popup_teksts = Label(popup, text="Vai tu vēlies uzsākt krājkontu?")
    popup_teksts.pack(pady=10)

    yes_button = Button(popup, text="Yes", command=yes)
    yes_button.place(x=20, y=50)

    no_button = Button(popup, text="no", command=no)
    no_button.place(x=80, y=50)

def show_krajriks_frame():
    krajriks_frame.place(relx=0.5, rely=0.5, anchor='center')  # Place the krajriks_frame


logs = Tk()
logs.title("Main window")
logs.geometry("1000x800")
logs['bg'] = 'orange'
label_font = ("Arial",15) 
center_window(logs, 1000, 800)


bilance_label = Label(logs, text="Bilance:", bg='orange', font=("Arial", 15))
bilance_label.place(x=40, y=40)
nauda = 10000
naudas_text = StringVar(value="{:.2f}".format(nauda))
label = Label(logs, textvariable=naudas_text, font=("Arial", 15), bg="orange")
label.place(x=120, y=40)

# krajrika widget
krajriks_frame = Frame(logs, width=1000, height=800, bg="orange")
krajriks_label = Label(krajriks_frame, text="krajkonts", bg='orange', font=("Arial", 15))
krajriks_label.place(x=500,y=10)
krajriks_frame.place(x=0, y=0, relwidth=1, relheight=1)

#krajkonts
krajkonts=0
krajkonts_v2="{:.2f}".format(krajkonts)
krajkonta_text = StringVar(krajriks_frame, value=krajkonts_v2)
krajkonta_nauda = Label(krajriks_frame, textvariable=krajkonta_text, font=label_font, bg="orange")
krajkonta_nauda.place(x=800, y=20)

# pogas lai tiktu no konta uz krajkontu
basic_button = Button(krajriks_frame, text="back",activebackground='darkorange',
                     bg='orange', command=close_krajriks_widgets)
basic_button.place(x=400, y=400)

krajriks_button = Button(logs, text="Krajriks",activebackground='darkorange',
                     bg='orange', command=show_krajriks_widgets)
krajriks_button.place(x=500, y=400)

# ievades priekš krajrika testēšnaas
test=Label(krajriks_frame, text='testēšana priekš krājkonta', bg='orange')
test.place(x= 100, y=20)

produkta_summa=Label(krajriks_frame, text='Produkta summa, testēšanai.', bg='orange')
produkta_summa.place(x=100, y=60)
prod_sum = Entry(krajriks_frame)
prod_sum.place(x=100, y=80)
def update_bilance():
    global nauda
    user_input = prod_sum.get()
    if user_input:
        try:
            amount = float(user_input)
            if amount > nauda:
                print("Error: Nav tik daudz naudas")
            else:
                nauda -= amount
                naudas_text.set("{:.2f}".format(nauda))
        except ValueError as e:
            print("Error:", e)
    else:
        print("Error: Input is empty")

def krajkonta_bilance():
    global change, krajkonts, nauda
    user_input = prod_sum.get()
    if user_input:
        try:
            change = get_change(user_input)
            changes = float(change)
            krajkonts += changes
            nauda -= changes
            naudas_text.set("{:.2f}".format(nauda))
            krajkonta_text.set("{:.2f}".format(krajkonts))
        except ValueError as e:
            print("Error:", e)
    else:
        print("Error: Input is empty")
        
        
vienreizeja_iemaksa=Label(krajriks_frame, text='Vienreizējās iemaksas testēšanai', bg='orange')
vienreizeja_iemaksa.place(x=100, y= 120)
vienrsum = Entry(krajriks_frame)
vienrsum.place(x=100, y=140)

def one_off_payment():
    global krajkonts, nauda
    user_input_one_off = vienrsum.get()
    if user_input_one_off:
        try:
            one_off = float(user_input_one_off)
            if nauda < one_off:
                print("Nav tik daudz naudas.")
            else:
                krajkonts += one_off
                nauda -= one_off
                naudas_text.set("{:.2f}".format(nauda))
                krajkonta_text.set("{:.2f}".format(krajkonts))
        except ValueError as e:
            print("Error:", e)
    else:
        print("Error: Input is empty")
  
#galvenais cikls      
def galvenais_cikls():
    update_bilance()
    krajkonta_bilance()
    one_off_payment()
# Saglabāšanas poga priekš testu palaišanas
save_button_explanination=Label(krajriks_frame, text="Kad tiek ievadīta produkta summa un vai vienreizēja iemaksa, tad uzspiežot šo pogu tiks testēts vai darbojas kr,ajkonta funkcionalitāte",
                                                wraplength=200, 
                                                bg='orange',
                                                justify='center')
save_button_explanination.place(x=100, y=180)
save_button = Button(krajriks_frame, text="Start", command=galvenais_cikls,bg='orange', activebackground='darkorange')
save_button.place(x=180, y= 250)

 
logs.mainloop()
