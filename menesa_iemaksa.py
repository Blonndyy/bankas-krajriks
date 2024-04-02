import time
nauda = 100
krajkonts = 0
vienrsum = 10
def monthly_payment():
    global krajkonts, nauda, vienrsum
    user_input_one_off = vienrsum
    if  user_input_one_off:
        try:
            one_off = float(user_input_one_off)
            krajkonts +=one_off
            nauda -=one_off
            print(("{:.2f}".format(nauda)))
            print(("{:.2f}".format(krajkonts)))
           
        except ValueError as e:
            print("Error:", e)
    else:
        print("Error: Input is empty")
while True:
    monthly_payment()
    time.sleep(30)        