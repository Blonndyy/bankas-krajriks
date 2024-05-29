import math

def get_change(user_input):
    user_input2 = float(user_input)  
    vesals = math.ceil(user_input2)  # Nākamais veselais skaitlis
    change = abs(vesals - user_input2)

    return  change 