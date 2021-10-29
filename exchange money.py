n, m, k = map(int, input().split())

data=list(map(int, input().split()))

sum = 0
data.sort(reverse=True)

count = m // (k+1) * k
count += m % (k+1)

sum = count * data[0] + data[1] * (m-count)

print(sum)