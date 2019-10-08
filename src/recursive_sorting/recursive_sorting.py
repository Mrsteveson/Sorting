# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    i = x = z = 0
    # Three cases
    # Check both sides
    while i < len(arrA) and x < len(arrB):
        if arrA[i] < arrB[x]:
            merged_arr[z] = arrA[i]
            i += 1
        else:
            merged_arr[z] = arrB[x]
            x += 1
        k += 1
    # Check first array
    while i < len(arrA):

    # Check second array
    while x < len(arrB):


    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    # Len > 1, means we have an array to sort. 
    # Len <= 1, we do not need to sort for we either have an empty array or an array of 1 (which would already be considered sorted).
    if len(arr) > 1:
        middle = len(arr)//2 # Set the middle value to separate the left and right portions
        left_side = merge_sort(arr[:middle]) # Start at the beginning of the array till the middle value
        right_side = merge_sort(arr[middle:]) # Start at the middle value and continue to the end of the array
        arr = merge(left_side, right_side) # Combine the two sides using our helper function to create our sorted array

        # middle = len(arr)//2
        # left_side = arr[:middle]
        # right_side = arr[middle:]

        # merge_sort(left_side)
        # merge_sort(right_side)
        # arr = merge(left_side, right_side)
    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
