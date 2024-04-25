def partition(A, left, right) :
    low = left + 1
    high = right
    pivot = A[left]
    while (low <= high) : # 왼쪽의 작은수가 오른쪽의 큰수보다 작으면 계속 실행
        while low <= right and A[low] <= pivot : low += 1
        while high >= left and A[high]> pivot : high-= 1
        
        if low < high :  # 왼쪽과 오른쪽이 만나서 교차하게되면 서로 교환을 해준다
            A[low], A[high] = A[high], A[low]
            
    A[left], A[high] = A[high], A[left]  # 처음에 고정된 피벗을 high 위치와 교환한다
    return high                          # 피벗의 위치로 반환

def quick_sort(A, left, right) :
    if left<right :
        mid = partition(A, left, right)
        quick_sort(A, left, mid-1)
        quick_sort(A, mid+1, right)

data = [ 5, 3, 8, 4, 9, 1, 6, 2, 7 ]
print("Original : ", data)
quick_sort(data, 0, len(data)-1)
print("QuickSort : ", data)