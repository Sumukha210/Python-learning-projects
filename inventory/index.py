import pandas as pd

AVAILABLE_USER_INPUT_OPTIONS={
    1:"List company with product count",
    2:"Display the data as table",
    3:"List Products with inventory less than 10",
    4:"List each company with respective total inventory value",
}

# Display welcome message which will list the avialable options
def show_user_options():    
    WELCOME_TEXT="Welcome to inventory, Please select below options\n"

    for key,value in AVAILABLE_USER_INPUT_OPTIONS.items():
        WELCOME_TEXT+=f"[{key}]. {value}\n"

    return int(input(f"{WELCOME_TEXT}Enter:- "))


# List company with product count in dictionary
def list_company_product_count(df):
    result=df.groupby("Supplier")["Product No"].count()
    return result.to_dict()

# List Products with inventory less than 10
def list_products_below():
    low_inventory = df[df['Inventory'] < 10].set_index('Product No')['Inventory'].to_dict()
    print(low_inventory)

# List each company with respective total inventory value
def list_company_total_inventory_value():
    total_inventory_value_dict = df.groupby('Supplier').apply(lambda x: (x['Inventory'] * x['Price']).sum()).to_dict()
    print(total_inventory_value_dict)


try:

    USER_SELECTED_OPTION= show_user_options()

    df=pd.read_excel("./assets/inventory.xlsx")
    match USER_SELECTED_OPTION:
        case 1: list_company_product_count()
        case 2: print(f"\n {df.to_string()}")
        case 3: list_products_below()
        case 4: list_company_total_inventory_value()
        case _: print("Invalid option")
    
    
except Exception as e:
    if e==FileNotFoundError:
        print("File not found. Please check the path")
    else:
        print("Unknown error",e)