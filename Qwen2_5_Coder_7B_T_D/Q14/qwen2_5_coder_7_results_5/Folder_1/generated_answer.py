def find_second_smallest_num(lst):
    sliced_list = lst[34:56]
    if len(sliced_list) < 2:
        return None
    smallest = min(sliced_list[0], sliced_list[1])
    second_smallest = max(sliced_list[0], sliced_list[1])
    for i in range(2, len(sliced_list)):
        if sliced_list[i] < smallest:
            second_smallest = smallest
            smallest = sliced_list[i]
        elif smallest < sliced_list[i] < second_smallest:
            second_smallest = sliced_list[i]
    return second_smallest if second_smallest != smallest else None