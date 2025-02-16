import re

#Function for user to input pharmacy data
def getPharmacyInfo():
    #Intializes variable for user start input
    userIn = input("Would you like to input or change pharmacy information? (Y/N): ")

    #User indicated that they would like to amend or input data
    if userIn.upper() == "Y":
        #Initializes variable for pharmacy name
        pharName = input("Please input the name of your pharmacy: ")

        #Ensures that user is using correct format
        phone_pattern = r'^\d{3}-\d{3}-\d{4}$'
        while True:
            #Initializes variable for pharmacy number
            pharNumber = input("Please input the phone number of your pharmacy (xxx-xxx-xxxx): ")
            if re.match(phone_pattern, pharNumber):
                break
            else:
                print("Invalid phone number format. Please try again.")

        #Ensures that user is using correct format
        address_pattern = r'^[\w\s]+,\s*[\w\s]+,\s*[\w\s]+,\s*\d{5}$'
        while True:
            #Initializes variable for pharmacy address
            pharAddress = input("Please input the address of your pharmacy (Street address, City, State, Postal code): ")
            if re.match(address_pattern, pharAddress):
                break
            else:
                print("Invalid address format. Please try again.")

        #Prints the pharmacy information inputted by user
        print("Pharmacy Name:", pharName)
        print("Pharmacy Phone Number:", pharNumber)
        print("Pharmacy Address:", pharAddress)

    #User indicated that they would not like to amend or input data
    elif userIn.upper() == "N":
        print("Thank you for visiting and/or inputting your pharmacy information.")

     #Invalid initial user input
    else:
        print("Invalid input.")
