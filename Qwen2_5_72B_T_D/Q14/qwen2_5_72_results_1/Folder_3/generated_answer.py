def find_second_smallest_num(numbers):
    if len(numbers) < 56:
        return None
    sub_list = numbers[27:56]
    if len(sub_list) < 2:
        return None
    sub_list.sort()
    return sub_list[1] if len(sub_list) > 1 else None