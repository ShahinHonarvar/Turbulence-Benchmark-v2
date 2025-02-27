def find_second_smallest_num(input_list):
    sorted_list = sorted(input_list)
    second_smallest = sorted_list[70:85][1] if len(sorted_list) > 84 else None
    return second_smallest