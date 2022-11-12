print("*********  PROGRAMMED BY  ********")
print("***** JIMWELL L. MANGULABNAN *****")
print("********** BSCOE 2-2 *************")
print()

# Display a menu 
print()
print("#######################")
print("#        MENU         #")
print("#---------------------#")
print("#   1 >> Add an item  #")	
print("#   2 >> Search       #")
print("#   3 >> Exit         #")	 
print("#######################")
print()
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


#ask the user
choice = int(input("Enter a number that you would like to do: "))
#if option 1 = add item
if choice == 1:
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
    
#if option 2 = search
if choice == 2:
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

        
#if option 3 = exit