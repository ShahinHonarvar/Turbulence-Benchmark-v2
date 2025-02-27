def find_second_largest_num(input_list):
    sorted_list = sorted(input_list, reverse=True)
    sublist = sorted_list[661:925]
    if len(sublist) < 2:
        return None
    return sublist[1]