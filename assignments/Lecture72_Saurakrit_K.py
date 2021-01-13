menuList = []


def showBill(bill):
    print("Your Bill".center(31, '-'))
    for i in range(len(bill)):
        print('%s %s THB' % (bill[i][0], bill[i][1]))


def sumPrice(price):
    sum = 0
    for i in range(len(price)):
        sum += int(price[i][1])
    return sum


while True:
    menuName = input('Enter Your Menu: ')
    if (menuName.lower() == 'exit'):
        break
    else:
        menuPrice = input('Price: ')
        menuList.append([menuName, menuPrice])
showBill(menuList)
print('ราคารวม = %d THB'%(sumPrice(menuList)))
