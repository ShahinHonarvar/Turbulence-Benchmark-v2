def find_second_largest_num(numbers):
    if len(numbers) < 52 or len(numbers) < 30:
        return None
    sub_list = numbers[29:52]
    if len(sub_list) < 2:
        return None
    sub_list.sort(reverse=True)
    return sub_list[1] if len(sub_list) > 1 else None