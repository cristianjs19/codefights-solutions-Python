def replaceMiddle(arr):
    mid = 0
    if len(arr) % 2 == 0:
        mid = arr[len(arr) // 2] + arr[(len(arr) // 2) - 1]
        arr.pop(len(arr) // 2)
        arr[len(arr) // 2] = mid
        
    return arr
