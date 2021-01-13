menuList = []
priceList = []
def showBill(bill):
    print("Your Bill".center(31,'-'))
    for i in range(len(bill)):
        print('%s %s THB'%(menuList[i],priceList[i]))
def sumPrice(price):
    sum = 0
    for i in price:
        sum += int(i)
    return sum
while True:
    menuName = input('Enter Your Menu: ')
    if(menuName.lower() == 'exit'):
        break
    else:
        menuPrice = input('Price: ')
        menuList.append(menuName)
        priceList.append(menuPrice)
showBill(menuList)
print('ราคารวม = %d THB'%(sumPrice(priceList)))

