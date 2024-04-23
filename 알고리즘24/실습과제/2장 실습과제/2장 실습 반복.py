def factorial(n):
    result = 1
    for k in range(1, n + 1):
        result *= k
    return result

n = int(input("팩토리얼을 구할 값을 입력하세요: "))
result = factorial(n)
print(f"{n}의 팩토리얼은 {result}입니다.")
