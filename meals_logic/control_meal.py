
def track_meal():
    morning=[]
    
    
def manual_track():
    print("--Quick Add---")
    name_food=input("Description :")
    cal_food=input("Energy (cal) :")   
    prote_food=input("Protein (g) :")
    carb_food=input("Carb (g) : ")
    fat_food=input("Enter your fat value ")
    
    user_info={
        "Description":name_food,
        "Calories":cal_food,
        "Protein":prote_food,
        "Carbs":carb_food,
        "Fats":fat_food
        
    }
    print("Save it as? :")
    print("1.Breakfast, 2. Snack , 3.Meal , 4. Dinner")
    enter_type=int(input("What are you going to choose??:"))
    if enter_type==1:
        name_track.append(breakfast_area)
    
    
    
    

def api_track():
    
    while True:
        print("1.Enter your food manually")
        print("2.Enter your food with our api sistem ")
        self_or_api=int(input("What are you going to choose?:"))
        if self_or_api==1:
            manual_track()
        elif self_or_api==2:
            pass
        
    
    
    

    