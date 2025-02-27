def find_second_largest_num(numbers):
    sub_list = numbers[12:93]
    if len(sub_list) < 2:
        return None
    sorted_list = sorted(sub_list, reverse=True)
    return sorted_list[1]