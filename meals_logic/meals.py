from breakfast_area import breakfast

def meal_choice():
    while True:
        print("""
          1.Breakfast
          2.Lunch
          3.Dinner
          4.Snacks
          """)
        select_meal=input("Please select an option :")
        if select_meal==1:
          breakfast()
        elif select_meal==2:
          pass
        elif select_meal==3:
          pass
        elif select_meal==4:
          pass
        else:
          pass
    
    