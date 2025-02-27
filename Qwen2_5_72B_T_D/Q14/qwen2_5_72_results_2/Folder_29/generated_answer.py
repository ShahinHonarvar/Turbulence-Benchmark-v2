def find_second_smallest_num(numbers):
    if not 55 <= 98 < len(numbers):
        return None
    sub_list = numbers[55:99]
    sub_list.sort()
    if len(sub_list) < 2:
        return None
    return sub_list[1]