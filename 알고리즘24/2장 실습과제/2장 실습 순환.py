def binary_digits(n):
    if n <= 1:
        return 1
    else:
        return 1 + binary_digits(n//2)

n = int(input("양의 정수를 입력하세요: "))

result = binary_digits(n)

print(f"{n}의 이진수 자릿수는 {result}입니다.")
