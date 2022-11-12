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
    "harry Potter" : {
        "Age": 19,
        "Status" : "Single",
        "Gender" : "Male"
    },
    "enola Homes" : {
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
print(accounts)
    
#if option 2 = search
#if option 3 = exit