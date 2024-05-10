import Customer

products = [[1, "Bru", "50g", 10, 5],
            [2, "Snickers", "40g", 20, 15],
            [3, "Water Bottle", "100g", 20, 20],
            [4, "Coca Cola", "100g", 30, 20],
            [5, "Gems", "75g", 50, 10]]


def updateStock(product):                                                        #product na oru particular item oda list, motha product list illa
    id = product[0]
    products[id-1][3] -= product[3]                                   #motha product list la irundhu count decrement pannurom
    if products[id-1][3] == 0:
        print("\n", products[id-1][1], "is empty")
        products.remove(products[id-1])
        updateId(id)
    Customer.selectedProducts = []


def updateId(id):                                                                              #ignore paniru innum pannala
    for i in range(1, len(products)+1):
        for item in products:
            if products.index(item)+1 == i:
                item[0] = i


def printSpecificItem(id):
    print("\n----------------------------------------------------")
    for i in products:
        if i[0] == id:
            print(*i, sep="\t")
    print("----------------------------------------------------\n")


def viewItems():                                                                               #idhu konjam modify pannanum
    print("\n================VENDING MACHINE=====================\n")
    print("Product Id\tProduct Name\tWeight\tStock Available\tCost")
    for i in products:
        for j in i:
            print(j, end="\t")
        print()
    print("\n====================================================\n")