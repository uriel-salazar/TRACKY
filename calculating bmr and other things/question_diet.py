from personalize_macros import tdee_value

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
                      sum=tdee_value+500
                      print(f"Your total of calories for your bulking are : {sum:.0f} cal     ")
                elif bulk_type==2:
    
                     sum=tdee_value+300
                    
                     print(f' {sum:.0f} cal ')
                return sum
        elif ask==2:
            print(""" 1. Agressive cutting
              2. Normal cutting  """)
            cutting_type=int(input("What type of cutting are you looking for :  "))
            if cutting_type==1:
                print("Welcome to aggressive cutting")
                
                sum=tdee_value-700
                print(f'{sum:.0f} cal ')
                
            elif cutting_type==2:
                print("Welcome to normal cutting")
                sum=tdee_value-500
                print(f'{sum:.0f} cal ')
            return sum
                
                
    #defining two functions for setting up the daily protein 
            
def prote(wg):
  rule_prote=2.2
  calcul=rule_prote*wg
  print(f'Your daily ingest of protein : {calcul:.0f}')
  
  
  

def fats_bk(sum):
    if sum:
      intake_f=0.25
      fat_sum=int(sum*intake_f/9)
      print(f"Your daily fat intake is : {fat_sum:.0f} gr")
       
    else:
      pass
    return fat_sum
    
  
    

   
            
option(tdee_value)

prote(wg)

fat_sum=fats_bk(sum)

fats_bk(fat_sum)




    

    
    

