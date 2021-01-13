def login():
    usernameInput = input("Username :")
    passwordInput = input("Password :")
    if usernameInput == "admin" and passwordInput == "1234":
        showMenu()
    else:
        print("Wrong Username or Password or Both >> Try Again")
        return login()
def showMenu():
    print("----- izeShop -----")
    print("1. Vat Calculator")
    print("2. Price Calculator")
    menuSelect()
def menuSelect():
    userSelected = int(input(">>"))
    if userSelected == 1:
        price = int(input("Price (THB): "))
        print(vatCalculator(price))
    elif userSelected == 2:
        priceCalculator()
    else:
        print("Error!!! Pls select 1 or 2")
        return menuSelect()
def vatCalculator(price):
    vat = 7
    result = price + (price * vat / 100)
    return result
def priceCalculator():
    price1 = int(input("First Product Price : "))
    price2 = int(input("Second Product Price : "))
    return print("Total Price = ",vatCalculator(price1+price2))
login()