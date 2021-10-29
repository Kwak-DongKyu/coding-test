n, k = map(int, input().split())
j=0
while n > 1:
    if n % k ==0:
        n /= k
        j += 1
    else :
        n -= 1
        j += 1

print(j)