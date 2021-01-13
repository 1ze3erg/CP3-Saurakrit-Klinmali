import random


def dice():
    number = random.randint(1, 6)
    print("Dice show: ", number)
    return number


def ht():
    number = random.randint(0, 1)
    if number == 0:
        print("Tail")
        return 0
    else:
        print("Head")
        return 1


while True:
    select = input("Please select 1 for Head/Tail or 2 for Dice or Another for Exit: ")
    if select != '1' and select != '2':
        print("Good bye")
        break
    else:
        if select == '1':
            start = int(input("Head(1) or Tail(0): "))
            assert 1 >= start >= 0, "error pls type 0 or 1"
            bet = float(input("How much that you want to bet(1/10): "))
            if start != ht():
                print("You lose your ", bet)
            else:
                bet = bet * 10
                print("Congrats~ You get ", bet)
        else:
            lucky = int(input("Select your lucky number(1-6 only): "))
            assert 6 >= lucky >= 1, "error pls type only 1 to 6"
            bet2 = float(input("How much money you want to bet: "))
            if lucky != dice():
                print("Too bad")
                print("You lose your ", bet2)
            else:
                bet2 = bet2 * 10
                print("Congrats~ You get ", bet2)
