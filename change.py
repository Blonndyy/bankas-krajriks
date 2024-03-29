import math

cena = 3.25

def nako_vesels(cena):
    vesals = math.ceil(cena)  # Nākamais veselais skaitlis
    change = abs(vesals - cena)
    change_str = "{:.2f}".format(change)  # Format change to two decimal places as a string

    return vesals, change_str

vesals, change = nako_vesels(cena)
print(vesals)
print(change)