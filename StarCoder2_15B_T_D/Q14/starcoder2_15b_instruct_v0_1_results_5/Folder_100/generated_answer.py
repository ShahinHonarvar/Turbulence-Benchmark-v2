def find_second_smallest_num(input_list):
    sorted_list = sorted(input_list)
    second_smallest = sorted_list[43:52]
    if len(second_smallest) < 2:
        return None
    return second_smallest[1]