import pandas as pd

AVAILABLE_USER_INPUT_OPTIONS={
    1:"List company with product count",
    2:"Display the data as table"
}

# Display welcome message which will list the avialable options
def show_user_options():    
    print("Welcome to inventory")
    WELCOME_TEXT="Welcome to inventory, Please select below options\n"

    for key,value in AVAILABLE_USER_INPUT_OPTIONS.items():
        WELCOME_TEXT+=f"[{key}]. {value}\n"

    return int(input(f"{WELCOME_TEXT}Enter:- "))


# List company with product count in dictionary
def list_company_product_count(df):
    result=df.groupby("Supplier")["Product No"].count()
    return result.to_dict()

try:

    USER_SELECTED_OPTION= show_user_options()

    df=pd.read_excel("./assets/inventory.xlsx")
    match USER_SELECTED_OPTION:
        case 1: list_company_product_count()
        case 2: print(f"\n {df.to_string()}")
        case _: print("Invalid option")
    
    
except Exception as e:
    if e==FileNotFoundError:
        print("File not found. Please check the path")
    else:
        print("Unknown error",e)