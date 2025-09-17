#----------------------------Find minimum value in array---------------------------------------#
# array = [1,2,3,4,34,6,0,8]
#
# minvalue= array[0]
#
# for i in array:
#     if i<minvalue:
#         minvalue= i
#
# print(minvalue)
from heapq import merge


#-----------------------------------bubble sort--------------------------------------------------#

# #
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

#-----------------------------------selection sort----------------------------------------------------------#
# my_array = [64, 34, 25, 5, 22, 11, 90, 12]
# n= len(my_array)
# for i in range(n-1):
#     min_index= i
#     for j in range(i+1, n):
#         if my_array[j] < my_array[min_index]:
#             min_index= j
#     # min_value= my_array.pop(min_index)
#     # my_array.insert(i,min_value)
#     my_array[i],my_array[min_index]=my_array[min_index],my_array[i]
# print(my_array)

#-----------------------------------insertion sort-----------------------------------------------------#
# def insertion_sort(arr):
#     n = len(arr)
#     for i in range(1,n):
#         insert_index= i
#         current_value= arr.pop(i)
#         for j in range(i-1,-1,-1):
#             if arr[j]> current_value:
#                 insert_index= j
#         arr.insert(insert_index,current_value)
#     return arr
#     # for i in range(1,n):
#     #     key = arr[i]
#     #     j = i-1
#     #     while j>=0 and arr[j] > key:
#     #         arr[j+1]=arr[j]
#     #         j= j-1
#     #     arr[j+1]=key
#     # return arr
#
# my_array = [9, 5, 1, 4, 3]
# print("Original:", my_array)
# sorted_array = insertion_sort(my_array)
# print("Sorted:", sorted_array)

#-------------------------------------Quick Sort --------------------------------------------------#
# def partition(array, low, high):
#     p= array[low]
#     i = low +1
#     j = high
#     while True:
#         while i <=j and array[i] <= p:
#             i+=1
#         while i <= j and array[j]>= p:
#             j-=1
#         if i <= j:
#             array[i],array[j] = array[j] , array[i]
#         else:
#             break
#     array[low],array[j]= array[j],array[low]
#     return j
# def quicksort(array, low=0, high=None):
#     if high is None:
#         high = len(array) - 1
#
#     if low < high:
#         pivot_index = partition(array, low, high)
#         quicksort(array, low, pivot_index-1)
#         quicksort(array, pivot_index+1, high)
#
# my_array = [64, 34, 25, 12, 22, 11, 90, 5]
# quicksort(my_array)
# print("Sorted array:", my_array)

#---------------------------------------------------counting sort----------------------------------------#
# def counting_sort(arr):
#     max_val= max(arr)
#     count= [0] * (max_val +1)
#
#     while len(arr) > 0:
#         num = arr.pop(0)
#         count[num]+=1
#
#     for i in range(len(count)):
#         while count[i]>0:
#             arr.append(i)
#             count[i]-=1
#     return arr
#
# unsortedArr = [4, 2, 2, 6, 3, 3, 1, 6, 5, 2, 3]
# sortedArr = counting_sort(unsortedArr)
# print("Sorted array:", sortedArr)

#---------------------------------------------Merge sort---------------------------------#
# def merge_sort(arr):
#     if len(arr) <= 1:
#         return arr
#
#     mid = len(arr) // 2
#     left_half = arr[:mid]
#     rightHalf = arr[mid:]
#
#     sortedLeft = merge_sort(left_half)
#     sortedRight = merge_sort(rightHalf)
#
#     return merge(sortedLeft, sortedRight)
#
# def merge(left, right):
#     result = []
#     i = j = 0
#
#     while i < len(left) and j < len(right):
#         if left[i] < right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1
#
#     result.extend(left[i:])
#     result.extend(right[j:])
#
#     return result
#
# unsortedArr = [3, 7, 6, -10, 15, 23.5, 55, -13]
# sortedArr = merge_sort(unsortedArr)
# print("Sorted array:", sortedArr)
#---------------------------------------------linear search-----------------------------------#
# def linear_search(arr, val):
#     for i in range(len(arr)):
#         if arr[i] == val:
#             return i
#     return -1
#
# array= [1,2,34,2,3,4,6,4,5,6,4]
# value= 34
# answer= linear_search(array,value)
# if answer == -1:
#     print(f"the index of {value} not find")
# else:
#     print(f"the index of {value} is {answer}")

#------------------------------------------Binary search--------------------------------#
def binarySearch(arr, targetVal):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == targetVal:
            return mid

        if arr[mid] < targetVal:
            left = mid + 1
        else:
            right = mid - 1

    return -1


myArray = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
myTarget = 15

result = binarySearch(myArray, myTarget)

if result != -1:
    print("Value", myTarget, "found at index", result)
else:
    print("Target not found in array.")