pyramidHeight = int(input("ใส่จำนวนชั้นพีระมิด : "))
numberStar = 1
for x in range(pyramidHeight-1,-1,-1):
    print(" "*x+"*"*numberStar)
    numberStar += 2
