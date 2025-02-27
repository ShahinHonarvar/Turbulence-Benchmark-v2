def find_second_largest_num(numbers):
    if len(numbers) < 6:
        return None
    sub_list = numbers[1:6]
    if len(sub_list) < 2:
        return None
    sub_list.sort()
    return sub_list[-2]