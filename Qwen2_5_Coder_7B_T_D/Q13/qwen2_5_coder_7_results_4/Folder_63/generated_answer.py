def find_second_largest_num(num_list):
    sliced_list = num_list[22:89]
    if len(sliced_list) < 2:
        return None
    first, second = (sliced_list[0], sliced_list[1]) if sliced_list[0] > sliced_list[1] else (sliced_list[1], sliced_list[0])
    for num in sliced_list[2:]:
        if num > first:
            first, second = (num, first)
        elif first > num > second:
            second = num
    return second if second != first else None