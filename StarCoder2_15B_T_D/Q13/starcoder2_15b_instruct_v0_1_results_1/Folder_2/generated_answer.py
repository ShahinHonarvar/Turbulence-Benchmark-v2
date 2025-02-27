def find_second_largest_num(input_list):
    if len(input_list) < 40:
        return None
    sorted_list = sorted(input_list[15:40], reverse=True)
    return sorted_list[1]