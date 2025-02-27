def find_second_largest_num(numbers):
    if len(numbers) < 99 or len(numbers) < 57:
        return None
    sub_list = numbers[56:99]
    if len(sub_list) < 2:
        return None
    sub_list.sort()
    return sub_list[-2]