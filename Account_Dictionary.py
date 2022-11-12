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
        "Gender" : "Male"
    },
    "Enola Homes" : {
        "Age": 16,
        "Status" : "Single",
        "Gender" : "Female"
    },
    "Marian Rivera" : {
        "Age": 30,
        "Status" : "Married",
        "Gender" : "Female"
    },
    "Naruto Uzumaki " : {
        "Age": 47,
        "Status" : "widow",
        "Gender" : "Male"
    }
}

while True:
    #ask the user
    choice = int(input("Enter a number that you would like to do: "))
    #if option 1 = add item
    if choice == 1:
        print("\n\t\t|  Add an item |\n")
        name = input("Enter the fullname (first name, surname): ")
        age = int(input("Enter his/her age: "))
        status = input("Enter the status of the person: ")
        gender = input("Enter the gender: ")
        accounts[name] = {
            "Age": age,
            "Status" : status,
            "Gender" : gender
        }
        print("Succesfully added!!!\n")
        print("this is the accounts have been updated: ", accounts)
        print_menu()
        
    #if option 2 = search
    elif choice == 2:
        print("\n\t\t|  Search |\n")
        fullname = input("Please Enter the Fullname you would like to search or type ALL to see all: ")
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
        decision = int(input("Would you like to end this program? please Enter 1 if no and 2 if yes: "))
        if decision == 1:
            print_menu()
        else:
            break




        print("""
        ===================================
        |                                 |
        |           Thank You             |
        |    For Using The Program!!!     |
        |                                 |
        ===================================  
        """)