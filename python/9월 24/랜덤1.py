import random
computer_num = int(random.random() * 10)

while (True):
    #computer_num = int(random.random() * 11)
    user_num = int(input("숫자 입력: "))

    if computer_num == user_num:
        print("정답. 숫자는 ", user_num)
        break