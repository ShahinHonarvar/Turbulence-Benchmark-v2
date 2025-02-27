def find_second_smallest_num(input_list):
    sorted_list = sorted(input_list)
    if len(sorted_list) < 30:
        return None
    second_smallest = sorted_list[30]
    for num in sorted_list[31:49]:
        if num < second_smallest:
            second_smallest = num
    return second_smallest