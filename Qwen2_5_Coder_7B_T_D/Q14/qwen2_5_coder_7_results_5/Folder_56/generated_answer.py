def find_second_smallest_num(num_list):
    if len(num_list) <= 1:
        return None
    first, second = (float('inf'), float('inf'))
    for num in num_list:
        if num <= first:
            first, second = (num, first)
        elif num < second:
            second = num
    return second if second != float('inf') else None