#Task 1

def user_name(full_name):
    
    
    return full_name


while True:
    full_string = ''

    first_name = input("Enter your first name: ")
    if len(first_name) >= 2:
        full_string += first_name + ' '
        last_name = input("Enter your last name: ")
        if len(last_name) >= 2:
            full_string += last_name
            full_name = full_string
            print(f"Full name: {full_name}")
        else:
            print("Error: One or more names less than two characters.")
        
    else:
        print("ERROR: One or more names less than two characters")
    
    
    
    continue_input = input("Try Again? (y/n) :")
    if continue_input.lower() != 'y':
        break


    

    