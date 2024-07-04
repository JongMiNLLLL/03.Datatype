dic = {'이종민' : 27, '팜하니': 20}

print("업데이트 이전의 이종민 나이: ", dic['이종민'])

data = ['이종민', 25,'팜하니', 20]

dic['이종민'] = 31
print("업데이트 이후의 이종민 나이: ",dic['이종민'])

print(dic.keys())
print(dic.values())

# 주어진 딕셔너리 {'apple': 3, 'banana': 5, 'cherry': 2}ㅔ서 'banana'의 값을 추출하는 파이썬 코드를 작성하세요.

fruits = {'apple': 3, 'banana': 5, 'cherry': 2}
print(fruits['banana'])