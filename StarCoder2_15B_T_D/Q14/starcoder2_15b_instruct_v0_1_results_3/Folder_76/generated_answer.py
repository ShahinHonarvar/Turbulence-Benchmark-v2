def find_second_smallest_num(input_list):
    sorted_list = sorted(input_list)
    try:
        return sorted_list[533:606][1]
    except IndexError:
        return None