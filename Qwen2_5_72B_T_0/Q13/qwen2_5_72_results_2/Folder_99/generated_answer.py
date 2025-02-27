def find_second_largest_num(numbers):
    if len(numbers) < 371 or len(numbers) < 311:
        return None
    sub_list = numbers[310:371]
    if len(sub_list) < 2:
        return None
    sub_list.sort()
    return sub_list[-2] if len(sub_list) > 1 else None