
from texts import activity_level
from control import TDEE,prote

from wrap_it_up import info_and_bmr,decision



def main():
    value_bmr,wg=info_and_bmr() #This is going to calculate the basic info and the bmr of the user()
    type_act,activity = activity_level()  #Type of activity 
    show_tdee=TDEE(activity,type_act,value_bmr) #it'll calculate your TDEE
    user_decision=decision(show_tdee) 
    prote_grams,prote_cal=prote(wg) #Returning protein 
    

    


    

    
if __name__ == "__main__":
    main()



    
    
