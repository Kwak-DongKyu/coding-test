

n, m = map(int, input().split())

A=list(map(int, input().split()))
B = list(map(int,input().split()))
for i in range(m):
    min_index = i
    max_index = i
    for j in range(n):
        if A[min_index] > A[j]:
            min_index = j
        if B[max_index] < B[j]:
            max_index = j
    A[min_index], B[max_index] = B[max_index], A[min_index]

print(sum(A))




# a=int(input())
#
# array=[]
# for i in range(a):
#     input_data = input().split()
#     array.append((input_data[0], int(input_data[1])))
#
# array = sorted(array, key=lambda student:student[1])
#
# for i in array:
#     print(i[0], end='')




# array= [('바나나',2), ('사과', 3), ('당근',3)]
# def setting(data):
#     return data[0]
# result = sorted(array, key = setting)
# print(result)




# array = [7, 5, 9, 0, 3, 1, 2, 9, 1, 4, 8, 0, 5, 2]
# count = [0] * (max(array)+1)
# for i in range(len(array)) :
#     count[array[i]] += 1
# for i in range(len(count)):
#     for j in range(count[i]):
#         print(i, end='')




# for i in range(1, len(array)):
#     j = i
#     while j > 0 :
#         if array[j] < array[j-1]:
#             array[j], array[j-1] = array[j-1], array[j]
#         else
#             break
#         j -= 1




# for i in range(len(array)):
#     for j in range(i+1, len(array)):
#         if array[i] == min(array[i:]):
#             break
#         if array[j] == min(array[i+1:]):
#             array[i], array[j] = array[j], array[i]
#             break
# for i in range(len(array)):
#     min_index = i
#     for j in range(i+1, len(array)):
#         if array[min_index] > array[j]:
#             min_index = j
#     array[i], array[min_index] = array[min_index], array[i]

