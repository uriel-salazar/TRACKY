import pandas as pd



def remaining():
    user_data = pd.read_csv("data_macros.csv")
      

    print("Your macros in gr:")
    print(user_data.iloc[0].to_string(index=True))
    name_main=user_data.loc[0,"Name"]
    fat_main=user_data.loc[0,"Fat"]
    prote_main=user_data.loc[0,"Protein"]
    carb_main=user_data.loc[0,"Carbs"]
    calories_main=user_data.loc[0,"Total Calories"]
    return name_main,fat_main,prote_main,carb_main,calories_main


def goal_user(name, fat_goal, prote_goal, carb_goal, cal_goal, 
               fat_u, prote_u, carb_u,cal_u):
    fat_goal = int(fat_goal)
    prote_goal = int(prote_goal)
    carb_goal = int(carb_goal)
    cal_goal = int(cal_goal)
    fat_u = int(fat_u)
    prote_u = int(prote_u)
    carb_u = int(carb_u)
    cal_u = int(cal_u)

    print(f'Hii {name}!'  )
    full_cal=cal_goal-cal_u
    full_carb=carb_goal-carb_u
    full_prote=prote_goal-prote_u
    print(f"CAL:{full_cal}")
    print(f" CARBS :  {full_carb}")
    print(f"PROTE : {full_prote}")
   
    
    