def find_second_smallest_num(num_list):
    sorted_list = sorted(num_list)
    sliced_list = sorted_list[8:10]
    if len(sliced_list) == 2:
        return sliced_list[1]
    else:
        return None