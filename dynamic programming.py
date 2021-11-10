# 메모이제이션, 캐싱, 다이내믹 프로그래밍의 탑다운 방식에만 메모이제이션이 사용된다. 메모이제이션이 더 큰 개념으로 계산된 결과를 일시적으로 기록하는 것을 의미한다.
# 큰 문제를 작은 문제로 나눌 수 있고, 작은 문제에서 구한 정답은 그것을 포함하는 큰 문제에서도 동일할때


#개미 전사
n = int(input())
array = list(map(int, input().split()))
d = [0] * 100

d[0] = array[0]
d[1] = max(d[0], array[1])

for i in range(2, n):
    d[i] = max(d[i-1], d[i-2] + array[i])

print(d[n-1])


#보텀업 방식
# d = [0] * 100
# d[1]= 1
# d[2] = 1
# n=99
# for i in range(3, n+1):
#     d[i] = d[i-1] + d[i-2]
#
# print(d[n])
#
#
#
# # 탑다운 방식
# d = [0] * 100
# def fibo(x):
#     if x==1 or x==2:
#         return 1
#     if d[x] != 0:
#         return d[x]
#     d[x] = fibo(x-1) + fibo(x-2)
#     return d[x]
#
# print(fibo(99))
#