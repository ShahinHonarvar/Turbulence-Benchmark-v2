def find_second_smallest_num(numbers):
    if len(numbers) < 52:
        return None
    sub_list = numbers[43:52]
    sub_list.sort()
    return sub_list[1] if len(sub_list) > 1 else None