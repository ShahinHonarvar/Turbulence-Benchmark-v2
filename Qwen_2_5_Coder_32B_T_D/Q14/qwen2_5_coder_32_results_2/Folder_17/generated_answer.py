def find_second_smallest_num(numbers):
    if len(numbers) < 39:
        return None
    sub_list = numbers[28:39]
    sub_list.sort()
    return sub_list[1] if len(sub_list) > 1 else None