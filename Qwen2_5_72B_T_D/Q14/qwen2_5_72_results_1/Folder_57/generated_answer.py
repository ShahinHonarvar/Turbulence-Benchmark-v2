def find_second_smallest_num(numbers):
    sub_list = numbers[20:31]
    if len(sub_list) < 2:
        return None
    sub_list.sort()
    return sub_list[1] if sub_list[0] < sub_list[1] else None