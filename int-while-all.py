#### 정수를 입력받아 자릿수 합 구하기, 0을 입력하면 프로그램 종료
# 사용자가 123을 입력했다고 가정하고 주석문에서 설명함

## 예1

while True :
    num = int(input("정수를 입력하세요 :"))

    if num != 0 :
        result = 0 #자릿수 합 구하기 시작
        while True :
            result += num %10 # 123%10 = 3, 12%10 = 2, 1%10=1
            num //= 10   #123/10 = 12.3 실수, 123//10 = 12, 12//10 = 1, 1//10== 0
                         #// 정수몫을 구하는 연산자
    
            if num == 0 :
                print("각 자릿수의 합: ", result)
                break
    else :
        print("종료되었습니다.")
        break


## 예2

while True : #무한루프
    num = int(input("정수를 입력하세요 :"))

    if num == 0 : # 종료조건
       break

    result = 0    #자리수 합구하기
    while True :
        result += num %10
        num //= 10
        if num == 0 :
            print("각 자릿수의 합: ", result)
            break

print("종료되었습니다.")


## 예3 : 입력 에러 체크, 입력값이 리스트라는 것에 착안

import sys


while True:
    value = input("입력값 : ") # 사용자가 123입력하면 문자열 '123'이 value에 저장

    # 입력받은 값이 숫자가 아니거나 실수형이면 
    if value.isdigit() == False or float(value) == True:
        print("정수를 입력해주세요!")

    # 입력받은 값이 0이면, 프로그램 종료
    elif int(value) == 0:
        print("프로그램을 종료합니다.")
        break;       

    # 입력받은 값의 각 자리수의 합을 계산
    else:
        sum = 0         # 숫자형 변수를 위해 초기값을 0으로 함
        
        for n in value: # value는 문자열 '123'있음. 문자열은 리스트=['1','2','3']로 처리함
            sum += int(n) #for n in ['1','2','3']

        print("출력값 : %s" %sum)


## 예4 : 정수 체크 에러 코딩 추가
        
while True:
    n= input('양수를 입력하세요(종료는 0)')

    #종료조건 확인
    if n == '0' :
        break

    #입력값이 정수인지 확인
    junsu=True
    for i in n: # n변수는 '123'가짐
        if i == '.' or not ('1'<= i <= '9') :
            junsu= False
            break  # 가장 근처에 있는 반복을 빠져나옴

    #입력값이 정수가 아니면 다시 입력받게 위로 감 	    
    if(junsu == False) :
        continue # 가장 근처에 있는 반복문 처음으로 감

    
   #  자릿수 합구하기
    sum = 0
    for i in n:
        sum += int(i)
    print("자릿수합:%d"%sum)
      
print("프로그램 종료")
