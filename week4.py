#5장5번 연습문제
import random
a = random.randint(1,100)
b = random.randint(1,100)

num = int(input(str(a) + "-" + str(b) + "="))


if (num == a-b):
   print("맞았습니다.")
else:
   print("틀렸습니다.")


#5장7번 연습문제
import random

number = random.randrange(100)
luck = int(input("복권번호를 입력하시오(0~99): "))
print("당첨번호는", number, "입니다.")

a1 = number//10
a2 = number%10
b1 = luck//10
b2 = luck%10

if (number == luck):
   print("상금은 100만원입니다.")
elif (a1 == b1 or a1 == b2 or a2 == b1 or a2 == b2):
   print("상금은 50만원입니다.")
else:
   print("상금은 없습니다.")
