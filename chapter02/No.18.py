def sum(n) :
    print(n)
    if n<1 : return 0
    else : return n+sum(n-1)
'''
n이 n자신과 -1을 한 값을 서로 더하며 n이 0이 될때 까지 반복하는 구조이다
n에 5를 넣게되면 출력문에는
5
4
3
2
1
0
이 나온다
'''
