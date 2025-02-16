import re

def getPharmacyInfo():
    userIn = input("Would you like to input or amend pharmacy information? (Y/N): ")
    
    if userIn.upper() == "Y":
        pharName = input("Please input the name of your pharmacy: ")
        
        phone_pattern = r'^\d{3}-\d{3}-\d{4}$'
        while True:
            pharNumber = input("Please input the phone number of your pharmacy (xxx-xxx-xxxx): ")
            if re.match(phone_pattern, pharNumber):
                break
            else:
                print("Invalid phone number format. Please try again.")
        
        address_pattern = r'^[\w\s]+,\s*[\w\s]+,\s*[\w\s]+,\s*\d{5}$'
        while True:
            pharAddress = input("Please input the address of your pharmacy (Street address, City, State, Postal code): ")
            if re.match(address_pattern, pharAddress):
                break
            else:
                print("Invalid address format. Please try again.")
        
        print("Pharmacy Name:", pharName)
        print("Pharmacy Phone Number:", pharNumber)
        print("Pharmacy Address:", pharAddress)
    
    elif userIn.upper() == "N":
        print("Thank you for visiting and/or inputting your pharmacy information.")
    
    else:
        print("Invalid input.")
