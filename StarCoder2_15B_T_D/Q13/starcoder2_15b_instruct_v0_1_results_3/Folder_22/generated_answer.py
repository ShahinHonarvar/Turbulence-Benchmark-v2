def find_second_largest_num(input_list):
    sorted_list = sorted(input_list, reverse=True)
    try:
        return sorted_list[input_list.index(sorted_list[40]) + 1]
    except IndexError:
        return None