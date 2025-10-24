
import pandas as pd
import numpy as np

def check_macro():
    read_macro=pd.read_csv("data_macros.csv")
    name_user=str(read_macro.iloc[-1]['Name'])
    protein_value=int(read_macro.iloc[-1]['Protein'])
    fat_value=int(read_macro.iloc[-1]['Fat'])
    cal_value=int(read_macro.iloc[-1]["Total Calories"])
    macro_user={
        "User":name_user,
        "Protein":protein_value,
        "Fats":fat_value,
        "Goal Calories":cal_value
        
    }
    return macro_user




        
        
