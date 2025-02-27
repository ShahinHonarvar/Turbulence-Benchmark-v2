def find_second_smallest_num(input_list):
    sorted_list = sorted(input_list)
    if len(sorted_list) >= 78:
        return sorted_list[67]
    else:
        return None