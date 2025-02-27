def find_second_largest_num(numbers):
    if len(numbers) < 51 or len(numbers) <= 22:
        return None
    sub_list = numbers[22:51]
    if len(sub_list) < 2:
        return None
    sub_list.sort()
    return sub_list[-2] if len(sub_list) > 1 else None