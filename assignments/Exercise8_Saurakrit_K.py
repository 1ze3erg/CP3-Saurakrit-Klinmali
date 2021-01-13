usernameInput = input("Username: ")
passwordInput = input("Password: ")
if usernameInput == "admin" and passwordInput == "1234":
    print("-----Welcome to izeShop-----")
    print("Product List")
    print("1.Mouse = 100 THB")
    print("2.Keyboard = 300 THB")
    print("3.Headset = 500 THB")
    print("4.MousePad = 50 THB")
    print("5.Bungee = 30 THB")
    print("----------------------------")
    selectedProduct = int(input("เลือกสินค้า(พิมพ์เลขสินค้า 1-5) >> "))
    if selectedProduct == 1:
        price = 100
        quantity = int(input("ใส่จำนวน Mouse ที่ต้องการ: "))
        totalPrice = price*quantity
        print("ราคารวม Mouse ", quantity, "x 100 THB = ", totalPrice, "THB")
    elif selectedProduct == 2:
        price = 300
        quantity = int(input("ใส่จำนวน Keyboard ที่ต้องการ: "))
        totalPrice = price*quantity
        print("ราคารวม Keyboard ", quantity, "x 300 THB = ", totalPrice, "THB")
    elif selectedProduct == 3:
        price = 500
        quantity = int(input("ใส่จำนวน Headset ที่ต้องการ: "))
        totalPrice = price*quantity
        print("ราคารวม Headset ", quantity, "x 500 THB = ", totalPrice, "THB")
    elif selectedProduct == 4:
        price = 50
        quantity = int(input("ใส่จำนวน MousePad ที่ต้องการ: "))
        totalPrice = price*quantity
        print("ราคารวม MousePad ", quantity, "x 50 THB = ", totalPrice, "THB")
    elif selectedProduct == 5:
        price = 30
        quantity = int(input("ใส่จำนวน Bungee ที่ต้องการ: "))
        totalPrice = price*quantity
        print("ราคารวม Bungee ", quantity, "x 30 THB = ", totalPrice, "THB")
    else:
        print("Error")
else:
    print("Wrong Username or Password or Both >> Try Again")
