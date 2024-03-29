import math

def get_change(user_input):
    user_input = float(user_input)  # Convert user_input to a float
    vesals = math.ceil(user_input)  # Nākamais veselais skaitlis
    change = abs(vesals - user_input)
    change_str = "{:.2f}".format(change)  # Format change to two decimal places as a string

    return vesals, change_str  # Return both the next integer and the change value