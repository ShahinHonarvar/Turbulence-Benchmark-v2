def find_second_smallest_num(arr):
    arr = sorted(arr)
    if len(arr) >= 81:
        return arr[80]
    else:
        return None