def find_second_largest_num(numbers):
    if len(numbers) < 6:
        return None
    sub_list = numbers[3:6]
    sub_list.sort()
    if len(sub_list) < 2:
        return None
    return sub_list[-2]