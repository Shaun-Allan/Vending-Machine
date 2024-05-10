import Inventory

def addNewProduct():
    id = len(Inventory.products) + 1                                                                      #last id + 1                                
    name = input("Enter Product Name: ")
    alreadyPresent = False

    for item in Inventory.products:
        if item[1] == name:
            alreadyPresent = True
    if alreadyPresent != True:
        weight = input("Enter Weight in grams: ") + "g"
        count = int(input("Enter number of units to be added: "))
        cost = int(input("Enter Cost of Product: "))
        Inventory.products.append([id, name, weight, count, cost])                                        #product list la append pannurom
    else:
        print("Item already available\n")