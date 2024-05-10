import Inventory

def updateExistingProduct(id):

    Inventory.printSpecificItem(id)                                                                       #oru item ku mattum data print pannum
    
    print("\n1.Edit Weight")
    print("2.Add unit of products\n")

    resp = int(input("What do you want to do(1/2)? "))
    print()

    if resp == 1:
        newWeight = input("Enter new Weight in grams: ") + "g"
        Inventory.products[id-1][2] = newWeight                                                           #product list newWeight assign pannurom
        Inventory.printSpecificItem(id)
    elif resp == 2:
        addedCount = int(input("Enter number of units to be added: "))
        Inventory.products[id-1][3] += addedCount                                                         #theriyumla
        Inventory.printSpecificItem(id)
    else:
        print("Invalid input")   