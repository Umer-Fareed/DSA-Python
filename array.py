# array = [1,2,3,4,34,6,0,8]
#
# minvalue= array[0]
#
# for i in array:
#     if i<minvalue:
#         minvalue= i
#
# print(minvalue)

# #bubble sort
# my_array = [64, 34, 25, 12, 22, 11, 90, 5]
# n = len(my_array)
# for i in range(n-1):
#     swapped = False
#     for j in range(n-i-1):
#         if my_array[j] > my_array[j+1]:
#             my_array[j], my_array[j+1] = my_array[j+1], my_array[j]
#             swapped= True
#     if not swapped:
#         break
# print("Sorted array:", my_array)

#selection sort
my_array = [64, 34, 25, 5, 22, 11, 90, 12]
n= len(my_array)
for i in range(n-1):
    min_index= i
    for j in range(i+1, n):
        if my_array[j] < my_array[min_index]:
            min_index= j
    # min_value= my_array.pop(min_index)
    # my_array.insert(i,min_value)
    my_array[i],my_array[min_index]=my_array[min_index],my_array[i]
print(my_array)

