def find_second_largest_num(numbers):
    if len(numbers) < 77 or len(numbers) < 38:
        return None
    sub_list = numbers[37:77]
    if len(sub_list) < 2:
        return None
    sub_list.sort()
    return sub_list[-2]