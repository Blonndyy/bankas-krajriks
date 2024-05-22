from tkinter import *
from tkinter import ttk, messagebox
from change_func import get_change
import time
from datetime import datetime
class KrajriksApp:
    def __init__(self, root):
        self.root = root
        self.krajriks_popup_check = False
        self.nauda = 10000.00
        self.krajkonts = 0.00
        
        self.root.title("Krajrīks")
        self.root.geometry("1000x800")
        self.root.configure(bg='orange')  
        
        self.center_window(1000, 800)
        
        self.style = ttk.Style()
        self.style.configure('Button',background='orange', font=('Arial', 12), padding=10)
        self.style.configure('Label',background='orange', font=('Arial', 12))
        self.style.configure('Header.TLabel',background='orange', font=('Arial', 15, 'bold'))
        self.style.configure('TFrame', background='orange')
        
        self.create_main_widgets()
        self.create_krajriks_widgets()
        
    def center_window(self, width, height):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x_coordinate = (screen_width - width) // 2
        y_coordinate = (screen_height - height) // 2
        self.root.geometry(f"{width}x{height}+{x_coordinate}+{y_coordinate}")
    
    def create_main_widgets(self):
        self.bilance_label = ttk.Label(self.root, text="Bilance:", style='Header.TLabel', background='orange')
        self.bilance_label.place(relx=0.05, rely=0.05)
        
        self.naudas_text = StringVar(value="{:.2f}".format(self.nauda))
        self.label = ttk.Label(self.root, textvariable=self.naudas_text, background="orange", )
        self.label.place(relx=0.15, rely=0.055)
        
        self.button_frame = ttk.Frame(self.root)
        self.button_frame.place(relx=0.1, rely=0.15)
        
        self.krajriks_button = ttk.Button(self.button_frame, text="Krajriks",  command=self.show_krajriks_widgets)
        self.krajriks_button.pack(pady=10)
    
    def create_krajriks_widgets(self):
        self.style = ttk.Style()
        self.style.configure('TButton',background='orange', font=('Arial', 12), padding=10)
        self.style.configure('TLabel',background='orange', font=('Arial', 12))
        self.style.configure('Header.TLabel',background='orange', font=('Arial', 15, 'bold'))
        self.style.configure('TFrame', background='orange')
        
        self.krajriks_frame = ttk.Frame(borderwidth=2, relief="solid")
        self.krajriks_frame.pack_propagate()
        self.krajriks_label = ttk.Label(self.krajriks_frame, text="Krajkonts:", style='Header.TLabel')
        self.krajriks_label.place(relx=0.40, rely=0.05)
        
        self.krajkonta_text = StringVar(value="{:.2f}".format(self.krajkonts))
        self.krajkonta_nauda = ttk.Label(self.krajriks_frame, textvariable=self.krajkonta_text, style='Header.TLabel')
        self.krajkonta_nauda.place(relx=0.55, rely=0.053)
        
        self.basic_button = ttk.Button(self.krajriks_frame, style='TButton', text="Back", command=self.close_krajriks_widgets)
        self.basic_button.place(relx=0.85, rely=0.02)
        
        self.test_label = ttk.Label(self.krajriks_frame, text='Testēšana priekš krājkonta')
        self.test_label.place(relx=0.3, rely=0.35)
        
        self.produkta_summa_label = ttk.Label(self.krajriks_frame, text='Produkta summa, testēšanai.')
        self.produkta_summa_label.place(relx=0.3, rely=0.40)
        
        self.prod_sum = ttk.Entry(self.krajriks_frame)
        self.prod_sum.place(relx=0.6, rely=0.40)
        
        
        self.save_button = ttk.Label(self.krajriks_frame, text="šo pogu tiks testēts vai darbojas krajkonta funkcionalitāte", wraplength=300)
        self.save_button.place(relx=0.3, rely=0.55)
        
        self.save_button = ttk.Button(self.krajriks_frame, text="Start", command=self.galvenais_cikls)
        self.save_button.place(relx=0.5, rely=0.6)
        
        #papildināšana
        self.vienreizeja_iemaksa_button=ttk.Button(self.krajriks_frame, text='Papildināt', command=self.open_papildinat)
        self.vienreizeja_iemaksa_button.place(relx=0.32, rely=0.2)
        #izņemšana
        self.iznemsana_button=ttk.Button(self.krajriks_frame, text='Izņemt', command=self.open_iznemt)
        self.iznemsana_button.place(relx=0.45, rely=0.2)
        
        #mēneša iemaksa
        self.menesa_iemaksa_label=ttk.Button(self.krajriks_frame, text='dads')
        
        #Paziņojums, kas parādas pēc krājkonta bilances sasniegšanai noteiktai summai.
        self.merka_button = ttk.Button(self.krajriks_frame, text="Nosaki mērķi", command=self.pazinojumi)
        self.merka_button.place(relx=0.45, rely=0.10)
        
    #papildināšanai    
    def open_papildinat(self):
        self.papildinat = Toplevel(self.root)
        self.papildinat.title("Papildinat")
        self.papildinat.grab_set()
        self.papildinat.configure(background="darkorange")
        self.papildinat.update_idletasks()
        x = self.root.winfo_x() + self.root.winfo_width() // 2 - 100
        y = self.root.winfo_y() + self.root.winfo_height() // 2 - 50
        self.papildinat.geometry(f"400x200+{x}+{y}")   
        
       
        
        self.vienrsum = ttk.Entry(self.papildinat)
        self.vienrsum.place(relx=0.3, rely=0.45)
        
        self.Nosutit=ttk.Button(self.papildinat,text='Nosūtīt', command=self.one_off_payment)
        self.Nosutit.place(relx=0.4, rely=0.60)
        
    #izņemšanai
    def open_iznemt(self):
        self.iznemt = Toplevel(self.root)
        self.iznemt.title("Izņemšana")
        self.iznemt.grab_set()
        self.iznemt.configure(background="darkorange")
        self.iznemt.update_idletasks()
        x = self.root.winfo_x() + self.root.winfo_width() // 2 - 100
        y = self.root.winfo_y() + self.root.winfo_height() // 2 - 50
        self.iznemt.geometry(f"400x200+{x}+{y}")   
        
       
        
       
    
    #mērķa noteikšanai un mērķa sasniegšanas paziņojums    
    def pazinojumi(self):
        self.pazinojumi = Toplevel(self.root)
        self.pazinojumi.title("pazinojumi")
        self.pazinojumi.grab_set()
        self.pazinojumi.configure(background="darkorange")
        self.pazinojumi.update_idletasks()
        x = self.root.winfo_x() + self.root.winfo_width() // 2 - 100
        y = self.root.winfo_y() + self.root.winfo_height() // 2 - 50
        self.pazinojumi.geometry(f"400x200+{x}+{y}")
        
        
    
        self.pazinojumi_text= ttk.Label(self.pazinojumi, background='darkorange', text= 'tu esi lohs')
        self.pazinojumi_text.place(relx=0.2, rely=0.2)
        
        self.pazinojumi_entry = ttk.Entry(self.pazinojumi)
        self.pazinojumi_entry.place(relx=0.1, rely=0.1)

        self.pazinojumi_button = ttk.Button(self.pazinojumi, text="Apstiprināt", command=self.merka_noteiksana)
        self.pazinojumi_button.place(relx=0.5, rely=0.1)
        
        self.pazinojumi_text= ttk.Label(self.pazinojumi, background='darkorange', text= 'kraj savu naudu')
        self.pazinojumi_text.place(relx=0.2, rely=0.2)

    def merka_noteiksana(self):
        global krajkonts
        merkis = self.pazinojumi_entry.get()
        try:
            amount2 = float(merkis)
            print(amount2)
            self.pazinojumi.destroy()
            if self.krajkonts >= amount2 :
                self.merka_noteiksana = Toplevel(self.root)
                self.merka_noteiksana.title(" MĒRĶIS?")
                self.merka_noteiksana.grab_set()
                self.merka_noteiksana.configure(background="darkorange")
                self.root.update_idletasks()
                x = self.root.winfo_x() + self.root.winfo_width() // 2 - 100
                y = self.root.winfo_y() + self.root.winfo_height() // 2 - 50
                self.merka_noteiksana.geometry(f"400x200+{x}+{y}")
            else:
                pass
        except:
            pass
     
       
             
        
    def menesa_iemaksa(self):
        global krajkonts, nauda
        if datetime.now().day==5:
            d
            
            
            
        
    def open_popup(self):
        
        self.popup = Toplevel(self.root)
        self.popup.title("Popup Window")
        self.popup.grab_set()
        self.popup.configure(background="darkorange")
        self.root.update_idletasks()
        x = self.root.winfo_x() + self.root.winfo_width() // 2 - 100
        y = self.root.winfo_y() + self.root.winfo_height() // 2 - 50
        self.popup.geometry(f"400x200+{x}+{y}")
        
        popup_text = ttk.Label(self.popup,background='darkorange', text="Vai tu vēlies uzsākt krājkontu?")
        popup_text.pack(pady=10)
        
        yes_button = ttk.Button(self.popup, text="Yes", command=self.yes)
        yes_button.place(x=20, y=50)
        
        no_button = ttk.Button(self.popup, text="No", command=self.no)
        no_button.place(x=150, y=50)
    
    def no(self):
        self.popup.destroy()
    
    def yes(self):
        self.krajriks_popup_check = True
        self.popup.destroy()
        self.show_krajriks_frame()
    
    def show_krajriks_widgets(self):
        if not self.krajriks_popup_check:
            self.open_popup()
        else:
            self.show_krajriks_frame()
    
    def show_krajriks_frame(self):
        self.krajriks_frame.place(relx=0, rely=0, relwidth=1, relheight=1)
    
    def close_krajriks_widgets(self):
        self.krajriks_frame.place_forget()
    
    def update_bilance(self):
        user_input = self.prod_sum.get()
        if user_input:
            try:
                amount = float(user_input)
                if amount > self.nauda:
                    messagebox.showerror("Error", "Nav tik daudz naudas")
                else:
                    self.nauda -= amount
                    self.naudas_text.set("{:.2f}".format(self.nauda))
            except ValueError as e:
                messagebox.showerror("Error", str(e))

    
    def krajkonta_bilance(self):
        user_input = self.prod_sum.get()
        if user_input:
            try:
                change = get_change(user_input)
                changes = float(change)
                if changes > self.nauda:
                    messagebox.showerror("Error", "Nav tik daudz naudas")
                else:
                    self.krajkonts += changes
                    self.nauda -= changes
                    self.naudas_text.set("{:.2f}".format(self.nauda))
                    self.krajkonta_text.set("{:.2f}".format(self.krajkonts))
            except ValueError as e:
                messagebox.showerror("Error", str(e))

    
    def one_off_payment(self):
        
        user_input_one_off = self.vienrsum.get()
        if user_input_one_off:
            try:
                one_off = float(user_input_one_off)
                self.papildinat.destroy()
                if self.nauda < one_off:
                    messagebox.showerror("Error", "Nav tik daudz naudas.")
                else:
                    self.krajkonts += one_off
                    self.nauda -= one_off
                    self.naudas_text.set("{:.2f}".format(self.nauda))
                    self.krajkonta_text.set("{:.2f}".format(self.krajkonts))
            except ValueError as e:
                messagebox.showerror("Error", str(e))


    def galvenais_cikls(self):
        self.update_bilance()
        self.krajkonta_bilance()
        self.one_off_payment()
        self.merka_noteiksana()

if __name__ == "__main__":
        root = Tk()
        app = KrajriksApp(root)
        root.mainloop()
    
