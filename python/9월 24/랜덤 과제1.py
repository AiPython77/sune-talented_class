import random

choice = ['가위', '바위', '보']
your_score = 0
computer_score = 0
while True:
    if computer_score == 5 or your_score == 5:
        break
    computer_choice = random.choice(choice)
    user_choice = input("가위 바위 보 중 하나를 입력하세요 : ")

    if computer_choice == user_choice:
        print("컴퓨터 :", computer_choice, "사용자 :", user_choice)
        print("비겼습니다.")
        print("컴퓨터 점수 :", computer_score, "사용자 점수 :", your_score, "\n")
    elif computer_choice == '가위' and user_choice == '바위':
        print("컴퓨터 :", computer_choice, "사용자 :", user_choice)
        print("이겼습니다.")
        your_score += 1
        print("컴퓨터 점수 :", computer_score, "사용자 점수 :", your_score, "\n")
    elif computer_choice == '바위' and user_choice == '보':
        print("컴퓨터 :", computer_choice, "사용자 :", user_choice)
        print("이겼습니다.")
        your_score += 1
        print("컴퓨터 점수 :", computer_score, "사용자 점수 :", your_score, "\n")
    elif computer_choice =='보' and user_choice == "가위":
        print("컴퓨터 :", computer_choice, "사용자 :", user_choice)
        print("이겼습니다.")
        your_score += 1
        print("컴퓨터 점수 :", computer_score, "사용자 점수 :", your_score, "\n")
    else:
        print("컴퓨터 :", computer_choice, "사용자 :", user_choice)
        print("졌습니다.")
        computer_score += 1
        print("컴퓨터 점수 :", computer_score, "사용자 점수 :", your_score, "\n")

print("게임이 끝났습니다.")