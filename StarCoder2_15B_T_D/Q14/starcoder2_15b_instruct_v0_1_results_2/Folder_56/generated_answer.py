def find_second_smallest_num(input_list):
    input_list.sort()
    if len(input_list) < 2:
        return None
    return input_list[1]