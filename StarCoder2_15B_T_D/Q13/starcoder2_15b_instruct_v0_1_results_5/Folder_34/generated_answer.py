def find_second_largest_num(input_list):
    sorted_list = sorted(input_list, reverse=True)
    sliced_list = sorted_list[16:62]
    if len(sliced_list) < 2:
        return None
    return sliced_list[1]