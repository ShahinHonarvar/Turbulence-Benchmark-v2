def find_second_largest_num(numbers):
    if len(numbers) < 40:
        return None
    sub_list = numbers[15:40]
    if len(sub_list) < 2:
        return None
    sub_list.sort()
    return sub_list[-2]