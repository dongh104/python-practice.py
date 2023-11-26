#5장8번 연습문제
import turtle
t = turtle.Turtle()

x1 = int(input("큰 원의 x좌표 x1: "))
y1 = int(input("큰 원의 y좌표 y1: "))
r1 = int(input("큰 원의 반지름: "))
x2 = int(input("작은 원의 x좌표 x2: "))
y2 = int(input("작은 원의 y표 y2: "))
r2 = int(input("작은 원의 반지름: "))

dis = ((x1-x2)**2 + (y1-y2)**2)**0.5 #두 원의 위치관계 공식

t.up()
t.goto(x1, y1-r1)
t.down()
t.circle(r1)

t.up()
t.goto(x2, y2-r2)
t.down()
t.circle(r2)

if (dis + r2 < r1):
   t.write("큰원안에 작은원 있음.")
elif (dis < r1 + r2):
   t.write("겹쳐있음.")
else:
   t.write("떨어져있음.")
