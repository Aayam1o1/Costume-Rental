import datetime

'''
defining function named GetFileContent and extracting values from the .txt file named Costume
and store value in the variable data
'''
def GetFileContent():
    files = open("Costume.txt","r")
    data = files.readlines()
    files.close()
    return data


'''
Creating function with parameter FileContent to get values of function FileContent
- [i+1] starts the index from 1 
 - "\n" is replaced with "" as we got values from a txt file \n represnts "enter" which is replaced wirth
      empty value.
'''
def Dictionary(FileContent):
  DataDictionary = {}
  for i in range(len(FileContent)):
      DataDictionary[i + 1] = FileContent[i].replace("\n","").split(",")
  return DataDictionary


'''
- CostumeDetails function with parameter CostumeDatabase to get value of function CostumeDatabase
- for loop for printing items stored in Costumedatabase doctionary
-  keys and values are inorder as in dictionary key comes first and value at second
'''
def CostumeDetails(CostumeDatabase):
    print("============================================")
    print("S/No","\t","Costume Name","\t","Brand Name","\t","Price","\t","Quantity")
    print("============================================")    

    for key, value, in CostumeDatabase.items():
        print(key,"\t",value[0],"\t", value[1],"\t", value[2],"\t",value[3])
        print()


        

'''
- Function GetValidSno with parameter CostumeDatabase 
- this function is created to help user choose costume with help of serial number aquired through
  function "CostumeDatabase" to rent the costume
  
'''

def GetValidSno(CostumeDatabase):
    ValidSno = False
    while ValidSno ==False:
        try:
            Sno = int(input("Please enter a serial number: "))
            print()
            if Sno > 0 and Sno <= len(CostumeDatabase):
                quantity = int(CostumeDatabase[Sno][3])
                if quantity == 0:
                    print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
                    print()
                    print("             Sorry, Costume is out of stock.Please choose another costume")
                    print()
                    print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
                    CostumeDetails(CostumeDatabase)
                    
                
                else:
                    ValidSno = True
                    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
                    print("\tCostume is available in the store.")
                    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
                    print()
                    return Sno

            else:
                print("Invalid Input. Please enter correct Serial Number")
                print()
                CostumeDetails(CostumeDatabase)
                print()
        except:
            print()
            print("-----------------------------------------------------------------------------")
            print("\t Invalid Input. Please enter Valid Serial Number")
            print("-----------------------------------------------------------------------------")
            

'''
- GetValidQuantity function with two parameter Costumedatabase and Sno
- The parametrer is to extract values from the respecrtive function.
- This function helps user to check quantity and enter valid data accordingly
'''
def GetValidQuantity(CostumeDatabase,Sno):
    ValidQuantity = False
    while ValidQuantity == False:
        try:
            Quantity = int(input("Please enter amount of costume you want to rent: "))
            print()
            
            if  Quantity > 0 and Quantity <= int(CostumeDatabase [Sno][3]):
                
                ValidQuantity = True
                
                CostumeDatabase[Sno][3] = str(int(CostumeDatabase [Sno] [3]) - Quantity)
                print()
                print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
                print("\tThe costume has been rented. Thank you!!")
                print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
                print()
                print()
                CostumeDetails(CostumeDatabase)
                return Quantity
            
            elif Quantity > int(CostumeDatabase[Sno] [3]):
                print("Quantity provided is greater  than we have in stock")

            else:
                print("Please provide valid input")
                print()
            
        
        except:
            print("------------------------------------------------------------------------")
            print("\t Invalid Input. Please enter valid Quantity")
            print("------------------------------------------------------------------------")





'''
- This function name is UpdateTextField with parameter CostumeDatabase
- This function updates the value which is changed when updating the quantity value when rented
'''
def UpdateTextField(CostumeDatabase):
    file = open("Costume.txt","w")
    for value in CostumeDatabase.values():
        WriteData = value[0] + "," + value[1] + "," + value[2] + "," + value[3] + "\n"
        file.write(WriteData)
    file.close()




# function to get date 
def GetDate():
    Year = str(datetime.datetime.now().year)
    Month = str(datetime.datetime.now().month)
    Day = str(datetime.datetime.now().day)
    
    Date = (Year+"-"+Month+"-"+Day)
    
    return Date

# function to get time
def GetTime():
    Hour = str(datetime.datetime.now().hour)
    Minute = str(datetime.datetime.now().minute)
    Second = str(datetime.datetime.now().second)

    Time = (Hour+ "hr" +"-"+Minute+ "min" +"-"+Second + "sec" )
    return Time


