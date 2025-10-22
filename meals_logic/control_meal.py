import os
morning=[]
import pandas as pd
    
def manual_track():
    control_meal = {"meals": {}}

    while True:
        print("--Quick Add---")
        meal_type = input("What is your meal? : ")
        name_food = input("Description: ")
        cal_food = int(input("Energy (cal): ")) 
        prote_food = int(input("Protein (g): "))
        carb_food = int(input("Carb (g): "))
        fat_food = int(input("Enter your fat value (g): "))
        save_it = input("Save it? (yes/no): ")

        if save_it.lower() == "yes":
            control_meal["meals"][meal_type] = {
            "Description": name_food,
            "Calories": cal_food,
            "Protein": prote_food,
            "Carbs": carb_food,
            "Fats": fat_food
            }
            print("Your info :")
            for meal_type, info in control_meal["meals"].items():
                print(f"{meal_type}")
                print(f"Cal :{info["Calories"]}")
                print(f"Protein :{ info["Protein"]}")
                
        repeat = input("Do you want to add another meal? (yes/no): ")
        if repeat.lower() != "yes":
            break  # exit loop if user says no
        else:
            continue
    return control_meal
    
    
    

def method_track():
    
    while True:
        print("1.Enter your food manually")
        print("2.Enter your food with our api sistem ")
        self_or_api=int(input("What are you going to choose?:"))
        if self_or_api==1:
            manual_track()
        elif self_or_api==2:
            pass
        

def track_macro_all(control_meal):
    rows = []
    for meal_type, info in control_meal["meals"].items():
            rows.append({
            "Meal": meal_type,
            "Description": info["Description"],
            "Calories": info["Calories"],
            "Protein": info["Protein"],
            "Carbs": info["Carbs"],
            "Fats": info["Fats"]
        })

    number_save = pd.DataFrame(rows)
    print("Your macros in gr:")
    print(number_save)

    file_macro = "manually_macros.csv"
    if not os.path.exists(file_macro):
        number_save.to_csv(file_macro, index=False, header=True)
    else:
        number_save.to_csv(file_macro, mode='a', header=False, index=False)
    return number_save


def show_table():
    see_table=input("Do you want to see the table?? (yes/no):")
    if see_table=="yes":
        calculate()
    else:
        pass
def calculate():
    read_macros=pd.read_csv("manually_macros.csv")
    dat_cal=read_macros["Calories"].sum()
    dat_prote=read_macros["Protein"].sum()
    dat_carb=read_macros["Carbs"].sum()
    dat_fats=read_macros["Fats"].sum()
    
    print(dat_cal,"calories")
    print("Protein :",dat_prote,"gr")
    print(f'Carbs :{dat_carb} gr')
    print(f'Fats : {dat_fats} gr') 
    

meals = manual_track()
track_macro_all(meals)
number_save=track_macro_all
calculate()


