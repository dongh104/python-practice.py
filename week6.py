while True:
    a = int(input('정수를입력 : '))
    q = a // 1000
    w = (a % 1000) // 100
    e = ((a % 1000) % 100) // 10
    r = (((a % 1000) % 100) % 10) // 1
    Sum = q + w + e + r
    print("자리수의 합 :", Sum)
    if(a==0):
        break
    
    
    
