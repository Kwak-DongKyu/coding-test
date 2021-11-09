
array= [('바나나',2), ('사과', 3), ('당근',3)]
def setting(data):
    return data[0]
result = sorted(array, key = setting)
print(result)

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