'''
- This function has parameter CostumeList and CostumeDatabase InvoiceType and Renting days
- this function prints the bill after costumer has sucessfully rented all the costume he wants
'''
def Bill(CostumeList, CostumeDatabase, InvoiceType, RentingDays):
    print()
     
    Number = True
    while Number == True:
        try:
            CustomerName = input("Please enter your name: ")
            PhoneNumber = int(input("Please enter your phone  number: "))

            if CustomerName == "" or PhoneNumber == "":
                print()
                print()
                print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
                print("\t Please enter your name and number")
                print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")

            else:
                print()
                break
        except:
            print()
            print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
            print("\t Invalid input. Please enter your name and number")
            print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
            print()
        

    TotalCost = 0
    TotalQuantity = 0
    TotalFine = 0
    
    print()
    print("=================================================")
    print("\t\t\t Bill")
    print("=================================================")
    print("Name: ", CustomerName)
    print("Phone Number: ", str(PhoneNumber))
    
    print(f"Date {InvoiceType}: ", GetDate())
    print(f"Time {InvoiceType}:", GetTime())
    
    print()
    print("=================================================")
    print("SN.","\t", "Costume Name", "\t","Brand", "\t\t", "Price", "\t", "Quantity")
    print("=================================================")


    for i in range(len(CostumeList)):
        Sno = int(CostumeList[i][0])
        Quantity = CostumeList[i][1]
    
        CostumeName = CostumeDatabase[Sno][0]
        CostumeBrand = CostumeDatabase[Sno][1]
        Price = float(CostumeDatabase[Sno][2])
        TotalQuantity += Quantity
        TotalCost += (Quantity * Price)

        print((i +1), "\t", CostumeName,"\t", CostumeBrand,"\t",Price,"\t",Quantity)

    print()
    print("\t\t\t\t\t\t Total Quantity: " + str(TotalQuantity))

    if RentingDays > 5:
        TotalFine += ((RentingDays - 5) * 5)
    
    if InvoiceType.lower() == "returned":
        print("\t\t\t\t\t\t Total Fine: "+ str(float(TotalFine)))
            
    else:
        print("\t\t\t\t\t\t Total Cost: " + str(TotalCost))


    print("=================================================")

    BillInText(CustomerName,PhoneNumber,TotalQuantity, TotalCost,TotalFine,CostumeList,InvoiceType, RentingDays)

'''
Thios function has 6 parameter CustomerName,PhoneNumber, TotalQuantity, TotalCost, InvoiceType and RentingDays
This function basically coverts the bill into txt file with costumer name number , Quantity , Cost and all
bill details
'''
def BillInText(CustomerName,PhoneNumber, TotalQuantity, TotalCost,TotalFine, CostumeList,InvoiceType, RentingDays):
 
    file  = open(CustomerName +" "+ "Date-" + str(GetDate()) +"   " +"Time-" +  str(GetTime()) + ".txt", "w")
    file.write("Customer Name: " + CustomerName + "\n")
    file.write("Customer Phone Number: " + str(PhoneNumber) + "\n")
    
    file.write(f"Date {InvoiceType}: "+ GetDate() + "\n")
    file.write(f"Time {InvoiceType}:"+ GetTime()+ "\n")
    file.write("\n")
    file.write("\n")

    file.write("====================================================="+"\n")
    file.write("SN."+"\t\t"+ "Costume Name"+ "\t\t"+"Costume Brand"+"\t\t"+ "Price"+ "\t\t"+  "Quantity" +"\n")
    file.write("====================================================="+"\n")

    for i in range(len(CostumeList)):
        Sno = int(CostumeList[i][0])
        Quantity = CostumeList[i][1]
        
        
        CostumeName = CostumeDatabase[Sno][0]
        CostumeBrand = CostumeDatabase[Sno][1]
        Price = float(CostumeDatabase[Sno][2])

        file.write(str((i+1)) + ")" + "\t\t" + CostumeName + "\t\t\t" + CostumeBrand + "\t\t\t" + str(Price) +"\t\t\t"+ str(Quantity) +"\n")
        file.write("----------------------------------------------------------------------------------------------"+ "\n")

    file.write("\n")
    
    
    if InvoiceType.lower() == "returned":
        file.write("Total Fine: "+ str(float(TotalFine)) + "\n")
            
    else:
        file.write("Total Cost: " + str(TotalCost) + "\n")
    file.write("Total Quantity:" +str(TotalQuantity))

    file.close()

'''
The function has parameter CostumeDatabase
It checks the total amount of costumes we have in stock
'''
def QuantityCalculation(CostumeDatabase):
    Quantity = 0

    for Sno in range(len(CostumeDatabase)):
        Sno = Sno + 1
        Quantity += int(CostumeDatabase[Sno][3])
  
    return Quantity
                    

def DeleteDoubleCostume(CostumeList, Sno,Quantity):
    
    Combine = False
        
    for RentCostume in CostumeList:
        if RentCostume[0] == Sno:
           RentCostume[1] += Quantity
           Combine = True
                        
    if Combine == False:
        CostumeList.append([Sno, Quantity])

    return CostumeList
 
