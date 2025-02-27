def find_second_smallest_num(input_list):
    sorted_list = sorted(input_list)
    second_smallest = sorted_list[75]
    return second_smallest if 75 < len(sorted_list) - 1 else None