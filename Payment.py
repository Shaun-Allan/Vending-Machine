import Inventory

def payment(selected_products):
    totalCost = 0
    for i in selected_products:
        totalCost += i[4] * i[3]                                            #count * cost
    print("\n----------------------------------------------------")
    print("Total Cost: Rs.", totalCost)
    print("----------------------------------------------------\n")
    amountPaid = int(input("Enter Amount: "))
    if amountPaid > totalCost:                                              #balance kudukurom
        print("Payment Successfull")
        balanceAmount = amountPaid - totalCost
        print("Rs.", balanceAmount, "returned")
        dispense(selected_products)
    elif amountPaid == totalCost:                                           #amount correctah irundha
        print("Payment Successfull")
        dispense(selected_products)
    else:                                                   
        getRequiredAmount(amountPaid, totalCost, selected_products)


def dispense(selected_products):
    print()
    for item in selected_products:
        print(item[3], "units of", item[1], "is dispensed")                       # * units of *product is dispensed
        Inventory.updateStock(item) 



def getRequiredAmount(amount, total, selected_products):
    if amount > total:
        balanceAmount = amount - total
        print("Payment Successfull")
        print("Rs.", balanceAmount, "returned")
        dispense(selected_products)
        return
    elif amount == total:
        print("Payment Suuccessfull")
        dispense(selected_products)
        return
    requiredAmount = total - amount
    print("Rs.", requiredAmount, "more required")
    amount += int(input("Enter remaining amount: "))
    getRequiredAmount(amount, total, selected_products)