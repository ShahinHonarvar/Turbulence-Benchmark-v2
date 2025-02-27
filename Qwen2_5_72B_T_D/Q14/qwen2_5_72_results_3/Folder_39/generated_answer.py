def find_second_smallest_num(numbers):
    if len(numbers) < 41:
        return None
    sub_list = numbers[28:41]
    sub_list.sort()
    if len(sub_list) < 2:
        return None
    return sub_list[1]