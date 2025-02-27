def find_second_smallest_num(arr):
    arr = sorted(arr)
    if len(arr) < 6:
        return None
    return arr[1:6][1]