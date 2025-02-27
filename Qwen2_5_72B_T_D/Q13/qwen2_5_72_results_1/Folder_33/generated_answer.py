def find_second_largest_num(numbers):
    sub_list = numbers[667:775]
    if len(sub_list) < 8:
        return None
    sub_list.sort()
    return sub_list[-2]