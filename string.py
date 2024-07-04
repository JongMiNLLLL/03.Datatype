a = "hello world"
b = 'hello world'
print(a)
print(b)

name = '홍길동'
print("안녕하세요." + name + "님 반가워요")
money = 1000
print("안녕하세요.", money ,"원만 주세요 힝힝.")

#데이터 풀력시, % 기호 사용하는 방법
name = '이종민'
print("안녕하세요 저의 이름은 %s입니다." %name)

money = 10000
print("입력하신 금액은 %d원 입니다." %money)

# alt + shift = E
a = 7
b = 3
result = a + b
print(result)

#  문자열 길이 구하기
hello_world = "엄마가 말했다. '밥 먹었니?'"
print(len(hello_world))

#문자열 슬라이싱
뉴진스 = "하니, 민지, 다니엘 ,해린, 혜인"
print(len(뉴진스))
print(뉴진스[0:2])

# 문자열 치환
date = "2024.07.04"
print("바꾸기 전의 데이터 :",date)
date = date.replace(".", "-")
print("바군 후의 데이터 :", date)

# 문자열 abcd에서 소문자 a를 대문자 A로 변경 후 출력하라
문자열 = "abcd"
문자열 = 문자열.replace("a", "A")
print(문자열)

# 문자열 "Python"을 거꾸로 뒤집어 출력하세요.
reverse = "Python"
new = reverse[5] + reverse[4] + reverse[3] + reverse[2] + reverse[1] + reverse[0]
print(new)

# 문자열 여러 줄 출력하기
자유로운_문자열 = "아무 말이나 적으라길래 적는데 \n무슨말을 해야 잘했다고 소문이 날까 응? 뭐라고? 닥쳐"
print(자유로운_문자열)