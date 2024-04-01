#(1)
def recursive1(n) :
    if n==1 : return 0
    return n * recursive1(n)
'''
0까지 계산이 되는 문제
'''
def recursive1(n) :
    if n == 1 :
        return 1
    return n * recursive1(n-1)

#(2)
def recursive2(n) :
    print('현재 n = ', n)
    return n * recursive2(n - 1)
'''
음수로 넘어가게 된다면 종료가 되지않는 구조
'''
def recursive2(n) :
    if n == 1 :
        print('현재 n = ',n)
        return 1
    print('현재 n = ', n)
    return n * recursive2(n - 1)