'''
This function is the renting procedure of the application after calling this function aoll tasks are
carried out and executed.
'''
def CostumeRent():
    ContinueLoop =True
    RentedCostumeList = []

    while ContinueLoop == True:
        
        TotalCostumesQuantity = QuantityCalculation(CostumeDatabase)
        InvoiceType = "Rented"
        RentingDays = 0

        if TotalCostumesQuantity == 0:
            
            if len(RentedCostumeList) == 0:
                print("----------------------------------------")
                print("All costumes are out of the stock!!!!!")
                print("----------------------------------------")
                
            else:
                print("----------------------------------------")
                print("All costumes are out of the stock!!!!!")
                print("----------------------------------------")
                
                
                Bill(RentedCostumeList, CostumeDatabase, InvoiceType, 0)
                RentedCostumeList.clear()
                
            ContinueLoop = False
    
        else:
            CostumeDetails(CostumeDatabase)
            
            Sno = GetValidSno(CostumeDatabase)
            
            Quantity = GetValidQuantity(CostumeDatabase, Sno)

            #Deleting the costume if it is double
            RentedCostumeList = DeleteDoubleCostume(RentedCostumeList, Sno,Quantity)
                
            UpdateTextField(CostumeDatabase)

            AskingCustomerLoop = True
            
            while AskingCustomerLoop == True:
                CustomerPreference= input("Would you like to rent another costume?? (Please answer in yes or no): ")
                print()
                
                if CustomerPreference.lower() == "yes":
                    AskingCustomerLoop = False
                    
                elif CustomerPreference.lower() == "no":
                    print("Thank you for renting the costume.")
                    Bill(RentedCostumeList, CostumeDatabase, InvoiceType, RentingDays)
                    AskingCustomerLoop = False
                    ContinueLoop = False
                    
                else:
                    print("Inavlid Input.")

'''
- Function GetValidSnoReturn with parameter CostumeDatabase 
- this function is created to help user choose costume with help of serial number aquired through
  function "CostumeDatabase" to return the costume
'''
def GetValidSnoReturn(CostumeDatabase):
   
    ValidSno = False

    while ValidSno == False:
        print()
        try:
            Sno = int(input("Please enter the serial number: "))

            if Sno > 0 and Sno <= len(CostumeDatabase):
                
                ValidSno = True
                print()
                return Sno

            else:
                print()
                print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
                print("\t Invalid input!!!, Please enter correct Serial Number")
                print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")

        except:
            print()
            print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
            print("\t Invalid input!!!, Please enter correct Serial Number")
            print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")


'''
- GetValidQuantity function with two parameter Costumedatabase and Sno
- The parametrer is to extract values from the respecrtive function.
- This function helps user to return the amount of costume to return
'''
def GetValidQuantityReturn(CostumeDatabase,Sno):
    
    LoopContinue = True

    while LoopContinue:
        try:
            
            TotalQuantity = int(input("Please enter the number of costumes you want to return: "))

            if TotalQuantity > 0:
                CostumeDatabase[Sno][3] = str(int(CostumeDatabase[Sno][3])+ TotalQuantity)
                    
                return TotalQuantity


            else:
                print()
                print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
                print("\t Invalid input!!!, Please enter the valid input!!")
                print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
                print()

        except:
            print()
            print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
            print("\t Invalid input!!!, Please enter the valid input!!")
            print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
            print()


'''
This function is to ask user how many days he/she had rented the costume for
'''
def GetRentingDays():

    LoopContinue = True

    while LoopContinue:
        try:
            TotalRentingDays = int(input("Please enter the number of days costume was rented: "))
            if TotalRentingDays > 0:
                return TotalRentingDays

            else:
                print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
                print("      Invalid input!!!, Total Renting Days cannnot be 0. Please enter the value again!!")
                print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
                
        except:
            print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
            print("\t Invalid input!!!, Please enter the valid input!!")
            print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
            print()

'''
This function is the returning procedure of the application after calling this function all tasks are
carried out and executed.
'''
def ReturnCostume():

    ReturnedCostumeList = []
    LoopContinue = True
    
    while LoopContinue:
        CostumeDetails(CostumeDatabase)

        Sno = GetValidSnoReturn(CostumeDatabase)

        TotalQuantity = GetValidQuantityReturn(CostumeDatabase, Sno)

        ReturnedCostumeList = DeleteDoubleCostume(ReturnedCostumeList, Sno, TotalQuantity)

        
        AskMultipleCostumeReturn = True
        
        while AskMultipleCostumeReturn:
                InvoiceType = "Returned"
                print()
                CustomerAnswer = input("Would you like to return another costume? (Please answer in yes or no): ")
                print()
                CustomerAnswer = CustomerAnswer.lower()
                
                if CustomerAnswer == "no":
                    RentingDays = GetRentingDays()
                    Bill(ReturnedCostumeList, CostumeDatabase, InvoiceType, RentingDays)
                    ReturnedCostumeList.clear()

                    AskMultipleCostumeReturn = False
                    LoopContinue = False
                    
                
                elif CustomerAnswer == "yes":
                    AskMultipleCostumeReturn = False

                else:
                    print()
                    print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
                    print("\t Invalid input!!!, Please enter the valid input")
                    print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
            
        UpdateTextField(CostumeDatabase)

            
    
#Reading file 
FileContent = GetFileContent()

#storing data of dictionary
CostumeDatabase = Dictionary(FileContent)



