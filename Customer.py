import Inventory, Payment

selectedProducts = []                                                       #cart madhiri

def selectItems():                                                          #items select pannna
    print("Enter 0 to pay") 
    print("Enter -1 to reset")
    print("Enter -2 to enter as Admin")
    print("Enter -3 to exit Vending Machine")
    id = 1                                                                  #default ah id 1 nu assign panrom
    while id>0:                                                             #product list la ellame id>1 ah dhan irukum, so indha condition
        id = int(input("\nEnter Product Id: "))

        if id == 0:                                                         #exceptions ku kudukurom
            global selectedProducts
            Payment.payment(selectedProducts)                                       #id 0 ah podumodhu payment ku poirum
            break                                                           #so loop break pannanum
        elif id == -1:
            selectedProducts = []                                           #id -1 ah podumodhu cart reset pannanum
            break
        elif id == -2:
            return -2                                                        #Also first la irundhu start aaganum
        elif id == -3:
            return -3
        elif id < -3 and id > Inventory.products[-1][0]:                                                      #Invalid inputs ku
            print("Enter Valid Input")                                      
            break

        count = int(input("Enter no. of units: "))
        checkStock(id, count)                                               #Apdi endha exception um illana loop break aagama stock check pannum ovvoru id entrykum


def checkStock(id, count):
    prodName = Inventory.products[id-1][1]                                      #idhellam vending machine la irukura product list oda datas
    prodWeight = Inventory.products[id-1][2]
    prodCount = Inventory.products[id-1][3]
    prodCost = Inventory.products[id-1][4]
    if prodCount >= count:                                                  #stock required count oda adhigama irundha cart la data lam append aaganum
        selectedProducts.append([id, prodName, prodWeight, count, prodCost])
    else:
        print("Insufficent Stock") 