import math

def get_change(user_input):
    user_input2 = float(user_input)  # Convert user_input to a float
    vesals = math.ceil(user_input2)  # Nākamais veselais skaitlis
    change = abs(vesals - user_input2)
      # Format change to two decimal places as a string

    return  change  # Return both the next integer and the change value