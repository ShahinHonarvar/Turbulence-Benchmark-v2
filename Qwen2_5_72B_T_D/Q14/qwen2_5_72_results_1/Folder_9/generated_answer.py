def find_second_smallest_num(numbers):
    if not numbers or len(numbers) < 70 or len(numbers) < 201:
        return None
    sub_list = numbers[70:201]
    if len(sub_list) < 2:
        return None
    sub_list.sort()
    return sub_list[1] if len(sub_list) > 1 else None