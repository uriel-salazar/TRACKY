from open_food.wrap_api import fetch_user_macros
from meals_logic.manual_functions import track,save_meal,calculate,goal_macro,remain
 
def manually_track():
    """ Shows a menu for track your macros 

    Returns:
        dict: Dict manual macros 
    """
    meals={}
    while True:
        print("--- Tracking your macros manually ---")
        print("1.Enter your food manually")
        print("2. Check you food registered food ")
        print("3.Check your total macros  ")
        print("4.Exit ")
        option=int(input("What are you going to choose?:"))
        if option == 1:
            meals = track()
        elif option == 2:
            if meals: 
                number_save=save_meal(meals)
            else:
                print(" ⚠️ First you have to track your food ⚠️")
        elif option == 3:
            dat_cal,dat_prote,dat_carb,dat_fats=calculate()
            name_main ,fat_main,prote_main,carb_main,calories_main=fetch_user_macros()
            goal,current=goal_macro(fat_main,prote_main,carb_main,calories_main,
                       dat_fats,dat_prote,dat_carb,dat_cal)
            remain(goal,current)
        elif option == 4:
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")
    
    return meals


    
    

