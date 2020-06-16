def linear_search(arr, target):
    # Your code here
    for i in range(len(arr)):
        if arr[i] == target:
            return i

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here
    # Set low to 0
    low = 0
    # Set high to len(arr) - 1
    high = len(arr) - 1
    # While low index is less than or equal to  high index
    while low <= high:
        # Get middle by adding low and high and // by 2
        mid = low + high // 2
        # If mid matches
        if target == arr[mid]:
            # return mid index
            return mid
        # if target less than mid,
        elif target < arr[mid]:
            # look at low -> mid - 1
            high = mid - 1
        # if target is greater than mid
        else:
            # look in mid + 1 -> high
            low = mid + 1

    return -1  # not found
