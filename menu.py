from texts import activity_level
from wrap_up import info_and_bmr
from control import TDEE
from wrap_up import info_and_bmr,set_macros
from open_food.wrap_api import calling

def menu_user():
    completed_info=False
    while True:
        print(" --- Macro Tracker --- ")
        print("1.Calculate your BMR : ")
        print(" 2 .Calculate your TDEE based on your activity")
        print("3. Search an ingredient ")
        choice=int(input("Choice a number (1/2/3):"))
        if choice==1:
            value_bmr,wg,name=info_and_bmr()
            completed_info=True
        
        elif choice==2:
            if completed_info:
                type_act,activity = activity_level() #Type of activity 
                show_tdee=TDEE(activity,type_act,value_bmr) #Calculates your TDEE in base of your activity
                set_macros(wg,name,show_tdee)
            else:
                print("First,you must fill your basic information.")
        elif choice==3:
            calling()
        else:
            print("Please,Enter a valid number")
            
            
            
        