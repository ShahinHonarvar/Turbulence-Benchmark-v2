def find_second_smallest_num(arr):
    sorted_arr = sorted(arr)
    if len(sorted_arr) < 2:
        return None
    return sorted_arr[1]