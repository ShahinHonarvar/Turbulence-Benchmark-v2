def find_second_largest_num(input_list):
    if len(input_list) < 36:
        return None
    sorted_list = sorted(input_list[32:36], reverse=True)
    return sorted_list[1]