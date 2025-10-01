def get_integer(prompt=ask):
    """
    Continuously prompt the user until a valid integer is entered.
    
    Returns:
        int: The integer entered by the user.
    """
    while True:
        try:
            value = int(input(prompt))
            return value  
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
