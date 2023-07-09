import datetime
import Functions


print()
print("********************************************************")
print()
print("             Welcome to Costume Rental Application")
print()
print("********************************************************")

'''
Costume rental function takes input from user and displays message for user to rent return
and exit application.
Uses if elif and else loop for displaying of message
'''
def CostumeRental():
    LoopContinue = True
    while LoopContinue == True:
        print()
        print()
        print("                 Select your desirable option ")
        print("============================================")
        print()
        print("1. || If you would like to rent a costume available on the store Press", "1.")
        print("2. || If you would like to return the costume you have rented Press","2.")
        print("3. || If you would like to exit the program Press","3.")
        print()
        print()

        option = input("Please press a number to choose an option: ")
        print()
        if(option == "1"):
            print()
            print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
            print("\t You may now rent a costume")
            print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
            print()
            print()
            
            Functions.CostumeRent()
            
        elif(option == "2"):
             print()
             print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
             print("\tYou may now return the costume")
             print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
             print()
             print()
             
             Functions.ReturnCostume()
             
        elif(option == "3"):
            print()
            print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
            print("\tThank you for using our application")
            print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
            print()
            print()
        
            LoopContinue = False
        else:
            print("Invalid input. Please choose a correct option")
            





#Displays message for user to rent or return costume and exit the application 
CostumeRental()
