def find_second_largest_num(numbers):
    if len(numbers) < 85 or len(numbers) < 71:
        return None
    sub_list = numbers[70:85]
    if len(sub_list) < 2:
        return None
    sub_list.sort(reverse=True)
    return sub_list[1] if len(sub_list) > 1 else None