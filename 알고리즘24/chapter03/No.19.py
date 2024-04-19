A = [1, 3, 5]
B = [2, 3, 1]
C = [6, 3, 9]

sum1=A[0]+B[1]+C[2]
sum2=A[0]+B[2]+C[1]
sum3=A[1]+B[0]+C[2]
sum4=A[1]+B[2]+C[0]
sum5=A[2]+B[1]+C[0]
sum6=A[2]+B[0]+C[1]

print("A, B, C")
print("0, 1, 2 : ", sum1)
print("0, 2, 1 : ", sum2)
print("1, 0, 2 : ", sum3)
print("1, 2, 0 : ", sum4)
print("2, 1, 0 : ", sum5)
print("2, 0, 1 : ", sum6)

minsum = min(sum1,sum2,sum3,sum4,sum5,sum6) 

print("제일 적은 비용의 일 배정은 : ",minsum,"A=0, B=2, C=1")