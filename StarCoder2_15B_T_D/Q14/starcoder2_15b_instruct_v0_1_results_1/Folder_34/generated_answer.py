def find_second_smallest_num(input_list):
    sorted_list = sorted(input_list)
    second_smallest = sorted_list[60:201][1] if len(sorted_list) > 61 else None
    return second_smallest