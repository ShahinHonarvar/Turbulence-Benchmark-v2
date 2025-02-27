def find_second_smallest_num(input_list):
    sorted_list = sorted(input_list)
    if len(sorted_list) < 89:
        return None
    return sorted_list[22:89][1]