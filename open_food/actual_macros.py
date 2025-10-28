import pandas as pd
from saving_data import basic_data


def remaining(group):
    if group == "MALE":
        user_data = pd.read_csv("data_macros.csv")
    else:
        user_data = pd.read_csv("data_macros.csv")

    print("Your macros in gr:")
    print(user_data.iloc[0].to_string(index=True))
    name_main=user_data.loc[0,"Name"]
    fat_main=user_data.loc[0,"Fat"]
    prote_main=user_data.loc[0,"Protein"]
    carb_main=user_data.loc[0,"Carbs"]
    calories_main=user_data.loc[0,"Total Calories"]
    
    