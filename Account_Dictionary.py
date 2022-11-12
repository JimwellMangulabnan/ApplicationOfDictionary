print("*********  PROGRAMMED BY  ********")
print("***** JIMWELL L. MANGULABNAN *****")
print("********** BSCOE 2-2 *************")
print()

def print_menu():
# Display a menu 
 print(
     """
    ########################
    #        MENU          #
    #----------------------#
    #   1 >>  Add an item  #
    #   2 >>  Search       #
    #   3 >>  Exit         #
    ########################
""")


print_menu()

#listed Accounts
accounts = {
    "Harry Potter" : {
        "Age": 19,
        "Status" : "Single",
        "Gender" : "Male",
        "Saving" : "5000$"
    },
    "Enola Homes" : {
        "Age": 16,
        "Status" : "Single",
        "Gender" : "Female",
        "Saving" : "800$"
    },
    "Marian Rivera" : {
        "Age": 30,
        "Status" : "Married",
        "Gender" : "Female",
        "Saving" : "3000$"
    },
    "Naruto Uzumaki " : {
        "Age": 47,
        "Status" : "widow",
        "Gender" : "Male",
        "Saving" : "10000$"
    }
}

while True:
    #ask the user
    choice = int(input("Enter a number that you would like to do: "))
    #if option 1 = add item
    if choice == 1:
        try: 
            print("\n\t\t|  Add an item |\n")
            name = input("Enter the fullname (first name, surname): ")
            age = int(input("Enter his/her age: "))
            status = input("Enter the status of the person: ")
            gender = input("Enter the gender: ")
            money = input("please Enter your money savings: (Please put $ sign) ")
        except ValueError:
            print("\nInvalid input")
        else:
            accounts[name] = {
                "Age": age,
                "Status" : status,
                "Gender" : gender,
                "Saving" : money
            }
            print("Succesfully added!!!\n")
            print("this is the accounts have been updated: ", accounts)
            print_menu()
        
    #if option 2 = search
    elif choice == 2:
        print("\n\t\t|  Search |\n")
        try:
            fullname = input("Please Enter the Fullname you would like to search or type ALL to see all: ")
        except ValueError:
            print("\nInvalid input")
        else:
            if fullname == "ALL":
                for key, value in accounts.items():
                    print ("Name: " + key)
                    print ("info: " + str(value) + "\n")
            elif fullname in accounts:
                print ("Name: " + fullname)
                print ("info: " + str(accounts[fullname]))
            else:
                print("I'm Sorry, invalid input!!!")
            print_menu()

            
    #if option 3 = exit
    elif choice ==3:
        print("\n\t\t|  Exit |\n")
        try:
            decision = int(input("Would you like to end this program? please Enter 1 if no and 2 if yes: "))
        except ValueError:
            print("\nInvalid input")
        else:
            if decision == 1:
                print_menu()
            else:
                print("""
            ===================================
            |                                 |
            |           Thank You             |
            |    For Using The Program!!!     |
            |                                 |
            ===================================  
            """)
                break  