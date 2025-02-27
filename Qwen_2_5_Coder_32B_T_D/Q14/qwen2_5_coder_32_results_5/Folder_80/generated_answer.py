def find_second_smallest_num(numbers):
    if len(numbers) < 88:
        return None
    sub_list = numbers[30:88]
    if len(sub_list) < 2:
        return None
    sub_list.sort()
    return sub_list[1]