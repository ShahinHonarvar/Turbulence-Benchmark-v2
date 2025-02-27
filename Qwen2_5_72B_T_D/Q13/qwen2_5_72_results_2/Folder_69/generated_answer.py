def find_second_largest_num(numbers):
    sub_list = numbers[32:36]
    if len(sub_list) < 4:
        return None
    sub_list.sort()
    if len(sub_list) < 2:
        return None
    return sub_list[-2]