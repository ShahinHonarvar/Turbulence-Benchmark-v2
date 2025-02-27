def find_second_smallest_num(numbers):
    if len(numbers) < 10:
        return None
    sub_list = numbers[8:10]
    sub_list.sort()
    return sub_list[1] if len(sub_list) > 1 else None