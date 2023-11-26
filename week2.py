#과제1
one=int(input("첫번째 값 입력:")) 
two=int(input("두번째 값 입력:")) 
three=int(input("세번째 값 입력:"))
Sum=(one+two+three)
avg=(one+two+three)/3 
print(one, two, three,"입력된값의 합은 ",Sum, "이고 평균값은 ",avg,"입니다.")

#과제2
import turtle
t=turtle.Turtle()
t.shape("turtle")
side = 50 
angle = 90  
for a in range(4): 
   for b in range(3): 
      t.forward(side) 
      t.left(angle) 
   t.forward(side)

#과제3
money = int(input("투입한 돈: "))
price = int(input("물건 값: "))

change = money-price
print("거스름돈: ", change)
coin500s = change // 500
change = change % 500
coin100s = change // 100
change = change % 100
coin50s = change // 50
change = change % 50
coin10s = change // 10

print("500원 동전의 개수: ", coin500s)
print("100원 동전의 개수: ", coin100s)
print("50원 동전의 개수: ", coin50s)
print("10원 동전의 개수: ", coin10s)
