#리스트를 받는데 split함수를 써서 공백으로 요소들을 구분하고 int로 정수값을 받음
A = list(map(int, input("A 리스트의 값을 입력하세요 (공백으로 구분): ").split()))
B = list(map(int, input("B 리스트의 값을 입력하세요 (공백으로 구분): ").split()))

set_A = set(A)  #리스트를 집합으로 바꿔줌
set_B = set(B)  #set합수는 집합으로 바꿔줌

print(set_A.issubset(set_B) and set_A != set_B )

"""
issubset은 A가 B에 부분집합인지 구하고 true와 false로 결과값이 나옴
진부분집합은 집합 A와 집합 B가 서로 같지 않아야하니 
and연산자 뒤에 !=를 써서 서로 같지 않다면 true가 그 외의 값은 false가 나온다
"""