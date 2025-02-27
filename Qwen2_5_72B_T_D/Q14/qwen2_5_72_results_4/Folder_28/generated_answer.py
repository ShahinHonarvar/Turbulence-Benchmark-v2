def find_second_smallest_num(numbers):
    if len(numbers) < 51:
        return None
    sub_list = numbers[22:51]
    sub_list.sort()
    return sub_list[1] if len(sub_list) > 1 else None