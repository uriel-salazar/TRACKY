

def basic_info():
        while True:
                print("Setting up your calories :")
                year=int(input("How old are you?? :"))
                wg=float(input("what is your weigh??: "))
                gre=input("Are you a women or men ? (woman/man)").upper()
                h=float(input(("What is your heigh??")))
                name=input("What is your name?? (STRING) : ")
    
                
                print("--- Confirming your data ---")
                check=print(f'''
                Name={name}
                Gender:{gre}
                Years :{year} years old 
                Weight:{wg}kg
                Heigh :{h} m''')
                
            