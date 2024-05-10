import Inventory

def removeExistingProduct(id):
    Inventory.printSpecificItem(id)
    prodCount = Inventory.products[id-1][3]                                                               #products list la irundhu count edukurom
    removeCount = int(input("Enter no. of units to be removed: "))
    if removeCount < prodCount:
        Inventory.products[id-1][3] -= removeCount                                                        #count decrement pannurom
        Inventory.printSpecificItem(id)
    elif removeCount > prodCount:                                                               #stock ku mela removeCount enter pannunomna
        print("Warning: Units to be removed is greater than stock available")
    else:
        print("\n", Inventory.products[id-1][1], "is empty")
        Inventory.products.remove(Inventory.products[id-1])
        Inventory.updateId(id)