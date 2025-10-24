
import pandas as pd

def check_macro():
    read_macro=pd.read_csv("data_macros.csv")
    name_user=read_macro.iloc[-1]['Name']
    protein_value=read_macro.iloc[-1]['Protein']
    fat_value=read_macro.iloc[-1]['Fat']
    cal_value=read_macro.iloc[-1]["Total Calories"]
    print(name_user,protein_value,cal_value,fat_value)
    macro_user={
        "User"
    }


def check_data():
    while True:
        
        
