def find_second_smallest_num(input_list):
    if len(input_list) < 10:
        return None
    sorted_list = sorted(input_list[8:10])
    return sorted_list[1]