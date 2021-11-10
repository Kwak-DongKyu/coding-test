n,m = map(int, input().split())
array = list(map(int, input().split()))
start = 0
end = max(array)
while start <= end:
    total = 0
    mid = (start+end) // 2
    for x in array:
        if x > mid:
            total += x - mid
    if total < m:
        end = mid - 1
    else:
        result = mid
        start = mid + 1
print(result)
# for j in range(max(array), 0, -1):
#     sum = 0
#     for i in range(len(array)):
#         if array[i] > j:
#             sum += array[i] - j
#     if sum >= m:
#         print(j)
#         break




# n = int(input())
# array1 = list(map(int, input().split()))
# m = int(input())
# target = list(map(int, input().split()))
# for i in range(len(target)):
#     if target[i] in array1:
#         print("Yes", end='')
#     else:
#         print("No", end='')







# n, m = map(int, input().split())
# array = list(map(int, input().split()))
# def binary_search(array, target, start, end):
#     if start > end:
#         return None
#     middle = int((start+end)/2)
#     if array[middle] == target:
#         return middle
#
#     elif array[middle] > target:
#         end = middle - 1
#         return binary_search(array, target, start, end)
#     else:
#         start = middle + 1
#         return binary_search(array, target, start, end)
#
# result = binary_search(array, m, 0, len(array)-1)
# if result == None:
#     print("없음")
#
# else:
#     print(result+1)





# print("생성할 원소 개수를 입력한 다음 한칸 띄고 찾을 문자열을 입력하세요")
# input_data = input().split()
# n = int(input_data[0])
# finding = input_data[1]
#
# array = list(map(str, input().split()))
# print(array.index(finding))