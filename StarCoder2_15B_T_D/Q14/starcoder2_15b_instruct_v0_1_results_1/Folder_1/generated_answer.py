def find_second_smallest_num(input_list):
    sublist = input_list[34:56]
    sorted_sublist = sorted(sublist)
    if len(sorted_sublist) < 2:
        return None
    return sorted_sublist[1]