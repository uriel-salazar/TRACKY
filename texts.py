import os 
from validation import verify,fun_m,incorrect


def clear_console():
    if os.name == 'nt': 
        _ = os.system('cls')

def basic_info():
    """ Ask user basic information 

    Returns:
         - year (int): User's year of birth.
            - wg (float): User's weight in kilograms.
            - h (float): User's height in centimeters.
            - gre (str): User's gender ("WOMAN" or "MAN").
            - name (str): User's name.
  
    """
  
  
    while True:
                print("-- Setting up your calories ---")
                year=fun_m("How old are you?? :",min_age=13,max_age=130)
                wg=verify("what is your weigh?? (kg): ",minim=20,maxim=300)
                gre=input("Are you a female or male ? (female/male)").upper()
                h=verify("What is your heigh?? (cm)",minim=10,maxim=300)
                name=input("What is your name?? (STRING) : ")
    
                
                print("--- Confirming your data ✔ ---")
                print(f'''
                Name={name}
                Gender:{gre}
                Years :{year} years old 
                Weight:{wg:.0f} kg
                Heigh :{h} cm''')
                confirm=incorrect("Does your data is correct?? ('yes'/'no'):",['yes','no']).lower()
                if confirm=="yes":
                    clear_console()
                
                    return year,wg,h,gre,name
                            
def activity_level():
    """ Shows a dictionary and iterates each activity to the user 

    Returns:
        type_act (int)  : User's activity chosen
        activity(dict):Type of activities with key as value
    """
    activity={
        "sedentary": 1.2,
        "light": 1.375,
        "moderate": 1.55,
        "very": 1.725,
        "extra": 1.9
    }
    for i,each in enumerate(activity.keys(),start=1):
        print(f'-{i} {each}')

    type_act=verify("What type of activty you are? (SELECT A NUMBER ) :",minim=0,maxim=5)
    return type_act,activity


def option_goal():
    print("Choose an option :")
    print("1. Volumen\n2. Cutting")
    return verify("What are you going to choose?:",minim=0,maxim=2)


def type_bulking():
    print("""
                1. Agressive bulking 
                2. Normal bulking """)
    return verify("What type of bulking are you looking for ?:",minim=1,maxim=2)
    
    
def type_cutting():
    print("""
          1. Aggressive cutting
          2. Normal cutting """)
    return verify("What type of cutting are you going to do??",minim=1,maxim=2)


    
    
    
