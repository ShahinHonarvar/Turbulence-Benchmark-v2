def find_second_smallest_num(lst):
    start, end = (62, 78)
    sub_list = lst[start:end + 1]
    if len(sub_list) < 2:
        return None
    first_smallest = min(sub_list)
    second_smallest = float('inf')
    for num in sub_list:
        if num > first_smallest and num < second_smallest:
            second_smallest = num
    return None if second_smallest == float('inf') else second_smallest