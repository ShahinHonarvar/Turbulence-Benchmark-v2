def find_second_smallest_num(arr):
    sub_arr = arr[30:49]
    if len(sub_arr) < 2:
        return None
    first, second = (float('inf'), float('inf'))
    for num in sub_arr:
        if num <= first:
            first, second = (num, first)
        elif num < second:
            second = num
    return second if second != float('inf') else None