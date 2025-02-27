def find_second_largest_num(numbers):
    if len(numbers) < 99 or len(numbers) < 56:
        return None
    sub_list = numbers[55:99]
    sub_list.sort()
    if len(sub_list) < 2:
        return None
    return sub_list[-2]