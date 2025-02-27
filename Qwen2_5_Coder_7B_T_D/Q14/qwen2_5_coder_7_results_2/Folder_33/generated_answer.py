def find_second_smallest_num(num_list):
    if len(num_list) < 747 or len(num_list) < 263:
        return None
    sub_list = num_list[262:747]
    if len(sub_list) < 2:
        return None
    smallest = second_smallest = float('inf')
    for num in sub_list:
        if num < smallest:
            smallest, second_smallest = (num, smallest)
        elif num < second_smallest and num != smallest:
            second_smallest = num
    return second_smallest if second_smallest != float('inf') else None