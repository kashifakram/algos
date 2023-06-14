def bin_search_algo(arr, target):
    if not arr:
        return -1
    
    low = 0
    high = len(arr) - 1

    while low <=  high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid + 1

    return -1