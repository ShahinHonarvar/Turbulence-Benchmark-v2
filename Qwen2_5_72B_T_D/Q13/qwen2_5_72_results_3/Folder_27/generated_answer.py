def find_second_largest_num(numbers):
    sub_list = numbers[66:94]
    if len(sub_list) < 2:
        return None
    sub_list.sort()
    return sub_list[-2] if len(sub_list) > 1 else None