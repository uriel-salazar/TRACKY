import os
import pandas as pd



def data():
    while True:
                print("Setting up your calories :")
                year=int(input("How old are you?? :"))
                wg=float(input("what is your weigh??: "))
                gre=input("Are you a women or men ? (woman/man)").lower()
                h=float(input(("What is your heigh??")))
                
                print("--- Confirming your data ---")
                check=print(f'''
                Years :{year} years old 
                Weight:{wg}kg
                Heigh :{h} m
                Gender:{gre} 
                            ''')
                confirm=input("Does your data is correct?? (yes/no):").lower()
                if confirm=="yes":
                    return year,wg,h,gre
                
                

          
def bmr(year,wg,h,gre):
    
    if gre=="man":
       value=10 *(wg) +6.25 *(h)-5*year+5
    else:
        value=10*(wg)+6.25*(h)-5*year-161
    return value
    
    
 
 
def write(value,gre):
    print("Your data has been saved succesfully!") 
    if  gre=="man":
        m_dat=pd.DataFrame({
                    "BMR":[value],
                    "Genre":[gre]
        })
        m_dat.to_csv("bmr_man.csv",mode="a",index=False,header=not os.path.exists("bmr_man.csv"))
    else:
        w_dat=pd.DataFrame({
                  "BMR":[value],
                  "Genre":[gre]
    })
        w_dat.to_csv("bmr_woman.csv",mode="a",index=False,header=not os.path.exists("bmr_woman.csv"))


def activity_level():
    activity={
        "sedentary": 1.2,
        "light": 1.375,
        "moderate": 1.55,
        "very": 1.725,
        "extra": 1.9
    }
    for i,each in enumerate(activity.keys(),start=1):
        print(f'-{i} {each}')

    type_act=int(input("What type of activty you are? (SELECT A NUMBER ) :"))
    return type_act,activity


def TDEE(type_act_key, bmr_value, activity_dict):
    multiply=activity_dict[type_act_key]
    result=bmr_value*multiply
    print(f'Your TDEE : {result}')
    return result
    
    
   
      
year,wg,h,gre=data()
bmr_value=bmr(year,wg,h,gre)
write(bmr_value,gre)

type_act_index,activity_dict=activity_level()
keys = list(activity_dict.keys())
type_act_key = keys[type_act_index - 1]

tdee_value = TDEE(type_act_key, bmr_value, activity_dict)


#print("Choose an opcion :")
 #   print("""
    #      1.Volumen
     #     2.Cutting""")
 #   ask=input("What are you going to choose??")


 
 
    



