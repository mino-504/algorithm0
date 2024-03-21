def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

number = int(input("숫자를 입력하세요 : "))
result = factorial(number)

print(f"{number}! = {result}")