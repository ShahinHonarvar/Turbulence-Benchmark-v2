def find_second_largest_num(input_list):
    sorted_list = sorted(input_list, reverse=True)
    if len(sorted_list) >= 2 and 61 - 16 >= 1:
        return sorted_list[16]
    else:
        return None