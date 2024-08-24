print("Welcome to the Calculator!")
avilable_option_list={
    1:"Addition",
    2:"Subtraction",
    3:"Multiplication",
    4:"Division"
}

input_text="Please select an operation \n"

for key,value in avilable_option_list.items():
    input_text+=f"{key}. {value}\n"


user_selected_option=int(input(f"{input_text} Choose: "))

if user_selected_option in avilable_option_list:
    print(f"Selected option= {avilable_option_list.get(user_selected_option)}")
    first_value=float(input("Enter the first number:"))
    second_value=float(input("Enter the second number:"))
    result=0
    match user_selected_option:
        case 1:
            result=first_value+second_value
        case 2:
            result=first_value-second_value
        case 3:
            result=first_value*second_value
        case 4:
            result=first_value/second_value
    print(f"Result= {result}") 
    print("Thank you for using our calculator")
else:
    print("Invalid option!!!")