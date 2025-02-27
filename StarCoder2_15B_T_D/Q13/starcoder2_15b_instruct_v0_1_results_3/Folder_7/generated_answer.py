def find_second_largest_num(input_list):
    sorted_list = sorted(input_list)
    try:
        return sorted_list[924 - 661 + 1]
    except IndexError:
        return None