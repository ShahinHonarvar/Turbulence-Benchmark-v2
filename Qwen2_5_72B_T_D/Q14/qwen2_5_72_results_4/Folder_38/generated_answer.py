def find_second_smallest_num(numbers):
    if len(numbers) < 52 or len(numbers) < 38:
        return None
    sub_list = numbers[37:52]
    sub_list.sort()
    if len(sub_list) < 2:
        return None
    return sub_list[1]