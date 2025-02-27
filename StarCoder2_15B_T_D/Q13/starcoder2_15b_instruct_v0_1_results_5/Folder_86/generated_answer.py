def find_second_largest_num(input_list):
    sorted_list = sorted(input_list[31:35], reverse=True)
    if len(sorted_list) < 2:
        return None
    return sorted_list[1]