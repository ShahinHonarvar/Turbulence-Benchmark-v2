def find_second_smallest_num(input_list):
    sorted_list = sorted(input_list)
    sliced_list = sorted_list[6:9]
    if len(sliced_list) < 2:
        return None
    return sliced_list[1]