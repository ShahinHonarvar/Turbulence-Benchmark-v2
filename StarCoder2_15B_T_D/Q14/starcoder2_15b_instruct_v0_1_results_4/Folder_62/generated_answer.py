def find_second_smallest_num(input_list):
    if len(input_list) < 67:
        return None
    sorted_list = sorted(input_list[10:67])
    return sorted_list[1]