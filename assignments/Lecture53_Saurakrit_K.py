def vatCalculator(price):
    netPrice = price+(price*7/100)
    return netPrice
price = int(input("ราคาสินค้า: "))
print("ราคาสินค้ารวม vat =",vatCalculator(price))
