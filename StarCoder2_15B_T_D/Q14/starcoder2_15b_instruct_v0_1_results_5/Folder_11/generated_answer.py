def find_second_smallest_num(input_list):
    sorted_list = sorted(input_list)
    if len(sorted_list) < 67:
        return None
    else:
        return sorted_list[66]