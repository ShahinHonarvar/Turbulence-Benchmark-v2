def find_second_smallest_num(numbers):
    if len(numbers) < 98:
        return None
    sub_list = numbers[59:98]
    if len(sub_list) < 2:
        return None
    sub_list.sort()
    return sub_list[1]