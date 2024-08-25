import json
from google_currency import convert  

try: 
    convert_from=input("Enter the currency you want to convert from(like inr,usd etc):- ")
    convert_to=input("Enter the currency you want to convert to:- ")
    amount=int(input("Enter the amount:- "))

    result= convert(convert_from, convert_to, amount)
    parsedResult=json.loads(result)


    if parsedResult["converted"]==True:
        print(f"Result:-\n {amount} {parsedResult["from"]} = {parsedResult["amount"]} {parsedResult["to"]}") 
    else:
        print("Failed to convert")
except Exception as e:
    print(f"An error occured: {e}")