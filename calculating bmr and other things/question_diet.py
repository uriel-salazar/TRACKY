from personalize_macros import tdee_value
import pandas as pd
from personalize_macros import wg




def option(tdee_value):
    
        print("Choose an opcion :")
        print("""
        #      1.Volumen
        #     2.Cutting """)
        ask=int(input("What are you going to choose??:"))
        
        
        if ask==1:
                print("""
                1. Agressive bulking 
                2. Normal bulking """)
                bulk_type=int(input("What type of bulking are you looking for ?:"))
                if bulk_type==1:  
                      cal=tdee_value+500
                      print(f"Your total of calories for your bulking are : {cal:.0f} cal     ")
                elif bulk_type==2:
    
                     cal=tdee_value+300
                    
                     print(f' {cal:.0f} cal ')
                return cal
        elif ask==2:
            print(""" 1. Agressive cutting
              2. Normal cutting  """)
            cutting_type=int(input("What type of cutting are you looking for :  "))
            if cutting_type==1:
                print("Welcome to aggressive cutting")
                
                cal=tdee_value-700
                print(f'{cal:.0f} cal ')
                
            elif cutting_type==2:
                print("Welcome to normal cutting")
                cal=tdee_value-500
                print(f'{cal:.0f} cal ')
            return cal,ask
                
                
    #defining two functions for setting up the daily protein 
            
def prote(wg):
  rule_prote=2.2
  calcul=rule_prote*wg
  gram_p=4
  cal_prote=calcul*gram_p
  
  print(f'Your daily ingest of protein : {calcul:.0f} gr  ({cal_prote:.0f}cal )')
  return cal_prote,calcul
  
   

def fats_bk(cal):
      intake_f=0.25
      cal=int(cal)
      fat_sum=cal*intake_f/9
      gram_f=9
      cal_fat=fat_sum*gram_f
      
      print(f"Your daily fat intake is : {fat_sum:.0f} gr equals : {cal_fat:.0f} cal")
      return cal_fat,fat_sum

    
  
def carbs_grams(cal,cal_fat,cal_prote):
        v_carb=cal-cal_prote-cal_fat
        grams=v_carb/4
        print(f"You carbs :{grams:.0f} gr")
        return grams
      

            

option(tdee_value)

prote_cals,prote_grams=prote(wg)

fat_cals,fat_grams=((fats_bk(tdee_value)))
grams=carbs_grams(tdee_value,prote_grams,fat_grams)

#### saving data 
def save_data():
    macros={
    "Fat":[fat_grams],
    "Protein":[prote_grams],
    "Carbs":[grams]
    
              }
    macro_save=pd.DataFrame(macros)
    print(macro_save)
  

save_data()







    

    
    

