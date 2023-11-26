def telephone_directory(dic, key) : #이름과 전화번호를 받아줄 함수 및 변수(dic, key) 생성
        a = dic[key] #딕셔너리 추가
        return True #값을 반환해줌

contacts = {} #이름과 전화번호를 저장할 리스트 생성

while True :
    name = input("(입력모드)이름을 입력하시오 : ") #이름을 받음
    if not name : #이름을 입력하지 않으면 멈춤
        break
   
    tel = input("전화번호를 입력하시오 : ") # 전화번호를 받음
    contacts[name] = tel #앞서 받음 키(이름)의 해당하는 값(전화번호)을 저장

while True :
    name = input("(검색모드)이름을 입력하시오 : ") #저장된 이름중 하나를 입력해서 검색
    if not name :
        break
    if telephone_directory(contacts, name) : #전화번호부에 저장된 이름과 전화번호를 호출
        print(name,"의 전화번호는",contacts[name],"입니다.") #사용자가 원하는 이름과 전화번호 호출
    else :
        print("저장되어있는 이름을 입력하시오. \n") #저장되지 않은 이름을 입력시 출력
