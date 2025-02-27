def find_second_smallest_num(numbers):
    if len(numbers) < 93 or len(numbers) < 20:
        return None
    sub_list = numbers[19:93]
    sub_list.sort()
    return sub_list[1] if len(sub_list) > 1 else None