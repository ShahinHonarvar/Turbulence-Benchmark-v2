def find_second_smallest_num(input_list):
    if len(input_list) < 81:
        return None
    sorted_list = sorted(input_list[40:81])
    return sorted_list[1]