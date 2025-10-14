import pandas as pd 
import os 


def begin_data(nickname,bmr_value,gen):
    """Save basic info data

    Args:
        nickname (str): User's name
        bmr_value (float): BMR value calculated
        gen (str ): Genre of the user 
    """
    print("Your data has been saved succesfully!") 
    nickname=str(nickname)
    bmr_value=float(bmr_value)
    gen=str(gen)
    if  gen=="MAN":
        m_dat=pd.DataFrame({
                    "Name":[nickname],
                    "BMR":[bmr_value],
                    "Genre":[gen]
                
        })
        m_dat.to_csv("bmr_man.csv",mode="a",index=False,header=not os.path.exists("bmr_man.csv"))
    else:
        w_dat=pd.DataFrame({
                  "Name":[nickname],
                  "BMR":[bmr_value],
                  "Genre":[gen]
        
    })
        w_dat.to_csv("bmr_woman.csv",mode="a",index=False,header=not os.path.exists("bmr_woman.csv"))




def save_macro(name,fat_gram,prote_grams,carb_grams,cal_value):
    name=str(name)
    fat_gram=int(fat_gram)
    prote_grams=int(prote_grams)
    carb_grams=int(carb_grams)
    cal_value=int(cal_value)
    macros={
     "Name":[name],
      "Fat":[fat_gram],
   "Protein":[prote_grams],
     "Carbs":[carb_grams],
     "Total Calories":[cal_value]
    }
    
    macro_save=pd.DataFrame(macros)
    print("Your macros in gr:")
    print(macro_save)
  
    file_macro="data_macros.csv"
    if not os.path.exists(file_macro):
            macro_save.to_csv(file_macro,index=False,header=True)
    else:
       macro_save.to_csv(file_macro,mode='a',header=False,index=False)