def find_second_smallest_num(arr):
    sub_arr = arr[4:9]
    if len(sub_arr) < 2:
        return None
    sub_arr.sort()
    return sub_arr[1]