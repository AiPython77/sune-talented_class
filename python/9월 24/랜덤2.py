import random
computer_dice = random.randint(1,7)
user_dice = random.randint(1,7)

if computer_dice > user_dice :
    print('컴퓨터 :', computer_dice ,'사용자 :', user_dice,' 컴퓨터 승리')
elif computer_dice< user_dice :
    print('컴퓨터 :', computer_dice, '사용자 :', user_dice, '사용자 승리')
else :
    print('컴퓨터 :', computer_dice, '사용자 :', user_dice, '비김')