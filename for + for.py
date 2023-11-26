## 2개 정수를 입력받아(정수 에러체크 생략)그 사이에 있는 소수들과 합을 출력

## 변수 선언
num1, num2 = 0,0
hap=0
sosuYN= True

#메인 코드

num1 = int(input("시작숫자 입력(2이상) : "))
num2 = int(input("끝숫자 입력 : "))

#소수인지 점검하여 소수이면 출력
print("소수 :", end=" ") #end=" "은 줄바꿈하지 말고 옆에 빈칸만 1개 출력

for  num in range(num1, num2+1) : # num1 ~ num2 반복
    sosuYN = True # num이 소수라고 가정하고 시작
    
    for i in range(2, num) : # i가 2~ num-1에 있는 값들을 가지면서 나눠지는지 체크
        if num % i == 0 :
            sosuYN = False
            break
        
    if sosuYN == True :
        print(num, end=" ") #소수 출력
        hap += num          # 현재 소수인 num을 hap변수에 더함
              
print("\n%d부터 %d까지 소수의 합은 %d 입니다. " %(num1,num2, hap))
