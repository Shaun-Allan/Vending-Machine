import Inventory
import AddProduct, UpdateProduct, Remove

def showAdminOptions():
    print("\n---------------------Admin Mode----------------------\n")
    print("1.Add new product")
    print("2.Update existing product")
    print("3.Remove existing product\n")
    print("Enter -1 to exit Admin mode\n")
    
    resp = int(input("Do you want to add/update/remove(1/2/3): "))                              #idhellam theriyumla
    print()
    if resp == 1:
        AddProduct.addNewProduct()
    elif resp == 2:
        id = int(input("Enter Product Id to be updated: "))                                     #endha product id ku update pannanum nu input vangurom
        if id in range(len(Inventory.products)):
            UpdateProduct.updateExistingProduct(id)
        else:
            print("Product Id not available")
    elif resp == 3:
        id = int(input("Enter product to be removed: "))
        if id in range(len(Inventory.products)):
            Remove.removeExistingProduct(id)
        else:
            print("Product Id not available")
    elif resp == -1:
        return -1                                                                               
    else:
        print("Invalid Input")

    Inventory.viewItems()