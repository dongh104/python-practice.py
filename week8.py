import random

def addProblem(x,y):
    add = x+y
    sentence = "정수" +str(x) + "+" + str(y) +"의 값은?"
    return add,int(input(sentence))

def subProblem(x,y):
    sub = x-y
    sentence = "정수" +str(x) + "-" + str(y) +"의 값은?"
    return sub,int(input(sentence))

def mulProblem(x,y):
    mul = x*y
    sentence = "정수" +str(x) + "*" + str(y) +"의 값은?"
    return mul,int(input(sentence))

def divProblem(x,y):
    div = x/y
    sentence = "정수" +str(x) + "/" + str(y) +"의 값은?"
    return div,int(input(sentence))




def get1Value():
    a = int(input("첫 번째 정수"))
    b = int(input("두 번째 정수"))
    add, answer = addProblem(a,b)
    if add == answer:
        return True
    else:
        return False
    
def get2Value():
    a = int(input("첫 번째 정수"))
    b = int(input("두 번째 정수"))
    sub, answer = subProblem(a,b)
    if sub == answer:
        return True
    else:
        return False

def get3Value():
    a = int(input("첫 번째 정수"))
    b = int(input("두 번째 정수"))
    mul, answer = mulProblem(a,b)
    if mul == answer:
        return True
    else:
        return False
    
def get4Value():
    a = int(input("첫 번째 정수"))
    b = int(input("두 번째 정수"))
    div, answer = divProblem(a,b)
    if div == answer:
        return True
    else:
        return False
    
   
    print("계산 맞추기 게임, 3번 맞추면 끝남\n")
count = 0

while True:
    symbol = random.choice(["+","-","*","/"])
    print("랜덤 연산기호는 : " + symbol)
    if symbol == '+':
        while True:
            if get1Value() == True:
                print("정답입니다\n")
                count+= 1
                break
            else:
                print("틀렸어요\n")
            
    if symbol == '-':
        while True:
            if get2Value() == True:
                print("정답입니다\n")
                count+= 1
                break
            else:
                print("틀렸어요\n")
    if symbol == '*':
        while True:
            if get3Value() == True:
                print("정답입니다\n")
                count+= 1
                break
            else:
                print("틀렸어요\n")
    if symbol == '/':
        while True:
            if get4Value() == True:
                print("정답입니다\n")
                count+= 1
                break
            else:
                print("틀렸어요\n")
    if count == 3:
        break
 
print("3번 맞춰서 프로그램 종료합니다")
