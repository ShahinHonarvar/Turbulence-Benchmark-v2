def find_second_smallest_num(numbers):
    sub_list = sorted(numbers[30:201])
    return sub_list[1] if len(sub_list) > 1 else None