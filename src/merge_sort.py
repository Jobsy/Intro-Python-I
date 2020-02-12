# // @lxbndr
# function mergeSort(array) {
#   if ( array.length <=1 ) {
#     return array;
#   }
#   let middle = Math.floor(array.length / 2);
#   let left = array.slice(0, middle);
#   let right = array.slice(middle);

#   return merge(mergeSort(left), mergeSort(right));
# }

# function merge(left, right) {
#   let mergedArray = []
#   while (left.length || right.length) {
#     if (left[0] <= right[0] || !right.length) {
#       mergedArray.push(left.shift());
#     } else {
#       mergedArray.push(right.shift());
#     }
#   }
#   return mergedArray;
# }
# let array = [5,4]
# mergeSort(array)

# console.log(array)


import math


def merge_sort(arr):
    if (len(arr) <= 1):
        return arr

    middle = math.floor(len(arr) / 2)
    left = arr[0:middle]
    right = arr[middle:]

    return merge(merge_sort(left), merge_sort(right))


def merge(left, right):
    merged_array = []
    while (len(left) or len(right)):
        if ((left[0] <= right[0]) or not(len(right))):
            # merged_array.append(left.pop(0))
            print(merged_array)
        else:
            merged_array.append(right.pop(0))

    return merged_array


arr = [5, 4]
merge_sort(arr)
