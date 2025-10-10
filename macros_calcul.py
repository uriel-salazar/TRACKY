
import pandas as pd




                
                
    #defining two functions for setting up the daily protein 
            


def fats(cal):
      intake_f=0.25
      cal=int(cal)
      fat_sum=round(cal*intake_f/9)
      gram_f=9
      cal_fat=fat_sum*gram_f
      
      print(f"Your daily fat intake is : {fat_sum} gr equals : {cal_fat} cal")
      return cal_fat,fat_sum

    
  
def carb(cal,cal_fat,cal_prote):
        v_carb=cal-cal_prote-cal_fat
        grams=round(v_carb/4)
        print(f"You carbs :{grams} gr")
        return grams
      

            

#total_cal=calories(tdee_value)

#prote_cals,prote_grams=prote(wg)

#fat_cals,fat_grams=((fats(total_cal)))
#grams = carb(total_cal, fat_cals, prote_cals)


##saving data 
 #def save_data():
 #   macros={
     "Name":[name],
      "Fat":[fat_grams],
   "Protein":[prote_grams],
     "Carbs":[grams]
    }
    
#    macro_save=pd.DataFrame(macros)
#    print(macro_save)
  
  #  file_macros="data_macros.csv"
 #   if not os.path.exists(file_macros):
        macro_save.to_csv(file_macros,index=False,header=True)
#    else:
 #      macro_save.to_csv(file_macros,mode='a',header=False,index=False)
      
#save_data()







    

    
    

