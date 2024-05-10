import Customer, Admin, Inventory


while True:
    Inventory.viewItems()
    res = Customer.selectItems()
    if res == -2:
        while True:                                                         #admin mode la irundhu exit aagura varaikum admin mode laye irukanum, so loop la poturukom
            res = Admin.showAdminOptions()                                  #showAdminOptions oda return value ah res ku assign panrom, Admin mode ku enter aguroms
            if res == -1:                                               
                break                                                       #res -1 ah irundha Admin mode la irundhu exit aaganum(loop break aaganum)
        print("Admin Mode Exitted")
    elif res == -3:                                                         #-3 ah irundha exit aagum                                                    
        print("\n**************Exiting Vending Machine****************")
        break