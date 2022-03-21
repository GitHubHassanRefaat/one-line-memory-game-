
import random
import time
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
char = ["a", "b", "c", "d", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "e", "f", "g", "h", "i", "j"]
negma ="*"

random.shuffle(char)
num1 = num.copy()
print("welcome: ", num)

score1 = 0
score2 = 0


def player1():
    global score1
    global num1

    first_num = int(input("enter first num"))
    second_num = int(input("enter second num"))
    while num1[first_num - 1] == "*" or num1[second_num - 1] == "*":
        print("number is unavailable")
        first_num = int(input("enter second num"))
        second_num = int(input("enter second num"))

    num1[first_num - 1] = char[first_num - 1]
    num1[second_num - 1] = char[second_num - 1]
    if num1[first_num - 1] == num1[second_num - 1]:

        print("Player#1 – score ", score1, ": ", first_num, ",", second_num)
        score1 += 1
        print("welcome : ", num1)
        num1[first_num - 1] = '*'
        num1[second_num - 1] = '*'
        return num1

    else:

        print(num1)
        time.sleep(3)
        num1[first_num - 1] = num[first_num - 1]
        num1[second_num - 1] = num[second_num - 1]
        print("Player#1 – score ", score1, ": ", first_num, ",", second_num)
        print("welcom: ", num1)

    print("screen is cleared")


def player2():
    global score2

    first_num2 = int(input("enter first num"))
    second_num2 = int(input("enter second num"))
    # num2 = num.copy()
    while num1[first_num2 - 1] == "*" or num1[second_num2 - 1] == "*":
        print("number is unavailable")
        first_num2 = int(input("enter second num"))
        second_num2 = int(input("enter second num"))

    num1[first_num2 - 1] = char[first_num2 - 1]
    num1[second_num2 - 1] = char[second_num2 - 1]
    if num1[first_num2 - 1] == num1[second_num2 - 1]:

        print("Player#2 – score ", score2, ": ", first_num2, ",", second_num2)
        score2 += 1
        print("welcome : ", num1)
        num1[first_num2 - 1] = '*'
        num1[second_num2 - 1] = '*'
        return num1
    else:
        print(num1)
        time.sleep(3)
        num1[first_num2 - 1] = num[first_num2 - 1]
        num1[second_num2 - 1] = num[second_num2 - 1]
        print("Player#2 – score ", score2, ": ", first_num2, ",", second_num2)
        print("welcome: ", num1)
    print("screen is cleared !")
print(char)
while num1 != negma:
    counter = 0
    try:


        for i in range(20):
          if num1[i]=="*":
              counter +=1


        if( counter==20):
            if(score1 >score2) :
                print("player1 is winner ")
                break
            elif (score1 <score2):
                print("player2 is winner")
                break
            else:
                print("drawwing")
                break
        else:


            player1()
            player2()
    except IndexError:
        print("enter a valid number")

    except ValueError:
     print("enter a valid number")
