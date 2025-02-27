def find_second_largest_num(numbers):
    if len(numbers) < 201 or len(numbers) <= 30:
        return None
    sub_list = numbers[30:201]
    if len(sub_list) < 2:
        return None
    sub_list.sort()
    return sub_list[-2] if len(sub_list) > 1 else None