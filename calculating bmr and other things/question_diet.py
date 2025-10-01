from personalize_macros import tdee_value
import time








def option(tdee_value):
    
        print("Choose an opcion :")
        print("""
        #      1.Volumen
        #     2.Cutting""")
        ask=int(input("What are you going to choose??:"))
        if ask==1:
            print(""" 1. Agressive bulking
              2. Normal bulking  """)
            bulk_type=int(input("What type of bulking are you looking for ?:"))
            if bulk_type==1:
                cal_ag=500
                sum_bulk=tdee_value+cal_ag
                print(f"Your total of calories for your bulking are : {sum_bulk}cal     ")
                return sum_bulk
            elif bulk_type==2:
                cal_n=300
                bulk_n=tdee_value+cal_n
                print(bulk_n)
                return bulk_n
        elif ask==2:
            print(""" 1. Agressive bulking
              2. Normal bulking  """)
            cutting_type=int(input("What type of cutting are you looking for :  "))
            if cutting_type==1:
                print("Welcome tu aggresive cutting")
                cut_1=700
                cutting_a=tdee_value+cut_1
                print(cutting_a +"cal")
                return cutting_a
            elif cutting_type==2:
                print("Welcome to normal cutting")
                cut_2=500
                cutting_n=cut_2+tdee_value
                print(cutting_n +"cal")
                return cutting_n
                
                
            
            
            
option(tdee_value)
    

    
    

