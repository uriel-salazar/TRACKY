def verify(answer, minim=None, maxim=None):
    while True:
        user_input = input(answer).strip()  
        try:
            num = int(user_input)
            
        except ValueError:
            print("Please enter a valid number")
            continue
        
        if minim is not None and num < minim:
            print(f"Number must be at least {minim}.")
            continue
        if maxim is not None and num > maxim:
            print(f"Number must be at most {maxim}.")
            continue
        
        return num 
    
    
def fun_m(prompt, min_age=None, max_age=None):
    while True:
        user_input = input(prompt).strip()
        try:
            num = int(user_input)
        except ValueError:
            print("Please enter a valid number")
            continue
        
        if min_age is not None and num < min_age:
            print(f"You have to at least have {min_age} years old for using this app")
            continue
        if max_age is not None and num > max_age:
            print("Are you an alien? 👽")
            continue
        
        return num

def incorrect(word,valid_words):
    while True: 
        option=input(word).strip()
        
        if option in valid_words:
            return option
        else:
            print('You have to enter a valid word ("yes" /"no")')
        
            
        
            
        
        