systemMenu = {"ไก่ทอด": 35, "เป็ดทอด": 45, "ปลาทอด": 55, "ผักทอด": 20}
menuList = []

def showBill(bill):
    print("Your Bill".center(31, '-'))
    for i in range(len(bill)):
        print('%s %s THB'%(bill[i][0], bill[i][1]))


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
        menuList.append([menuName,systemMenu.setdefault(menuName,0)])

showBill(menuList)
print('ราคารวม = %d THB'%(sumPrice(menuList)))