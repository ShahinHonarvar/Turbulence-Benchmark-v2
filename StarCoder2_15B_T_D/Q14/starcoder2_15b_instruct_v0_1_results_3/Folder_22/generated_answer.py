def find_second_smallest_num(input_list):
    if len(input_list) < 201:
        return None
    sorted_list = sorted(input_list[40:201])
    return sorted_list[1]