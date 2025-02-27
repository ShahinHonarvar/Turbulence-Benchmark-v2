def find_second_largest_num(input_list):
    sorted_list = sorted(input_list)
    if len(sorted_list) < 94:
        return None
    return sorted_list[93 - 29]